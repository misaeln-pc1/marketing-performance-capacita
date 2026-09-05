# Marketing Proactive Opportunity Scan — V01

## Estado

```text
STATUS=PR_LISTO_PARA_MERGE
BECOMES=VIGENTE_EN_MAIN_ON_PR_83_MERGE
PROJECT_INSTRUCTIONS=V3_1_CANDIDATE_NOT_ACTIVE
ISSUE_OWNER=#62
SCOPE=ANALISIS_Y_HANDOFF
EXTERNAL_WRITES=0
```

Este protocolo complementa, no reemplaza:

- `docs/seo-ai/MARKETING_PAGE_VISIBILITY_PROTOCOL_V01.md`;
- `docs/GTM_CONSUMPTION_BRIDGE.md`;
- `templates/CAMPAIGN_BRIEF_GTM.md`;
- canónicos específicos de Google Ads, Meta Ads, PageSense y campañas.

## Problema que corrige

Marketing no debe limitarse a responder la pregunta literal ni entregar consejos generales. Ante una página, campaña, producto o señal de desempeño debe consultar la evidencia pertinente disponible, detectar oportunidades y proponer la siguiente mejor acción.

Principio:

```text
DECISION DE NEGOCIO
→ FUENTES PERTINENTES
→ HALLAZGO
→ PRIORIDAD
→ ACCION EJECUTABLE
→ VALIDACION
→ APRENDIZAJE
```

## Activación automática

Aplicar este protocolo sin esperar una petición granular cuando Misael:

- muestre, publique o solicite revisar una landing o página;
- consulte por una campaña, anuncio, creatividad, keyword o audiencia;
- proponga un curso, modalidad, mercado o nueva oferta;
- pregunte por rendimiento, caída, gasto, leads o ventas;
- entregue una pieza creada por Edge, Content Factory, Canva, Gemini u otro ejecutor;
- pida una recomendación comercial o de marketing material.

No aplicarlo a preguntas simples que no requieren investigación ni a tareas puramente administrativas.

## Regla de herramientas

```text
CAPACIDAD_DIRECTA_READ_DISPONIBLE
→ USARLA
→ REGISTRAR FUENTE/VENTANA
→ FALLBACK MANUAL SOLO SI FALLA O NO APLICA
```

Marketing puede usar, cuando estén disponibles y autorizadas en modo lectura:

- Google Search Console y Google Analytics;
- Google Ads, Keyword Planner y términos de búsqueda;
- Meta Ads y datos de campañas, conjuntos, anuncios y creatividades;
- PageSense u otra analítica web vigente;
- SERP real, Google Trends, Semrush/HYPD y fuentes públicas verificables;
- datos agregados y autorizados de Zoho CRM;
- repositorios y documentos canónicos Capacita.

No solicitar copia/pega de datos que una fuente conectada puede entregar de forma segura. La ausencia de una fuente material se declara `DATA_GAP`; no se rellena con intuición.

Nuevos OAuth/scopes, instalación, costo, descarga sensible, acceso a PII o cualquier escritura mantienen autorización explícita.

## Matriz de activación mínima

| Tipo de trabajo | Fuentes mínimas pertinentes | Preguntas obligatorias | Salida mínima |
|---|---|---|---|
| Landing/página orgánica | render real, protocolo de visibilidad, GSC/GA4 si existen, SERP/keywords, competidores, canónicos GTM | ¿qué intención posee?, ¿se diferencia?, ¿convierte?, ¿compite con otra URL?, ¿qué falta medir? | P0/P1/P2, `DO_NOT_CHANGE`, handoff a Edge |
| Landing paid-only | render real, Ads de origen, GA4/PageSense, destino/formulario, canónicos GTM | ¿hay message match?, ¿qué fricción existe?, ¿qué señal llega al downstream? | hipótesis, variante, tracking, criterio de éxito |
| Google Ads | campaña, grupo, keyword, search term, negativas vigentes, landing, conversion actions, dispositivo y downstream disponible | ¿qué consume gasto?, ¿qué intención trae?, ¿qué destino recibe?, ¿qué resultado comercial existe? | mantener/corregir/probar/pausar como recomendación, nunca como write implícito |
| Meta Ads | campaña, adset, anuncio, creatividad, placement, frecuencia, gasto, acciones y downstream | ¿hay fatiga?, ¿qué dolor/mensaje se prueba?, ¿qué calidad comercial produce? | ganadores/perdedores provisionales, nueva prueba, activo requerido |
| Curso/oferta nueva | demanda, intención, competencia, CPC/KD cuando exista, GTM, capacidad real Capacita, margen/valor disponible | ¿hay demanda comercial?, ¿calza con capacidad?, ¿qué canal y página requiere? | `GO/PILOT/HOLD/NO_GO` con confianza y datos faltantes |
| Campaña activa | período actual, baseline comparable, cambios, Ads, web y downstream | ¿qué cambió?, ¿cuál es la causa probable?, ¿qué acción tiene mayor valor? | diagnóstico priorizado y `NEXT_BEST_ACTION` |

Una fuente se omite sólo con motivo explícito: `N/A`, `NO_ACCESS`, `PLAN_LIMIT`, `DATA_GAP` o bajo beneficio marginal.

## Contrato analítico

Separar siempre:

```text
HECHO
INTERPRETACION
HIPOTESIS
RECOMENDACION
```

No colapsar capas:

```text
ADS_PLATFORM_SIGNAL
!= WEB_SIGNAL
!= CRM_LEAD_OR_CONTACT
!= DEAL
!= CURSOALUMNO
!= VENTA_REAL
```

