# Investigación de palabras clave Google Ads — Office presencial Santiago

## 1. Estado

**HOLD de métricas / PASS documental.** La autenticación llegó al endpoint oficial de Google Ads API v24, pero falló antes de recuperar datos con `ACCESS_TOKEN_SCOPE_INSUFFICIENT`. No se ejecutaron `GenerateKeywordIdeas` ni `GenerateKeywordHistoricalMetrics`, no se inventaron métricas y no se modificó Google Ads.

## 2. Fecha

2026-07-24, zona horaria `America/Santiago`.

## 3. Gate utilizado

`Bootstrap`, semáforo amarillo.

## 4. Objetivo

Evaluar con datos de demanda una futura campaña Search B2C de un curso presencial básico de computación y Office en Santiago. Debido al bloqueo de autenticación, este documento entrega la preparación completa y deja la decisión cuantitativa pendiente.

## 5. Alcance

- B2C, modalidad presencial, Santiago y nivel principiante.
- Siete familias de semillas y negativas candidatas.
- Sin cambios de campañas, grupos, anuncios, palabras clave, pujas, presupuestos, conversiones, audiencias, ubicaciones ni credenciales.
- Sin mezcla B2B/B2C.

## 6. Autorización recibida

Se usó la autorización explícita del encargo para lectura de Google Ads API, documentación sanitizada y flujo Git reversible. La autorización no cubre reautenticar ADC, crear credenciales ni ampliar scopes; por eso la consulta se detuvo.

## 7. Fuentes revisadas

| Documento | Sección aplicada | Versión / vigencia |
|---|---|---|
| `capacita-global-control/docs/gtm-revops/CONSUMPTION_CONTRACT.md` | Principio rector; contrato mínimo; adaptación permitida | v1.0.1, 2026-07-10 |
| `capacita-global-control/docs/gtm-revops/BUYER_PERSONAS.md` | Reglas; registro canónico; `BP-000`; limitaciones | v1.0.0, 2026-07-10 |
| `capacita-global-control/docs/gtm-revops/BUYER_PERSONA_SIGNAL_MODEL.md` | Reglas centrales; dimensiones separadas; confianza | v1.0.0, 2026-07-10 |
| `capacita-global-control/docs/gtm-revops/VALUE_PROPOSITIONS.md` | A) práctica guiada; B) presencial céntrica; limitaciones | v0.2.1, 2026-06-22 |
| `capacita-global-control/docs/gtm-revops/CUSTOMER_JOURNEY.md` | 1. Visitante / audiencia fría; criterios de transición | v0.2, 2026-06-22 |
| `capacita-global-control/docs/gtm-revops/SEGMENTATION_RULES.md` | Dimensiones; segmentos iniciales; reglas mínimas | v0.1, 2026-06-21 |
| `docs/GTM_CONSUMPTION_BRIDGE.md` | Fuentes canónicas; contrato mínimo; bloques sin ID | v1.0.0, 2026-07-10 |
| `templates/CAMPAIGN_BRIEF_GTM.md` | Baseline; aplicación local; riesgos; medición | v1.0.0 |
| `docs/google-ads/GOOGLE_ADS_READONLY_PIPELINE_PLAN.md` | Configuración; flujo; guardrails | V0.1 |
| `docs/google-ads/GOOGLE_ADS_KEYWORD_IDEAS_FIRST_RUN_LOG.md` | Evidencia sanitizada; riesgo; siguiente barrido | ejecución 2026-07-08 |
| `docs/google-ads/GOOGLE_ADS_POWERSHELL_FAST_PATH.md` | Ruta validada; cuentas sanitizadas; guardrails | vigente desde 2026-07-08 |
| `docs/google-ads/GOOGLE_ADS_HISTORICAL_DIAGNOSIS_CONTRACT_V01.md` | Hipótesis; guardrails; salida versionable | V01 |
| `docs/google-ads/GOOGLE_ADS_HISTORICAL_DIAGNOSIS_RUNBOOK_V01.md` | Preflight; competencia; limitaciones | V01 |
| `docs/google-ads/GOOGLE_ADS_DIAGNOSIS_BASELINE_2026-07-11.md` | Mezcla de intención; tracking; regla de decisión | baseline 2026-07-11 |

## 8. Feedback scan

**Estado: aplicar y pendiente.**

- Aplicar: Marketing issue #27 permite `GenerateKeywordHistoricalMetrics` read-only y exige no decidir landings sin evidencia.
- Aplicar: Global issue #101 mantiene la taxonomía de intención como candidato local, no como canónico.
- Pendiente: Marketing issue #23 sigue evaluando V1; no cambia este alcance.
- Pendiente separado: Marketing issues #27 y #33 contienen diagnóstico/automatización más amplios; esta investigación no los cierra.
- No se encontró issue específico previo para Office presencial, computación básica, alfabetización digital o adultos mayores.

