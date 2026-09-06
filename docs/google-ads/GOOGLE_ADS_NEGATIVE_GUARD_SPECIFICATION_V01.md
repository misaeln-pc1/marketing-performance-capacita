# Google Ads — Especificación Técnica del Guard de Palabras Clave Negativas V01

Estado: `NEGATIVE_GUARD_OFFLINE_CORE=PASS | LIVE_NEGATIVE_ADAPTER=IMPLEMENTED_HOLD_AUTH | NEGATIVE_LIVE_SNAPSHOT=HOLD_DATA_GAP`
Fecha: 2026-09-05
Issue padre: #85
Tarea canónica: `misaeln-pc1/capacita-task-hub#215`
Rama: `feature/marketing-official-read-control-plane-p0`

## 1. Propósito

Implementar un guard determinista, liviano e idempotente que aplique la política de negocio aprobada (`docs/google-ads/GOOGLE_ADS_NEGATIVE_KEYWORDS_INTENT_POLICY.md`) contra el estado de palabras clave negativas de Google Ads para:

1. Proveer una interfaz adapter de lectura para los 6 niveles de criterios oficiales (`customer_negative_criterion`, `shared_set`, `shared_criterion`, `campaign_shared_set`, `campaign_criterion`, `ad_group_criterion`).
2. Evitar volver a recomendar negativas ya activas o heredadas en el mismo alcance o mediante listas compartidas asociadas a la campaña.
3. Separar exclusiones globales de campaña respecto de señales de routing A/B/C.
4. Prevenir la aplicación indebida de negativas B2C a campañas B2B/Empresa (y viceversa), evaluando contratos explícitos de campaña.
5. Operar de forma estrictamente fail-closed ante campañas, intenciones, scopes o match types desconocidos (`HOLD_REVIEW` / `ERROR`).
6. Proteger términos core como "paso a paso" (excepción aprobada para Landing B desde cero) y la propuesta de valor protegida de la campaña.
7. Emitir `HOLD_DATA_GAP` con código de salida machine-readable cuando no exista lectura viva suficiente, sin degradar seguridad ni inventar datos.
8. Garantizar estricta idempotencia persistente entre procesos distintos mediante ledger `manifest_hash + recommendation_hash` (`PROCESS_2_RECOMMENDATIONS=0`).

## 2. Flujo Operativo

```text
READ_CANONICAL_POLICY
→ READ_LIVE_OR_SIMULATED_SNAPSHOT (Adapter / Cache)
→ VERIFY_FAIL_CLOSED_GATES (Scope, MatchType, CampaignContract, Intent)
→ DETECT_DUPLICATES_AGAINST_ACTIVE_CRITERIA_AND_SHARED_SETS
→ CHECK_VALUE_PROPOSITION_CONFLICTS
→ CHECK_PERSISTENT_LEDGER_IDEMPOTENCY
→ RECOMMEND_ONLY_DELTA
```

## 3. Contrato de Datos del Snapshot (Schema v1.1.0)

Todo snapshot vivo o export debe cumplir con el siguiente contrato mínimo sanitizado (sin IDs completos ni tokens en GitHub):

| Campo | Tipo / Valores | Descripción |
|---|---|---|
| `schema_version` | string (`1.1.0`) | Versión del contrato de datos. |
| `snapshot_at` | ISO 8601 string | Timestamp UTC de la lectura. |
| `customer_id_hash` | string (hash_...) | Identificador de cuenta publicitaria sanitizado mediante hash SHA-256. |
| `evidence_source` | Enum validado | Origen de la evidencia (`FIXTURE`, `HISTORICAL_EXPORT`, `LIVE_API_HOLD`, `LIVE_API_READ`, `SIMULATED_API`). |
| `status` | `READY` \| `HOLD_DATA_GAP` | Estado general del snapshot. |
| `hold_reason` | string \| null | Motivo explícito de bloqueo cuando el estado es `HOLD_DATA_GAP`. |
| `campaign_shared_sets` | Map `campaign_id_hash -> [shared_set_names]` | Attachments de listas compartidas a campañas. |
| `manifest_hash` | SHA-256 (16 chars) | Hash determinista recalculado de integridad y estado completo. |
| `items` | Array de NegativeKeywordItem | Lista de criterios de negativas (con status `ENABLED`, `PAUSED`, `REMOVED`). |

Items con estado `REMOVED` o `UNKNOWN` son filtrados por `active_items()` y nunca se consideran negativas activas.

## 4. Clasificación Canónica de Intenciones

