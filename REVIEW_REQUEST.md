# REVIEW_REQUEST

## Objetivo de revisión vigente

Revisar y consolidar las correcciones P0 y DoD para el Review ID `5123583986` en el PR #86, rama `feature/marketing-official-read-control-plane-p0` (Issue padre #85 / Task Hub #215).

## Rama y Contexto

- **Repo:** `misaeln-pc1/marketing-performance-capacita`
- **Rama:** `feature/marketing-official-read-control-plane-p0`
- **PR:** #86
- **Review ID Resuelto:** `5123583986`
- **HEAD base del review:** `be31ae91c58b16ed0be580c00254fb8ca09d8608`

## Módulos y Código Principales

1. `docs/google-ads/GOOGLE_ADS_NEGATIVE_GUARD_SPECIFICATION_V01.md` (especificación técnica deduplicada)
2. `docs/analytics/MARKETING_OFFICIAL_READ_CONTROL_PLANE_V01.md` (control plane con eliminación de referencias a staging)
3. `core/negative_guard/`
   - `models.py`: hashes recalibrados, HMAC secreto fuera de git, sentinels preservados, state_hash recalculado.
   - `campaign_contract.py`: mapping por `campaign_id_hash`, fail-closed ante ambigüedad, validación de routing A/B/C y alineación B2C/B2B.
   - `classifier.py`: clasificación de intención ampliada con `SOLUCION_PUNTUAL` compuesta.
   - `guard.py`: evaluación match-aware y scope-aware de protected terms, validación de producto/modalidad, ledger atómico.
   - `ledger.py`: fail-closed ante corrupción (HOLD), lock atómico entre procesos concurrentes.
   - `adapter.py`: queries GAQL oficiales de 6 entidades (`customer_negative_criterion` vía shared sets, tipos `NEGATIVE_KEYWORDS` y `ACCOUNT_LEVEL_NEGATIVE_KEYWORDS`, filtros de tipo `KEYWORD`, descarte de sets `REMOVED`).
   - `snapshot.py`: serialización y verificación roundtrip.
4. `scripts/google_ads_readonly/run_negative_guard.py`: CLI de ejecución y evaluación.
5. `scripts/meta_ads_readonly/MetaAdsExportHelpers.psm1`: módulo PowerShell productivo importable con sanitización estricta.
6. `scripts/meta_ads_readonly/export_meta_ads_readonly.ps1`: script productivo Meta Ads read-only.
7. `tests/test_negative_guard.py`: suite de 16 tests unitarios y de regresión offline.
8. `tests/test_meta_script_mock.ps1`: test de código productivo Meta Ads con mock local sin duplicación.
9. `tests/fixtures/negative_snapshot_fixtures.json`: fixture sanitizado.
10. `scripts/run_offline_validations.py`: runner integral offline con verificación `origin/main` y assert de 2 subprocesos concurrentes.

## Hallazgos y Resultados Operativos / DoD

```text
GAQL_FIELD_VALIDATION=PASS
ACCOUNT_LEVEL_NEGATIVE_LIST=PASS
KEYWORD_TYPE_FILTERS=PASS
REMOVED_SHARED_SET_FILTER=PASS
CAMPAIGN_ID_MAPPING=PASS
AMBIGUOUS_MAPPING_FAIL_CLOSED=PASS
B2C_B2B_POLICY_ALIGNMENT=PASS
A_B_C_TARGET_ROUTING=PASS
PRODUCT_COMPATIBILITY=PASS
PROTECTED_TERM_COMPOUND_TESTS=PASS
LEDGER_CORRUPTION_FAIL_CLOSED=PASS
TWO_SUBPROCESS_IDEMPOTENCY=PASS
STATE_HASH_TAMPER_DETECTION=PASS
PUBLIC_ID_PSEUDONYMIZATION=PASS
META_PRODUCTION_CODE_MOCK=PASS
SECURITY_SCAN_REAL_DIFF=PASS
PR_METADATA_ALIGNMENT=PASS
OFFLINE_CORE=PASS
LIVE_ADAPTER=IMPLEMENTED_HOLD_AUTH
LIVE_SNAPSHOT=HOLD_DATA_GAP
LIVE_PARITY=NOT_RUN
ADS_WRITES=0
CRM_WRITES=0
PRODUCTION_WRITES=0
MERGE=0
PR_STATUS=DRAFT_READY_FOR_REREVIEW
```

## Pruebas Realizadas

- **Suite de 16 pruebas unitarias (`test_negative_guard.py`):** PASS (16/16 en ~0.48s).
- **Prueba de dos procesos concurrentes / ledger idempotency:** `PROCESS_1_RECOMMENDATIONS > 0` y `PROCESS_2_RECOMMENDATIONS = 0` (PASS).
- **Prueba de detección de manipulación de estado / hash tamper:** `STATE_HASH_TAMPER_DETECTED -> HOLD_REVIEW` (PASS).
- **Prueba de código productivo Meta Ads (`test_meta_script_mock.ps1`):** PASS, importación directa de `MetaAdsExportHelpers.psm1` con sanitización probada de URLs, query strings y mensajes de excepción.
- **Escaneo de seguridad en diff real contra `origin/main` y archivos modificados:**
  - `SECRETS_IN_DIFF_AND_FILES = 0`
  - `PII_IN_DIFF_AND_FILES = 0`
  - `RAW_IDS_IN_DIFF_AND_FILES = 0`
- **Git whitespace check:** PASS (0 trailing whitespace ni space before tab).

## Guardrails Cumplidos

- Cero modificaciones de campañas, pujas, anuncios o presupuestos reales (`ADS_WRITES=0`).
- Cero modificaciones o escrituras en Zoho CRM (`CRM_WRITES=0`).
- Cero escrituras en servidores web, Cloudflare o producción (`PRODUCTION_WRITES=0`).
- No se ejecutó OAuth vivo ni conexión live no autorizada.
- PR no mergeado (`MERGE=0`).

## Gate

```text
PR_LISTO_PARA_RE_REVISION
NO_MERGEAR_SIN_AUTORIZACION_MISAEL
```
