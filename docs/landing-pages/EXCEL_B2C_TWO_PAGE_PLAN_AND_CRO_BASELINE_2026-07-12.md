# Plan de dos páginas B2C Excel y baseline CRO — 2026-07-12

## Estado

Decisión documental previa a implementación. No autoriza por sí sola cambios en Google Ads, Cloudflare, Zoho Forms, PageSense, GTM, CRM o producción.

## Objetivo comercial

Reducir desperdicio de pauta y aumentar matrículas del curso presencial de Excel en Santiago mediante una arquitectura clara de dos intenciones de compra, manteniendo un único producto real:

> Curso de Excel Básico e Intermedio presencial, que parte sin conocimientos previos de Excel y avanza hasta nivel intermedio.

Requisito mínimo: manejo básico de computador e Internet. No se requieren conocimientos previos de Excel.

## Decisión vigente

Se adoptan dos páginas B2C indexables, con contenido y arquitectura propios:

1. **Página actual mejorada:** intención `Excel presencial completo / Básico e Intermedio`.
2. **Página nueva:** intención `Excel Básico presencial / desde cero / principiantes`.

No se crea en esta fase:

- página de Excel Intermedio independiente;
- página de clases particulares;
- tercera o cuarta landing B2C;
- página pagada `noindex` como solución final.

## Regla SEO

No existe una regla oficial de Google que exija 70%, 75% u otro porcentaje de diferencia textual. La diferenciación se evaluará por intención, utilidad y contenido propio, no por un contador artificial de palabras.

Las dos páginas pueden compartir legítimamente:

- imágenes;
- producto;
- fechas;
- precio;
- horario;
- duración;
- sede;
- profesor;
- temario;
- formulario;
- certificación;
- condiciones comerciales.

Deben diferenciarse materialmente en:

- problema de compra;
- promesa principal;
- H1 y jerarquía H2;
- introducción;
- objeciones;
- beneficios priorizados;
- preguntas frecuentes;
- ejemplos y explicaciones;
- testimonios o prueba social seleccionada;
- CTA y microcopy contextual;
- enlaces internos y keywords objetivo.

No crear páginas casi idénticas cambiando sólo title, H1 y sinónimos. Ese patrón aumenta riesgo de duplicidad, canonicalización no deseada y páginas puerta.

Fuentes oficiales:

- Google Search Central — contenido útil: https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- Google Search Central — consolidación de URLs duplicadas: https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls
- Google Search Central — políticas de spam / doorway abuse: https://developers.google.com/search/docs/essentials/spam-policies

## Arquitectura SEO propuesta

### Página A — actual mejorada

**URL:** `/curso-de-excel-presencial-en-santiago/`

**Intención principal:** curso presencial completo de Excel, Básico e Intermedio, Santiago Centro.

**Keywords objetivo:**

- curso Excel presencial Santiago;
- curso Excel Básico e Intermedio;
- curso completo Excel presencial;
- Excel presencial Santiago Centro;
- curso de Excel presencial.

**Promesa:** una ruta presencial completa desde fundamentos hasta nivel intermedio.

**Contenido exclusivo recomendado:**

- mapa de progresión Básico → Intermedio;
- qué competencias se adquieren en cada etapa;
- por qué ambos niveles se integran;
- aplicaciones laborales y productivas al finalizar;
- comparación frente a estudiar cursos separados;
- preguntas sobre ritmo, duración y exigencia;
- CTA orientado a recibir programa, fechas y matrícula.

### Página B — nueva

**URL propuesta:** `/curso-excel-basico-presencial-santiago/`

**Intención principal:** comenzar Excel desde cero, en formato presencial y con acompañamiento.

**Keywords objetivo:**

- curso Excel básico presencial;
- Excel desde cero presencial;
- aprender Excel desde cero;
- curso Excel para principiantes;
- clases de Excel básico presencial.

**Promesa:** comenzar sin conocimientos previos de Excel, con aprendizaje guiado paso a paso, avanzando luego hasta contenidos intermedios.

**Transparencia obligatoria:** no presentar un curso básico distinto. Debe indicarse que es el mismo curso Básico e Intermedio, contextualizado para quien busca empezar desde cero.

