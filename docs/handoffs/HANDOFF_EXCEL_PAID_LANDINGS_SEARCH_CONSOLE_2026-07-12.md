# Handoff — Landings pagadas Excel, PageSense y Search Console — 2026-07-12

## Propósito

Permitir continuar el trabajo en un hilo nuevo sin reconstruir el diagnóstico, las decisiones ni las restricciones operativas.

Este documento es un traspaso de contexto y no autoriza por sí solo cambios en Google Ads, Capacita Edge, PageSense, GTM, Zoho, Cloudflare, Search Console, Google Analytics o producción.

## Estado de gobernanza

- Repo dueño de estrategia y performance: `misaeln-pc1/marketing-performance-capacita`.
- Repo dueño de landings, tracking y SEO técnico: `misaeln-pc1/capacita-edge`.
- Rama documental activa: `docs/marketing-excel-b2c-two-page-plan-v01`.
- PR documental activo: #35.
- Issue Search Console API read-only: #36.
- Issue Edge de tracking/atribución: `capacita-edge#27`.
- Issue Edge de SEO/GEO técnico: `capacita-edge#28`.
- No trabajar directo en `main`.

## Decisión vigente sobre páginas

### 1. Página orgánica actual

La página orgánica actual se conserva:

- indexable;
- con canonical autorreferente;
- dentro del sitemap;
- sin reescritura agresiva;
- con correcciones operativas mínimas, como fecha vigente y errores evidentes;
- sin convertirla en superficie experimental principal.

Su valor SEO acumulado debe protegerse hasta disponer de evidencia de Search Console sobre consultas, páginas, clics, impresiones, CTR y posición.

### 2. Landing pagada A — ruta Básico–Intermedio

- Estado SEO inicial: `noindex,follow`.
- Fuera del sitemap y navegación orgánica principal.
- Producto real: curso Excel Básico e Intermedio presencial, grupal, en Santiago Centro.
- Buyer persona primario: `BP-001 — Desbordado Operativo`.
- Intención: curso presencial completo, productividad, autonomía, reducción de errores y dependencia.
- Hipótesis: un mensaje de ruta completa y aplicación laboral aumentará la probabilidad de consulta o matrícula de personas que ya usan Excel y necesitan trabajar con mayor orden y seguridad.

### 3. Landing pagada B — Excel Básico desde cero

- Estado SEO inicial: `noindex,follow`.
- Fuera del sitemap y navegación orgánica principal.
- Producto real: el mismo curso Básico–Intermedio; comienza sin conocimientos previos de Excel y avanza hasta nivel intermedio.
- Buyer persona primario: `BP-002 — Reinserción Laboral`.
- Intención: comenzar desde cero, entender el nivel, recibir acompañamiento y seguir una ruta clara.
- Hipótesis: un mensaje de confianza, nivel inicial y acompañamiento aumentará la probabilidad de consulta de personas inseguras respecto de su nivel o que no saben por dónde comenzar.

### 4. Landing pagada C — clases presenciales con profesor

Cambio aprobado por Misael el 2026-07-12 como prueba reversible.

- Estado SEO inicial: `noindex,follow`.
- Canal principal esperado: Google Search.
- Producto real: el mismo curso Básico–Intermedio presencial, grupal y en sede.
- Buyer persona primario: `BP-001 — Desbordado Operativo`.
- Intención: personas que buscan clases de Excel presenciales, profesor en vivo, acompañamiento directo o una alternativa estructurada frente a clases particulares.
- Hipótesis: si la persona descubre una alternativa grupal estructurada, con profesor presente, sede establecida, programa y horarios claros, aumentará su disposición a consultar precio, fecha o matrícula.

Verdad obligatoria de la oferta:

> Curso grupal presencial con profesor en vivo. No corresponde a clases particulares, atención uno a uno ni clases a domicilio.

No se utilizarán promesas de profesor exclusivo, horarios personalizados, visita al hogar ni atención individual permanente.

La página puede usar lenguaje compatible con la intención —por ejemplo, `clases de Excel presenciales`, `clases con profesor` o `profesor de Excel presencial`—, pero el anuncio y la landing deben aclarar de inmediato que se trata de un curso grupal estructurado.

