# Exclusión SENCE y alternativas de arquitectura orgánica/pagada — Excel B2C

Fecha: 2026-07-12  
Estado: conversación estratégica en evaluación; no constituye decisión final ni autoriza cambios productivos.

## 1. Regla operativa sobre SENCE

### B2C

No usar en páginas, anuncios, keywords, copies, FAQ, schema, títulos ni CTA B2C:

- SENCE;
- franquicia tributaria;
- beneficio tributario;
- curso SENCE;
- curso gratis SENCE;
- gratuidad asociada a SENCE.

Motivo operativo reportado por Misael: estos términos atrajeron búsquedas de cursos gratuitos y generaron gasto significativo sin intención de matrícula pagada.

### B2B

Usar con cautela y solo en una ruta empresarial explícita, separada de B2C. No introducir SENCE ni franquicia tributaria en la tarjeta puente "capacitación para equipos" de la landing B2C.

Cualquier mención futura en B2B requiere:

- oferta aplicable y vigente;
- copy que no sugiera gratuidad;
- campaña, landing y medición separadas;
- revisión de términos reales;
- negativas para consultas de gratuidad cuando corresponda;
- autorización antes de publicación.

## 2. Estado SEO actual

La página pública vigente de Excel presencial está accesible, indexable y contiene una oferta completa del curso Básico e Intermedio presencial.

Misael reporta que la página posee posicionamiento orgánico fuerte y aparece habitualmente en primera página para consultas relevantes.

Esta posición no debe darse por confirmada mediante una búsqueda aislada, porque el ranking varía por ubicación, historial, dispositivo y momento. Antes de modificar, redirigir o retirar una URL existente se debe revisar Search Console.

Regla provisional:

> No modificar, redirigir, poner noindex ni retirar del sitemap la página orgánica vigente hasta contar con su baseline en Search Console y la URL exacta de cualquier página histórica relacionada.

## 3. Riesgo de alterar una página orgánica ganadora

Modificar de forma extensa una URL con tráfico y ranking acumulado puede cambiar:

- consultas por las que aparece;
- CTR orgánico;
- cobertura semántica;
- enlaces internos;
- snippets;
- canonicalización;
- rendimiento por dispositivo.

No se recomienda reemplazarla o dividirla por intuición sin evidencia.

Google indica que, cuando existen páginas similares, las señales pueden consolidarse en una URL canónica y que las páginas sustancialmente similares creadas para consultas próximas pueden caer en patrones de doorway abuse si no aportan utilidad propia.

## 4. Alternativas en evaluación

### Alternativa A — Proteger SEO y crear dos landings pagadas noindex

**Arquitectura**

1. Mantener intacta la página orgánica actual.
2. Crear una landing pagada `Básico e Intermedio`.
3. Crear una landing pagada `Excel Básico desde cero`.
4. Ambas nuevas con `noindex`, fuera del sitemap y sin enlaces internos orgánicos.
5. Cada landing pagada con intención, buyer persona, anuncio, keyword y `landing_code` propios.

**Ventajas**

- protege la página orgánica existente;
- permite máxima alineación anuncio → landing;
- elimina canibalización SEO entre las dos nuevas;
- permite usar buyer persona de forma táctica en Search Ads;
- es reversible.

**Riesgos/costos**

- tres páginas del mismo curso;
- mantenimiento duplicado de fecha, precio y temario;
- el orgánico sigue resolviendo una intención amplia;
- requiere control para que las landings pagadas no entren al sitemap ni enlaces internos.

**Estado**

Candidata conservadora. Es la opción preferente si Search Console confirma que la página actual es un activo orgánico valioso.

### Alternativa B — Mantener orgánica actual y crear solo landing pagada básica

**Arquitectura**

- página actual orgánica y destino del grupo general/Básico–Intermedio;
- nueva landing pagada `Excel Básico desde cero` con `noindex`.

**Ventajas**

- menor trabajo;
- protege SEO;
- resuelve la intención básica más costosa.

**Riesgos/costos**

- la landing actual seguiría mezclando mensajes;
- la comparación no sería simétrica;
- la intención general mantendría el problema CRO actual.

**Estado**

Candidata mínima, pero menos limpia.

### Alternativa C — Refactor SEO completo con dos páginas indexables

**Arquitectura**

- modificar la página actual para Básico–Intermedio;
- crear una nueva página indexable Básico desde cero;
- resolver la página histórica mediante reutilización o 301.

**Ventajas**

- arquitectura orgánica clara a largo plazo;
- dos intenciones SEO distintas;
- menor dependencia de páginas pagadas noindex.

**Riesgos/costos**

- mayor riesgo sobre el ranking existente;
- requiere Search Console, inventario de URLs, canonicals, sitemap y enlaces internos;
- ejecución más lenta;
- cambios simultáneos dificultan atribución.

**Estado**

No recomendada todavía sin baseline SEO.

## 5. Buyer persona en las nuevas landings pagadas

Hipótesis de trabajo, no decisión final:

- landing pagada Básico–Intermedio: `BP-001 — Desbordado Operativo`;
- landing pagada Básico desde cero: `BP-002 — Reinserción Laboral`.

En Google Search la intención declarada por la consulta gobierna primero; el buyer persona organiza el dolor, la promesa, objeciones y CTA dentro de la página.

No inferir buyer persona por una sola keyword. El mapeo es una hipótesis táctica que debe validarse con calidad del lead y matrícula, no solo CPC o CTR.

## 6. Evidencia requerida antes de decidir

1. Search Console, idealmente 16 meses:
   - páginas;
   - consultas;
   - clics;
   - impresiones;
   - CTR;
   - posición media;
   - dispositivo;
   - país.
2. URL exacta de la página histórica de Excel básico.
3. Canonical, indexación y presencia en sitemap de cada URL.
4. Landing pages reales de Google Ads y origen de los desvíos.
5. Rendimiento orgánico y pagado separado.
6. Backlinks o enlaces internos relevantes, solo si afectan la decisión.

## 7. Decisión provisional

No definir todavía dos páginas indexables.

Mantener abiertas estas opciones:

- conservar la página orgánica actual como activo SEO;
- crear dos landings pagadas noindex con buyer persona;
- reevaluar una arquitectura SEO de dos páginas después del baseline de Search Console.

## 8. Prohibiciones mientras se decide

- no tocar la URL orgánica actual;
- no aplicar 301;
- no agregar `noindex` a la página vigente;
- no cambiar canonical;
- no eliminar del sitemap;
- no introducir SENCE en B2C;
- no activar campañas o landings nuevas sin medición separada;
- no declarar que una página rankea primera sin evidencia de Search Console o prueba reproducible.
