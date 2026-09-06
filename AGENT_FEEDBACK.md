# AGENT_FEEDBACK

## Fecha
2026-09-06

## Agente
Gemini / Google Antigravity.

## Tarea recibida
Recuperación bootstrap de trabajo interrumpido y resolución exhaustiva de los P0 del review formal sobre el PR #86 (rama `feature/marketing-official-read-control-plane-p0`, Task Hub #215, Issue padre Marketing #85):
1. Recuperar y preservar todo el trabajo local no comprometido.
2. Resolver los hallazgos P0:
   - A. HMAC Fail-Closed: eliminar fallback público, requerir `CAPACITA_HMAC_KEY` externa, validar pre-hashed con regex estricto `^hash_[0-9a-f]{12}$`, rechazar `alias_*` y strings ambiguos, preservar sentinels `none`, `unknown`, `global`, `n/a`.
   - B. Ledger Atómico: unificar en `claim_once(...)` bajo un solo lock (reload -> validación -> existencia -> escritura) retornando `CLAIMED | ALREADY_EXISTS | HOLD`. Test con 2 subprocesos concurrentes para misma key con exactamente un emisor `CLAIMED`.
   - C. PAUSED: solo `ENABLED` es activo; `PAUSED` no bloquea como negativa activa y produce señal diferenciada `EXISTS_PAUSED` / `REVIEW_REACTIVATION` en los 4 alcances (`CUSTOMER`, `SHARED_SET`, `CAMPAIGN`, `AD_GROUP`).
   - D. Live Executor Google Ads: `GoogleAdsLiveExecutor` SELECT-only reutilizando `GoogleAdsClient.load_from_storage` y `search_stream`, cableado al `GoogleAdsNegativeReadAdapter`, configuración externa privada `--runtime-config-path`, sin imprimir IDs ni secretos, mapping operacional privado y demo solo para tests (`LIVE_EXECUTOR_WIRED=IMPLEMENTED_HOLD_AUTH`, `LIVE_API_CALL=NOT_RUN`, `LIVE_SNAPSHOT=HOLD_DATA_GAP`).
   - E. Meta Ads Error Sanitization: script productivo sanitiza excepciones fatales antes de `Write-Error`; test e2e `test_meta_e2e_sanitization.ps1` con código productivo y mock con token/URL sensible valida `TOKEN_IN_STDOUT=0`, `TOKEN_IN_STDERR=0`, `TOKEN_IN_MANIFEST=0`.
   - F. Manifest Tamper Detection: recálculo y comparación de `manifest_hash` al cargar snapshot en `from_dict`; mismatch genera `HOLD_REVIEW` / `MANIFEST_HASH_TAMPER_DETECTED`; preservado también el chequeo a nivel de item `state_hash`.
