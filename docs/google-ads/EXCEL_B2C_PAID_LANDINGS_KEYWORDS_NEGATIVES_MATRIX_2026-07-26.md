# Matriz B2C — landings pagadas Excel, keywords y negativas — 2026-07-26

## Estado

- Estado: `V01_DOCUMENTAL`.
- Semáforo: amarillo.
- Repo: `misaeln-pc1/marketing-performance-capacita`.
- Rama: `docs/marketing-excel-b2c-two-page-plan-v01`.
- PR relacionado: #35.
- Dueño táctico: Marketing Performance / Campañas & Growth Capacita.
- Alcance: Google Search B2C para Excel presencial.
- Fuera de alcance: cambios productivos en Google Ads, presupuestos, pujas, anuncios, landings Edge, GTM, Zoho, Search Console, PageSense, credenciales y datos personales.

Este documento registra la evidencia y la arquitectura de intención para crear tres landings pagadas `noindex,follow` sin reemplazar la página orgánica posicionada.

## Decisión vigente

La página orgánica actual se conserva como activo SEO:

```text
https://capacita.cl/curso-de-excel-presencial-en-santiago/
```

Las tres nuevas landings son exclusivas para campañas, medición y experimentación:

| Código | Landing | Estado SEO inicial | Intención primaria | Buyer persona |
|---|---|---|---|---|
| A | Básico–Intermedio presencial | `noindex,follow` | curso presencial completo/ruta laboral | `BP-001` |
| B | Excel desde cero | `noindex,follow` | comenzar con baja seguridad o base inicial | `BP-002` |
| C | Clases presenciales con profesor | `noindex,follow` | clases/profesor en vivo como alternativa estructurada | `BP-001` |

Todas venden el mismo producto real: curso Excel Básico–Intermedio presencial, grupal, en sede. La landing C no puede prometer clases particulares, atención uno a uno ni clases a domicilio.

## Fuentes revisadas

### Archivos privados / SharePoint-OneDrive

Carpeta privada:

```text
CAPACITA/Proyectos/0-Origen/google
```

Export histórico Google Ads API read-only:

```text
CAPACITA/Proyectos/0-Origen/google/exports/google-ads-current-campaign-history-20260726-030015
```

Archivos relevantes:

- `02_campaign_config.csv`.
- `03_campaign_daily.csv`.
- `04_device_network_daily.csv`.
- `05_search_terms_daily.csv`.
- `06_keywords_quality_daily.csv`.
- `07_landing_pages_daily.csv`.
- `08_conversion_actions_daily.csv`.
- `09_ads_daily.csv`.
- `10_window_summary.csv`.
- `manifest.json`.
- `manifest_missing_reports.json`.

Keyword Planner read-only para las tres familias:

```text
CAPACITA/Proyectos/0-Origen/google/keyword-planner-excel-landings-20260726
```

Archivos:

- `keyword_ideas_excel_basico_intermedio.tsv`.
- `keyword_ideas_excel_desde_cero.tsv`.
- `keyword_ideas_clases_excel_profesor.tsv`.
- `seeds_excel_basico_intermedio.csv`.
- `seeds_excel_desde_cero.csv`.
- `seeds_clases_excel_profesor.csv`.

Listas negativas exportadas desde Google Ads:

- `Lista Negativas - Curso Presencial - Excel` — 104 términos.
- `Lista Negativas - EMPRESAS Curso Presencial - Excel` — 145 términos.

Los archivos privados, CSV completos, TSV, URLs completas, IDs, JSON OAuth, YAML y outputs crudos no se versionan en GitHub.

## Resultado general Google Ads

Export 730 días, cuenta en CLP:

| Ventana | Clics | Costo | CPC medio | Conversiones | CVR | CPA |
|---:|---:|---:|---:|---:|---:|---:|
| 7 días | 47 | 44.885 | 955 | 1 | 2,13% | 44.885 |
| 30 días | 215 | 215.294 | 1.001 | 12 | 5,58% | 17.941 |
| 730 días | 12.382 | 8.549.828 | 691 | 388,75 | 3,14% | 21.993 |

Lectura: el deterioro reciente está más asociado a baja conversión post-click que a CPC aislado. La medición sigue requiriendo reconciliación con Zoho hasta lead contactable, cotización y matrícula.

## Campañas Search activas detectadas