Los términos relacionados con `clases particulares` quedan como hipótesis exploratoria. No deben activarse masivamente ni presentarse de forma engañosa; requieren revisión previa de términos reales, CPC, concordancia, negativas y copy.

## Regla SENCE y gratuidad

En B2C está prohibido usar:

- SENCE;
- franquicia tributaria;
- beneficio tributario;
- curso gratis o gratuito;
- mensajes que puedan confundirse con capacitación financiada o sin costo.

La evidencia histórica aportada por Misael indica gasto significativo en búsquedas de gratuidad y SENCE sin intención de matrícula pagada.

En B2B estos conceptos solo pueden tratarse en rutas específicas, con cautela y sin sugerir gratuidad.

## Puente B2B

El bloque `¿La capacitación es para tu equipo?` se conserva como derivación secundaria porque ha generado consultas reales.

Condiciones:

- no aparece en el hero;
- no compite con el CTA individual;
- dirige a una landing B2B independiente;
- se mide como clic secundario y no como conversión B2C;
- no menciona SENCE ni beneficio tributario en la tarjeta B2C.

## PageSense y CRO — hallazgos consolidados

### Formulario B2C

Periodo revisado aproximado:

- 5.816 visitantes;
- 124 iniciadores;
- 94 abandonos;
- aproximadamente 30 envíos implícitos;
- inicio sobre visitantes: ~2,1%;
- abandono entre iniciadores: ~75,8%;
- envío implícito sobre visitantes: ~0,5%.

### Brecha clic → submit

El click map mostró aproximadamente:

- 289 clics en submit móvil;
- 81 clics en submit escritorio;
- cerca de 370 clics totales;
- frente a cerca de 30 envíos efectivos implícitos.

Conclusión:

> Clic en enviar no equivale a formulario aceptado.

Los goals revisados (`enviar Pre`, `inicio`, `Enviar Empresa-Excel`) son goals de pulsación en elementos y no deben usarse como leads, submits confirmados o matrículas.

### Campo Email

El campo Email concentra la principal señal visible de fricción. No se ha demostrado causalidad única; se debe revisar:

- formato y validación;
- microcopy;
- mensajes de error;
- comportamiento móvil;
- grabaciones de sesión;
- envíos controlados.

### Regalo / guía

La guía gratuita se retira como promesa principal del hero pagado.

- El visitante de pauta debe recibir una propuesta de matrícula e información comercial.
- La guía puede mantenerse como bono posterior.
- La descarga de temario queda como conversión secundaria.
- Una campaña de regalos o contenido gratuito debe vivir en otra landing y otro objetivo, no mezclada con la pauta de matrícula.

### Móvil

El tráfico móvil agregado mostró menor compromiso que escritorio, pero mezcla fuentes. La implementación debe ser mobile-first y segmentar al menos `google/cpc` versus otras fuentes antes de atribuir el problema exclusivamente al diseño.

## Formularios y redirecciones

### Formulario del hero

- Envía directamente a Zoho Forms.
- Redirige a una página de agradecimiento de Capacita después del éxito.
- La configuración observada incorporaba nombre y correo en la URL; eso es un riesgo de privacidad que debe corregirse en una tarea separada.

### Formulario de descarga de temario

- Usa un formulario Zoho distinto.
- Muestra agradecimiento interno de Zoho.
- Debe medirse como conversión secundaria, separada del formulario comercial.

### Turnstile

Turnstile no explica el abandono del formulario B2C actual porque esa landing envía directamente a Zoho Forms y no contiene el widget ni `cf-turnstile-response`.

Turnstile sí debe auditarse en landings que utilicen `/api/forms/lead`, especialmente ante:

- token vencido;
- doble envío;
- `timeout-or-duplicate`;
- falta de reset del widget;
- error server-side.

## Modelo de medición obligatorio para las tres landings pagadas

Cada landing debe poder distinguirse sin ambigüedad en todos los sistemas.

### Identidad técnica mínima

Cada una debe tener:

- URL propia;
- `landing_code` propio, definido y validado antes de producción;
- UTM propias por canal, campaña, contenido y término;
- identificación de variante;
- identificación conceptual de intención y buyer persona primario;
- confirmación de persistencia de `gclid`, `gbraid`, `wbraid` y UTM.

No inventar API names de Zoho ni nombres finales de eventos. Deben validarse primero en Edge, GTM y CRM.

