# Baseline técnico SEO, Local SEO y visibilidad en IA V01

## Objetivo

Definir una metodología técnica y medible para mejorar descubrimiento, posicionamiento y conversión de Capacita en:

- Google Search y Google Maps;
- resultados con IA de Google;
- ChatGPT Search;
- Gemini y otros motores de respuesta con fuentes públicas;
- tráfico orgánico que termina en lead y matrícula.

Este documento no autoriza cambios productivos. La implementación técnica pertenece a `misaeln-pc1/capacita-edge` y debe ejecutarse con plan, validación y rollback.

## Nombre operativo

Usar internamente **Visibilidad Orgánica y en Motores Generativos**.

Componentes:

1. SEO técnico.
2. SEO local.
3. contenido y arquitectura de información.
4. entidad, autoridad y reputación.
5. AEO/GEO — Answer Engine Optimization / Generative Engine Optimization.
6. medición y optimización de conversión.

No tratar GEO como una disciplina aislada ni como trucos para manipular modelos. La base sigue siendo rastreo, indexación, información verificable, contenido útil, señales de entidad, reputación y medición.

## Fuentes primarias de referencia

- OpenAI: documentación oficial de OAI-SearchBot, GPTBot y ChatGPT-User.
- Google Search Central: AI features, requisitos técnicos, crawling, indexación, canonicals, structured data y Search Console.
- Google Business Profile: relevancia, distancia y prominencia para SEO local.
- Cloudflare: Verified Bots, AI Crawl Control, WAF y métricas de crawlers.
- Schema.org / Google structured data: Organization, LocalBusiness, Course list, Breadcrumb y otros tipos aplicables.
- IndexNow: notificación de URLs actualizadas a buscadores participantes.
- Literatura académica sobre Generative Engine Optimization, usada como referencia experimental y no como garantía de ranking.

## Hallazgos preliminares públicos

1. `capacita.cl` es accesible y su contenido puede ser leído por un crawler web general.
2. Existe una landing específica y actual para `curso de Excel presencial en Santiago`.
3. Persisten páginas WordPress históricas con URLs y fechas de enero de 2026 que compiten semánticamente con la landing actual.
4. La página de cursos vigentes mezcla modalidades, públicos y múltiples niveles en una sola URL.
5. La homepage mezcla catálogo, modalidad presencial, e-learning, empresas y fechas; esto puede debilitar la señal específica para consultas locales de Excel presencial.
6. La ausencia de Capacita en respuestas generativas no prueba por sí sola un bloqueo de bots. Deben auditarse robots.txt, meta robots, X-Robots-Tag, canonicals, sitemaps, WAF, políticas de bots, logs, indexación, entidad y autoridad externa.

## Hipótesis técnicas

### H1 — Rastreo o acceso parcial

OAI-SearchBot, Googlebot, Bingbot u otros crawlers pueden estar bloqueados o desafiados por robots.txt, WAF, Bot Fight Mode, AI Crawl Control, redirecciones, cookies o respuestas diferentes por user-agent.

### H2 — Canonicalización y duplicidad

Páginas históricas y landings actuales pueden competir por la misma intención: Excel presencial, básico, intermedio y Santiago. Canonicals, redirects y enlaces internos podrían no consolidar correctamente la página vigente.

### H3 — Frescura y vigencia

Fechas antiguas visibles, slugs con meses pasados y páginas que siguen indexables pueden enviar señales inconsistentes sobre oferta vigente.

### H4 — Entidad local insuficiente

La relación entre marca, razón social, OTEC, dirección, teléfono, sede, servicios, perfiles externos y Google Business Profile puede no estar expresada de forma consistente y verificable.

### H5 — Cobertura semántica insuficiente

Puede existir contenido comercial, pero faltar páginas estables y claramente diferenciadas para intenciones como:

- curso de Excel presencial en Santiago Centro;
- Excel básico desde cero;
- Excel básico e intermedio;
- Excel intermedio;
- clases particulares o profesor a domicilio;
- capacitación Excel para empresas.

La creación de páginas adicionales se decide después de analizar demanda, términos reales, canibalización, conversión y capacidad operativa.

### H6 — Autoridad externa insuficiente

Los motores generativos pueden preferir fuentes externas y entidades con mayor reconocimiento, enlaces, menciones, reseñas y consistencia en directorios. Una web técnicamente correcta no garantiza aparecer entre las primeras instituciones recomendadas.

### H7 — Medición incompleta

Search Console, GA4/GTM, Google Ads y Zoho pueden no estar conectados de extremo a extremo, impidiendo medir impresión, clic, sesión, consulta, formulario, lead contactable, cotización y matrícula.