| Campaña | Estado | Estrategia | Presupuesto diario | Lectura |
|---|---|---|---:|---|
| `EXCEL-PRE-STGO` | ENABLED | `TARGET_SPEND` | 25.000 | B2C principal |
| `EXCEL-EMPRESA` | ENABLED | `TARGET_SPEND` | 10.000 | B2B, fuera de esta fase |
| `EXCEL-PRE-STGO Test_ZLanding_vs_WordPressLaning_2026.02` | ENABLED | `TARGET_SPEND` | 25.000 | test histórico |

El aviso de Google Ads sobre objetivos desde 2026-08-17 no gatilla acción inmediata para estas campañas porque no aparecen con `TARGET_CPA` ni `TARGET_ROAS` en el export revisado. No aceptar recomendaciones automáticas sin revisión.

## Lectura agregada por intención B2C

Clasificación preliminar sobre `EXCEL-PRE-STGO` y test B2C, usando `05_search_terms_daily.csv`:

| Categoría | Clics | Costo aprox. | Conversiones | CPC aprox. | CVR aprox. | CPA aprox. | Decisión |
|---|---:|---:|---:|---:|---:|---:|---|
| A — Básico/intermedio/presencial | 4.162 | 2.635.226 | 179,01 | 633 | 4,30% | 14.721 | núcleo B2C |
| B — Desde cero/básico | 780 | 517.656 | 13,84 | 664 | 1,77% | 37.397 | crear landing con control |
| C — Clases/profesor compatible | 182 | 115.860 | 8,5 | 637 | 4,67% | 13.631 | experimento viable |
| Riesgo particular/domicilio | 24 | 36.644 | 2 | 1.527 | 8,33% | 18.322 | no prometer / bloquear fuerte |
| Negativas globales | 940 | 608.979 | 14,55 | 648 | 1,55% | 41.867 | bloquear / limpiar |
| B2B backlog | 19 | 20.934 | 0 | 1.102 | 0% | — | diferir a campaña B2B |
| Revisar manual | 2.259 | 1.419.608 | 38 | 628 | 1,68% | 37.358 | clasificar en iteración posterior |

## Landing A — Básico–Intermedio presencial

### Rol

Landing principal de producto B2C. Captura intención de curso presencial completo, no principiante inseguro ni clases particulares.

### URL propuesta

```text
/lp/curso-excel-basico-intermedio-presencial-santiago/
```

### Keyword eje

```text
curso excel básico intermedio presencial santiago
```

### H1

```text
Curso Excel Básico–Intermedio presencial en Santiago
```

### H2

```text
Aprende Excel desde lo esencial hasta herramientas intermedias, con profesor en vivo y práctica guiada.
```

### Keywords prioritarias

| Prioridad | Keyword / término | Evidencia | Acción |
|---:|---|---|---|
| 1 | `curso de excel presencial santiago` | bajo CPA relativo y alta coherencia local | conservar / exacta o frase |
| 2 | `curso excel presencial santiago` | intención local clara | conservar / exacta o frase |
| 3 | `curso excel presencial` | buena base de campaña, QS alto histórico | conservar |
| 4 | `cursos de excel presencial` | buen CPA histórico | conservar |
| 5 | `curso de excel presencial` | alto volumen relativo | conservar con control |
| 6 | `cursos excel presencial` | compatible | probar |
| 7 | `excel presencial` | útil pero amplio | probar acotado |
| 8 | `curso excel básico e intermedio` | keyword estratégica, pero requiere aislamiento | mantener grupo separado |
| 9 | `curso de excel basico intermedio` | intención directa | probar |
| 10 | `curso presencial de excel` | compatible | probar |

### Frases consistentes

- Curso presencial, grupal y con profesor en vivo.
- Ruta completa para avanzar desde fundamentos hasta herramientas intermedias.
- Ideal si ya usas Excel y necesitas trabajar con más orden, seguridad y autonomía.
- Práctica guiada en sala, ejercicios aplicados y acompañamiento del relator.
- No es una clase suelta: es un curso estructurado.

### Negativas cruzadas para A

```text
desde cero
principiante
principiantes
clases
profesor
particular
clases particulares
profesor particular
a domicilio
en casa
uno a uno
1 a 1
online
en línea
virtual
gratis
gratuito
sence
```

## Landing B — Excel desde cero

### Rol

Landing para personas con baja seguridad o base inicial. No debe competir con la intención de ruta completa ni con clases/profesor.

### URL propuesta

```text
/lp/curso-excel-desde-cero-presencial-santiago/
```

### Keyword eje

```text
curso excel desde cero presencial santiago
```

