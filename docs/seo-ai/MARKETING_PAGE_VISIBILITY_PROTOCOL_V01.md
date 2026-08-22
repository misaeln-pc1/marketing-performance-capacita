# Protocolo obligatorio de visibilidad de páginas — V01

## Estado y vigencia

- Decisión aprobada por Misael: 2026-08-22.
- Issue de control: `#63 [INSTRUCCIONES] Protocolo obligatorio de visibilidad de páginas`.
- Estado: este protocolo es `VIGENTE_EN_MAIN` únicamente cuando este archivo esté mergeado en `main`.
- Alcance: Marketing Performance / Campañas & Growth Capacita.
- Reutiliza y no reemplaza `SEO_GEO_TECHNICAL_RESEARCH_BASELINE_V01.md`, `AI_VISIBILITY_QUERY_BENCHMARK_V01.md`, `SEO_GEO_AUDIT_HANDOFF_TO_EDGE_V01.md` y `SEO_GEO_MEASUREMENT_MODEL_V01.md`.

## Regla obligatoria

Toda página o landing que Marketing cree, revise, audite, relance o use como destino de campaña debe pasar por este protocolo antes de declararse lista.

Aplica a:

- páginas orgánicas de cursos;
- landings de campañas pagadas;
- home, hubs, categorías y páginas de servicio;
- páginas locales;
- páginas informativas o de captación;
- nuevas URLs y revisiones materiales de URLs existentes.

El protocolo es obligatorio aunque una página sea `noindex` por diseño. **Aplicar el protocolo no significa hacer indexable todo.** Una landing paid-only puede conservar `noindex,follow` si ese es el baseline aprobado; en ese caso SEO/GEO público se evalúa para detectar conflictos, canibalización y coherencia, pero la salida debe registrar `INDEXABILITY=NOINDEX_INTENTIONAL`.

## Objetivo integral

No optimizar una página sólo por palabras clave. La secuencia obligatoria es:

```text
CONTEXTO / REUSE BEFORE REINVENT
→ SEO
→ LOCAL SEO cuando aplique
→ AEO
→ GEO / AI SEARCH
→ AI-READABILITY / CITABILIDAD
→ DEMANDA / KEYWORDS
→ INTENCIÓN
→ BUYER PERSONA
→ PROPUESTA DE VALOR
→ JOURNEY / CTA
→ COMPETENCIA
→ ADS / CPC cuando aporte señal comercial
→ CRO / CONVERSIÓN
→ MEDICIÓN
→ IMPACTO COMERCIAL
→ PRIORIDAD / HANDOFF
```

No se declara una página lista porque sólo tenga buen diseño, buen SEO técnico o un alto volumen de búsqueda.

## 1. Contexto y Reuse Before Reinvent

Antes de investigar o recomendar:

1. leer `TASK_STATUS.md`, `DECISIONES.md` y el canónico específico del frente;
2. recuperar GTM/RevOps aplicable: buyer persona, propuesta de valor, journey y segmentación;
3. revisar capacidades conectadas disponibles antes de pedir copy/paste o construir una integración;
4. reutilizar GSC, Google Ads/Keyword Planner, SERP, analytics, Meta, Bing, GBP, plugins/MCP y otras fuentes ya autorizadas cuando aporten evidencia real;
5. analizar sólo el delta cuando la página o intención ya fue trabajada.

## 2. Gate de indexabilidad y propósito

Registrar antes de optimizar:

- objetivo de la página;
- audiencia B2C/B2B;
- orgánica, paid-only o híbrida;
- `INDEX`, `NOINDEX_INTENTIONAL` o `PENDING_DECISION`;
- intención primaria;
- buyer persona primario;
- CTA primario;
- URL/canonical esperado;
- relación con páginas existentes.

No mezclar B2C y B2B cuando intención, oferta o ciclo comercial difieran.

## 3. SEO obligatorio

Evaluar como mínimo:

- intención de búsqueda principal y clusters secundarios;
- URL, title, meta description y H1;
- jerarquía H2/H3 y HTML semántico;
- cobertura factual y semántica sin keyword stuffing;
- internal linking y anchors naturales;
- canonical, robots/meta robots y sitemap según propósito;
- redirecciones y riesgo de cadenas;
- páginas duplicadas, históricas y canibalización;
- structured data consistente con contenido visible;
- performance/Core Web Vitals cuando exista evidencia de campo o Lighthouse;
- imágenes/alt cuando sean informativas;
- autoridad, enlaces y menciones externas cuando sean relevantes.

### Demanda y keywords

Usar primero evidencia real y conectada cuando esté disponible:

- Google Search Console: consultas y páginas donde Capacita ya aparece;
- Google Ads Keyword Planner: volumen, histórico, competencia y CPC como señal comercial, incluso si no habrá campaña;
- Google Trends: tendencia/estacionalidad cuando aplique;
- Bing Webmaster/keyword data cuando esté configurado;
- Google Business Profile para demanda local cuando aplique;
- SERP real para validar intención, formatos y competidores.