### Funnel conceptual

1. visita a landing;
2. visualización del hero;
3. clic CTA principal;
4. inicio de formulario;
5. intento de submit;
6. submit confirmado;
7. lead recibido en Zoho;
8. lead contactable;
9. cotización;
10. matrícula.

### Conversiones

- Primaria técnica: submit confirmado del formulario comercial.
- Secundarias: clic WhatsApp, descarga de temario, clic al puente B2B.
- Comercial: lead contactable, cotización y matrícula desde Zoho.

### PageSense

Para cada landing:

- proyecto o segmentación inequívoca;
- heatmap móvil y escritorio;
- Form Analytics;
- session recordings con PII enmascarada;
- funnel;
- segmentación por canal y campaña;
- goals de éxito real, no solo de clic.

### Google Analytics 4

GA4 debe aportar:

- source/medium/campaign;
- landing page;
- dispositivo;
- navegación;
- engagement;
- eventos y conversiones, una vez auditados.

GA4 no reemplaza Search Console, Google Ads, PageSense ni Zoho.

### Zoho

El mapeo conceptual debe preservar:

- fuente;
- medio;
- campaña;
- término;
- contenido;
- landing/variante;
- intención;
- buyer persona como hipótesis, no como verdad inferida;
- resultado comercial.

No crear campos ni API names sin auditar el módulo y los campos obligatorios.

## Google Ads y cluster `clases/profesor`

Antes de activar la landing C, ejecutar análisis read-only:

- términos que contengan `clases`, `profesor`, `particular`, `domicilio`, `presencial` y variantes;
- gasto, clics, CPC y conversiones registradas;
- Keyword Planner para consultas equivalentes;
- Auction Insights cuando exista evidencia útil;
- clasificación entre compatible, dudosa e incompatible.

Negativas conceptuales candidatas para la landing C, sujetas a revisión de concordancias:

- a domicilio;
- en casa;
- uno a uno / 1 a 1 cuando la intención sea exclusiva;
- gratis / gratuito;
- SENCE;
- online cuando no corresponda;
- profesor a domicilio.

No fijar un umbral monetario de corte sin aprobar presupuesto, ventana y criterio comercial.

## Search Console API

### Diferencia de fuentes

- Google Ads API: campañas, términos pagados, gasto, CPC, conversiones registradas y Keyword Planner.
- Search Console API: consultas orgánicas, páginas, clics, impresiones, CTR y posición media.
- GA4: comportamiento posterior al ingreso al sitio.
- PageSense: fricción y comportamiento dentro de la página.
- Zoho: submit, lead, cotización y matrícula.

### Estado

- Issue #36 creado para implementar export read-only.
- Scope previsto: `webmasters.readonly`.
- Credenciales, client secret, refresh token y CSV crudos deben permanecer fuera del repo.
- Primer export esperado: hasta 16 meses o máximo disponible, con `query + page`, `date + page`, `query + device` y filtros sobre Excel/presencial/básico/intermedio/Santiago.

### Próxima acción manual

Confirmar en Search Console:

- propiedad exacta, idealmente `sc-domain:capacita.cl` o el prefijo real;
- cuenta con acceso;
- rol/permiso en `Configuración → Usuarios y permisos`.

Después se habilita Search Console API en Google Cloud y se crea un cliente OAuth de escritorio read-only.

## Estado de Google Ads ya analizado

Periodo: 2026-04-12 a 2026-07-10.

Campaña B2C `EXCEL-PRE-STGO`:

- gasto aproximado: CLP 632.218;
- 670 clics;
- 100 conversiones registradas;
- CPA registrado aproximado: CLP 6.322.

Deterioro por bloques aproximados:

- CPA: 4.652 → 5.971 → 9.384;
- la caída principal está en conversión post-click, no solo en CPC.

Keyword crítica `curso excel básico e intermedio`:

- 99 clics;
- gasto aproximado: CLP 120.996;
- CPC medio aproximado: CLP 1.222;
- 4 conversiones registradas;
- CPA registrado aproximado: CLP 30.249.

La keyword mezcla básico, intermedio, desde cero, clases, gratis e intención informativa.

Competencia:

- Superprof es un competidor plausible, pero no se demostró como causa principal del deterioro;
- `ninjaexcel.com` mostró presión reciente en Auction Insights;
- Capacita mantuvo alta participación de impresiones y poca pérdida por presupuesto/ranking.

