# Gate obligatorio SEO + IA para contenido público V01

## Estado

- Estado: `OBLIGATORIO_DESDE_V01`.
- Semáforo: amarillo.
- Repo dueño de criterio: `misaeln-pc1/marketing-performance-capacita`.
- Implementación técnica: `misaeln-pc1/capacita-edge` u otro repo dueño de la web pública.
- Alcance: toda página, landing, artículo, ficha, FAQ, recurso o pieza pública de Capacita antes de publicar o actualizar.
- Fuera de alcance: cambios productivos, DNS, Cloudflare, GTM, PageSense, Zoho, campañas, presupuestos o formularios reales sin autorización explícita.

## Nombre operativo

Usar como nombre interno:

```text
SEO + IA Publication Gate
```

También puede referirse como:

```text
Gate SEO-AI
Visibilidad Orgánica y en Motores Generativos
SEO / AEO / GEO
```

Definición interna:

- **SEO:** rastreo, indexación, contenido útil, arquitectura, títulos, enlaces, page experience, structured data y medición orgánica.
- **Local SEO:** coherencia de entidad local, sede, nombre, dirección, teléfono, Google Business Profile, reseñas y presencia local.
- **AEO/GEO:** Answer Engine Optimization / Generative Engine Optimization. No se trata como trucos para manipular IA; se implementa como contenido verificable, textual, estructurado, útil, consistente y fácil de citar por motores de respuesta.

## Principio crítico

Google declara que las buenas prácticas SEO existentes siguen siendo relevantes para AI Overviews y AI Mode, y que no existen requisitos técnicos adicionales ni un marcado especial obligatorio para aparecer en esas funciones. Por tanto, Capacita no debe crear contenido inflado, oculto, engañoso ni archivos “para IA” como sustituto de SEO real.

Regla interna:

```text
Primero personas, luego buscadores, luego motores generativos.
```

## Estados posibles de una página pública

Toda URL pública debe quedar clasificada antes de publicarse:

| Estado | Uso | Reglas |
|---|---|---|
| `SEO_INDEXABLE` | Página orgánica o evergreen | indexable, canonical claro, sitemap si corresponde, enlaces internos, Search Console, structured data válido |
| `PAID_NOINDEX` | Landing pagada o experimento Ads | `noindex,follow`, fuera de sitemap, no compite con SEO, medición Ads/GA4/PageSense/Zoho |
| `TEMPORAL_NOINDEX` | Preview, staging, evento temporal, prueba | noindex, fuera de sitemap, no usar como fuente canónica |
| `ARCHIVAR_REDIRECT` | Página histórica que compite | plan de redirect/noindex solo con autorización |
| `NO_PUBLICAR` | Riesgo legal, comercial, técnico o de medición | detener |

## Caso especial: landings pagadas B2C Excel

Las tres landings pagadas de Excel B2C quedan inicialmente como:

```text
PAID_NOINDEX
```

Implicancias:

- No buscan posicionamiento orgánico inicial.
- No deben ir al sitemap.
- Deben usar `noindex,follow`.
- Deben proteger la página orgánica vigente:

```text
https://capacita.cl/curso-de-excel-presencial-en-santiago/
```

- No deben canibalizar SEO.
- Deben medir conversión y aprendizaje de mensaje.
- Si una variante demuestra potencial SEO, se abre una decisión posterior para convertirla en `SEO_INDEXABLE` o crear una página orgánica separada.

## Checklist obligatorio antes de publicar

### 1. Intención y público

- [ ] La intención principal está definida en una frase.
- [ ] Existe buyer persona o hipótesis de usuario asociada.
- [ ] La página no mezcla B2C con B2B si la medición requiere separación.
- [ ] La página no mezcla presencial, online, e-learning, SENCE, empresas y particulares salvo que ese sea el objetivo explícito.
- [ ] El CTA corresponde a la intención real.

### 2. Estado SEO

- [ ] La página está marcada como `SEO_INDEXABLE`, `PAID_NOINDEX`, `TEMPORAL_NOINDEX`, `ARCHIVAR_REDIRECT` o `NO_PUBLICAR`.
- [ ] Si es indexable, tiene canonical correcto.
- [ ] Si es noindex, no está en sitemap.
- [ ] Si es landing Ads noindex, no reemplaza ni contradice una página orgánica vigente.

### 3. Rastreo e indexación

- [ ] Googlebot puede recibir HTML completo cuando corresponda.
- [ ] Bingbot puede recibir HTML completo cuando corresponda.
- [ ] OAI-SearchBot no está bloqueado si la política aprobada permite visibilidad en ChatGPT Search.
- [ ] No hay desafío WAF, cookie wall, redirect extraño o bloqueo accidental para bots de búsqueda permitidos.
- [ ] Se valida robots.txt, meta robots y `X-Robots-Tag`.

### 4. Title, H1, H2 y metadatos

- [ ] `<title>` único, descriptivo y no inflado.
- [ ] H1 único y alineado con la intención.
- [ ] H2 explica promesa o diferenciador, no repite sin aportar.
- [ ] Meta description describe la oferta real y CTA.
- [ ] No hay keyword stuffing.
- [ ] Open Graph/Twitter metadata coherente si aplica.

### 5. Contenido visible

