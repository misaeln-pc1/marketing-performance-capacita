# Google Ads — Especificación Técnica del Guard de Palabras Clave Negativas V01

Estado: `IMPLEMENTADO_Y_PROBADO_OFFLINE`
Fecha: 2026-09-05
Issue padre: #85
Tarea canónica: `misaeln-pc1/capacita-task-hub#215`
Rama: `feature/marketing-official-read-control-plane-p0`

## 1. Propósito

Implementar un guard determinista, liviano e idempotente que aplique la política de negocio aprobada (`docs/google-ads/GOOGLE_ADS_NEGATIVE_KEYWORDS_INTENT_POLICY.md`) contra el estado vivo de palabras clave negativas de Google Ads para:

1. Leer el estado vivo de negativas en todos los niveles (cuenta, shared sets, campañas, grupos de anuncios).
2. Evitar volver a recomendar negativas ya activas o heredadas en el mismo alcance.
3. Separar exclusiones globales de campaña respecto de señales de routing A/B/C.
4. Prevenir la aplicación indebida de negativas B2C a campañas B2B/Empresa (y viceversa).
5. Proteger términos core como "paso a paso" (excepción aprobada para Landing B desde cero).
6. Emitir `HOLD_DATA_GAP` cuando no exista lectura viva suficiente, sin degradar seguridad ni inventar datos.
7. Garantizar estricta idempotencia (la segunda ejecución sobre el mismo estado emite 0 recomendaciones).

## 2. Flujo Operativo

```text
READ_CANONICAL_POLICY
→ READ_LIVE_NEGATIVE_STATE
→ NORMALIZE_SCOPE_AND_MATCH_TYPE
→ MAP_CAMPAIGN_OWNERSHIP_B2C_B2B
→ DETECT_DUPLICATE_OR_CONFLICT
→ RECOMMEND_ONLY_DELTA
```

## 3. Contrato de Datos del Snapshot

Todo snapshot vivo o export debe cumplir con el siguiente contrato mínimo sanitizado (sin IDs completos en GitHub):

| Campo | Tipo / Valores | Descripción |
|---|---|---|
| `snapshot_at` | ISO 8601 string | Timestamp UTC de la lectura. |
| `customer_id_hash` | string (hash_...) | Identificador de cuenta publicitaria sanitizado mediante hash SHA-256. |
| `campaign_id_hash` | string (hash_...) | Identificador de campaña sanitizado. |
| `campaign_name` | string | Nombre de la campaña. |
| `ad_group_id_hash` | string (hash_...) | Identificador de grupo de anuncios sanitizado. |
| `ad_group_name` | string | Nombre del grupo de anuncios. |
| `source_scope` | `CUSTOMER` \| `SHARED_SET` \| `CAMPAIGN` \| `AD_GROUP` | Alcance donde reside la negativa. |
| `shared_set_name` | string | Nombre de la lista compartida, si aplica. |
| `keyword_text` | string | Término normalizado (sin corchetes, comillas ni espacios redundantes). |
| `match_type` | `EXACT` \| `PHRASE` \| `BROAD` | Tipo de concordancia normalizado. |
| `status` | `ENABLED` \| `REMOVED` \| `UNKNOWN` | Estado del criterio. |
| `intent_class` | Enum (ver sección 4) | Clasificación de intención. |
| `policy_decision` | `PRESERVE` \| `REVIEW` \| `ROUTE` \| `CONFLICT` \| `CANDIDATE` \| `HOLD_DATA_GAP` | Veredicto del guard. |
| `evidence_source` | `LIVE_API` \| `LIVE_MCP` \| `HISTORICAL_EXPORT` \| `FIXTURE` | Origen de la evidencia. |
| `state_hash` | SHA-256 (16 chars) | Hash de integridad para auditoría y drift. |

## 4. Clasificación Canónica de Intenciones