## Arquitectura de campaña todavía no ejecutada

No se ha autorizado ni ejecutado:

- creación de grupos de anuncios;
- nuevas keywords;
- negativas;
- cambios de anuncios;
- destinos;
- presupuesto;
- pujas;
- pausas.

La arquitectura candidata es una campaña B2C con grupos separados por intención, pero debe definirse después de publicar y validar las landings.

## Próxima secuencia recomendada

1. Abrir nuevo hilo usando este handoff.
2. Ejecutar `Context Gate: Bootstrap` por cambio de hilo.
3. Confirmar el estado real de PR #35, issue #36 y Edge #27/#28.
4. Cerrar matriz contractual de las tres landings: intención, buyer persona, H1, H2, CTA, exclusiones y contenido compartido.
5. Auditar bloques HTML de la landing actual en Capacita Edge.
6. Definir medición exacta por landing antes de construir.
7. Preparar un único prompt para Work con tres landings pagadas `noindex`, sin tocar Google Ads.
8. Implementar en rama y PR de Capacita Edge, con previews y pruebas.
9. Ejecutar Search Console API read-only.
10. Analizar cluster `clases/profesor` con Google Ads API y Keyword Planner.
11. Solo después autorizar cambios productivos en Google Ads.

## Criterios de continuidad de la landing C

La landing C es una prueba reversible. Debe mantenerse solo si produce señales comerciales suficientes:

- consultas compatibles con curso grupal;
- submits confirmados;
- leads contactables;
- cotizaciones o matrículas;
- términos de búsqueda coherentes;
- CPC y CPA aceptables según umbral aprobado.

Debe pausarse o retirarse si atrae principalmente:

- clases a domicilio;
- atención uno a uno exclusiva;
- gratuidad/SENCE;
- consultas incompatibles;
- gasto sin leads contactables.

## Prohibiciones permanentes

- No mentir sobre la oferta.
- No presentar curso grupal como particular.
- No prometer profesor a domicilio.
- No mezclar B2C y B2B en landing, formulario o medición.
- No usar SENCE ni beneficio tributario en B2C.
- No usar goals de clic como submit confirmado.
- No subir PII, secretos, credenciales, IDs completos, CSV crudos, grabaciones o binarios al repo público.
- No trabajar en `main`.
- No modificar campañas, presupuestos, pujas o producción sin autorización explícita.

## Prompt de inicio para el nuevo hilo

```text
Context Gate: Bootstrap.

Repo principal: misaeln-pc1/marketing-performance-capacita.
Repo técnico de landings: misaeln-pc1/capacita-edge.

Lee primero:
- docs/handoffs/HANDOFF_EXCEL_PAID_LANDINGS_SEARCH_CONSOLE_2026-07-12.md en la rama/PR documental vigente;
- DECISIONES.md;
- TASK_STATUS.md;
- PR #35;
- issue Marketing #36;
- issues Edge #27 y #28;
- briefs BP-001 y BP-002.

Objetivo inmediato:
1. recuperar y validar la decisión de conservar la página orgánica actual;
2. diseñar tres landings pagadas noindex:
   - Básico–Intermedio / BP-001;
   - Básico desde cero / BP-002;
   - clases presenciales con profesor / BP-001;
3. definir medición exacta para PageSense, GA4, GTM, Google Ads y Zoho antes de construir;
4. revisar los bloques HTML de la landing actual;
5. preparar después un único prompt operativo para Work en Capacita Edge.

Reglas:
- las tres venden el mismo curso grupal Básico–Intermedio presencial;
- la tercera no promete clases particulares ni a domicilio;
- no usar SENCE, beneficio tributario ni gratuidad en B2C;
- conservar el puente B2B como secundario;
- no tocar campañas ni producción sin autorización;
- no inventar eventos, IDs o API names;
- no tratar goals de clic como submits.
```

## Evidencia de cierre del hilo

- Documento de handoff creado en PR #35.
- Decisión de tercera landing registrada en `DECISIONES.md`.
- PR #35 actualizado.
- No se modificó producción.
- No se ejecutó Search Console OAuth.
- No se modificó Google Ads, PageSense, GTM, Zoho ni Cloudflare.