1. `SOLUCION_PUNTUAL`: Búsquedas que buscan resolver una duda inmediata (ejercicios, ejemplos, fórmulas, BUSCARV, tablas dinámicas, plantillas, tutoriales). Se normalizan diacríticos y se negativizan para proteger presupuesto en campañas de cursos.
2. `EMPLEO`: Empleo, vacantes, bolsas de trabajo, currículum, búsqueda de trabajo. (Excepción: "curso excel para el trabajo" es intención comercial válida).
3. `MODALIDAD`: Términos no presenciales (online, en línea, virtual, zoom, a distancia) para campañas presenciales. Incompatibles como negativas en campañas de modalidad online.
4. `B2B_SENCE`: Empresa, SENCE, OTIC, franquicia tributaria, cotización, factura, "clases para empresas". Evaluada con precedencia antes de routing. Exclusiones para B2C, pero NUNCA aplicables a campañas B2B.
5. `CLASES_PARTICULARES`: Clases particulares, 1 a 1, a domicilio para productos grupales.
6. `FUERA_ALCANCE`: VBA, macros, Power BI, Python para cursos introductorios de Excel.
7. `ROUTING_A_B_C`: "desde cero", "principiante", "profesor", "clases", "personalizado". Términos legítimos para enrutamiento entre grupos de anuncios A/B/C. NO deben ser exclusión global.
8. `DESCONOCIDO`: Toda intención no categorizada. Falla cerrado con `HOLD_REVIEW`.

## 5. Reglas Duras de Evaluación (Fail-Closed)

1. **Fail-Closed para Campañas e Intenciones:**
   - Campaña desconocida o no registrada en `CampaignRegistry` → `PolicyDecision.HOLD_REVIEW`.
   - Intención desconocida (`DESCONOCIDO`) → `PolicyDecision.HOLD_REVIEW`.
   - Scope desconocido o MatchType desconocido → `PolicyDecision.ERROR`.
2. **Excepción "paso a paso":** `paso a paso` no es negativa global bajo ninguna circunstancia. Si un candidato lo contiene a nivel cuenta, lista compartida o campaña, el guard emite `CONFLICT` y lo rechaza.
3. **Routing vs Exclusión Global:** Términos clasificados como `ROUTING_A_B_C` solo pueden recomendarse como negativas exactas dentro de grupos de anuncios específicos para ceder tráfico a otro grupo. El guard rechaza su aplicación a nivel campaña o global con decisión `ROUTE`.
4. **Frontera B2C vs B2B y Compatibilidad de Modalidad:**
   - Una campaña clasificada como `B2B_EMPRESA` jamás puede recibir negativas de intención `B2B_SENCE` (`CONFLICT`).
   - Una campaña `B2C` presencial no puede negativizar sus propios pilares de oferta protegida ("presencial", "santiago", "capacita").
   - Una campaña con modalidad `ONLINE` o `MIXTA` no puede negativizar términos de modalidad no presencial (`CONFLICT`).
5. **Deduplicación contra Criterios Activos:** Si un término ya existe activo en el mismo match type y en el mismo scope o en un scope superior/adjunto (customer o shared set vinculado), el guard emite `PRESERVE` y no genera delta.
6. **Idempotencia Persistente entre Procesos:** Cada recomendación se registra en el ledger persistente mediante la clave `f"{manifest_hash}:{recommendation_hash}"`. Una segunda ejecución (en el mismo proceso o en un proceso independiente) produce exactamente 0 recomendaciones (`PROCESS_2_RECOMMENDATIONS=0`).
7. **Data Gap:** Si el snapshot no está disponible o la autenticación viva falla con `ACCESS_TOKEN_SCOPE_INSUFFICIENT`, el guard emite `NEGATIVE_RECOMMENDATION=HOLD_DATA_GAP`, entrega JSON machine-readable y detiene la CLI con código de salida 2.

## 6. Arquitectura del Componente

- `core/negative_guard/models.py`: Estructuras de datos, enums, hashing y serialización JSON (Schema v1.1.0).
- `core/negative_guard/campaign_contract.py`: Contratos explícitos de campaña (audiencia, producto, modalidad, familia, términos protegidos) y registro canónico.
- `core/negative_guard/classifier.py`: Clasificador de intenciones con precedencia B2B y normalización diacrítica.
- `core/negative_guard/guard.py`: Motor de reglas fail-closed, evaluación de lotes y deduplicación.
- `core/negative_guard/ledger.py`: Ledger persistente de recomendaciones para idempotencia entre procesos.
- `core/negative_guard/adapter.py`: Adaptador oficial READ para las 6 entidades de negativas de Google Ads.
- `core/negative_guard/snapshot.py`: Persistencia, sanitización y roundtrip verification de snapshots.
- `scripts/google_ads_readonly/run_negative_guard.py`: CLI fail-closed (sin demo implícito) para ejecución manual o en pipelines de lectura.
- `tests/test_negative_guard.py`: Suite de 13 pruebas unitarias y de regresión offline.

## 7. Almacenamiento Canónico de Pesados

Los snapshots completos o exports brutos generados por la API o scripts se almacenan en:
- **Bodega Canónica:** `SharePoint Site / Documentos / CAPACITA/Proyectos/external-files/marketing-performance-capacita`
- **Acceso Local Sincronizado:** `OneDrive "Sitio de comunicación - external-files"`
- En GitHub se conservan únicamente resúmenes agregados, manifiestos con hashes y fixtures sanitizados.
