# Análisis Search Console — Excel presencial y arquitectura de landings pagadas

**Fecha del análisis:** 2026-07-12  
**Propiedad:** `https://capacita.cl/`  
**Periodo:** 2025-03-09 a 2026-07-09  
**Modo:** Search Console API read-only  
**Estado:** análisis agregado completado; faltan cruce con GA4, Google Ads y resultados comerciales.

## 1. Evidencia analizada

Export privado local, no versionado:

| Reporte | Filas |
|---|---:|
| `query_page.csv` | 16.489 |
| `date_page.csv` | 41.197 |
| `query_device.csv` | 12.877 |
| Cluster Excel | 10.305 |
| Landing orgánica Excel | 301 consultas visibles |

Baseline agregado informado por la API:

- 36.301 clics;
- 932.546 impresiones;
- CTR 3,89%;
- posición media 10,82;
- errores API: 0;
- token y credenciales no incluidos en los outputs.

### Regla metodológica

- `date_page` se usa para los totales de una URL y su evolución.
- `query_page` se usa para distribuir consultas e intención.
- `query_device` se usa para tendencias por dispositivo a nivel de consulta.
- Search Console omite o agrega parte de las consultas por privacidad. Por eso la suma de las filas con dimensión `query` no equivale al total de la página.
- No se publican CSV crudos, consultas de cola larga potencialmente sensibles ni credenciales.

## 2. Conclusión ejecutiva

1. **La página orgánica actual debe conservarse.** Tiene rendimiento sólido para la intención general `curso de Excel presencial en Santiago`.
2. **No está posicionada principalmente para “Excel básico” ni “Básico–Intermedio”.** Su fortaleza orgánica real es la intención presencial general.
3. **La hipótesis de una landing pagada de “clases presenciales con profesor” tiene evidencia real**, pero el núcleo debe ser `clases de Excel presencial`; no `profesor particular` ni `a domicilio`.
4. **La arquitectura vigente de tres landings pagadas `noindex` sigue siendo la opción de menor riesgo.** Publicarlas indexables ahora aumentaría una fragmentación orgánica ya relevante.
5. **Existe una deuda SEO importante por páginas históricas.** Decenas de URLs de Excel siguen recibiendo impresiones o clics y varias compiten por consultas similares.
6. **Google Analytics 4 no es redundante.** Search Console explica qué ocurre antes del clic orgánico; GA4 debe explicar qué ocurre después de entrar a la web.

## 3. Rendimiento de la landing orgánica actual

Se consolidaron las dos formas históricas de la misma ruta:

- `https://capacita.cl/curso-de-excel-presencial-en-santiago/`
- `https://capacita.cl/curso-de-excel-presencial-en-santiago`

### Total consolidado

| Métrica | Resultado |
|---|---:|
| Clics orgánicos | 876 |
| Impresiones | 11.349 |
| CTR | 7,72% |
| Posición media | 6,05 |
| Primera fecha observada | 2026-01-12 |
| Última fecha del export | 2026-07-09 |

La landing representa aproximadamente:

- 2,4% de los clics agregados de la propiedad;
- 1,2% de las impresiones agregadas de la propiedad.

### Evolución reciente

| Ventana | Clics | Impresiones | CTR | Posición |
|---|---:|---:|---:|---:|
| 90 días | 366 | 4.353 | 8,41% | 6,47 |
| 30 días | 119 | 1.553 | 7,66% | 7,35 |
| 7 días | 27 | 347 | 7,78% | 7,85 |

Interpretación:

- el tráfico se mantiene relativamente estable;
- la posición media muestra un deterioro moderado reciente;
- no existe evidencia para alterar agresivamente la página;
- sí corresponde monitorear la pérdida gradual de posición.

## 4. Consultas que realmente sostienen la página

Principales consultas visibles y sanitizadas:

