# Baseline PageSense para CRO y atribución V01

## Estado

Documento de trabajo basado en exports privados de Zoho PageSense del periodo aproximado 2026-04-15/17 a 2026-07-12.

Los CSV originales, capturas, grabaciones y datos sensibles permanecen fuera del repositorio. Este archivo conserva solo síntesis agregada y sanitizada.

## Objetivo

Incorporar PageSense como fuente complementaria para analizar CRO de la landing B2C de Excel presencial, formularios y comportamiento post-click.

PageSense no reemplaza:

- Google Ads / PowerShell para gasto, clics, términos, keywords y subasta;
- `Historial_Rendimiento_GoogleAds` para continuidad histórica;
- GTM/Google tag para atribución publicitaria;
- Zoho CRM para leads, contactabilidad, cotizaciones y matrículas reales.

## Fuentes revisadas

- Web Analytics: páginas, landing pages, exit pages, canales y source/medium.
- Form Analytics B2C `FR EXCEL12-PRE`.
- Form Analytics B2B `Formulario Empresa-Exel`.
- Goal B2C `enviar Pre`.
- Goal B2B `Enviar Empresa-Excel`.
- Click map/heatmap de la landing B2C `Landing-Excel12-PRE`.
- Click map/heatmap de la landing B2B `Landing-Excel-Empresa`.

## Calidad de los exports

La carga revisada contenía 15 CSV, pero el hash de contenido mostró solo cuatro archivos únicos. Las copias no constituyen evidencia independiente ni deben sumarse.

Para futuras cargas se debe conservar una sola copia por experimento, periodo y tipo de reporte.

## Hallazgo crítico

Los goals revisados no equivalen todavía a lead confirmado ni submit aceptado.

### B2C

Form Analytics reporta aproximadamente:

- 5.816 visitantes de la página con formulario;
- 124 iniciadores;
- 94 abandonos;
- tasa de conversión del formulario: 24% entre iniciadores;
- envíos implícitos aproximados: 30.

El goal `enviar Pre` reporta:

- 5.621 visitantes elegibles;
- 777 conversiones;
- tasa de goal: 13,82%.

La diferencia es demasiado grande para interpretar `enviar Pre` como envío exitoso del formulario.

El click map agrega una señal consistente:

- botón submit B2C: 289 clics en móvil y 81 en escritorio;
- esos clics son muy superiores a los aproximadamente 30 envíos implícitos;
- un clic en submit no puede tratarse como formulario aceptado por Zoho.

### B2B

Form Analytics reporta aproximadamente:

- 271 visitantes;
- 24 iniciadores;
- 17 abandonos;
- envíos implícitos aproximados: 7.

El goal `Enviar Empresa-Excel` reporta 23 conversiones sobre 207 visitantes elegibles.

También existe discrepancia material entre goal e intento/envío real.

## Señales de formulario B2C

- tasa de inicio sobre visitantes aproximada: 2,1%;
- abandono entre iniciadores aproximado: 75,8%;
- envío implícito sobre visitantes aproximado: 0,5%;
- el campo Email concentra la mayoría de los abandonos registrados;
- las métricas de campo pueden contar eventos y no necesariamente personas únicas.

## Click map de la landing B2C

PageSense reporta:

| Dispositivo | Visitantes de la vista | Comprometidos | Visitas | Clics/visita |
|---|---:|---:|---:|---:|
| Escritorio | 343 | 48,40% | 639 | 2,7 |
| Móvil | 5.286 | 13,39% | 6.692 | 0,6 |
| Tableta | 14 | 42,86% | 19 | 4,1 |

Interpretación provisional:

- el formulario es uno de los principales focos de interacción;
- existe una brecha fuerte entre clics de submit y envíos implícitos;
- el comportamiento móvil agregado es mucho menos comprometido que escritorio;
- este click map mezcla fuentes de tráfico y no permite atribuir la diferencia a Google Ads ni al diseño móvil por sí solo;
- se debe segmentar `google/cpc` antes de concluir un problema exclusivo de UX móvil.

## Señales de adquisición

PageSense Web Analytics muestra que `google/cpc` tuvo, en el periodo revisado:

- 751 sesiones;
- menor tasa de abandono que Meta paid social;
- mayor duración promedio de sesión;
- 161 cumplimientos de `Todos los objetivos`.

Los cumplimientos de objetivos son proxies de interacción hasta corregir el mapeo de goals. No equivalen a leads ni matrículas.

## Uso recomendado de PageSense

1. Auditar goals: tipo, selector/evento, audiencia y condición real de éxito.
2. Segmentar Form Analytics: `google/cpc` + landing B2C + mobile/desktop.
3. Separar click map/heatmap por dispositivo y paid search.
4. Revisar session recordings privadas con PII enmascarada.
5. Medir funnel mínimo: entrada landing → CTA → inicio formulario → submit confirmado → lead recibido.
6. Ejecutar A/B o Split URL solo después de validar goals y atribución.

## Diseño experimental recomendado

Producto constante: Curso de Excel Básico e Intermedio presencial, desde cero en Excel hasta nivel intermedio.

- Control: landing B2C actual corregida.
- Variante: mismo curso, oferta, fecha, precio, formulario y CTA; hero con énfasis `Excel básico desde cero`, aclarando que avanza hasta intermedio.
- Buyer persona primario e hipótesis única según brief GTM vigente.
- B2B excluido de ambas páginas.

## Evidencia todavía requerida

- definición/configuración de los goals `enviar Pre`, `Enviar Empresa-Excel` e `inicio`;
- Form Analytics segmentado por `google/cpc` y dispositivo;
- grabaciones de sesión filtradas y con privacidad validada;
- confirmación de evento de submit exitoso;
- reconciliación agregada con Zoho CRM.

## Seguridad

- no usar email, teléfono u otro dato personal como identificador en documentación pública;
- mantener grabaciones y exports privados;
- enmascarar campos de formulario y datos sensibles;
- GitHub conserva solo síntesis agregada, decisiones y metodología.

## Estado de decisión

PageSense queda aceptado como fuente complementaria de CRO. No autoriza por sí solo cambios productivos.

El siguiente gate es corregir/validar goals y luego ejecutar una prueba controlada de una sola variante B2C con énfasis básico.
