# AGENT_FEEDBACK

## Fecha
2026-09-06

## Agente
Gemini / Google Antigravity.

## Tarea recibida
Resolver exclusivamente el último bloqueo de revisión (Global Review ID: 5124064245):
Compatibilidad real de `GoogleAdsLiveExecutor` con filas protobuf y proto-plus.

1. En `core/negative_guard/live_executor.py`:
   - Hacer `_protobuf_row_to_dict()` compatible explícitamente con los dos formatos oficialmente soportados por `google-ads-python`:
     1. Protobuf nativo (`google.protobuf.message.Message`);
     2. `proto-plus` (`proto.Message`).
   - Para proto-plus: convertir primero al protobuf subyacente usando la utilidad oficial de `google-ads-python` (`google.ads.googleads.util.convert_proto_plus_to_protobuf`) o mecanismo equivalente soportado (`type(row).pb(row)` / `row._pb`).
   - Convertir a dict preservando la estructura anidada que espera `GoogleAdsNegativeReadAdapter` (`campaign`, `ad_group`, `shared_set`, `customer_negative_criterion`, `shared_criterion`, `campaign_criterion`, `ad_group_criterion`, `keyword`).
   - Eliminar `str(row)` como fallback operativo.
   - Si el tipo de fila no puede convertirse: fail-closed (`TypeError`) sin inventar estructura.
2. En `core/negative_guard/adapter.py`:
   - Fortalecer defensivamente la lectura de criterios (`shared_criterion`, `campaign_criterion`, `ad_group_criterion`) para aceptar tanto `keyword` en la raíz como anidado en el criterio, junto con su estado `status`.
3. Agregar pruebas offline que cubran:
   - GoogleAdsRow-like protobuf;
   - GoogleAdsRow-like proto-plus;
   - Resultado anidado consumible por `GoogleAdsNegativeReadAdapter`;
   - Formato desconocido -> fail-closed.
4. Ejecutar suite completa (Python unittests, PowerShell scripts, offline validations, git diff check).
5. Mantener guardrails: `LIVE_API_CALL=NOT_RUN`, `LIVE_SNAPSHOT=HOLD_DATA_GAP`, `ADS_WRITES=0`, `CRM_WRITES=0`, `PRODUCTION_WRITES=0`, `MERGE=0`.

## Resultado
Hecho.

## Evidencia
* Rama: `feature/marketing-official-read-control-plane-p0`
* PR: #86
* HEAD revisado anterior: `82f54d01a5067a1f87f482b47a9dc9726a7a7bfe`
* Comandos ejecutados y validaciones:
  - `python -m unittest discover -s tests -p "test_*.py"`: 29/29 tests PASS en 3.25s.
  - `powershell -ExecutionPolicy Bypass -File tests/test_meta_script_mock.ps1`: `META_PRODUCTION_CODE_MOCK=PASS`, `META_SCRIPT_RUNTIME=MOCK_PASS`.
  - `powershell -ExecutionPolicy Bypass -File tests/test_meta_e2e_sanitization.ps1`: `TOKEN_IN_STDOUT=0`, `TOKEN_IN_STDERR=0`, `TOKEN_IN_MANIFEST=0`, `META_END_TO_END_ERROR_SANITIZATION=PASS`.
  - `python scripts/run_offline_validations.py`: `ALL OFFLINE VALIDATIONS PASSED CLEANLY (100%)`, `SECRETS_IN_DIFF_AND_FILES=0`, `PII_IN_DIFF_AND_FILES=0`, `RAW_IDS_IN_DIFF_AND_FILES=0`.
  - `git diff origin/main...HEAD --check`: limpio.
* Pruebas nuevas implementadas:
  - `test_26_protobuf_row_conversion`: Conversión real de fila protobuf nativa a dict con estructura anidada y sin fallback `_raw`.
  - `test_27_proto_plus_row_conversion`: Conversión real de fila proto-plus a dict con estructura anidada y sin fallback `_raw`.
  - `test_28_row_conversion_consumed_by_adapter`: Filas convertidas en los 6 tipos (`shared_set`, `customer_negative_criterion`, `shared_criterion`, `campaign_shared_set`, `campaign_criterion`, `ad_group_criterion`) son consumidas por `GoogleAdsNegativeReadAdapter`, produciendo un snapshot `READY` con 3 items en los scopes `CUSTOMER`, `CAMPAIGN` y `AD_GROUP`.
  - `test_29_unknown_row_fail_closed`: Tipos no soportados (`str`, `int`, `dict`, `None`, `list`, `object()`) lanzan `TypeError` con mensaje `ROW_CONVERSION_FAILED`.

## Objeciones o desacuerdos
Ninguno. Plenamente de acuerdo con el requerimiento de formalizar la conversión de filas de Google Ads a protobuf y proto-plus sin depender de representaciones de texto ni heurísticas inseguras.

## Riesgos detectados
Ninguno detectado en el cambio. La compatibilidad dual garantiza soporte tanto para entornos donde `use_proto_plus=True` (default oficial) como donde se trabaje con mensajes protobuf puros.

## Archivos modificados en este ciclo
- `core/negative_guard/live_executor.py`
- `core/negative_guard/adapter.py`
- `tests/test_negative_guard.py`
- `CHANGELOG_AGENT.md`
- `AGENT_FEEDBACK.md`
- `REVIEW_REQUEST.md`

## Qué no se tocó
- NO se tocó ninguna otra parte de Negative Guard ni su taxonomía.
- NO se ejecutó OAuth en vivo ni llamadas de red.
- NO se creó otra rama ni otro PR.
- NO se hizo merge a `main` (`MERGE=0`).
- Cero escrituras en Ads, CRM o Producción (`ADS_WRITES=0`, `CRM_WRITES=0`, `PRODUCTION_WRITES=0`).

## Siguiente recomendación
Hacer commit y push a la rama `feature/marketing-official-read-control-plane-p0`, actualizar el body del PR #86 en GitHub y notificar la resolución del Review ID 5124064245. Mantener en modo DRAFT para revisión final.

