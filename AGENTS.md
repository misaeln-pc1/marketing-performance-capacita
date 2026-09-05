# AGENTS

## Lectura obligatoria y Gate de Vigencia

Antes de modificar documentación, prompts, estructuras, protocolos, campañas, criterios de medición, fuentes oficiales o decisiones que afecten futuros chats, leer en Global:

```text
misaeln-pc1/capacita-global-control/docs/LECTURA_OBLIGATORIA_GLOBAL.md
misaeln-pc1/capacita-global-control/docs/CONTROL_CAMBIOS_PLAN_ACORDADO.md
misaeln-pc1/capacita-global-control/docs/DICCIONARIO_OPERATIVO_CAPACITA.md
misaeln-pc1/capacita-global-control/docs/ESTANDAR_GLOBAL_PROYECTOS.md
misaeln-pc1/capacita-global-control/docs/ISSUE_TASK_ROUTING_STANDARD.md
misaeln-pc1/capacita-global-control/docs/ORQUESTACION_HERRAMIENTAS_IA_CAPACITA.md
misaeln-pc1/capacita-global-control/docs/REUSE_BEFORE_REINVENT_CAPACITA.md
misaeln-pc1/capacita-global-control/docs/ESTANDAR_FUENTES_PESADAS_CAPACITA.md
```

Regla de vigencia:

- Una definición aprobada por Misael debe cerrar como `VIGENTE_EN_MAIN`, `PR_LISTO_PARA_MERGE`, `TRANSITORIO_NO_VIGENTE_EN_MAIN`, `DRAFT_NO_VIGENTE` o `SUPERSEDED/HISTORICO`.
- Si el PR documental queda listo, pedir autorización con: `PR #X listo para merge. ¿Autorizas que yo haga el merge?`.
- Si dos documentos o protocolos vigentes se contradicen, detenerse y preparar consolidación.
- No afirmar estado vivo con instrucciones, PR o evidencia no leídos.

## Continuidad por frente — anti-reinicio

Antes de recomendar sobre una campaña, canal, cuenta, buyer persona, landing, medición o regla con historial:

1. leer `TASK_STATUS.md` y `DECISIONES.md`;
2. buscar el documento canónico específico en raíz y `docs/`;
3. revisar issue/PR reciente sólo si aporta estado aún no consolidado;
4. aplicar primero la decisión vigente y analizar únicamente delta o evidencia nueva;
5. no volver a pedir a Misael que justifique una regla documentada salvo contradicción o evidencia material nueva.

No reemplazar una decisión local vigente por consejos genéricos de plataforma. Si una recomendación estándar contradice aprendizaje Capacita documentado, señalar la diferencia y mantener la evidencia local hasta revisión controlada.

Ejemplo Google Ads: antes de opinar sobre palabras clave negativas de Excel B2C presencial, leer `docs/google-ads/GOOGLE_ADS_NEGATIVE_KEYWORDS_INTENT_POLICY.md`.

## Proactividad obligatoria de Growth

Ante una página, landing, campaña, curso, canal, creatividad, keyword, caída de desempeño u oportunidad comercial material, leer y aplicar:

```text
docs/analytics/MARKETING_PROACTIVE_OPPORTUNITY_SCAN_V01.md
```

Marketing no debe esperar que Misael pida por separado análisis de datos, keywords, negativas, buyer persona, competencia, CRO, diferenciación visual o tracking cuando sean necesarios para responder bien.

La frase histórica de `TASK_STATUS.md` “retomar Google Ads/Meta Ads cuando Misael lo indique” no es un gate para análisis READ ni para detectar oportunidades. Sólo mantiene en pausa writes, activaciones, campañas reales o cambios de presupuesto hasta instrucción y autorización.

El ciclo obligatorio es:

```text
DECISION DE NEGOCIO
→ FUENTES PERTINENTES
→ HALLAZGO
→ PRIORIDAD
→ ACCION EJECUTABLE
→ VALIDACION
→ NEXT_BEST_ACTION
```

Toda recomendación material debe contener evidencia o `DATA_GAP`, acción exacta, impacto, esfuerzo, confianza, riesgo, dueño, métrica y criterio de validación. No cerrar con consejos genéricos como “mejorar el copy”, “agregar imágenes” o “revisar palabras clave”.

## Uso de herramientas conectadas

Aplicar:

```text
CAPACIDAD_DIRECTA_READ_DISPONIBLE
→ USAR/ORQUESTAR
→ REGISTRAR FUENTE Y VENTANA
→ FALLBACK MANUAL SI NO APLICA O FALLA
```

Pueden utilizarse sin autorización adicional las capacidades ya conectadas y autorizadas en modo lectura que sean pertinentes —por ejemplo GSC, GA4, Google Ads, Meta Ads, Keyword Planner, SERP, Semrush/HYPD, PageSense y datos CRM agregados autorizados— siempre que no impliquen PII, secretos, export crudo, costo nuevo, OAuth/scope nuevo ni efectos externos.