**Contenido exclusivo recomendado:**

- qué significa realmente “desde cero”;
- requisitos mínimos de alfabetización digital;
- primeras habilidades que se aprenderán;
- temores y errores frecuentes del principiante;
- ritmo, práctica guiada y acompañamiento;
- computador individual;
- sección “este curso es para ti si…”;
- FAQ de personas sin experiencia;
- CTA orientado a comenzar y recibir apoyo.

### Controles técnicos comunes

Ambas páginas deben tener:

- canonical autorreferente;
- indexación permitida;
- title y meta description propios;
- H1 único;
- inclusión en sitemap;
- breadcrumb coherente;
- enlaces internos naturales entre ambas;
- `landing_code` distinto;
- información comercial consistente;
- structured data coherente con el mismo curso real.

Antes de publicar, se debe inventariar y resolver la URL histórica de Excel Básico. Debe reutilizarse o redirigirse con 301 hacia la nueva página; no debe quedar una tercera página básica compitiendo.

## Arquitectura Google Ads propuesta

Mantener inicialmente una sola campaña B2C y separar intención en dos grupos de anuncios.

### Grupo A — presencial completo / Básico e Intermedio

**Destino:** página A.

Keywords candidatas:

- `"curso excel presencial"`;
- `[curso excel presencial]`;
- `"curso excel presencial santiago"`;
- `"curso excel básico e intermedio"`;
- `[curso excel básico e intermedio]`;
- `"curso completo excel presencial"`.

### Grupo B — Básico / desde cero

**Destino:** página B.

Keywords candidatas:

- `"curso excel básico presencial"`;
- `[curso excel básico presencial]`;
- `"excel desde cero presencial"`;
- `"curso excel desde cero"`;
- `"excel para principiantes presencial"`.

### Negativas

Las negativas generales pueden compartirse cuando son irrelevantes para ambos grupos: gratis, online cuando no corresponda, tutoriales, archivos, descargas no comerciales, empleo y otras búsquedas no objetivo.

Las negativas cruzadas deben usarse con prudencia para orientar intención:

- Grupo A: excluir consultas puramente `desde cero` o `principiantes` sólo después de validar que el Grupo B ya las cubre.
- Grupo B: excluir `intermedio`, `Básico e Intermedio` y búsquedas de ruta completa cuando desvíen la intención.

No ejecutar negativas cruzadas masivas sin revisar términos reales y concordancias. Una negativa demasiado amplia puede bloquear demanda válida.

## Hallazgos PageSense y CRO

### Formulario B2C

Periodo aproximado revisado:

- 5.816 visitantes;
- 124 iniciadores;
- 94 abandonos;
- aproximadamente 30 envíos implícitos;
- inicio sobre visitantes: ~2,1%;
- abandono entre iniciadores: ~75,8%;
- envío implícito sobre visitantes: ~0,5%.

### Brecha clic → éxito

El click map mostró aproximadamente:

- 289 clics en submit móvil;
- 81 clics en submit escritorio;
- cerca de 370 clics totales en el botón;
- frente a aproximadamente 30 envíos efectivos implícitos.

Conclusión:

> `clic en enviar` no equivale a `formulario aceptado`.

Los goals PageSense revisados (`enviar Pre`, `inicio`, `Enviar Empresa-Excel`) son de tipo pulsación en elementos y no deben usarse como leads, matrículas ni conversiones primarias.

### Campo Email

El campo Email concentra la principal señal visible de fricción. Esto no prueba causalidad única, porque PageSense puede contar eventos y no personas únicas. Debe validarse con grabaciones, mensajes de error, formato y prueba controlada.

### Móvil

El tráfico móvil agregado tiene menor compromiso que escritorio, pero mezcla fuentes. Meta aportó gran volumen móvil de baja calidad. No atribuir el problema exclusivamente al diseño sin segmentar `google/cpc`.

Aun así, la implementación debe ser mobile-first porque móvil concentra gran parte de clics y conversiones registradas.

### Regalo / guía gratuita

Decisión comercial:

- retirar la guía gratuita como promesa principal del hero pagado;
- el visitante de Google Ads debe recibir una propuesta clara de matrícula/información comercial;
- mantener la guía, si se conserva, como bono posterior o como activo de captación en una campaña/landing separada, no pagada por intención de matrícula;
- la descarga de temario se clasifica como conversión secundaria, no como lead comercial equivalente al formulario principal.