| Consulta | Clics | Impresiones | CTR | Posición |
|---|---:|---:|---:|---:|
| curso de excel presencial | 92 | 636 | 14,47% | 2,03 |
| curso excel presencial santiago | 86 | 460 | 18,70% | 1,35 |
| cursos de excel presencial | 63 | 474 | 13,29% | 1,92 |
| curso excel presencial | 61 | 435 | 14,02% | 1,85 |
| cursos de excel presencial en santiago de chile | 46 | 230 | 20,00% | 1,17 |
| cursos excel presencial | 37 | 312 | 11,86% | 1,98 |
| curso de excel presencial santiago | 31 | 159 | 19,50% | 1,14 |
| curso presencial de excel | 23 | 240 | 9,58% | 3,35 |
| excel presencial | 11 | 61 | 18,03% | 1,70 |
| clases de excel presencial | 10 | 138 | 7,25% | 2,59 |

Esto confirma la percepción de Misael: para búsquedas comerciales específicas de presencialidad, Capacita aparece habitualmente en posiciones orgánicas muy altas.

## 5. Distribución por intención de la landing actual

Distribución sobre las consultas visibles de `query_page`; no incluye consultas anonimizadas:

| Intención | Clics | Impresiones | CTR | Posición | % clics visibles |
|---|---:|---:|---:|---:|---:|
| Presencial general | 499 | 4.235 | 11,78% | 3,02 | 89,6% |
| Clases/profesor | 19 | 320 | 5,94% | 8,33 | 3,4% |
| Genérico/otro | 28 | 3.128 | 0,90% | 11,56 | 5,0% |
| Intermedio | 7 | 31 | 22,58% | 3,81 | 1,3% |
| Básico/desde cero | 2 | 64 | 3,13% | 9,91 | 0,4% |
| Gratuidad/SENCE | 2 | 25 | 8,00% | 9,68 | 0,4% |
| Básico–Intermedio | 0 | 4 | 0,00% | 4,75 | 0,0% |

### Implicación

La página orgánica no es actualmente una página fuerte para:

- `curso Excel básico presencial`;
- `Excel desde cero`;
- `curso Excel básico e intermedio`.

Su posicionamiento real es mucho más claro:

> curso de Excel presencial en Santiago.

Por eso no debe reescribirse para forzar las tres intenciones.

## 6. Evidencia para la landing C — clases presenciales con profesor

### Señal en la página actual

Cluster visible `clases/profesor`:

- 19 clics;
- 320 impresiones;
- CTR 5,94%;
- posición media 8,33.

Consultas destacadas:

- `clases de excel presencial`: 10 clics, 138 impresiones, posición 2,59;
- `clases excel presencial`: 6 clics, 23 impresiones, posición 1,22;
- `clases presenciales de excel`: 2 clics, 14 impresiones, posición 2,93.

### Señal en todo el sitio

`clases de excel presencial` acumuló:

- 53 clics;
- 1.101 impresiones;
- posición media 5,70;
- presencia histórica en 46 URLs.

En cambio, `profesor de excel` registró:

- 0 clics;
- 42 impresiones;
- posición media 10,14.

### Decisión derivada

La tercera landing tiene sustento para prueba pagada, pero debe priorizar:

> Clases de Excel presenciales con profesor en vivo, dentro de un curso grupal estructurado.

No debe priorizar como keyword principal:

- profesor particular;
- profesor a domicilio;
- clases uno a uno.

## 7. Evidencia para la landing B — Excel básico desde cero

La landing orgánica actual solo obtuvo, en consultas visibles del cluster básico:

- 2 clics;
- 64 impresiones;
- posición media 9,91.

En todo el sitio existe demanda, pero está fragmentada:

| Consulta | Clics | Impresiones | Posición | URLs observadas |
|---|---:|---:|---:|---:|
| curso excel básico presencial | 29 | 340 | 4,64 | 25 |
| curso de excel básico presencial | 9 | 171 | 3,64 | 22 |

Esto apoya una landing pagada específica para principiantes, pero no justifica indexarla todavía: el sitio ya distribuye la intención básica entre demasiadas URLs.

## 8. Evidencia para la landing A — Básico–Intermedio

