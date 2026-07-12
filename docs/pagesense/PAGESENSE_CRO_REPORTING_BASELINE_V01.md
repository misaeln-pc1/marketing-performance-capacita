# Baseline PageSense para CRO y atribución V01

## Estado

Documento de trabajo basado en exports privados de Zoho PageSense del periodo aproximado 2026-04-15/17 a 2026-07-12.

Los CSV originales permanecen fuera del repo. Este archivo conserva sólo síntesis agregada y sanitizada.

## Objetivo

Incorporar PageSense como fuente complementaria para analizar la landing B2C de Excel presencial, el formulario y el comportamiento post-click.

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
- Heatmap de una página de diagnóstico de Excel, no aplicable como evidencia principal de la landing B2C.

## Calidad de los exports 2026-07-12

La carga más reciente contenía 15 CSV, pero el hash de contenido mostró sólo cuatro archivos únicos:

- dos copias idénticas de Form Analytics B2C;
- seis copias idénticas del click map B2C;
- seis copias idénticas del click map B2B;
- un goal B2B.

Las copias no constituyen evidencia independiente ni deben sumarse. Para futuras cargas se debe conservar una sola copia por experimento, periodo y tipo de reporte.

## Hallazgo crítico: goal no equivale todavía a lead confirmado

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

La diferencia es demasiado grande para interpretar `enviar Pre` como envío exitoso del formulario. Debe auditarse si el goal mide clic en botón, scroll/ancla, interacción o evento que también se dispara ante validación fallida.

El click map agrega una señal consistente con esa hipótesis:

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

También existe discrepancia material entre goal e intento/envío real. El reporte de goal distribuye 12 conversiones en móvil y 11 en escritorio, pero no demuestra aceptación del formulario. Las filas de URL con fragmentos no son mutuamente excluyentes y no deben sumarse como conversiones nuevas.

## Señales de formulario B2C

- tasa de inicio sobre visitantes aproximada: 2,1%;
- abandono entre iniciadores aproximado: 75,8%;
- envío implícito sobre visitantes aproximado: 0,5%;
- el campo Email concentra la mayoría de los abandonos registrados;
- Email registra 115 enfoques, 101 interacciones, 104 abandonos y 24 casos en blanco;
- el formulario requiere validar nombres técnicos, campos realmente detectados y definición exacta de conversión antes de optimizar.

Las métricas de campo pueden contar eventos y no necesariamente personas únicas; deben contrastarse con grabaciones privadas y con el submit confirmado.

## Click map de la landing B2C

Distribución general del experimento:

- móvil: 6.692 visitas/dispositivos reportados;
- escritorio: 639;
- tableta: 19.

PageSense reporta:

| Dispositivo | Visitantes de la vista | Comprometidos | Visitas | Clics/visita |
|---|---:|---:|---:|---:|
| Escritorio | 343 | 48,40% | 639 | 2,7 |
| Móvil | 5.286 | 13,39% | 6.692 | 0,6 |
| Tableta | 14 | 42,86% | 19 | 4,1 |

Elementos con mayor interacción en móvil:

- ancla `#inicio`: 393 clics;
- botón submit: 289;
- textarea: 275;
- tres inputs principales: 264, 260 y 217;
- CTA naranja: 57;
- CTA azul: 53.

En escritorio, formulario y submit también concentran interacción: textarea 92, primer input 84 y botón submit 81.

Interpretación provisional:

- el formulario es uno de los principales focos de interacción;
- existe una brecha fuerte entre clics de submit y envíos implícitos;
- el comportamiento móvil agregado es mucho menos comprometido que escritorio;
- este click map mezcla fuentes de tráfico y no permite atribuir la diferencia a Google Ads ni al diseño móvil por sí solo;
- dado que Meta aporta gran volumen móvil de baja calidad en el Web Analytics revisado, se debe segmentar `google/cpc` antes de concluir un problema exclusivo de UX móvil.

## Click map de la landing B2B

PageSense reporta:

| Dispositivo | Visitantes de la vista | Comprometidos | Visitas | Clics/visita |
|---|---:|---:|---:|---:|
| Escritorio | 115 | 33,91% | 164 | 1,2 |
| Móvil | 117 | 10,26% | 143 | 0,4 |

Los campos del formulario y el botón de envío concentran la mayor parte de los clics útiles. El volumen es bajo y no habilita una conclusión estructural; sirve para confirmar la necesidad de separar goal de submit confirmado.

## Señales de adquisición

PageSense Web Analytics muestra que `google/cpc` tuvo, en el periodo revisado:

- 751 sesiones;
- menor tasa de abandono que Meta paid social;
- mayor duración promedio de sesión;
- 161 cumplimientos de `Todos los objetivos`.

Los cumplimientos de objetivos son proxies de interacción hasta corregir el mapeo de goals. No equivalen a leads ni matrículas.

## Señales de arquitectura y contaminación

Los exports incluyen:

- URLs con fragmentos `#registro` tratadas como páginas separadas;
- páginas de prueba, archivos locales y dominios sandbox;
- tráfico de WordPress admin y previews.

Para decisiones de campaña se debe segmentar por:

- hostname de producción;
- landing B2C vigente;
- source/medium `google/cpc`;
- campaña/UTM cuando estén disponibles;
- Chile;
- dispositivo;
- visitante nuevo/retornante;
- excluir admin, local files, previews, sandbox y páginas de diagnóstico no relacionadas.

## Uso recomendado de PageSense

1. Goal audit: documentar tipo, selector/evento, audiencia y condición real de éxito.
2. Form Analytics segmentado: `google/cpc` + landing B2C + mobile/desktop.
3. Click map/heatmap de la landing B2C, separado por dispositivo y paid search.
4. Session recordings: revisar muestras de mobile/desktop, iniciadores que abandonan y visitantes que completan el goal.
5. Funnel mínimo:
   - entrada landing;
   - interacción CTA;
   - inicio formulario;
   - submit confirmado;
   - confirmación/lead recibido.
6. Split URL o A/B test sólo después de validar goals y atribución.

## Diseño experimental propuesto

Producto constante: Curso de Excel Básico e Intermedio presencial, desde cero en Excel hasta nivel intermedio.

- Control: landing B2C actual corregida.
- Variante: mismo curso, oferta, fecha, precio, formulario y CTA; hero con énfasis `Excel básico desde cero`, aclarando que avanza hasta intermedio.
- Buyer persona primario e hipótesis única según brief GTM vigente.
- B2B excluido de ambas páginas.
- No crear variante intermedia ni de clases particulares en esta fase.

## Evidencia todavía requerida

- definición/configuración de los goals `enviar Pre`, `Enviar Empresa-Excel` e `inicio`;
- Form Analytics segmentado por `google/cpc` y dispositivo;
- grabaciones de sesión filtradas y con privacidad validada;
- confirmación de evento de submit exitoso;
- reconciliación agregada con Zoho CRM.

El click map de la landing B2C principal ya está disponible; no debe volver a declararse pendiente como reporte general. Lo pendiente es su segmentación por fuente/campaña cuando PageSense lo permita.

## Seguridad

- no usar email, teléfono u otro dato personal como identificador en documentación pública;
- mantener grabaciones y exports privados;
- enmascarar campos de formulario y datos sensibles;
- GitHub conserva sólo síntesis agregada, decisiones y metodología.

## Estado de decisión

PageSense queda aceptado como fuente complementaria de CRO. No autoriza por sí solo cambios productivos. El siguiente gate es corregir/validar goals y luego ejecutar una prueba controlada de una sola variante B2C con énfasis básico.