1. `SOLUCION_PUNTUAL`: Búsquedas que buscan resolver una duda inmediata (ejercicios, ejemplos, fórmulas, BUSCARV, tablas dinámicas, plantillas, tutoriales). Se negativizan deliberadamente para proteger presupuesto en campañas de cursos.
2. `EMPLEO`: Empleo, vacantes, bolsas de trabajo. (Excepción: "curso excel para el trabajo" es intención comercial válida).
3. `MODALIDAD`: Términos no presenciales (online, virtual, zoom, a distancia) para campañas presenciales.
4. `B2B_SENCE`: Empresa, SENCE, OTIC, franquicia tributaria, factura. Exclusiones para B2C, pero NUNCA aplicables a campañas B2B.
5. `CLASES_PARTICULARES`: Clases particulares, 1 a 1, a domicilio para productos grupales.
6. `FUERA_ALCANCE`: VBA, macros, Power BI, Python para cursos introductorios de Excel.
7. `ROUTING_A_B_C`: "desde cero", "principiante", "profesor", "clases". Términos legítimos para enrutamiento entre grupos de anuncios A/B/C. NO deben ser exclusión global.

## 5. Reglas Duras de Evaluación

1. **Excepción "paso a paso":** `paso a paso` no es negativa global bajo ninguna circunstancia. Si un candidato lo contiene a nivel cuenta, lista compartida o campaña, el guard emite `CONFLICT` y lo rechaza.
2. **Routing vs Exclusión Global:** Términos clasificados como `ROUTING_A_B_C` solo pueden recomendarse como negativas exactas dentro de grupos de anuncios específicos para ceder tráfico a otro grupo (ej. grupo A excluye "desde cero" para que el grupo B lo capture). El guard rechaza su aplicación a nivel campaña o global con decisión `ROUTE`.
3. **Frontera B2C vs B2B:**
   - Una campaña clasificada como `B2B_EMPRESA` jamás puede recibir negativas de intención `B2B_SENCE` (conflicto severo).
   - Una campaña `B2C` no puede negativizar sus propios pilares de oferta ("presencial", "santiago", "curso").
4. **Deduplicación:** Si un término ya existe en el mismo match type y en el mismo scope o en un scope superior jerárquico (ej. customer level o shared set vinculado), el guard emite `PRESERVE` y no genera delta.
5. **Idempotencia:** Una recomendación emitida queda registrada por su hash de recomendación. En ejecuciones sucesivas sobre el mismo snapshot, el número de recomendaciones emitidas es 0.
6. **Data Gap:** Si el snapshot no está disponible o la autenticación viva falla con `ACCESS_TOKEN_SCOPE_INSUFFICIENT`, el guard emite `NEGATIVE_RECOMMENDATION=HOLD_DATA_GAP` y se detiene sin inventar recomendaciones.

## 6. Arquitectura del Componente

- `core/negative_guard/models.py`: Estructuras de datos, enums, hashing y serialización JSON.
- `core/negative_guard/classifier.py`: Clasificador de campañas (B2C, B2B_EMPRESA, UNKNOWN) e intenciones de búsqueda.
- `core/negative_guard/guard.py`: Motor de reglas y evaluación de lotes.
- `core/negative_guard/snapshot.py`: Persistencia y sanitización de snapshots.
- `scripts/google_ads_readonly/run_negative_guard.py`: CLI para ejecución manual o en pipelines de lectura.
- `tests/test_negative_guard.py`: Suite de 10 pruebas unitarias y de regresión offline.

## 7. Almacenamiento Canónico de Pesados

Los snapshots completos o exports brutos generados por la API o scripts se almacenan en:
- **Bodega Canónica:** `SharePoint Site / Documentos / CAPACITA/Proyectos/external-files/marketing-performance-capacita`
- **Acceso Local Sincronizado:** `OneDrive "Sitio de comunicación - external-files"`
- En GitHub se conservan únicamente resúmenes agregados, manifiestos con hashes y fixtures sanitizados.