Las estimaciones no reemplazan GSC ni resultados comerciales. CPC no equivale a valor del negocio; se usa sólo como señal complementaria.

## 4. Local SEO cuando exista componente geográfico

Evaluar:

- intención local explícita e implícita;
- Google Business Profile;
- consistencia de nombre, dirección y teléfono;
- sede, comuna/ciudad y modalidad presencial claramente visibles;
- `Organization` / `LocalBusiness` cuando corresponda y sin duplicar graphs;
- Local Pack y competidores locales;
- reseñas, prominencia y menciones verificables;
- enlaces internos desde páginas locales/hubs;
- evidencia de ubicación real.

No inventar proximidad, distancias, número de reseñas, ratings ni atributos del perfil.

## 5. AEO — Answer Engine Optimization

AEO significa optimizar para motores que responden preguntas directamente. No basta con permitir un bot.

Toda página indexable con intención informativa/comercial debe ofrecer respuestas visibles y autosuficientes a las preguntas clave del usuario.

### Formato recomendado

- H2 formulado como pregunta o necesidad real cuando aporte claridad;
- primera frase responde directamente;
- después se amplía con detalles, listas o ejemplos;
- sujeto explícito: `Este curso...`, `Excel avanzado...`, `Capacita...`;
- datos verificables y vigentes;
- evitar slogans vacíos como respuesta principal.

### Preguntas mínimas por tipo de curso/servicio

Adaptar según el caso:

- qué es / qué incluye;
- para quién es;
- qué conocimientos previos requiere;
- qué aprenderá o podrá hacer;
- modalidad;
- ubicación cuando aplique;
- duración, precio y fechas sólo si están confirmados;
- certificado o evidencia sólo si es verificable;
- diferencias entre niveles/alternativas cuando ayuden a decidir.

No crear preguntas sólo por volumen; priorizar intención real, GSC, Keyword Planner, People Also Ask, AI Overviews y conversaciones comerciales.

## 6. GEO / AI Search

GEO/AI Search busca aumentar la probabilidad de que motores generativos comprendan, seleccionen y citen a Capacita como fuente. No es una garantía de aparición ni un conjunto de trucos independientes del SEO.

Evaluar:

- accesibilidad e indexabilidad;
- claridad de entidad: Capacita, OTEC, curso/servicio, modalidad y sede;
- información factual, específica y actualizada;
- secciones citables y autosuficientes;
- autoridad temática y externa;
- referencias/menciones coherentes en otras fuentes;
- benchmark de presencia/cita en motores IA;
- correspondencia entre contenido visible y structured data.

No declarar que `llms.txt`, `ai.txt` o un schema especial sean requisitos de ranking/citación. Pueden evaluarse en el futuro si aportan valor demostrado, pero no son gate por defecto.

## 7. AI-readability / citabilidad obligatoria

La página debe ser fácil de entender para una IA **después de que el crawler accede**.

### Contrato de lectura

En el HTML/render principal, sin depender de una imagen, carrusel cerrado o interacción compleja, una herramienta de recuperación debe poder identificar de forma inequívoca, cuando aplique:

- qué ofrece Capacita;
- nombre del curso/servicio;
- nivel o alcance;
- modalidad;
- ubicación;
- público objetivo;
- prerrequisitos;
- contenidos/temario o capacidades principales;
- resultados esperados sin promesas garantizadas;
- certificación si está confirmada;
- CTA y siguiente paso;
- hechos institucionales relevantes.

Cada bloque clave debe conservar sentido si se recupera de forma aislada. Evitar pronombres ambiguos, copy excesivamente publicitario y datos esenciales presentes sólo en imágenes.

### Test mínimo de AI-readability

Para páginas indexables, comprobar si un lector/fetch puede responder sólo con el contenido de la página:

1. ¿Qué ofrece esta página?
2. ¿Para quién es?
3. ¿Qué problema/intención resuelve?
4. ¿Dónde y cómo se entrega?
5. ¿Qué incluye realmente?
6. ¿Qué debe saber el usuario antes de elegir?
7. ¿Por qué esta página es una fuente verificable y no sólo publicidad?

Si una respuesta crítica requiere inferencia externa, marcar `AI_READABILITY=WARN` y corregir el contenido cuando corresponda.

## 8. Crawlers de búsqueda/recuperación vs entrenamiento

Cuando la página deba ser descubierta/citada por motores IA, auditar robots/CDN/WAF y verificar la documentación oficial vigente de cada proveedor antes de cambiar reglas.

Distinguir:

### Search / retrieval

- `Googlebot` para Google Search y superficies AI de Google;
- `Bingbot` para Bing y superficies dependientes;
- `OAI-SearchBot` para ChatGPT Search;
- `PerplexityBot` para Perplexity;
- `Claude-SearchBot` y `Claude-User` para búsqueda/recuperación de Claude cuando sigan vigentes según documentación oficial.

### Training / desarrollo

Bots como `GPTBot`, `ClaudeBot` o controles como `Google-Extended` no deben habilitarse automáticamente sólo para cumplir GEO. Search/retrieval y training son decisiones distintas.

