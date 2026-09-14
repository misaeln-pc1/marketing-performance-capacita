"""Minimal, sanitized READ smoke for the official Google Ads MCP stdio server.

Requires GOOGLE_APPLICATION_CREDENTIALS and GOOGLE_PROJECT_ID in the process.
No credential or customer identifier is printed or persisted.
"""

import json
import os
import queue
import re
import subprocess
import sys
import threading
import time


SPEC = "git+https://github.com/googleads/google-ads-mcp.git"
TIMEOUT_SECONDS = 90


def main() -> int:
    if not os.environ.get("GOOGLE_APPLICATION_CREDENTIALS") or not os.environ.get("GOOGLE_PROJECT_ID"):
        print("MCP_ENV=HOLD_MISSING")
        return 2

    process = subprocess.Popen(
        [sys.executable, "-m", "pipx", "run", "--spec", SPEC, "google-ads-mcp"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True,
        encoding="utf-8",
        bufsize=1,
        env=os.environ.copy(),
    )
    replies: queue.Queue[dict] = queue.Queue()

    def read_stdout() -> None:
        assert process.stdout is not None
        for line in process.stdout:
            try:
                value = json.loads(line)
                if isinstance(value, dict):
                    replies.put(value)
            except json.JSONDecodeError:
                continue

    threading.Thread(target=read_stdout, daemon=True).start()
    next_id = 0

    def send(method: str, params: dict | None = None) -> dict:
        nonlocal next_id
        next_id += 1
        assert process.stdin is not None
        process.stdin.write(json.dumps({"jsonrpc": "2.0", "id": next_id, "method": method, "params": params or {}}) + "\n")
        process.stdin.flush()
        deadline = time.monotonic() + TIMEOUT_SECONDS
        while time.monotonic() < deadline:
            try:
                reply = replies.get(timeout=min(1, deadline - time.monotonic()))
            except queue.Empty:
                if process.poll() is not None:
                    raise RuntimeError("MCP_PROCESS_EXITED")
                continue
            if reply.get("id") == next_id:
                return reply
        raise TimeoutError("MCP_RESPONSE_TIMEOUT")

    try:
        init = send("initialize", {
            "protocolVersion": "2025-06-18",
            "capabilities": {},
            "clientInfo": {"name": "capacita-read-probe", "version": "1.0"},
        })
        if "error" in init:
            print("GOOGLE_ADS_MCP_INIT=HOLD")
            return 2
        print("GOOGLE_ADS_MCP_INIT=PASS")
        assert process.stdin is not None
        process.stdin.write('{"jsonrpc":"2.0","method":"notifications/initialized"}\n')
        process.stdin.flush()

        tools = send("tools/list")
        names = {tool.get("name") for tool in tools.get("result", {}).get("tools", [])}
        customer_tool = next(
            (name for name in names if isinstance(name, str) and name.endswith("list_accessible_customers")),
            None,
        )
        if customer_tool is None:
            print("GOOGLE_ADS_MCP_READ_TOOLS=HOLD")
            return 2
        print("GOOGLE_ADS_MCP_READ_TOOLS=PASS")

        customers = send("tools/call", {"name": customer_tool, "arguments": {}})
        result = customers.get("result", {})
        if "error" in customers or result.get("isError"):
            print("GOOGLE_ADS_MCP_AUTH=HOLD_TOOL_ERROR")
            return 2
        payload = json.dumps(result, ensure_ascii=False)
        customer_refs = set(re.findall(r"customers/([0-9]+)", payload))
        if not customer_refs:
            # Some MCP versions return bare customer IDs in a structured list.
            customer_refs = set(re.findall(r"(?<![0-9])[0-9]{10}(?![0-9])", payload))
        print("GOOGLE_ADS_MCP_AUTH=PASS")
        print(f"GOOGLE_ADS_ACCOUNT_ACCESS={len(customer_refs)}")
        return 0 if len(customer_refs) == 1 else 2
    except (BrokenPipeError, RuntimeError, TimeoutError) as exc:
        print(f"GOOGLE_ADS_MCP_PROBE=HOLD_{type(exc).__name__.upper()}")
        return 2
    finally:
        process.terminate()
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()


if __name__ == "__main__":
    sys.exit(main())