3. Reconciliar la rama con `origin/main` (que avanzó con PR #88: handoff Marketing → Edge, `VENUE_ID`, `CAMPAIGN_LAUNCH_ALLOWED`) sin perder ni sobrescribir el trabajo de PR #88, resolviendo cuidadosamente `TASK_STATUS.md`.
4. Ejecutar suite completa de pruebas (25 unit tests Python, 2 PowerShell scripts, runner de seguridad offline).
5. Commit + push sobre la misma rama.
6. Actualizar PR #86.
7. Detenerse sin hacer merge a `main`.

## Resultado
Hecho.

## Evidencia
* Rama: `feature/marketing-official-read-control-plane-p0`
* PR: #86
* HEAD inicial bootstrap: `2bdd3c8870dda3d80edb83bf8bdde1a8597a6313`
* Commits agregados:
  - `72a71dc`: `fix(marketing): resolve review P0 findings (HMAC fail-closed, atomic ledger claim, PAUSED signal, live executor wiring, manifest tamper, Meta error sanitization)`
  - `cfad2cd`: `chore(marketing): reconcile PR #86 with main (merge PR #88 edge handoff and slot publication)`
* Diff stat contra `origin/main`: 28 archivos modificados/creados, +5296 / -62 líneas.
* Comandos ejecutados y validaciones:
  - `python -m unittest discover -s tests -p "test_*.py"`: 25 tests OK en ~2.5s.
  - `powershell -ExecutionPolicy Bypass -File tests/test_meta_script_mock.ps1`: `META_PRODUCTION_CODE_MOCK=PASS`, `META_SCRIPT_RUNTIME=MOCK_PASS`.
  - `powershell -ExecutionPolicy Bypass -File tests/test_meta_e2e_sanitization.ps1`: `TOKEN_IN_STDOUT=0`, `TOKEN_IN_STDERR=0`, `TOKEN_IN_MANIFEST=0`, `META_END_TO_END_ERROR_SANITIZATION=PASS`.
  - `python scripts/run_offline_validations.py`: `ALL OFFLINE VALIDATIONS PASSED CLEANLY (100%)`, `SECRETS_IN_DIFF_AND_FILES=0`, `PII_IN_DIFF_AND_FILES=0`, `RAW_IDS_IN_DIFF_AND_FILES=0`.
  - `git diff origin/main...HEAD --check`: salida limpia, sin errores de whitespace ni marcadores de conflicto.
* Pruebas destacadas implementadas:
  - `test_19_invalid_prehashed_id_rejected`: validación estricta de formato `^hash_[0-9a-f]{12}$` y rechazo de `alias_*` / strings enmascarados.
  - `test_20_sentinels_preserved`: sentinels `none`, `unknown`, `global`, `n/a` preservados sin hashing.
  - `test_21_atomic_ledger_claim_concurrent_subprocesses`: dos subprocesos de Python compitiendo concurrentemente por la misma recomendación: exactamente un `CLAIMED` y un `ALREADY_EXISTS`, total entradas en ledger = 1.
  - `test_22_paused_not_active`: los criterios `PAUSED` no se consideran activos en `active_items()`, cubren los 4 scopes (`CUSTOMER`, `SHARED_SET`, `CAMPAIGN`, `AD_GROUP`) y generan señal diferenciada `EXISTS_PAUSED` / `REVIEW_REACTIVATION`.
  - `test_23_live_executor_wired_hold_auth`: `GoogleAdsLiveExecutor` existe, solo permite `SELECT`, y falla cerrado ante configuración ausente o incompleta.
  - `test_24_private_campaign_mapping_required`: registry sin contratos falla cerrado ante cualquier candidato; carga de archivo inexistente falla cerrado.
  - `test_25_manifest_hash_tamper_detection`: manipulación de shared sets, status, hold_reason, adición de items o remoción de items detectada con `MANIFEST_HASH_TAMPER_DETECTED -> HOLD_REVIEW`; roundtrip limpio preserva `READY`.

## Objeciones o desacuerdos
Ninguno. Plenamente alineado con el plan de control global y las especificaciones técnicas. La arquitectura fail-closed previene cualquier emisión errónea o fuga de información.

## Riesgos detectados
1. **Credenciales en vivo (Google Ads & Meta Ads):** El executor y los adaptadores están completamente cableados y cubiertos por pruebas offline; la ejecución en vivo requiere inyección de archivo runtime privado y credenciales con scope adecuado (`adwords` para Google Ads, token para Meta). Se mantiene honestamente en `HOLD_AUTH` / `HOLD_DATA_GAP` sin llamadas de red no autorizadas.
2. **Campos conceptuales en CRM:** Se preserva `DESIGNED_CONCEPTUAL_UNVERIFIED` para campos de Zoho CRM hasta contar con inspección de metadata formal.

## Archivos modificados en este ciclo
- `core/negative_guard/__init__.py`
- `core/negative_guard/campaign_contract.py`
- `core/negative_guard/classifier.py`
- `core/negative_guard/guard.py`
- `core/negative_guard/ledger.py`
- `core/negative_guard/models.py`
- `core/negative_guard/live_executor.py` [NUEVO]
- `scripts/google_ads_readonly/run_negative_guard.py`
- `scripts/meta_ads_readonly/export_meta_ads_readonly.ps1`
- `tests/fixtures/negative_snapshot_fixtures.json`
- `tests/test_negative_guard.py`
- `tests/test_meta_e2e_sanitization.ps1` [NUEVO]
- `TASK_STATUS.md`
- `AGENT_FEEDBACK.md`
- `REVIEW_REQUEST.md`
- `CHANGELOG_AGENT.md`

## Qué no se tocó
- NO se mergeó a `main` (`MERGE=0`).
- NO se tocó la rama histórica de PR #52.
- NO se ejecutaron mutaciones en plataformas de Ads (`ADS_WRITES=0`), CRM (`CRM_WRITES=0`) ni producción (`PRODUCTION_WRITES=0`).
- NO se subieron tokens, credenciales ni PII.

## Siguiente recomendación
Hacer push del commit de documentación sobre la rama `feature/marketing-official-read-control-plane-p0`, actualizar el body del PR #86 en GitHub reflejando los 25 tests y la reconciliación con `main`, y notificar en Task Hub #215, Marketing #85 y AI OS #40. Mantener el PR en estado `DRAFT_READY_FOR_FINAL_REVIEW` sin mergear.