## 9. Skills utilizadas

- Flujos de sesión: `data-analytics:gather-business-context`, `data-analytics:product-business-analysis`, `data-analytics:validate-data` y `github:yeet`.
- AI OS: no se usó una skill interna. `google-ads-campaign-audit-capacita` figura como `draft`, no `draft operativo`, por lo que no cumple la prioridad autorizada. `buyer-persona-signal-map-capacita` tampoco se usó.

## 10. Baseline GTM consumido

La investigación consume las propuestas canónicas **A) Capacidad práctica y guiada** y **B) Experiencia presencial confiable en ubicación céntrica**, y la etapa **1. Visitante / audiencia fría**. No asigna un buyer persona canónico: la edad y el bajo nivel digital descritos son hipótesis de público, no evidencia suficiente. `BP-000` es el control metodológico aplicable hasta obtener señales declaradas.

## 11. Buyer persona aplicable

No determinado. `BP-002` podría ser una hipótesis secundaria cuando exista motivación laboral declarada, pero no se usa como conclusión ni se limita el estudio por edad.

## 12. Hipótesis principal

> Las personas con baja experiencia digital buscan con mayor frecuencia “curso de computación básica presencial” o equivalentes que “curso de alfabetización digital”.

**Resultado: inconclusa.** No hubo respuesta de Keyword Planner en esta ejecución.

## 13. Configuración solicitada de Google Ads

| Campo | Configuración |
|---|---|
| API / cliente | Google Ads API v24; paquete Python `google-ads` 31.1.0 |
| Servicios previstos | `GenerateKeywordIdeas` y `GenerateKeywordHistoricalMetrics` |
| Cuenta objetivo sanitizada | `***-***-7322` (configuración local; no verificada en esta ejecución) |
| Login customer sanitizado | `***-***-6623` (configuración local; no verificada en esta ejecución) |
| Ubicación | Santiago de Chile; geo target no resuelto por bloqueo previo |
| Idioma | Español; language constant no resuelto por bloqueo previo |
| Red | Google Search solicitada; no consultada |
| Histórico | Últimos 12 meses disponibles solicitados; no consultado |
| Moneda | Desconocida en esta ejecución |

## 14. Método técnico utilizado

1. Se materializó el checkout oficial y se creó la rama requerida desde `origin/main`.
2. Se localizó `google-ads.yaml` y el runner existentes fuera del repo, sin imprimir sus valores.
3. Se ejecutó `CustomerService.ListAccessibleCustomers` con el script read-only validado.
4. Google respondió `ACCESS_TOKEN_SCOPE_INSUFFICIENT`.
5. Se comprobó, sin emitir ni mostrar tokens, que el ADC existente no puede solicitar `https://www.googleapis.com/auth/adwords`.
6. Se detuvo la API: corregirlo requiere reautenticación y excede la autorización.

Presupuesto consumido: dos ciclos diagnósticos; sin cambio de arquitectura.

## 15. Semillas y resultados

- Semillas obligatorias preparadas: **104**.
- Familias: **7**.
- Semillas consultadas por Keyword Planner: **0**.
- Ideas recibidas: **0**.
- Keywords únicas en el CSV, incluidas negativas manuales: **137**.
- Negativas candidatas manuales: **33**.

## 16. Normalización

Se convirtió a minúsculas, se consolidaron espacios, se conservó Unicode NFC y las tildes, y se deduplicó solo por igualdad exacta de `normalized_keyword`. No se fusionaron sinónimos.

## 17. Clasificación analítica

Las categorías y señales son inferencias manuales del texto. No son datos de Google. Todos los términos positivos quedan `INSUFFICIENT_DATA`; las negativas quedan `NEGATIVE_CANDIDATE` y no se aplicaron.

## 18. Puntaje de relevancia

Puntaje documental de 0–100, no métrica de Google:

- intención comercial explícita: hasta 25;
- presencialidad: 20;
- Santiago: 15;
- nivel principiante: 15;
- coherencia temática: hasta 25;
- riesgo de software/descarga: −30;
- riesgo informativo: −20.

El puntaje no usa volumen, competencia ni puja y, por tanto, no ordena oportunidad económica.

## 19. Top keywords por volumen

No disponible. `avg_monthly_searches` quedó vacío; no se rellenó con cero.

## 20. Top keywords por intención presencial, local, principiante y oportunidad documental

