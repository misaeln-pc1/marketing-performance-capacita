# Fichas de Proyectos y Sistemas

Este documento contiene fichas detalladas para cada componente principal del ecosistema de marketing y ventas, facilitando un entendimiento rápido de su rol, dependencias y estado.

---

## Proyecto: Leads Machine Zoho
### Objetivo
Construir una arquitectura de captación, calificación automática, nurturing y derivación comercial para Capacita usando Zoho One. Filtrar leads para que venta humana intervenga solo con intención real.
### Infraestructura usada
Zoho CRM, Zoho Marketing Automation, Zoho Campaigns, Zoho SalesIQ, Zoho Forms, Zoho PageSense.
### Entradas
Leads desde Meta Ads, Google Ads, Web/SEO. Datos de comportamiento web (tracking).
### Salidas
Leads calificados (MQL/SQL) para venta humana. Leads segmentados en pipelines (B2C, B2B). Reportes de calidad y conversión.
### Dependencias
Correcta configuración de plataformas de captación. Estructura de campos y campañas en Zoho CRM. Definición clara de scoring y journeys.
### Riesgos
Medir solo CPL y no calidad. Mezclar B2C con B2B. Duplicar lógica entre CRM, MA y Campaigns. Automatizaciones sin campos CRM claros.
### Indicadores
% MQL, % SQL, Tasa de conversión a matrícula, Costo por matriculado, Calidad del lead.
### Estado
En fase de diseño y documentación.
### Pendientes
Definir campos CRM exactos. Decidir dónde vivirá el scoring (CRM vs MA). Implementar primer journey real.

---

## Proyecto: Meta Ads Excel presencial
### Objetivo
Generar un volumen constante de leads B2C para el curso de Excel presencial, probando hipótesis de dolor ("Desbordado Operativo") y necesidad ("Reinserción Laboral").
### Infraestructura usada
Meta Ads, Meta Lead Forms, UTM Tracking, Zoho CRM.
### Entradas
Presupuesto, creatividades, copies, buyer personas.
### Salidas
Leads en formato Meta Lead Form, datos de rendimiento de campaña (CTR, CPL).
### Dependencias
Creatividades y copies aprobados. Formulario de Lead Ads configurado. Integración con Zoho CRM activa.
### Riesgos
Generar leads de baja calidad o fuera de perfil (empresas). No prometer empleo. No tener confirmados precio/fecha.
### Indicadores
CPL, Tasa de envío del formulario, Calidad percibida del lead, Contactabilidad.
### Estado
Creatividades v1 aprobadas. Listo para configurar en Meta Ads Manager.
### Pendientes
Confirmar precio, fecha y política de privacidad. Preparar copies y formulario final.

---

## Proyecto: Google Ads Excel presencial
### Objetivo
Capturar la demanda con intención directa de personas que buscan activamente cursos de Excel presenciales en Santiago.
### Infraestructura usada
Google Ads, Landing Pages, Zoho Forms, UTM Tracking, Zoho CRM.
### Entradas
Presupuesto, palabras clave, anuncios de texto, landing page.
### Salidas
Clics hacia la landing, conversiones (formularios enviados), datos de rendimiento (CPC, CPA).
### Dependencias
Landing page optimizada y funcional. Formulario de Zoho Forms incrustado y funcionando. Tracking de conversiones configurado.
### Riesgos
CPC alto. Baja tasa de conversión en la landing. Competencia alta.
### Indicadores
CPA (Costo por Adquisición/Lead), Tasa de conversión, Nivel de calidad de anuncios.
### Estado
Borrador. Pendiente de implementación.
### Pendientes
Definir landing final, palabras clave y grupos de anuncios.

---

## Proyecto: Web / Landing / SEO
### Objetivo
Atraer demanda orgánica y servir como punto central de conversión para campañas pagadas.
### Infraestructura usada
CMS/Web, Zoho Forms, SalesIQ, PageSense, Google Analytics, Google Search Console.
### Entradas
Contenido (artículos, páginas de curso), backlinks, tráfico de campañas.
### Salidas
Leads orgánicos, datos de comportamiento de usuario, punto de conversión para otras fuentes.
### Dependencias
Contenido de calidad. Optimización técnica SEO. Formularios y chatbots funcionales.
### Riesgos
Caída de rankings. Problemas técnicos (velocidad, móvil). Formularios rotos.
### Indicadores
Tráfico orgánico, Posiciones de palabras clave, Leads orgánicos, Tasa de conversión de landings.
### Estado
Activo y en operación continua.
### Pendientes
Crear y optimizar landings específicas para campañas.

---

## Sistema: Zoho CRM comercial
### Objetivo
Ser la fuente única de verdad para toda la información de clientes, prospectos y oportunidades comerciales.
### Infraestructura usada
Es la base. Se integra con Forms, MA, Campaigns, SalesIQ, etc.
### Entradas
Leads de todas las fuentes. Actualizaciones de estado por parte del equipo de ventas.
### Salidas
Reportes de ventas, pipelines actualizados, base para segmentación y journeys.
### Dependencias
Todos los sistemas dependen de su correcta estructura.
### Riesgos
Campos mal estructurados. Datos duplicados o sucios. Falta de uso por parte del equipo.
### Indicadores
Tasa de contactabilidad, Tasa de conversión por etapa del pipeline, Tiempo de ciclo de venta.
### Estado
Activo. Requiere mantenimiento y gobernanza constante.
### Pendientes
Validar y limpiar campos existentes. Definir y documentar procesos estándar.

---

*Nota: Las fichas para Zoho Marketing Automation, Campaigns, SalesIQ, TrainerCentral y Empresas/SENCE se crearán en una siguiente iteración para mantener este documento inicial enfocado.*