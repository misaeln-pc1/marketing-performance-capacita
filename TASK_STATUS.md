# Estado de Tareas

Fecha de revisión: 2026-07-12

## Prioridad activa

Cerrar la arquitectura y medición de tres landings pagadas B2C antes de modificar Google Ads o producción, protegiendo la página orgánica actual y preparando Search Console API read-only.

La línea activa integra:

- página orgánica actual protegida;
- landing pagada Básico–Intermedio / `BP-001`;
- landing pagada Básico desde cero / `BP-002`;
- landing pagada clases presenciales con profesor / `BP-001`;
- PageSense, GA4, GTM, formularios y Zoho;
- Google Ads histórico, términos reales, Keyword Planner y competencia;
- Search Console API para consultas y páginas orgánicas;
- contrato futuro de datos para dashboard y mejora continua.

## Estado Google Ads

- Basic Access de Google Ads API aprobado.
- Pipeline local read-only validado.
- PR #26 mergeado con export histórico.
- Export de 90 días completado para 2026-04-12 a 2026-07-10.
- Los siete reportes iniciales válidos fueron analizados localmente.
- PR #29 corrigió los dos reportes faltantes:
  - `05_search_terms_daily.csv`: 1.825 filas, `ok`;
  - `07_landing_pages_daily.csv`: 8.482 filas, `ok`.
- La evidencia agregada y sanitizada quedó en `docs/google-ads/GOOGLE_ADS_DIAGNOSIS_BASELINE_2026-07-11.md`.
- PR #29, PR #30 y PR #31 están mergeados.
- Se validó acceso por Google Drive a `Historial_Rendimiento_GoogleAds`.
- PR #32 define el procedimiento recurrente de análisis con dos fuentes obligatorias.
- Los CSV, ZIP, URLs completas, IDs, YAML, tokens y credenciales permanecen fuera del repo.

## Procedimiento recurrente de estatus

Para cada solicitud futura de análisis de estatus de Google Ads:

1. obtener y validar un export fresco read-only por PowerShell / Google Ads API;
2. localizar y leer `Historial_Rendimiento_GoogleAds` en Google Drive;
3. declarar disponibilidad de ambas fuentes y periodo común;
4. reconciliar métricas, fechas, cambios y discrepancias;
5. etiquetar el análisis como completo, provisional o bloqueado.

Si Drive no está disponible, debe indicarse explícitamente aunque exista PowerShell. Si PowerShell no está disponible, debe indicarse aunque Drive sea accesible. Con una sola fuente el resultado es provisional.

Documento dueño:

- `docs/google-ads/GOOGLE_ADS_STATUS_ANALYSIS_PROCEDURE_V01.md` — PR #32.

## Hallazgos confirmados

- `curso excel básico e intermedio` aumentó fuertemente su volumen y participación de gasto con baja conversión registrada.
- Esa keyword mezcla intenciones: básico, intermedio, desde cero, clases, gratis e informativas.
- `EXCEL-PRE-STGO` concentra múltiples intenciones en un solo grupo y un único anuncio responsive activo.
- Existe tráfico pagado hacia páginas secundarias con desempeño considerablemente inferior a la landing principal.
- `EXCEL-EMPRESA` presenta gasto relevante y conversión registrada muy débil; requiere auditoría B2B y de objetivos compartidos.
- La campaña presencial conserva alta participación de impresiones y poca pérdida por ranking/presupuesto; la competencia no está confirmada como causa principal.
- PageSense confirma una brecha crítica entre clic en enviar y submit aceptado; los goals actuales de clic no son leads.
- La página orgánica actual debe protegerse hasta analizar Search Console.

## Decisión de landings pagadas

Se aprueban documentalmente tres landings nuevas, inicialmente `noindex,follow`, fuera del sitemap y sin tocar la página orgánica:

1. **Básico–Intermedio / BP-001**
   - productividad, errores, dependencia y ruta completa;
   - mismo curso real y misma oferta.

2. **Excel Básico desde cero / BP-002**
   - inseguridad de nivel, acompañamiento y ruta clara;
   - mismo curso real, presentado para quien comienza sin Excel previo.

3. **Clases presenciales con profesor / BP-001**
   - intención de clases, profesor en vivo y alternativa estructurada frente a particulares;
   - curso grupal Básico–Intermedio en sede;
   - no clases particulares, uno a uno ni a domicilio;
   - prueba reversible con medición independiente y criterio de retiro.

No se aprueba todavía:

- crear landings adicionales;
- mezclar Excel Avanzado con esta oferta;
- modificar Google Ads;
- aumentar presupuesto o pujas;
- pausar campañas o keywords;
- agregar negativas;
- modificar conversiones;
- cambiar GTM, WordPress, Cloudflare, Zoho o producción.

## Restricciones de mensaje

- No usar SENCE, franquicia tributaria, beneficio tributario, gratis o gratuito en B2C.
- Mantener el puente `¿La capacitación es para tu equipo?` como derivación secundaria hacia B2B.
- No usar la guía gratuita como promesa principal del hero pagado.
- No mentir sobre la modalidad grupal, sede, profesor, horario o producto.

## Hipótesis de competencia y cluster `clases/profesor`