| Keyword | Familia | Puntaje documental | Categoría |
|---|---|---:|---|
| curso alfabetización digital presencial | alfabetizacion_digital | 85 | BEGINNER_GENERAL |
| curso computación básica presencial | computacion_basica_presencial | 85 | CORE_HIGH_INTENT |
| curso computación presencial santiago | computacion_basica_presencial | 85 | PRESENTIAL_LOCAL |
| curso excel básico presencial | herramientas_especificas | 85 | TOOL_SPECIFIC |
| curso excel presencial santiago | herramientas_especificas | 85 | TOOL_SPECIFIC |
| curso informática básica presencial | computacion_basica_presencial | 85 | CORE_HIGH_INTENT |
| curso office básico presencial | office_presencial | 85 | CORE_HIGH_INTENT |
| curso office presencial santiago | office_presencial | 85 | PRESENTIAL_LOCAL |
| curso powerpoint básico presencial | herramientas_especificas | 85 | TOOL_SPECIFIC |
| curso windows básico presencial | herramientas_especificas | 85 | TOOL_SPECIFIC |
| curso word básico presencial | herramientas_especificas | 85 | TOOL_SPECIFIC |
| curso word presencial santiago | herramientas_especificas | 85 | TOOL_SPECIFIC |

Este ranking solo prioriza qué reconsultar primero.

## 21. Top keywords explícitas para adultos mayores

La familia contiene 15 semillas explícitas. Sin volumen real no se recomienda un grupo por edad ni se infiere que la edad explique la necesidad.

## 22. Keywords de alto costo

No disponible. Las pujas quedaron vacías.

## 23. Keywords de alta competencia

No disponible. `competition` y `competition_index` quedaron vacíos.

## 24. Keywords con volumen insuficiente

No se puede distinguir volumen insuficiente de dato ausente. Todas las semillas requieren nueva consulta.

## 25. Keywords ambiguas

Mayor ambigüedad esperada: `curso autonomía digital`, `curso actualización digital`, `capacitación digital para personas` y consultas sin modalidad o ubicación. Es una inferencia, no resultado de Google.

## 26. Keywords informativas

`tutorial`, `youtube`, `pdf`, `manual`, `plantilla` y `ejercicios gratis` son negativas candidatas manuales. Deben contrastarse con consultas reales antes de aplicar.

## 27. Software o licencias

`licencia office`, `comprar office`, `descargar office`, `instalar office`, `office 365 gratis`, `crack` y `pirata` presentan riesgo alto de intención no formativa.

## 28. Negativas candidatas

Se incluyeron 33 términos. `SENCE`, `capacitación`, `tercera edad`, `adulto mayor` y `trabajo` no fueron negativizados automáticamente. `empleo`, `trabajo remoto` y `curso avanzado` requieren revisión de concordancia/oferta antes de excluir.

## 29. Comparación obligatoria entre familias

| Familia | Semillas | Búsquedas promedio | Competencia | Puja | Lectura disponible |
|---|---:|---|---|---|---|
| office_presencial | 15 | No disponible | No disponible | No disponible | Clasificación textual solamente |
| computacion_basica_presencial | 19 | No disponible | No disponible | No disponible | Clasificación textual solamente |
| alfabetizacion_digital | 12 | No disponible | No disponible | No disponible | Clasificación textual solamente |
| adultos_mayores | 15 | No disponible | No disponible | No disponible | Clasificación textual solamente |
| principiantes_desde_cero | 14 | No disponible | No disponible | No disponible | Clasificación textual solamente |
| herramientas_especificas | 15 | No disponible | No disponible | No disponible | Clasificación textual solamente |
| uso_laboral_autonomia | 14 | No disponible | No disponible | No disponible | Clasificación textual solamente |

No es posible declarar familia ganadora por volumen, costo o competencia. Textualmente, computación básica y Office presencial expresan mejor la oferta que alfabetización digital; esto sigue siendo supuesto.

## 30. Estacionalidad

No disponible: `monthly_searches_json` es `null` en todas las filas.

## 31. Riesgos

- Reautenticar sin aprobación violaría el alcance de credenciales.
- Las familias amplias pueden atraer online, gratis, soporte o software.
- Un segmento por adultos mayores puede estereotipar o reducir cobertura si se decide sin volumen/intención.
- La oferta multi-herramienta puede diluir relevancia entre consulta, anuncio y landing.
- Tracking Ads → landing → formulario/WhatsApp → Zoho sigue pendiente antes de activar.

## 32. Limitaciones

