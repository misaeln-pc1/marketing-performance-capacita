# AGENT_FEEDBACK

## Fecha
2026-09-05

## Agente
Gemini/Antigravity.

## Tarea recibida
Corrección obligatoria de los hallazgos P0/P1 del review formal del PR #86 (Review ID: `5123538405`) en la rama `feature/marketing-official-read-control-plane-p0`, en coordinación con ChatGPT / Global Control:
1. Calibración de estado honesto (`OFFLINE_CORE=PASS`, `LIVE_ADAPTER=IMPLEMENTED_HOLD_AUTH`, `LIVE_SNAPSHOT=HOLD_DATA_GAP`, `METHOD_COMPARISON=DESIGN_ONLY`, `LIVE_PARITY=NOT_RUN`, `METHOD_A=BASELINE_FALLBACK`).
2. Implementación de adaptador READ de estado vivo para 6 entidades de negativas con soporte mock e inyección segura.
3. Contrato de campaña fail-closed (`CampaignContract`, `CampaignRegistry`) con clasificación estricta de audiencia, producto, modalidad y rechazo fail-closed (`HOLD_REVIEW` / `CONFLICT` / `ERROR`).
4. Normalización Unicode/diacríticos (NFKD) y precedencia de clasificación B2B antes de routing A/B/C.
5. Idempotencia persistente entre procesos (`RecommendationLedger`) basada en `manifest_hash + recommendation_hash` en almacenamiento fuera de git / tempdir.
6. Snapshot completo (Schema 1.1.0, campaign_shared_sets, enums, hold_reason) y verificación de round-trip.
7. CLI fail-closed sin demos implícitos y salida machine-readable para `HOLD_DATA_GAP`.
8. Escaneo de seguridad real sobre el diff neto `origin/main...HEAD` y archivos modificados (0 secretos, 0 PII, 0 IDs sin hash).
9. Script Meta export blindado ante `Set-StrictMode -Version Latest` con pruebas mock.
10. Alineación documental en `DECISIONES.md`, `TASK_STATUS.md`, `CHANGELOG_AGENT.md` y especificaciones técnicas (Zoho marcado como `CONCEPTUAL_UNVERIFIED`).

## Resultado
Hecho.

## Evidencia
* Rama: `feature/marketing-official-read-control-plane-p0`
* PR: #86
* Commit SHA: Se registra en el commit subsiguiente a esta edición.
* Diff stat: 25 files changed (incluyendo adapter, campaign contract, ledger, strict mode mocks y suite de 13 pruebas).
* Comandos ejecutados:
  - `python -m unittest tests/test_negative_guard.py` (suite de 13 tests unitarios: 100% OK en 0.026s)
  - `powershell -NoProfile -ExecutionPolicy Bypass -File tests/test_meta_script_mock.ps1` (`META_SCRIPT_RUNTIME=MOCK_PASS`)
  - `python scripts/google_ads_readonly/run_negative_guard.py --snapshot-path tests/fixtures/negative_snapshot_fixtures.json --idempotency-check` (2 procesos/instancias independientes: proceso 1 = N, proceso 2 = 0)
  - `python scripts/google_ads_readonly/run_negative_guard.py` (fail-closed verificado: sin candidates ni demo arroja exit code 1)
  - `python scripts/run_offline_validations.py` (evaluando diff real `origin/main...HEAD`: 0 secretos, 0 PII, 0 IDs sin máscara, git whitespace limpio, tests 100% PASS)
* Pruebas realizadas:
  - 13/13 tests unitarios completados satisfactoriamente.
  - Idempotencia persistente verificada entre procesos independientes vía `RecommendationLedger`.
  - Normalización de tildes/diacríticos verificada (`fórmulas`, `tablas dinámicas`, `cómo hacer`, `búsqueda de trabajo`, `en línea`, `currículum`, `cotización`).
  - Precedencia B2B verificada: `clases para empresas` clasifica estrictamente como `B2B_SENCE`.
  - Exclusión de criterios `REMOVED` y `UNKNOWN` en snapshot y adapter.
  - Round-trip de snapshot probado (raw -> snapshot -> JSON -> snapshot -> hash idéntico).
  - CLI fail-closed probado.
  - Flatten de Meta Ads probado bajo PowerShell `Set-StrictMode -Version Latest`.
  - Auditoría de seguridad sobre diff completo `origin/main...HEAD`: 0 secretos, 0 PII.

## Objeciones o desacuerdos
Plenamente de acuerdo con el review de ChatGPT / Global Control (Review ID: `5123538405`).
Los hallazgos P0 y P1 identificaron con total precisión brechas entre la declaración documental y el estado real del código offline. Las correcciones implementadas elevan la robustez técnica al estándar de producción fail-closed sin necesidad de exponer credenciales vivas antes de tiempo.

## Riesgos detectados
1. **Scope y Credenciales Vivas (Google Ads & Meta Ads):** El adaptador y los scripts están listos y validados con mocks/fixtures, pero las conexiones vivas permanecen en `HOLD_WITH_EVIDENCE` / `HOLD_DATA_GAP` hasta que Misael autorice y configure credenciales OAuth con scope `adwords` y tokens formales de Meta.
2. **Metadata de Zoho CRM:** Los nombres de campos en la documentación analítica permanecen como `CONCEPTUAL_UNVERIFIED` hasta que se ejecute una lectura formal de metadata de la API de Zoho CRM.

## Archivos modificados
- `DECISIONES.md`
- `TASK_STATUS.md`
- `CHANGELOG_AGENT.md`
- `AGENT_FEEDBACK.md`
- `docs/analytics/MARKETING_OFFICIAL_READ_CONTROL_PLANE_V01.md`
- `docs/google-ads/GOOGLE_ADS_NEGATIVE_GUARD_SPECIFICATION_V01.md`
- `docs/meta-ads/META_ADS_READONLY_API_ROUTE_A_PROCEDURE_V01.md`
- `core/negative_guard/__init__.py`
- `core/negative_guard/models.py`
- `core/negative_guard/classifier.py`
- `core/negative_guard/guard.py`
- `core/negative_guard/snapshot.py`
- `scripts/google_ads_readonly/run_negative_guard.py`
- `scripts/meta_ads_readonly/export_meta_ads_readonly.ps1`
- `scripts/run_offline_validations.py`
- `tests/fixtures/negative_snapshot_fixtures.json`
- `tests/test_negative_guard.py`

## Archivos creados
- `core/negative_guard/campaign_contract.py`
- `core/negative_guard/adapter.py`
- `core/negative_guard/ledger.py`
- `tests/test_meta_script_mock.ps1`

## Qué no se tocó
- La rama histórica de PR #52 permaneció intacta; no se hizo merge de PR #52.
- No se crearon ramas nuevas ni PRs paralelos; todo el trabajo se concentró en PR #86.
- No se realizaron mutaciones ni escrituras en Google Ads, Meta Ads ni Zoho CRM (`ADS_WRITES=0`, `CRM_WRITES=0`, `PRODUCTION_WRITES=0`).
- No se realizó merge a `main` (`MERGE=0`).

## Siguiente recomendación
Hacer commit de las correcciones sobre la rama `feature/marketing-official-read-control-plane-p0`, hacer push a `origin` para actualizar el PR #86 y solicitar la re-revisión formal de ChatGPT / Global Control.