- Superprof es un competidor plausible, pero no se demostró como causa principal del deterioro.
- Antes de activar la tercera landing se debe analizar read-only:
  - `clases`;
  - `profesor`;
  - `particular`;
  - `domicilio`;
  - `presencial`;
  - gasto, clics, CPC y conversiones;
  - Keyword Planner y términos reales.
- La landing C debe mantenerse solo si atrae consultas compatibles, submits, leads contactables, cotizaciones o matrículas.

## Medición obligatoria

Cada landing debe tener:

- URL propia;
- `landing_code` propio validado;
- UTM y click IDs persistentes;
- variante e intención identificables;
- buyer persona registrado como hipótesis;
- PageSense separado;
- GA4/GTM auditados;
- submit confirmado como conversión técnica primaria;
- Zoho reconciliado hasta lead contactable, cotización y matrícula.

Funnel conceptual:

1. visita;
2. hero;
3. CTA;
4. form start;
5. submit attempt;
6. submit confirmado;
7. lead recibido;
8. lead contactable;
9. cotización;
10. matrícula.

No inventar API names ni usar clics como submits.

## Search Console API

- Issue #36 creado para export read-only.
- Scope previsto: `webmasters.readonly`.
- Objetivo: consultas, páginas, clics, impresiones, CTR y posición.
- Credenciales y exports crudos deben permanecer fuera del repo.
- Confirmar propiedad exacta y permisos antes de OAuth.

## Bloque 0 — medición y atribución

Issue técnico dueño:

- `misaeln-pc1/capacita-edge#27` — cobertura GTM/Google tag y atribución Ads → formularios → Zoho.

Debe validar:

- cobertura en todas las rutas relevantes;
- persistencia de `gclid`, `gbraid`, `wbraid` y UTM;
- navegación entre WordPress, Cloudflare Pages, dominios y subdominios;
- formularios, WhatsApp, llamadas y confirmaciones;
- eventos duplicados o ausentes;
- objetivos primarios/secundarios y posibles conversiones compartidas;
- comparación agregada Google Ads → formularios → leads Zoho → resultados comerciales.

La submedición puede afectar conversiones, CVR y CPA; no invalida gasto, clics, CPC, términos, Quality Score o señales de subasta.

## SEO, SEO local y visibilidad IA

- PR #31 mergeado con la metodología SEO/GEO independiente.
- Edge issue #28 conserva la auditoría técnica dueña.
- Marketing define consultas, intención, benchmark, medición agregada e impacto comercial.
- Capacita Edge implementa robots, headers, sitemap, canonicals, structured data, Cloudflare, frontend y eventos.

La página orgánica actual no se redirige, no recibe `noindex` y no se reescribe agresivamente sin evidencia de Search Console.

## Buyer persona y activos transversales

Los buyer persona, propuestas de valor y customer journey se consumen desde Global/Atlas. Marketing no los redefine.

- Landing A: `BP-001`.
- Landing B: `BP-002`.
- Landing C: `BP-001`, con hipótesis distinta basada en profesor en vivo y estructura grupal.

Ciclo de mejora continua:

1. hipótesis o aplicación local;
2. prueba y evidencia en el repo dueño;
3. aprendizaje estable y reutilizable;
4. candidato transversal;
5. revisión en Global/Atlas;
6. adopción versionada, permanencia local o rechazo.

Punto de revisión:

- `misaeln-pc1/capacita-global-control#101`.

Ningún candidato nuevo se considera canónico todavía.

## PR e issues activos

| Elemento | Alcance | Estado |
|---|---|---|
| PR #35 | decisiones de landings pagadas, PageSense, Search Console y handoff | abierto, documental |
| Issue #36 | Search Console API read-only | abierto |
| Edge #27 | tracking y atribución | abierto |
| Edge #28 | SEO/GEO técnico | abierto |

## Secuencia inmediata

1. Abrir nuevo hilo con `Context Gate: Bootstrap`.
2. Leer `docs/handoffs/HANDOFF_EXCEL_PAID_LANDINGS_SEARCH_CONSOLE_2026-07-12.md`.
3. Verificar estado real de PR #35, issue #36 y Edge #27/#28.
4. Cerrar matriz contractual de las tres landings.
5. Revisar bloques HTML de la landing actual.
6. Definir medición exacta por landing.
7. Preparar un único prompt para Work en Capacita Edge.
8. Implementar landings en rama/PR, sin tocar Google Ads.
9. Configurar Search Console API read-only.
10. Analizar cluster `clases/profesor`.
11. Solicitar autorización antes de cambios productivos.

## Reglas operativas vigentes

- Un buyer persona primario y una hipótesis por prueba.
- Separar B2C y B2B en campaña, landing y medición.
- Mantener constantes oferta y variables relevantes al comparar mensajes.
- No mezclar conversiones registradas por Google con resultados comerciales sin reconciliación.
- No declarar completo un análisis recurrente si falta PowerShell/API o `Historial_Rendimiento_GoogleAds`.
- No trabajar directo en `main`.
- No subir PII, secretos, IDs completos, exports crudos, capturas sensibles ni binarios.
- No inventar métricas, claims, eventos, IDs o resultados.

## Definition of Done de la fase documental

- decisión de tres landings registrada;
- página orgánica protegida;
- SENCE excluido de B2C;
- buyer persona e hipótesis definidos;
- medición conceptual documentada;
- Search Console API en issue separado;
- handoff exportable creado;
- no se modificó producción.