La consulta exacta sin tildes `curso de excel basico e intermedio` tuvo, en todo el sitio:

- 3 clics;
- 276 impresiones;
- posición media 34,0;
- 22 URLs observadas.

`curso excel basico intermedio` tuvo:

- 2 clics;
- 66 impresiones;
- posición media 18,7;
- 17 URLs observadas.

La landing orgánica actual casi no captura esta intención. Existe una brecha clara entre:

- el volumen pagado y el gasto elevado de la keyword;
- la débil visibilidad orgánica para la formulación Básico–Intermedio.

La landing A tiene sentido como destino pagado específico. Su publicación `noindex` no solucionará el SEO de este cluster, pero sí permitirá probar relevancia y conversión sin aumentar la fragmentación orgánica.

## 9. Fragmentación y canibalización histórica

### Volumen de URLs activas

URLs que contienen `excel` y registraron actividad:

| Ventana | URLs con impresiones | URLs con clics |
|---|---:|---:|
| 90 días | 123 | 52 |
| 30 días | 92 | 30 |

Esto no significa que todas sean duplicados, porque existen tests, artículos y cursos de otros niveles. Sin embargo, sí confirma una superficie histórica demasiado amplia para consultas comerciales presenciales.

### Ejemplos

- `curso excel presencial` apareció asociado históricamente a 53 URLs;
- `curso de excel presencial` a 51 URLs;
- `curso excel básico presencial` a 25 URLs;
- `clases de excel presencial` a 46 URLs.

### Página histórica principal

`https://capacita.cl/curso-excel-presencial-julio2023/` registró:

- 1.345 clics;
- 17.423 impresiones;
- último día observado: 2026-01-27.

La página orgánica actual comenzó a aparecer el 2026-01-12. Ambas coexistieron durante una transición corta. La página histórica actualmente redirige a la landing nueva.

### Normalización con y sin slash

- La versión con slash recibió tráfico entre 2026-01-12 y 2026-05-12.
- La versión sin slash comenzó el 2026-05-09 y continúa vigente.
- Actualmente la URL con slash redirige a la versión sin slash.

Esto parece una migración de URL, no dos páginas activas actuales. Sin embargo, el historial queda dividido y debe confirmarse:

- canonical autorreferente final;
- redirección 301 directa;
- ausencia de cadenas de dos saltos desde URLs históricas;
- sitemap con una sola forma de URL;
- enlaces internos apuntando directamente a la URL final.

### Riesgo observado

La ruta histórica `curso-excel-presencial-julio2023/` redirige aparentemente a la versión con slash, y ésta redirige a la versión sin slash. Edge #28 debe validar mediante respuesta HTTP si existe una cadena de dos redirecciones y simplificarla solo con autorización.

## 10. SENCE y páginas históricas

La landing B2C vigente no debe recuperar contenido SENCE.

Todavía existen páginas históricas indexables de Excel con encabezados o texto como:

- Curso Excel SENCE;
- franquicia;
- empresa;
- curso básico presencial con fechas antiguas.

Esto puede:

- atraer intención orgánica de gratuidad;
- confundir la arquitectura B2C/B2B;
- aparecer en resultados o enlaces secundarios;
- competir con la URL principal.

No se recomienda borrarlas masivamente. Se debe construir un inventario URL por URL con:

- clics e impresiones recientes;
- consulta dominante;
- backlinks;
- canonical;
- estado HTTP;
- decisión: conservar, actualizar, redirigir o `noindex`.

## 11. Dispositivo

Para las consultas comerciales presenciales visibles en el sitio:

| Dispositivo | Clics | Impresiones | CTR | Posición |
|---|---:|---:|---:|---:|
| Móvil | 1.046 | 8.323 | 12,57% | 6,36 |
| Escritorio | 465 | 4.792 | 9,70% | 16,40 |

Para el cluster clases/profesor:

