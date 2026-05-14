# Infraestructura Compartida y Dependencias

Este documento mapea los activos tecnológicos y de datos que son compartidos por múltiples proyectos, destacando los riesgos de modificarlos.

| Infraestructura | Usada por | Qué controla | Riesgo si cambia | Proyectos afectados | Dueño / sistema fuente |
|---|---|---|---|---|---|
| Zoho CRM | Todos | Fuente única de verdad para leads, contactos, deals. | **Alto**. Desincroniza todo el sistema comercial. | Todos | Zoho CRM |
| Campos CRM | Zoho CRM, Forms, MA, Campaigns, Reportes | Estructura de datos del lead/contacto (ej: `Programa_Estrategico`). | **Alto**. Rompe automatizaciones, reportes y segmentación. | Leads Machine, Meta Ads, Google Ads, Web, Empresas, Exalumnos | Zoho CRM |
| Fuente de Posible Cliente | Zoho CRM, UTMs, Formularios | Atribución de origen del lead. | **Medio**. Se pierde visibilidad de qué canal funciona. | Meta Ads, Google Ads, Web, Reportes | Zoho CRM / Formularios |
| `Programa_Estrategico` | Zoho CRM, Reportes | Agrupación de campañas para análisis de alto nivel. | **Medio**. Afecta reportes estratégicos y de negocio. | Todos los de captación | Zoho CRM |
| Campañas CRM | Zoho CRM, Reportes | Agrupación de leads por iniciativa táctica. | **Bajo/Medio**. Afecta reportes de campaña específicos. | Meta Ads, Google Ads, etc. | Zoho CRM |
| Zoho Forms | Landings, Web | Captura de datos estructurada. | **Medio**. Leads no entran o entran con datos incorrectos. | Web / Landing / SEO, Google Ads | Zoho Forms |
| Meta Lead Forms | Meta Ads | Captura de datos nativa en Meta. | **Medio**. Leads de Meta no entran al CRM. | Meta Ads Excel presencial | Meta Ads |
| Landing pages | Google Ads, Meta Ads, SEO | Punto de conversión y entrega de información. | **Medio**. Cae la conversión, se rompe el tracking. | Google Ads, Web / SEO, a veces Meta Ads | Web (CMS/código) |
| UTM tracking | Meta Ads, Google Ads, Campaigns | Parámetros de URL para atribución. | **Alto**. Se pierde toda la atribución de campañas. | Meta Ads, Google Ads, Campaigns, Reportes | Marketing (definición) / Plataformas Ads (ejecución) |
| Zoho Marketing Automation | Leads Machine | Scoring, journeys complejos, tracking web. | **Alto**. Se detiene la calificación y nutrición automática. | Leads Machine Zoho | Zoho Marketing Automation |
| Zoho Campaigns | Exalumnos, Nurturing | Email masivo a bases con permiso. | **Medio**. Se detiene la comunicación con exalumnos/bases. | Exalumnos / continuidad formativa | Zoho Campaigns |
| SalesIQ | Web / Landing | Chatbot, chat en vivo, tracking de visitantes. | **Medio**. Se pierde captura de intención en tiempo real. | Web / Landing / SEO, Leads Machine | Zoho SalesIQ |
| PageSense | Web / Landing | A/B testing, heatmaps. | **Bajo**. Se pierde capacidad de optimización de landings. | Web / Landing / SEO | Zoho PageSense |
| WhatsApp | Venta humana | Contacto directo con leads calificados. | **Bajo**. Afecta velocidad de contacto, no el sistema. | Venta humana | Venta (equipo) |
| Google Ads | Google Ads Excel presencial | Plataforma de anuncios de búsqueda. | **N/A** (es fuente). | Google Ads Excel presencial | Google Ads |
| Meta Ads | Meta Ads Excel presencial | Plataforma de anuncios sociales. | **N/A** (es fuente). | Meta Ads Excel presencial | Meta Ads |
| TrainerCentral | eLearning | Plataforma de cursos online. | **Medio**. Afecta flujo de alumnos online a CRM. | TrainerCentral / eLearning | TrainerCentral |