### H1

```text
Curso Excel desde cero presencial en Santiago
```

### H2

```text
Aprende paso a paso, aunque hoy no tengas conocimientos previos de Excel.
```

### Keywords prioritarias

| Prioridad | Keyword / término | Evidencia | Acción |
|---:|---|---|---|
| 1 | `curso excel desde cero` | señal directa Keyword Planner/Search Terms | probar |
| 2 | `curso de excel desde cero` | señal directa | probar |
| 3 | `aprender excel desde cero` | compatible con inseguridad inicial | probar con frase |
| 4 | `curso excel para principiantes` | intención inicial | probar |
| 5 | `curso de excel para principiantes` | intención inicial | probar |
| 6 | `curso excel básico presencial` | actual, pero debe ir separado | mover a B o A según término |
| 7 | `curso de excel basico` | volumen alto, CPA débil | probar acotado |
| 8 | `curso basico de excel` | volumen alto, CPA débil | probar acotado |
| 9 | `excel básico presencial` | compatible | probar |
| 10 | `excel para principiantes` | compatible | observar |

### Frases consistentes

- Empieza desde cero, sin asumir conocimientos previos.
- Aprende Excel paso a paso, con ejercicios guiados.
- Ideal si te cuesta usar planillas o no sabes por dónde comenzar.
- Curso presencial con profesor en vivo y apoyo durante la práctica.
- Comienza desde la base y avanza hacia herramientas intermedias.

### Negativas cruzadas para B

```text
intermedio avanzado
avanzado
macros
macro
vba
power bi
power query
clases particulares
profesor particular
a domicilio
en casa
uno a uno
1 a 1
online
en línea
virtual
gratis
gratuito
sence
```

No usar `intermedio` como negativa amplia en B, porque el producto real avanza hacia intermedio. Bloquear sólo intenciones avanzadas o técnicas.

## Landing C — Clases presenciales con profesor

### Rol

Landing para intención `clases/profesor`, pero con transparencia: curso grupal presencial estructurado, no servicio particular.

### URL propuesta

```text
/lp/clases-excel-presenciales-profesor-santiago/
```

### Keyword eje

```text
clases de excel presenciales con profesor en santiago
```

### H1

```text
Clases de Excel presenciales con profesor en Santiago
```

### H2

```text
Una alternativa estructurada a clases sueltas: curso grupal, práctico y con profesor en vivo.
```

### Texto obligatorio de transparencia

```text
Este es un curso grupal presencial con profesor en vivo. No corresponde a clases particulares, atención uno a uno ni clases a domicilio.
```

### Keywords prioritarias

| Prioridad | Keyword / término | Evidencia | Acción |
|---:|---|---|---|
| 1 | `clases de excel presencial` | 94 clics, 3 conv., CPA aprox. 19.096 | conservar/probar |
| 2 | `clases de excel presenciales` | señal Keyword Planner/Search Terms | probar |
| 3 | `clases presenciales de excel` | CPA bajo relativo, bajo volumen | probar |
| 4 | `clases excel presencial` | compatible | probar |
| 5 | `clases de excel basico` | compatible | probar acotado |
| 6 | `clases de excel intermedio` | compatible | probar acotado |
| 7 | `profesor de excel` | compatible, revisar intención | probar limitado |
| 8 | `curso de excel con profesor` | compatible | probar |
| 9 | `aprender excel con profesor` | compatible | observar |
| 10 | `profesor excel santiago` | compatible | observar |

### Frases consistentes

- Clases presenciales de Excel con profesor en vivo.
- Formato grupal, práctico y estructurado.
- No son clases particulares ni a domicilio.
- Aprende con un programa definido, fechas claras y práctica guiada.
- Ideal si buscas acompañamiento directo, pero con una ruta ordenada.

### Negativas cruzadas para C

```text
a domicilio
en casa
profesor a domicilio
clases a domicilio
particular a domicilio
uno a uno
1 a 1
personalizado exclusivo
online
profesor online
gratis
gratuito
sence
pdf
descargar
tutorial
youtube
```

### Decisión sobre `particular`

Los términos `profesor excel particular`, `profesor particular excel`, `clases particulares excel` y similares muestran riesgo de CPC alto y baja calidad. No deben usarse como positivos amplios. Recomendación actual: bloquear `a domicilio`, `uno a uno`, `profesor a domicilio` y `particular a domicilio` siempre. Bloquear también `particular`, `clases particulares` y `profesor particular` si la prueba C no puede absorber consultas ambiguas sin dañar CPA.