- [ ] El contenido importante está en texto HTML visible, no sólo en imagen.
- [ ] Se explican modalidad, ubicación, duración, nivel, requisitos, temario y CTA.
- [ ] Las FAQs responden preguntas reales.
- [ ] No hay promesas no verificables: empleo garantizado, gratuidad, ROI, resultados garantizados, cupos falsos, fechas falsas.
- [ ] Las menciones a SENCE, Ministerio, normas de calidad, certificación o reemisión de certificados tienen base verificable y redacción prudente.

### 6. Confianza, E-E-A-T y entidad

- [ ] Se identifica Capacita como institución/OTEC cuando corresponda.
- [ ] La sede, ciudad y modalidad son consistentes.
- [ ] Se declara respaldo institucional sin exagerar.
- [ ] Se usan testimonios, logos, reseñas o evidencia sólo si están autorizados.
- [ ] Existe forma clara de contacto y trazabilidad comercial.

### 7. Structured data

- [ ] JSON-LD sólo marca contenido visible.
- [ ] No se marca contenido irrelevante, falso o no visible.
- [ ] `Organization`/`LocalBusiness` son coherentes con la entidad real.
- [ ] Course/Event/FAQ/Breadcrumb se usan sólo si corresponden y pasan validación.
- [ ] Rich Results Test o validador equivalente queda documentado si aplica.

### 8. Page experience y accesibilidad

- [ ] Mobile visible y legible.
- [ ] Core Web Vitals/PageSpeed revisados para bloqueo evidente.
- [ ] Imágenes optimizadas con alt útil.
- [ ] No hay interstitials intrusivos.
- [ ] Formularios son usables en móvil.
- [ ] No hay contenido principal oculto detrás de scripts que no cargan.

### 9. Medición

- [ ] `landing_code` definido.
- [ ] UTMs preservadas.
- [ ] GA4/GTM/PageSense configurados o explicitados como pendiente.
- [ ] Evento de submit confirmado separado de clics.
- [ ] Zoho puede distinguir landing/intención/fuente de forma agregada.
- [ ] Search Console se revisa si la página es indexable.
- [ ] Benchmark IA se usa sólo para páginas indexables o páginas de entidad.

### 10. Riesgos y aprobación

- [ ] Se declara si el cambio puede afectar SEO orgánico.
- [ ] Se declara si toca formularios, tracking, producción, DNS, Cloudflare, campañas o presupuestos.
- [ ] Si hay riesgo rojo, se detiene hasta autorización explícita.

## Checklist posterior a publicación

### Día 0 — publicación técnica

- [ ] URL responde 200.
- [ ] Estado SEO correcto (`indexable` o `noindex`).
- [ ] Canonical correcto.
- [ ] Sitemap correcto.
- [ ] Formulario funciona.
- [ ] Submit confirmado registrado.
- [ ] GA4/GTM/PageSense reciben eventos.
- [ ] No hay errores visuales mobile.

### Día 1–3 — sanity check

- [ ] No hay tráfico roto.
- [ ] No hay leads sin fuente.
- [ ] No hay duplicidad de conversiones.
- [ ] No hay URL incorrecta en Ads.
- [ ] No hay canibalización evidente de la página orgánica.

### Día 7 — primera lectura táctica

- [ ] Impresiones/clics/sesiones por fuente.
- [ ] CTR Ads u orgánico según estado.
- [ ] Form start / submit attempt / submit confirmado.
- [ ] Lead contactable y señales comerciales iniciales.
- [ ] Primeras hipótesis de copy o UX.

### Día 14–30 — aprendizaje

- [ ] Comparar contra baseline.
- [ ] Definir conservar, iterar, pausar o convertir en orgánica.
- [ ] Registrar aprendizaje en GitHub.

## DoD para declarar una página pública lista

Una página pública sólo queda lista cuando existe:

- URL final o preview estable.
- estado SEO declarado.
- title/H1/H2/meta revisados.
- contenido visible y coherente.
- claims verificados o redactados con cautela.
- structured data validado si aplica.
- tracking validado.
- formulario probado.
- riesgo SEO declarado.
- evidencia mínima: captura, diff, SHA, PR, preview o validación.

## Relación con documentos existentes

Este gate complementa:

- `docs/seo-ai/SEO_GEO_TECHNICAL_RESEARCH_BASELINE_V01.md`.
- `docs/seo-ai/SEO_GEO_MEASUREMENT_MODEL_V01.md`.
- `docs/seo-ai/SEO_GEO_AUDIT_HANDOFF_TO_EDGE_V01.md`.
- `docs/landing-pages/EXCEL_B2C_PAID_LANDINGS_STATUS_BASELINE_2026-07-26.md`.

## Fuentes normativas

Fuentes primarias a revisar ante cambios relevantes:

- Google Search Essentials.
- Google AI features and your website.
- Google SEO guide for developers.
- Google helpful, reliable, people-first content.
- Google title links documentation.
- Google structured data guidelines.
- Google Page Experience.
- Bing Webmaster guidance para robots/meta cuando se audite Bing.

## Seguridad documental

GitHub guarda metodología, checklist, decisiones, síntesis sanitizada y evidencia mínima. No versionar:

- exports completos de Search Console, GA4, Ads o Zoho;
- logs crudos;
- credenciales;
- IDs completos;
- datos personales;
- capturas sensibles;
- información privada de alumnos, leads o clientes.