### CTA principal

Propuesta:

> Recibir programa, próximas fechas y opciones de matrícula.

CTA secundario:

> Hablar por WhatsApp.

Mantener separados:

1. clic CTA;
2. inicio de formulario;
3. intento de submit;
4. submit confirmado;
5. lead recibido;
6. lead contactable;
7. cotización;
8. matrícula.

## Hipótesis Cloudflare Turnstile

### Resultado sobre la landing B2C vigente

La landing B2C actual `landing-excel12-presencial.html` envía directamente a Zoho Forms y no contiene widget Turnstile ni campo `cf-turnstile-response`.

Conclusión:

> Turnstile no puede explicar el abandono o bloqueo del formulario B2C vigente, porque ese formulario no lo utiliza.

La experiencia relatada en modo incógnito pudo corresponder a otra landing que sí usa Turnstile, a un token vencido/duplicado o a una regla general de Cloudflare; requiere identificar la URL exacta.

### Dónde sí existe Turnstile

Landings B2B y nuevas landings estandarizadas usan `/api/forms/lead`, validación server-side, Turnstile y honeypot.

Cloudflare documenta que:

- el token vence a los 300 segundos;
- es de un solo uso;
- reintentos o tokens vencidos pueden producir `timeout-or-duplicate`;
- un widget debe regenerar/resetear token cuando corresponde.

Fuentes oficiales:

- Turnstile Analytics: https://developers.cloudflare.com/turnstile/turnstile-analytics/
- Validación server-side y errores: https://developers.cloudflare.com/turnstile/get-started/server-side-validation/

### Evidencia disponible en Cloudflare

Turnstile Analytics permite revisar:

- solve rate;
- volumen del widget;
- challenge outcomes;
- token validation;
- hostname;
- navegador;
- país;
- user agent;
- ASN;
- IP de origen agregada.

Para confirmar bloqueos del formulario en `/api/forms/lead` se necesita además registrar y analizar en Workers/Pages Functions:

- `missing_turnstile_token`;
- `turnstile_failed`;
- `timeout-or-duplicate`;
- `zoho_submit_failed`;
- fecha, ruta y resultado sanitizado;
- sin PII, token ni IP completa en GitHub.

### Validación mínima futura

1. Revisar Turnstile Analytics para el widget y periodo relevante.
2. Ejecutar prueba incógnita controlada en una landing que realmente use Turnstile.
3. Probar primer envío, doble clic, espera mayor a cinco minutos y reintento.
4. Confirmar respuesta de `/api/forms/lead` y código de error.
5. Verificar que el widget se resetee tras `timeout-or-duplicate`.
6. Registrar agregados de éxito/fallo, sin PII.

## Priorización comercial

### Ahora

1. Diseñar las dos páginas indexables y su matriz contractual.
2. Resolver la URL histórica.
3. Implementar primero contenido, SEO y medición coherente.
4. Retirar regalo del hero de tráfico pagado.
5. Definir submit confirmado como conversión primaria técnica.
6. Publicar y validar ambas páginas.
7. Separar grupos de anuncios y keywords sólo después de publicación.
8. Mantener presupuesto y pujas durante el primer ciclo.
9. Medir siete días y revisar términos diariamente.

### Después

- seguridad de PII en redirecciones;
- migración del formulario B2C legacy a `/api/forms/lead`;
- observabilidad Turnstile;
- reconciliación completa con Zoho CRM;
- automatización del dashboard.

La seguridad no se elimina del plan, pero no debe bloquear el diseño comercial de las dos páginas. Los cambios productivos deben quedar separados y reversibles.

## Definition of Done documental

- decisión de dos páginas indexables registrada;
- intención y keywords de cada página separadas;
- secciones exclusivas y compartidas definidas;
- regalo clasificado fuera del hero comercial;
- findings PageSense preservados;
- hipótesis Turnstile clasificada correctamente;
- URL histórica identificada antes de publicar;
- implementación delegada a Capacita Edge en rama y PR;
- campañas reales no modificadas sin autorización.