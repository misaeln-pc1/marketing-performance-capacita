# Search Console API y decisión de landings pagadas — V01

Fecha: 2026-07-12
Estado: decisión aprobada para diseño; implementación pendiente y separada

## Decisión vigente

1. Conservar la página orgánica actual de Excel presencial indexable, con cambios sólo operativos mínimos como fechas vigentes y correcciones evidentes.
2. Crear dos landings B2C nuevas, exclusivas de tráfico pagado y configuradas inicialmente con `noindex,follow`:
   - landing pagada Básico–Intermedio, orientada a `BP-001 — Desbordado Operativo`;
   - landing pagada Excel Básico desde cero, orientada a `BP-002 — Reinserción Laboral`.
3. Las landings pagadas deben ser reutilizables por Google Ads, Meta y otros canales mediante UTM y `landing_code` propios.
4. No crear tres o cuatro landings en esta fase. Una landing adicional exige producto, intención, buyer persona, hipótesis, oferta y medición propios.
5. Excel Avanzado es otro producto/curso y no se agrega a este experimento.
6. SENCE, beneficio tributario y gratuidad quedan excluidos de toda comunicación B2C.

Esta decisión reemplaza la alternativa anterior de crear dos páginas nuevas indexables.

## Arquitectura propuesta

### Página orgánica actual

- indexable;
- canonical autorreferente;
- en sitemap;
- no se reescribe agresivamente;
- preserva el activo SEO acumulado;
- sólo recibe cambios operativos mínimos hasta revisar Search Console.

### Landing pagada 1 — Básico–Intermedio

- `noindex,follow`;
- fuera del sitemap;
- intención: ruta completa presencial desde fundamentos hasta nivel intermedio;
- buyer persona primario: `BP-001`;
- mensaje: productividad, errores, dependencia y aplicación laboral;
- misma oferta real, precio, fechas, duración y temario;
- formulario y `landing_code` propios;
- CTA comercial único;
- sin SENCE ni regalo como promesa principal.

### Landing pagada 2 — Básico desde cero

- `noindex,follow`;
- fuera del sitemap;
- intención: comenzar sin conocimientos previos de Excel;
- buyer persona primario: `BP-002`;
- mensaje: inseguridad de nivel, ruta clara, acompañamiento y confianza;
- transparencia: es el mismo curso Básico–Intermedio, presentado desde la necesidad de comenzar desde cero;
- formulario y `landing_code` propios;
- CTA comercial único;
- sin SENCE ni regalo como promesa principal.

## Diferencia entre Google Ads API y Search Console API

### Google Ads API

Responde qué ocurre dentro de la publicidad pagada:

- campañas, grupos, anuncios y keywords;
- impresiones, clics, gasto, CPC y conversiones registradas;
- términos reales de búsqueda pagada mediante `search_term_view`;
- ideas, volumen histórico, competencia, CPC estimado y previsiones mediante Keyword Planning;
- dispositivos, ubicaciones, assets, sitelinks y cambios de cuenta cuando la API lo permite.

No entrega por sí sola el rendimiento orgánico completo del sitio.

### Search Console API

Responde qué ocurre en los resultados orgánicos de Google:

- consultas orgánicas;
- páginas que aparecieron;
- clics, impresiones, CTR y posición media;
- país, dispositivo, fecha y apariencia de búsqueda;
- comparación por URL y consulta;
- evolución histórica de la página orgánica.

Requiere autorización OAuth separada y scope read-only `https://www.googleapis.com/auth/webmasters.readonly`.

### Diferencia operativa

- Ads API: demanda pagada y eficiencia de campañas.
- Search Console API: visibilidad orgánica y consultas SEO.
- Keyword Planner: demanda potencial estimada, incluso sin campaña activa.
- PageSense: comportamiento dentro de la landing.
- Zoho Forms/CRM: submit, lead, cotización y matrícula real.

Ninguna fuente reemplaza a las otras.

## Cruce mínimo recomendado

1. Google Ads `search_term_view`: qué búsquedas pagadas activaron anuncios y cuánto costaron.
2. Google Ads Keyword Planner: qué términos tienen volumen, competencia y CPC estimado.
3. Search Console API: qué consultas orgánicas muestran la página actual, con clics, impresiones, CTR y posición.
4. PageSense: qué hacen los visitantes dentro de la página.
5. Zoho: qué termina en lead contactable, cotización y matrícula.

## Primera extracción Search Console

Periodo objetivo: hasta 16 meses o el máximo disponible para la propiedad.

Exportar agregados privados:

- `query + page`;
- `date + page`;
- `query + device`;
- filtro por la URL orgánica actual;
- filtro por consultas con `excel`, `basico`, `intermedio`, `presencial`, `santiago`;
- clics, impresiones, CTR y posición;
- paginación hasta 25.000 filas por solicitud usando `startRow` cuando corresponda.

Los exports crudos, credenciales, client secret, refresh token y URLs sensibles permanecen fuera del repo público. GitHub conserva sólo metodología, agregados y decisiones sanitizadas.

## Definition of Done de la API read-only

- Search Console API habilitada en un proyecto Google Cloud apropiado;
- autorización read-only validada;
- propiedad correcta identificada sin exponer datos sensibles;
- script read-only local fuera del repo o sanitizado;
- export inicial de consultas y páginas;
- comparación con términos pagados y Keyword Planner;
- informe agregado sobre la página orgánica actual;
- ninguna modificación de Search Console, Ads, sitemap, canonicals o producción.

## Pendiente

- confirmar la propiedad exacta de Search Console;
- definir si se reutiliza el proyecto Google Cloud existente o uno separado;
- validar si el usuario autenticado tiene acceso suficiente a la propiedad;
- implementar y ejecutar el export read-only;
- decidir después si alguna landing pagada merece evolucionar a página SEO independiente.