| Dispositivo | Clics | Impresiones | CTR | Posición |
|---|---:|---:|---:|---:|
| Móvil | 57 | 1.256 | 4,54% | 6,88 |
| Escritorio | 16 | 828 | 1,93% | 13,74 |

Estos datos son por consulta en todo el sitio, no por una sola landing. Aun así, refuerzan la exigencia mobile-first ya observada en Google Ads y PageSense.

## 12. Impacto en la arquitectura aprobada

### Se mantiene

1. Página orgánica actual:
   - indexable;
   - cambios operativos mínimos;
   - no experimentar agresivamente;
   - proteger su intención general presencial.

2. Landing A pagada:
   - Básico–Intermedio / `BP-001`;
   - `noindex,follow`.

3. Landing B pagada:
   - Básico desde cero / `BP-002`;
   - `noindex,follow`.

4. Landing C pagada:
   - clases presenciales con profesor / `BP-001`;
   - `noindex,follow`;
   - curso grupal, no particular ni domicilio.

### No se recomienda todavía

- hacer indexables las tres landings;
- crear más variantes;
- eliminar páginas históricas en masa;
- cambiar la página orgánica para perseguir “básico”;
- interpretar tráfico orgánico como matrícula sin GA4 y Zoho.

## 13. Google Analytics 4: sí aporta y no es redundante

### Search Console responde

> ¿Qué consulta mostró Google, qué URL apareció, cuántas impresiones y clics obtuvo, con qué CTR y posición?

### GA4 debe responder

> ¿Qué hizo la persona después de entrar, desde qué canal y campaña llegó, qué páginas recorrió y qué evento o conversión completó?

### PageSense responde

> ¿Dónde hizo clic, hasta dónde avanzó, dónde abandonó y qué campo generó fricción?

### Zoho responde

> ¿El submit llegó, fue contactable, cotizó y se matriculó?

Por tanto, el modelo completo es:

```text
Search Console / Google Ads
→ adquisición
→ GA4
→ comportamiento y atribución
→ PageSense
→ fricción UX
→ Zoho
→ resultado comercial
```

### Integración recomendada

1. Verificar primero la cobertura y calidad de GA4/GTM en Edge #27.
2. Confirmar la propiedad GA4 y el flujo web que cubren `capacita.cl`.
3. Vincular Search Console con GA4 si no está ya vinculado.
4. Habilitar después Google Analytics Data API read-only.
5. Exportar por landing, canal, campaña y dispositivo:
   - sesiones;
   - sesiones con interacción;
   - tasa de interacción;
   - eventos relevantes;
   - eventos clave;
   - navegación y abandonos.
6. Reconciliar con PageSense y Zoho.

### Restricción

GA4 solo será una fuente confiable si:

- la etiqueta está en todas las rutas;
- los dominios/subdominios no fragmentan la sesión;
- UTM y click IDs persisten;
- el submit exitoso se mide como éxito real;
- no existen eventos duplicados.

Por eso GA4 **sí aplica**, pero su API no debe configurarse como sustituto de la auditoría Edge #27.

## 14. Próximos pasos

1. Mantener los CSV y token fuera de GitHub.
2. Incorporar este análisis agregado a PR #35.
3. Actualizar issue #36 con autenticación y export completados.
4. En Edge #28:
   - auditar redirecciones;
   - inventariar URLs históricas;
   - validar canonical y sitemap.
5. En Edge #27:
   - auditar GA4/GTM;
   - confirmar eventos y atribución;
   - verificar formularios y Zoho.
6. Después configurar GA4 Data API read-only.
7. Cerrar la matriz contractual de las tres landings.
8. Implementar landings en PR separado de Capacita Edge.
9. Modificar Google Ads solo con autorización posterior.

## 15. Fuentes oficiales aplicables

- Search Console Search Analytics API:  
  `https://developers.google.com/webmaster-tools/v1/searchanalytics/query`
- Integración Search Console con Google Analytics:  
  `https://support.google.com/analytics/answer/10737381`
- Google Analytics Data API:  
  `https://developers.google.com/analytics/devguides/reporting/data/v1/basics`