Cualquier write, nueva conexión, instalación, costo, acceso sensible, cambio de campaña, presupuesto, puja, audiencia, conversión, CRM o producción requiere autorización explícita.

## Protocolo obligatorio para páginas y landings

Ante cualquier solicitud de crear, revisar, auditar, relanzar, publicar u optimizar una página o landing de Capacita, leer y aplicar además:

```text
docs/seo-ai/MARKETING_PAGE_VISIBILITY_PROTOCOL_V01.md
```

Es obligatorio aunque Misael no vuelva a pedir explícitamente SEO/AEO/GEO.

La evaluación integra, según aplique:

```text
SEO
→ Local SEO
→ AEO
→ GEO / AI Search
→ AI-readability / citabilidad
→ demanda / keywords
→ intención
→ buyer persona
→ propuesta de valor
→ journey / CTA
→ competencia
→ diferenciación entre landings hermanas
→ Ads / CPC como señal
→ CRO / conversión
→ pain signals y tracking
→ medición
→ impacto comercial
```

Reglas duras:

- El protocolo no obliga a indexar todas las páginas. Preservar `noindex` cuando una landing paid-only tenga esa decisión vigente.
- Mantener familia corporativa sin clonar la experiencia: `MISMA_MARCA != MISMA_PAGINA`.
- Comparar hero/imagen, acento, ejemplo, prueba, dolor, CTA y elemento distintivo contra páginas hermanas.
- Un clic expresa una señal conductual; no prueba el dolor real ni el buyer persona definitivo.
- No confundir acceso de crawlers con comprensión/citabilidad.
- No inventar `llms.txt`, schema especial, keywords, claims, ratings, fechas, precios, duración, certificaciones ni contenidos no verificados.
- Separar crawlers de búsqueda/recuperación de crawlers de entrenamiento y verificar documentación oficial antes de cambiar políticas.
- Marketing define demanda, intención, contenido, diferenciación, AEO/GEO, CRO, eventos y prioridad; Capacita Edge implementa frontend, robots, headers, canonical, sitemap, structured data, Cloudflare y tracking técnico.

## Separación de señales

Nunca colapsar:

```text
ADS_PLATFORM_SIGNAL
!= WEB_SIGNAL
!= CRM_LEAD_OR_CONTACT
!= DEAL
!= CURSOALUMNO
!= VENTA_REAL
```

No declarar éxito sólo por clic, CTR o conversión de plataforma si existe o debería existir una medida comercial posterior.

## Sistema de Tareas Atlas

Regla vigente:

```text
El problema vive en el repo.
La tarea ejecutable vive en Task Hub.
La evidencia tecnica vive en el repo.
```

- Ideas, investigaciones, decisiones, riesgos, bloqueos, épicas e incidentes: issue en este repo.
- Tareas ejecutables, personales, administrativas y seguimientos accionables: issue en `misaeln-pc1/capacita-task-hub`.
- Si una tarea deriva de un issue local, registrar `Issue padre` y `Repo dueño`.
- Referencia: `misaeln-pc1/capacita-global-control/docs/ISSUE_TASK_ROUTING_STANDARD.md`.

## Fuentes pesadas

- SharePoint Site `Documentos/CAPACITA/Proyectos/external-files/marketing-performance-capacita` es la fuente canónica de binarios pesados.
- OneDrive `Sitio de comunicación - external-files` es acceso local sincronizado, no segunda bodega.
- GitHub guarda mapa, síntesis, manifests y evidencia liviana.
- No mover, borrar, renombrar ni cambiar permisos sin autorización y validación.

## Feedback scan

Antes de cerrar un cambio material, revisar feedback y estado en raíz/`docs/`, issues y PRs abiertos. Clasificar cada hallazgo como `APLICADO`, `PENDIENTE`, `ESCALADO`, `RECHAZADO_CON_MOTIVO` o `NO_APLICA`. No crear un archivo nuevo sólo por plantilla si la información ya tiene dueño.

## Reglas duras

- No trabajar directo en `main`.
- No ejecutar scripts, workflows, integraciones, automatizaciones ni nuevas APIs sin autorización.
- No subir tokens, credenciales, `.env`, IDs sensibles, PII ni datos crudos no sanitizados.
- No modificar campañas reales, presupuestos, conversiones, etiquetas, GTM, PageSense, formularios, CRM ni producción sin autorización explícita.
- Los cambios documentales reversibles deben ir en rama `docs/marketing-[objetivo]` o equivalente.
- Un plan aprobado es baseline; cualquier cambio material de objetivo, secuencia, ejecutor, herramienta, validación, evidencia o cierre debe comunicarse antes.