## Auditoría técnica mínima

### Rastreo e indexación

- comprobar `robots.txt` en dominio y subdominios;
- validar OAI-SearchBot, Googlebot y Bingbot;
- revisar Cloudflare WAF, Bot Fight Mode, AI Crawl Control y Verified Bots;
- inspeccionar códigos HTTP, redirecciones y desafíos por user-agent;
- validar meta robots y `X-Robots-Tag`;
- inventariar sitemaps y URLs enviadas;
- revisar indexación y URL Inspection en Search Console;
- revisar Bing Webmaster Tools e IndexNow cuando corresponda;
- analizar logs de crawlers sin PII.

### Arquitectura y canonicals

- inventariar WordPress, Cloudflare Pages y subdominios;
- mapear URL vigente, duplicada, histórica, redirigida y canónica;
- revisar `rel=canonical`, hreflang si aplica, enlaces internos y breadcrumbs;
- eliminar del índice páginas de campañas expiradas solo mediante plan aprobado;
- mantener páginas evergreen separadas de fechas/ofertas temporales.

### Entidad y SEO local

- auditar Google Business Profile;
- consistencia de nombre, dirección y teléfono;
- `Organization` y `LocalBusiness` JSON-LD coherentes con contenido visible;
- perfiles oficiales, redes, directorios y menciones verificables;
- reseñas, respuestas y evidencia de sede física;
- relación entre Capacita, OTEC, cursos, sede y modalidades.

### Contenido y motores generativos

- contenido factual, específico, vigente y fácil de citar;
- preguntas y respuestas reales, no texto inflado;
- páginas con oferta, modalidad, nivel, ubicación, duración, requisitos, temario y evidencia;
- autores, fechas de actualización y fuentes cuando correspondan;
- structured data consistente con el texto visible;
- permitir OAI-SearchBot para Search cuando esa sea la política aprobada;
- no confundir GPTBot de entrenamiento con OAI-SearchBot de búsqueda;
- no depender de `llms.txt` como requisito de Google o garantía de visibilidad.

### Medición

- Search Console: consultas, páginas, países, dispositivos e indexación;
- Bing Webmaster Tools: indexación y consultas cuando exista volumen;
- GA4/GTM: landing, navegación, eventos y conversiones;
- logs Cloudflare: crawler, hostname, path, status y regla aplicada;
- benchmark periódico de respuestas de ChatGPT y Gemini;
- Zoho: leads, contactabilidad, cotización y matrícula agregadas.

## Benchmark de visibilidad IA

Construir un set versionado de consultas, sin personalización y con fecha:

- `15 instituciones con cursos de Excel presencial en Santiago`;
- `curso de Excel básico presencial Santiago Centro`;
- `curso Excel básico e intermedio presencial Chile`;
- `dónde estudiar Excel presencial cerca de Metro La Moneda`;
- `clases de Excel presenciales para principiantes en Santiago`;
- consultas B2B separadas de B2C.

Registrar por motor y ejecución:

- si Capacita aparece;
- posición aproximada o presencia/ausencia;
- URL citada;
- fuentes utilizadas;
- competidores repetidos;
- exactitud de modalidad, ubicación y oferta;
- variación entre formulaciones;
- fecha, país/idioma y condición de sesión.

No interpretar una sola respuesta como ranking estable. Medir persistencia y cobertura en un conjunto de prompts repetibles.

## Sistema de mejora continua

Ciclo mensual recomendado después del baseline:

1. rastrear e indexar;
2. medir consultas y conversiones;
3. detectar brechas de intención y entidad;
4. priorizar una hipótesis;
5. implementar un cambio reversible;
6. validar crawling, indexación y tracking;
7. medir 28–30 días;
8. conservar, corregir o revertir;
9. registrar aprendizaje agregado.

## DoD del baseline

- mapa dominio/subdominio/tecnología;
- inventario de URLs vigentes, históricas y duplicadas;
- robots, headers, sitemap, canonicals y WAF auditados;
- OAI-SearchBot, Googlebot y Bingbot probados;
- Search Console y Business Profile revisados;
- structured data validado;
- benchmark IA versionado;
- eventos y atribución reconciliados con Zoho de forma agregada;
- backlog priorizado por impacto en ventas, esfuerzo y riesgo;
- ninguna recomendación de producción sin evidencia y autorización.

## Seguridad

No versionar credenciales, IDs completos, capturas sensibles, logs crudos, exports de Search Console/Analytics/CRM ni PII. GitHub guarda metodología, síntesis sanitizada, decisiones y evidencia mínima.