No declarar causalidad por correlación temporal, un único clic, una conversión de plataforma o una muestra pequeña.

## Umbral de calidad

Una recomendación material no puede cerrarse como “mejorar”, “probar otro copy”, “agregar imágenes” o “revisar keywords”. Debe incluir:

```text
EVIDENCIA
HALLAZGO
ACCION_EXACTA
IMPACTO_ESPERADO
ESFUERZO
CONFIANZA
RIESGO
DUENO
METRICA
CRITERIO_DE_VALIDACION
NEXT_BEST_ACTION
```

Cuando la evidencia no permite escoger, presentar una prueba mínima reversible, no una opinión disfrazada de decisión.

## Diferenciación controlada de landings

Objetivo:

```text
MISMA_MARCA != MISMA_PAGINA
```

Las landings hermanas deben conservar sistema corporativo, navegación y componentes reutilizables. No requieren rediseños completos. Marketing debe compararlas y definir diferencias justificadas por producto, intención y buyer persona.

Matriz mínima:

| Dimensión | Regla |
|---|---|
| Hero/imagen | activo principal propio y representativo del curso/modalidad |
| Acento visual | variación controlada dentro del sistema de marca, no color arbitrario |
| Ejemplo aplicado | tarea, resultado o situación específica del curso |
| Dolor/señal | problema principal explícito y verificable |
| Prueba/confianza | evidencia pertinente al producto, no bloque genérico repetido |
| CTA/microcopy | acción coherente con intención y etapa del journey |
| Elemento distintivo | al menos un recurso visual o de contenido que ayude a reconocer la página |

Antes de pedir nuevos activos, revisar reutilización interna y derechos de uso. No cambiar por variedad estética si perjudica accesibilidad, claridad, velocidad o marca.

## Pain signals y CTA medibles

El clic expresa una señal conductual; no demuestra la identidad, el dolor real ni el buyer persona definitivo del visitante.

Marketing debe mantener una taxonomía pequeña y versionada, idealmente de tres a cinco `pain_signal` por oferta o familia. Cada señal registra:

- ID estable;
- etiqueta legible;
- evidencia/origen;
- buyer persona compatible como hipótesis, no verdad;
- mensaje y CTA asociados;
- estado `CANDIDATE`, `PILOT`, `VALIDATED` o `RETIRED`.

Contrato recomendado para eventos frontend:

```text
course
modality
audience
pain_signal
bp_hypothesis
cta_action
cta_location
page_variant
```

Marketing define nomenclatura y análisis. Edge implementa el evento. Analytics registra comportamiento. Zoho conserva atribución o resultado sólo si existe diseño autorizado. No incluir PII en nombres o parámetros de evento.

Evitar taxonomías libres por página. Una nueva categoría requiere evidencia de que las existentes no explican el patrón.

## Revisión de campañas

Toda campaña material debe cerrar con cuatro decisiones explícitas:

1. qué mantener;
2. qué corregir;
3. qué probar después;
4. qué no tocar todavía.

Para keywords negativas:

- en Ads aplicar el documento canónico de intención antes de recomendar exclusiones;
- en orgánico hablar de intención no objetivo, arquitectura y canibalización, no confundirlo con una lista de negativas de campaña.

Para creatividades:

- comparar mensaje, dolor, buyer persona, formato, placement, fatiga y downstream;
- un CTR mayor no convierte automáticamente una pieza en ganadora;
- especificar el activo faltante y su función, no sólo “hacer otra imagen”.

## Handoff ejecutable

Cuando Edge u otro agente implemente, Marketing debe entregar en un único bloque:

- repo, rama y página/campaña;
- objetivo e hipótesis;
- sección y cambio exacto;
- copy/activo o criterio de activo;
- evento y parámetros;
- permitidos, prohibidos y `DO_NOT_CHANGE`;
- validación visual, técnica y analítica;
- evidencia esperada y DoD.

Marketing vuelve a revisar el resultado. Delegar implementación no delega criterio ni aceptación.

## Piloto obligatorio antes de promover instrucciones

### Caso A — landing orgánica

Marketing debe, sin petición granular adicional:

- usar fuentes conectadas pertinentes;
- comparar al menos una landing hermana;
- detectar diferenciación, intención, canibalización, CTA y medición;
- producir handoff ejecutable a Edge.

### Caso B — campaña pagada READ

Marketing debe:

- leer configuración/performance disponibles;
- relacionar Ads, landing y downstream sin colapsarlos;
- identificar una oportunidad no obvia o declarar honestamente que no existe;
- entregar `NEXT_BEST_ACTION` sin ejecutar cambios.

PASS sólo si:

```text
CONNECTED_SOURCES_USED_WITHOUT_GRANULAR_PROMPT=PASS
NO_GENERIC_ADVICE=PASS
LANDING_DIFFERENTIATION=PASS
PAIN_SIGNAL_TRACKING_SPEC=PASS
CAMPAIGN_OPPORTUNITY_SCAN=PASS
HANDOFF_EXECUTABLE=PASS
EXTERNAL_WRITES=0
```

## DoD

- fuentes y ventana identificadas;
- hechos separados de inferencias;
- oportunidad priorizada por impacto/esfuerzo/confianza/riesgo;
- acción exacta, dueño y validación definidos;
- `DO_NOT_CHANGE` explícito cuando corresponda;
- sin PII, secretos, export crudo ni writes;
- resultado registrado en issue/PR o canónico del frente;
- aprendizaje reusable devuelto a GTM/RevOps o AI OS sólo si aporta valor transversal.