## Negativas globales B2C

Lista global recomendada para campañas B2C Excel presencial:

```text
gratis
gratuito
curso gratis
curso gratuito
sence
franquicia tributaria
beneficio tributario
sena
colsubsidio
online
on line
en línea
virtual
remoto
e-learning
elearning
pdf
descargar
download
manual
plantilla
tutorial
youtube
tio tech
el tio tech
udemy
teleduc
ninja excel
macros
macro
vba
power bi
power query
programar macros
formulas de
ejercicios de
que es
definicion
universidad
unam
udd
escolar
examen
vacante
sueldo
```

## Lista negativa B2C actual

Archivo revisado:

```text
Lista Negativas - Curso Presencial - Excel
```

Contiene 104 términos. Es una buena base de exclusión B2C. Contiene exclusiones coherentes como:

- `gratis`.
- `online` / `virtual` / `en linea`.
- `pdf` / `tutorial` / `youtube`.
- `sence` / `convenio sence` / `curso excel online sence`.
- `power bi`.
- `macros excel`.
- `vba`.
- `curso de excel para empresas`.
- `capacitacion excel para empresas`.
- `excel empresas`.
- `a domicilio`.

Riesgo: no debe aplicarse sin revisión a todas las landings si alguna intenta capturar intención cercana a `paso a paso`, `básico` o `clases`, porque podría bloquear aprendizaje útil. Debe dividirse en globales y cruzadas.

## Lista negativa EMPRESAS actual

Archivo revisado:

```text
Lista Negativas - EMPRESAS Curso Presencial - Excel
```

Contiene 145 términos. La inclusión de términos como `curso excel`, `capacitacion excel`, `excel presencial`, `curso excel santiago`, `curso excel basico presencial` fue una decisión defensiva de Misael por experiencia previa de CPC alto y leads malos, no se registra como error.

Lectura actual:

- Mantener esta decisión como protección temporal B2B.
- No reutilizar esta lista para B2C.
- No depurar B2B dentro de esta fase.
- Crear backlog posterior para landings B2B con intención estricta y keywords propias.

## Backlog B2B separado

B2B interesa comercialmente, pero no debe mezclarse con esta fase B2C. Pendiente futuro:

- Revisar campañas `EXCEL-EMPRESA`.
- Separar intención `curso para empresas`, `capacitación para equipos`, `OTEC`, `SENCE/franquicia`, `Excel para trabajadores`, `Excel in company`.
- Crear landing(s) B2B separadas.
- Definir keywords y negativas propias.
- Medir por lead empresa, cotización y venta corporativa, no por lead individual B2C.

## Arquitectura de campaña sugerida, no ejecutada

Campaña B2C futura:

```text
EXCEL-B2C-PRESENCIAL-STGO
```

Grupos:

```text
AG_EXCEL_BASICO_INTERMEDIO
AG_EXCEL_DESDE_CERO
AG_CLASES_EXCEL_PROFESOR
```

Destinos:

| Grupo | Landing |
|---|---|
| `AG_EXCEL_BASICO_INTERMEDIO` | `/lp/curso-excel-basico-intermedio-presencial-santiago/` |
| `AG_EXCEL_DESDE_CERO` | `/lp/curso-excel-desde-cero-presencial-santiago/` |
| `AG_CLASES_EXCEL_PROFESOR` | `/lp/clases-excel-presenciales-profesor-santiago/` |

## Reglas de implementación

- No activar cambios en Google Ads sin autorización explícita.
- No tocar presupuestos ni pujas en este documento.
- No mezclar B2C y B2B.
- No mandar tráfico pagado a la URL antigua `presencial-elearning`.
- No reemplazar la página orgánica actual.
- Cada landing debe tener URL, `landing_code`, UTM, variante, intención, buyer persona como hipótesis, PageSense/GA4/GTM y reconciliación Zoho.
- Conversiones de decisión: submit confirmado, lead contactable, cotización y matrícula.

## Siguiente paso recomendado

1. Crear las tres landings `noindex,follow` en `capacita-edge`.
2. Registrar `landing_code` conceptual para cada una.
3. Preparar PR técnico reversible con previews.
4. Mantener la página orgánica actual como control.
5. Sólo después preparar propuesta de reestructura Ads con keywords, negativas y migración controlada.

## Estado de cierre

Este documento deja la matriz táctica registrada para no reconstruir desde chat. No autoriza producción ni cambios en Google Ads.
