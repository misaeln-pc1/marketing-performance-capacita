# AGENT_FEEDBACK

## Fecha
2026-09-05

## Agente
Gemini/Antigravity.

## Tarea recibida
Corrección obligatoria de los hallazgos P0 y cumplimiento integral del DoD para el Review ID `5123583986` sobre el PR #86 en la rama `feature/marketing-official-read-control-plane-p0`:
1. Reemplazo del GAQL de `customer_negative_criterion` por el modelo oficial v17+ basado en `negative_keyword_list.shared_set`, tipos `NEGATIVE_KEYWORDS` y `ACCOUNT_LEVEL_NEGATIVE_KEYWORDS`, y términos en `shared_criterion`.
2. Filtro estricto de tipos (`KEYWORD`), descarte de criterios sin keyword text, match type `UNKNOWN`, parents ausentes o shared sets `REMOVED`.
3. Campaign Mapping con clave principal `campaign_id_hash`, validación secundaria por nombre/familia, fail-closed ante ID no registrado, nombre incompatible, cero matches o matches múltiples. Retiro de campañas Meta del registry Google Ads.
4. Alineación B2C/B2B (permitir `B2B_SENCE` como intención excluible en B2C Excel) y matriz de routing A/B/C explícita (A y C ceden a B; B no negativiza dentro de B; profesor/clases solo en destinos válidos; fail-closed en grupos desconocidos).
5. Compatibilidad estricta de producto y modalidad (taxonomía Excel no aplicable a Power BI; no negativizar online en campañas online o mixtas; producto `UNKNOWN` -> `HOLD_REVIEW`).
6. Protected terms match-aware y scope-aware: eliminación de substring simple; evaluación por intención para frases compuestas con modificador (`curso excel presencial gratis`, `curso excel presencial empleo`, `curso excel para empresas`).
7. Ledger fail-closed: corrupción genera `HOLD_REVIEW` (no `{}`); lock atómico entre procesos concurrentes; prueba de dos subprocesos con `PROCESS_1_RECOMMENDATIONS > 0` y `PROCESS_2_RECOMMENDATIONS = 0`.
8. Hashes e identificadores: recálculo continuo de `state_hash` y detección de manipulación (`HOLD_REVIEW`); preservación de sentinels (`none`, `unknown`, `global`, `n/a`) sin hashear; HMAC dinámico fuera de git.
9. Meta productive code: extracción de helpers a módulo importable `MetaAdsExportHelpers.psm1`, eliminación de código duplicado en test, y sanitización estricta de URLs, query strings y mensajes de error.
10. Security validation: verificación obligatoria de `origin/main`, diff real `origin/main...HEAD`, escaneo de archivos completos modificados, y validación limpia de whitespace.
11. Documentación: deduplicación de títulos, eliminación de referencias restantes a staging, actualización de PR #86, `REVIEW_REQUEST.md`, `CHANGELOG_AGENT.md` y `AGENT_FEEDBACK.md`.

## Resultado
Hecho.

## Evidencia
* Rama: `feature/marketing-official-read-control-plane-p0`
* PR: #86
* Commit SHA: `f772342638e8feb8bd2c50e37f130a55ec333326`
* Diff stat: 26 archivos modificados/añadidos en el branch.
* Comandos ejecutados:
  - `python -m unittest tests/test_negative_guard.py` (16 tests unitarios y de integración offline: 100% OK en ~0.48s)
  - `powershell -NoProfile -ExecutionPolicy Bypass -File tests/test_meta_script_mock.ps1` (`META_SCRIPT_RUNTIME=MOCK_PASS`)
  - `python scripts/google_ads_readonly/run_negative_guard.py --snapshot-path tests/fixtures/negative_snapshot_fixtures.json --candidates-json "[{\"keyword_text\": \"curso excel online\", \"match_type\": \"PHRASE\", \"source_scope\": \"CAMPAIGN\", \"target_campaign_id_hash\": \"hash_c11111111111\"}]" --idempotency-check` (Run 1 = 1 recomendación; Run 2 = 0 recomendaciones)
  - `python scripts/run_offline_validations.py` (validación integral del diff contra `origin/main`: 16 tests unitarios PASS, idempotencia 2 subprocesos PASS, escaneo de diff y archivos completos con 0 secretos, 0 PII y 0 IDs crudos, git whitespace limpio)