- Sin métricas, ideas generadas, geo target, language constant, moneda ni histórico mensual de esta ejecución.
- Los datos históricos de Excel sirven como antecedente metodológico, no como sustituto de demanda para Office/computación básica.
- No se usó URL semilla porque no se verificó una landing pública que represente honestamente este curso completo.

## 33. Recomendación principal

**No decidir todavía la familia ni activar una campaña.** Restaurar de forma humana y autorizada el scope OAuth `adwords` de la configuración existente y repetir primero un barrido mínimo de las siete familias para Santiago. La comparación debe ponderar volumen, intención presencial/local, competencia y pujas, no solo el lenguaje.

## 34. Opción rápida, riesgo y mitigación

- Opción rápida: reconsultar las 104 semillas en lotes por familia.
- Riesgo: volver a obtener bajo volumen por geo demasiado estrecho.
- Mitigación: ejecutar Santiago y, solo si es necesario, una segunda lectura separada para Región Metropolitana; no atribuir datos regionales a Santiago Centro.

## 35. Alternativa segura

Si no se autoriza reautenticación, mantener este paquete como diseño pendiente y no usar sus scores para inversión.

## 36. Próximo experimento mínimo

Consulta read-only de `computacion_basica_presencial`, `office_presencial` y `alfabetizacion_digital`, más un conjunto general sin modalidad, con idéntico geo/idioma/red. Criterio: comparar volumen e intención relevante, conservando resultados mensuales y pujas.

## 37. Estructura documental sugerida de grupos de anuncios

1. Computación básica presencial.
2. Office desde cero presencial.
3. Adultos mayores, solo si volumen e intención lo justifican.
4. Herramientas individuales, separando las que muestren demanda suficiente.
5. Uso laboral y autonomía digital como experimento independiente.

No mezclar B2C/B2B ni activar esta estructura desde el documento.

## 38. Landing requerida

Se requiere una landing B2C específica y honesta para nivel inicial, profesor en vivo, modalidad presencial y ubicación confirmada. Debe detallar contenido real por herramienta, nivel, requisitos y CTA. No reutilizar automáticamente una landing de Excel si el curso ofrece Office/computación integral.

## 39. Tracking pendiente

Antes de pauta: UTMs, `gclid`/`gbraid`/`wbraid`, eventos de formulario/WhatsApp/llamada, deduplicación y reconciliación agregada con Zoho. No declarar lista la campaña.

## 40. Decisiones que requieren aprobación de Misael

1. Reconsentir o restaurar el ADC existente con scope `adwords`.
2. Confirmar el contenido/oferta y una landing específica.
3. Aprobar cualquier presupuesto, estructura real, negativas o tracking productivo.

## 41. Evidencia técnica

- Configuración externa localizada como `...\Proyectos\0-Origen\google-ads.yaml`.
- Runner externo localizado; no imprime secretos.
- Cliente: `google-ads` 31.1.0; API por defecto v24.
- Error de autenticación: `ACCESS_TOKEN_SCOPE_INSUFFICIENT`.
- No se imprimieron tokens, client secrets, refresh tokens ni IDs completos.

## 42. Validaciones

- CSV UTF-8 con BOM para Excel: PASS.
- Encabezados únicos y filas consistentes: PASS.
- Duplicados normalizados: PASS.
- Fórmulas peligrosas: PASS; sanitización defensiva aplicada.
- Métricas inventadas: PASS; todos los campos Google desconocidos están vacíos o `null`.
- PII, secretos e IDs completos: PASS.
- Binarios/archivos pesados: PASS.
- Hashes SHA-256: incluidos en el manifest para CSV y Markdown.
- Confianza analítica: **Needs revision / métricas API bloqueadas**.

## 43. Archivos generados

- `campaigns/office-presencial-santiago/keyword-research/google_ads_keyword_research_2026-07-24.csv`
- `campaigns/office-presencial-santiago/keyword-research/GOOGLE_ADS_KEYWORD_RESEARCH_2026-07-24.md`
- `campaigns/office-presencial-santiago/keyword-research/google_ads_keyword_research_manifest_2026-07-24.json`

## 44. Estado Git

Rama `docs/marketing-office-presencial-keywords`. Commit, push y PR se registrarán en el cierre del ejecutor.

## 45. Estado de cierre

Entregables documentales preparados; investigación cuantitativa bloqueada hasta resolver el scope OAuth con autorización humana. `MERGE GATE: REQUIERE_REVISION_MISAEL`.

## Confirmación obligatoria

No se modificaron campañas, anuncios, grupos de anuncios, palabras clave activas, presupuestos, pujas, conversiones, audiencias, configuraciones ni credenciales de Google Ads.
