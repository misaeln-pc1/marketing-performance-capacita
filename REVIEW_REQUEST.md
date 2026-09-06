# REVIEW_REQUEST

## Objetivo de revisión vigente

Revisión final de PR #86, rama `feature/marketing-official-read-control-plane-p0` (Issue padre Marketing #85 / Task Hub #215), con resolución total del último bloqueo de revisión (Global Review ID: 5124064245): compatibilidad real de `GoogleAdsLiveExecutor` con filas protobuf nativo y `proto-plus`.

## Rama y Contexto

- **Repo:** `misaeln-pc1/marketing-performance-capacita`
- **Rama:** `feature/marketing-official-read-control-plane-p0`
- **PR:** #86
- **Task Hub:** `capacita-task-hub#215`
- **Issue Padre:** `marketing-performance-capacita#85`
- **Última revisión formal resuelta:** `REVIEW_ID=5124064245`
- **HEAD base de revisión:** `82f54d01a5067a1f87f482b47a9dc9726a7a7bfe`

## Módulos y Código Principales

1. `core/negative_guard/`
   - `live_executor.py`: `_protobuf_row_to_dict()` y `_row_to_protobuf_message()` compatibles explícitamente con `google.protobuf.message.Message` y `proto.Message`. Convierte proto-plus al protobuf subyacente con `google.ads.googleads.util.convert_proto_plus_to_protobuf` (o fallback `type(row).pb(row)` / `row._pb`). Serializa vía `MessageToDict` preservando nombres de proto, normaliza `type_` -> `type`, y promueve `keyword` a la raíz de la fila. Falla cerrado (`TypeError`) ante tipos desconocidos/no soportados; nunca usa `str(row)` como fallback operativo.
   - `adapter.py`: Adaptador oficial v17+ para negative keyword criteria en 6 entidades (`customer_negative_criterion` vía shared sets, tipos `NEGATIVE_KEYWORDS` y `ACCOUNT_LEVEL_NEGATIVE_KEYWORDS`, filtros de tipo `KEYWORD`, descarte de sets `REMOVED`). Fortalecido para inspeccionar directamente el sub-objeto `keyword` y `status` dentro de cada criterio (`shared_criterion`, `campaign_criterion`, `ad_group_criterion`).
   - `models.py`: Seudonimización estricta fail-closed con `CAPACITA_HMAC_KEY` obligatoria; validación regex `^hash_[0-9a-f]{12}$`; rechazo de `alias_*` y strings ambiguos; preservación de sentinels (`none`, `unknown`, `global`, `n/a`); recálculo y detección de manipulación de `manifest_hash` y `state_hash` (`HOLD_REVIEW`); soporte para `CriterionStatus.PAUSED` excluido de `active_items()`.
   - `ledger.py`: Deduplicación interproceso atómica mediante `claim_once(...)` bajo un único lock con recarga de disco y verificación de corrupción (`HOLD_CORRUPT`).
   - `guard.py`: Evaluación match-aware y scope-aware de protected terms; reglas de routing A/B/C y alineación B2C/B2B; detección y emisión de señal diferenciada `EXISTS_PAUSED` / `REVIEW_REACTIVATION`.
   - `campaign_contract.py`: Contratos de campaña canónicos; fail-closed ante campañas no registradas o ambiguas; soporte de contratos privados externos vía `load_contracts_from_json(...)` y contratos demo para tests.
2. `scripts/google_ads_readonly/run_negative_guard.py`: CLI de ejecución y evaluación con soporte de `--runtime-config-path`, cableado al executor y adaptador.
3. `scripts/meta_ads_readonly/export_meta_ads_readonly.ps1`: Script productivo con captura de errores sanitizada sin exponer tokens, URLs ni query strings.
4. `scripts/meta_ads_readonly/MetaAdsExportHelpers.psm1`: Módulo PowerShell con funciones de sanitización (`Sanitize-MetaText`, `Sanitize-MetaUri`).
5. `tests/test_negative_guard.py`: Suite de 29 pruebas unitarias y de integración offline cubriendo todas las especificaciones y hallazgos.
6. `tests/test_meta_script_mock.ps1`: Prueba de código productivo de Meta Ads bajo Strict Mode.
7. `tests/test_meta_e2e_sanitization.ps1`: Prueba end-to-end de sanitización de errores con tokens simulados verificando `TOKEN_IN_STDOUT=0`, `TOKEN_IN_STDERR=0`, `TOKEN_IN_MANIFEST=0`.
8. `TASK_STATUS.md`: Reconciliado con `main` incorporando handoff Marketing → Edge, `VENUE_ID`, `CAMPAIGN_LAUNCH_ALLOWED=YES` y prioridad Task Hub #215.

## Declaración Operativa y DoD

```text
PROTOBUF_ROW_CONVERSION=PASS
PROTO_PLUS_ROW_CONVERSION=PASS
UNKNOWN_ROW_FAIL_CLOSED=PASS
ADAPTER_NESTED_STRUCTURE=PASS
HMAC_EXTERNAL_KEY_REQUIRED=PASS
ATOMIC_LEDGER_CLAIM=PASS
SAME_KEY_CONCURRENT_PROCESSES=PASS
PAUSED_NOT_ACTIVE=PASS
LIVE_EXECUTOR_WIRED=IMPLEMENTED_HOLD_AUTH
LIVE_API_CALL=NOT_RUN
LIVE_SNAPSHOT=HOLD_DATA_GAP
PRIVATE_CAMPAIGN_MAPPING_REQUIRED=PASS
META_END_TO_END_ERROR_SANITIZATION=PASS
MANIFEST_HASH_TAMPER_DETECTION=PASS
MAIN_RECONCILIATION=PASS
TESTS=PASS (29/29 Python, 2/2 PowerShell)
SECURITY_SCAN_REAL_DIFF=PASS
SECRETS_IN_DIFF=0
PII_IN_DIFF=0
RAW_IDS_IN_DIFF=0
ADS_WRITES=0
CRM_WRITES=0
PRODUCTION_WRITES=0
MERGE=0
PR_STATUS=DRAFT_READY_FOR_FINAL_REVIEW
```

## Pruebas Ejecutadas

- **29 pruebas unitarias en Python (`test_negative_guard.py`):** 29/29 PASS en ~3.2s.
  - `test_26_protobuf_row_conversion`: PASS
  - `test_27_proto_plus_row_conversion`: PASS
  - `test_28_row_conversion_consumed_by_adapter`: PASS
  - `test_29_unknown_row_fail_closed`: PASS
- **Pruebas de PowerShell:**
  - `test_meta_script_mock.ps1`: PASS (`META_PRODUCTION_CODE_MOCK=PASS`).
  - `test_meta_e2e_sanitization.ps1`: PASS (`META_END_TO_END_ERROR_SANITIZATION=PASS`).
- **Runner integral de validaciones offline (`run_offline_validations.py`):** 100% PASS.
- **Git whitespace check:** Salida limpia sin advertencias.

## Guardrails

- NO se modificó ninguna campaña real ni presupuesto (`ADS_WRITES=0`).
- NO se escribió en CRM (`CRM_WRITES=0`).
- NO se tocó producción ni servidores (`PRODUCTION_WRITES=0`).
- NO se hizo merge a `main` (`MERGE=0`).
- PR listo en modo borrador para revisión formal.