* Pruebas realizadas:
  - 16/16 tests unitarios completados satisfactoriamente.
  - Account-level negatives vía shared sets y shared criteria probados.
  - Filtro de tipo no-keyword (`LOCATION`, `PLACEMENT`, `USER_LIST`), match type `UNKNOWN` y shared sets `REMOVED` probado.
  - Mapeo por `campaign_id_hash` con fail-closed ante ID desconocido, nombre incompatible y colisión probado.
  - Matriz de routing A/B/C y alineación B2C/B2B probada.
  - Verificación de producto/modalidad probada.
  - Frases compuestas con protected terms evaluadas por intención probadas.
  - Ledger con fail-closed ante archivo corrupto y concurrencia atómica probado.
  - Detección de manipulación de `state_hash` probada.
  - Identificadores seudonimizados preservando sentinels probados.
  - Módulo productivo Meta Ads con sanitización probado.
  - Auditoría de seguridad sobre diff completo `origin/main...HEAD`: 0 secretos, 0 PII, 0 IDs crudos.

## Objeciones o desacuerdos
Plenamente de acuerdo con el review de ChatGPT / Global Control (Review ID: `5123583986`).
Todas las observaciones P0 y requerimientos del DoD fueron abordados de manera quirúrgica y exhaustiva, asegurando fail-closed en cada subsistema y respetando los guardrails operativos de Capacita.

## Riesgos detectados
1. **Scope y Credenciales Vivas (Google Ads & Meta Ads):** El adaptador y los scripts están listos y validados con mocks/fixtures, pero las conexiones vivas permanecen en `HOLD_WITH_EVIDENCE` / `HOLD_DATA_GAP` hasta que Misael autorice y configure credenciales OAuth con scope `adwords` y tokens formales de Meta.
2. **Metadata de Zoho CRM:** Los nombres de campos en la documentación analítica permanecen como `CONCEPTUAL_UNVERIFIED` hasta que se ejecute una lectura formal de metadata de la API de Zoho CRM.

## Archivos modificados
- `DECISIONES.md`
- `TASK_STATUS.md`
- `CHANGELOG_AGENT.md`
- `AGENT_FEEDBACK.md`
- `REVIEW_REQUEST.md`
- `docs/analytics/MARKETING_OFFICIAL_READ_CONTROL_PLANE_V01.md`
- `docs/google-ads/GOOGLE_ADS_NEGATIVE_GUARD_SPECIFICATION_V01.md`
- `docs/meta-ads/META_ADS_READONLY_API_ROUTE_A_PROCEDURE_V01.md`
- `core/negative_guard/__init__.py`
- `core/negative_guard/models.py`
- `core/negative_guard/classifier.py`
- `core/negative_guard/guard.py`
- `core/negative_guard/snapshot.py`
- `core/negative_guard/campaign_contract.py`
- `core/negative_guard/adapter.py`
- `core/negative_guard/ledger.py`
- `scripts/google_ads_readonly/run_negative_guard.py`
- `scripts/meta_ads_readonly/export_meta_ads_readonly.ps1`
- `scripts/run_offline_validations.py`
- `tests/fixtures/negative_snapshot_fixtures.json`
- `tests/test_negative_guard.py`

## Archivos creados
- `core/negative_guard/campaign_contract.py`
- `core/negative_guard/adapter.py`
- `core/negative_guard/ledger.py`
- `scripts/meta_ads_readonly/MetaAdsExportHelpers.psm1`
- `tests/test_meta_script_mock.ps1`

## Qué no se tocó
- No se tocó la rama `main` ni se realizó merge (`MERGE=0`).
- La rama histórica de PR #52 permaneció intacta; no se hizo merge de PR #52.
- No se crearon ramas nuevas ni PRs paralelos; todo el trabajo se concentró en PR #86.
- No se realizaron mutaciones ni escrituras en Google Ads, Meta Ads ni Zoho CRM (`ADS_WRITES=0`, `CRM_WRITES=0`, `PRODUCTION_WRITES=0`).
- No se generaron tokens ni credenciales vivas en repositorios ni logs.

## Siguiente recomendación
Hacer commit de las correcciones sobre la rama `feature/marketing-official-read-control-plane-p0`, hacer push a `origin` para actualizar el PR #86, actualizar la descripción del PR y notificar en los canales correspondientes (PR #86, Issue #85, Task Hub #215, AI OS #40).