No declarar `CRAWLER_ACCESS=PASS` sólo por `robots.txt`; revisar Cloudflare/WAF/challenge/status/contenido cuando corresponda.

## 9. Competencia y SERP

Para cada intención material evaluar, cuando aplique:

- top orgánicos;
- anuncios pagados visibles;
- Local Pack;
- People Also Ask / related searches;
- AI Overview/AI answer y fuentes citadas;
- marketplaces/directorios separados de proveedores reales;
- mensajes, oferta, prueba de confianza, precio público y contenido de competidores;
- brechas de contenido y entidad.

No inventar tráfico, ventas, ROAS, conversiones o presupuesto de terceros.

## 10. Buyer persona, propuesta de valor y journey

Marketing consume primero los canónicos GTM/RevOps. Toda página debe registrar:

- buyer persona primario o `BP-000/NO_MATCH_CANONICO` si no encaja;
- intención y etapa del journey;
- problema/resultado buscado;
- propuesta de valor aplicada;
- CTA coherente;
- señales emergentes que deban volver a GTM como hipótesis, no como nuevo canónico creado por Marketing.

## 11. CRO y conversión

Evaluar:

- claridad above-the-fold;
- correspondencia intención → mensaje → oferta → CTA;
- confianza y evidencia;
- fricción de formulario;
- mobile/desktop;
- navegación y distracciones;
- separación B2C/B2B;
- tracking y evento de submit real;
- PageSense/analytics como señales web, no como leads;
- Zoho CRM como fuente comercial cuando exista mapping agregado verificable.

No optimizar sólo CTR o clics si el resultado comercial está disponible.

## 12. Impacto comercial y prioridad

Toda recomendación material debe contrastar:

- demanda;
- intención;
- competencia;
- oferta real;
- canal;
- CPC/valor de mercado cuando exista;
- conversión web;
- leads/deals/matrículas agregados cuando estén disponibles;
- riesgo y esfuerzo.

No recomendar una nueva página o negocio sólo por volumen de búsqueda.

## 13. Salida obligatoria de cada revisión

Toda revisión material de página debe cerrar, como mínimo, con:

```text
PAGE_VISIBILITY_PROTOCOL=PASS|WARN|FAIL
INDEXABILITY=INDEX|NOINDEX_INTENTIONAL|PENDING_DECISION
SEO=PASS|WARN|FAIL
LOCAL_SEO=PASS|WARN|FAIL|N/A
AEO=PASS|WARN|FAIL
GEO_AI_SEARCH=PASS|WARN|FAIL
AI_READABILITY=PASS|WARN|FAIL
CRAWLER_ACCESS=PASS|WARN|FAIL|N/A
DEMAND_EVIDENCE=PASS|PARTIAL|DATA_GAP
CANNIBALIZATION=PASS|WARN|FAIL
BUYER_PERSONA=<ID/version o BP-000>
CRO=PASS|WARN|FAIL
MEASUREMENT=PASS|PARTIAL|DATA_GAP
COMMERCIAL_FIT=HIGH|MEDIUM|LOW|DATA_GAP
```

Y debe entregar:

1. evidencia;
2. interpretación;
3. cambios recomendados priorizados P0/P1/P2;
4. qué NO cambiar;
5. riesgos/data gaps;
6. siguiente paso y dueño.

## 14. Handoff e implementación

Marketing define y audita:

- demanda, keywords e intención;
- benchmark SERP/AI;
- buyer persona aplicado;
- contenido/mensaje recomendado;
- AEO/GEO/AI-readability;
- CRO e impacto comercial.

Capacita Edge implementa cuando corresponda:

- HTML/CSS/frontend;
- robots/meta/X-Robots-Tag;
- canonical/sitemap/redirects;
- structured data;
- Cloudflare/WAF/Worker;
- performance técnica;
- tracking/frontend.

Los cambios productivos, credenciales/scopes, Ads reales, Cloudflare productivo, redirects adicionales, merge/main o decisiones destructivas mantienen sus gates de autorización.

## 15. DoD del protocolo

Una página no queda `LISTA` bajo este protocolo hasta que:

- propósito e indexabilidad estén explícitos;
- exista evidencia de demanda/intención suficiente o `DATA_GAP` declarado;
- SEO esté revisado;
- Local SEO esté revisado si aplica;
- AEO esté cubierto;
- GEO/AI Search y AI-readability estén evaluados;
- canibalización y arquitectura estén consideradas;
- buyer persona/propuesta/journey sean coherentes;
- CRO y medición estén revisados;
- hechos/claims no inventados estén validados;
- pendientes técnicos estén derivados al dueño correcto;
- no se haya confundido una página paid-only `noindex` con una página orgánica.

## Regla de aplicación futura

Ante solicitudes como `revisa esta página`, `crea una landing`, `hagamos una página`, `optimiza este curso`, `quiero publicar esta URL` o equivalentes, Marketing debe invocar este protocolo por defecto sin esperar que Misael vuelva a pedir SEO/AEO/GEO explícitamente.
