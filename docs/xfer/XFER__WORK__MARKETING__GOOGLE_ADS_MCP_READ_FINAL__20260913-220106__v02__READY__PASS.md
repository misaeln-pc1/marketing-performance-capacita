# XFER — Google Ads MCP READ final

```text
CASE=GOOGLE_ADS_MCP_READ_FINAL
VERSION=v02
STATE=READY
DECISION=PASS
DATE=2026-09-13
ISSUE=104
PR=103
BRANCH=feature/marketing-google-official-permanent-read
```

## Resultado

La conexión primaria directa quedó operativa:

```text
ChatGPT
-> Capacita Google Ads READ
-> OpenAI Secure MCP Tunnel
-> Google Ads MCP oficial
-> Service Account con permiso Solo lectura
-> Google Ads API
```

Evidencia sanitizada:

```text
LOCAL_LAUNCHER_REPRODUCIBLE=PASS
TUNNEL_CONTROL_PLANE=PASS
TUNNEL_REAL_TO_GOOGLE_ADS_MCP=PASS
WORKSPACE_TUNNEL_BINDING=PASS
CHATGPT_GOOGLE_ADS_TOOLS=PASS
GOOGLE_ADS_MCP_INIT=PASS
GOOGLE_ADS_MCP_READ_TOOLS=PASS
GOOGLE_ADS_MCP_AUTH=PASS
GOOGLE_ADS_ACCOUNT_ACCESS=1
LIVE_READ_QUERY=PASS
CUSTOMER_COUNT=1
SECRETS_IN_GITHUB=0
ADS_WRITES=0
GA4_CONFIG_WRITES=0
MERGE=0
```

La consulta viva desde un chat nuevo del proyecto `MKT - Cloud` llamó la herramienta oficial `customers_list_accessible_customers`. El identificador de cliente no se registra en este XFER.

## Artefactos

- `scripts/google_ads_mcp_read/Start-CapacitaGoogleAdsMcpRead.ps1`
- `scripts/google_ads_mcp_read/probe_official_mcp.py`
- `scripts/google_ads_mcp_read/README.md`
- `docs/ads-connectivity/ADS_MCP_SECURE_CONNECTION_RUNBOOK_V01_2026-09-13.md`

El launcher del Escritorio apunta al script versionado, solicita la Runtime API key con entrada oculta y mantiene esa clave sólo durante la vida del proceso.

## Alcance preservado

- No se ejecutaron mutaciones en Google Ads.
- No se configuró GA4.
- No se versionaron credenciales, tokens, claves privadas ni IDs de cliente.
- No se hizo merge.
- El XFER v01 `HOLD_OAUTH_INTERACTIVE_PASSKEY` queda superado para la ruta Google Ads READ por esta implementación basada en Service Account.

