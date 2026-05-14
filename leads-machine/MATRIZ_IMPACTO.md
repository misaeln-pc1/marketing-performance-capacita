# Matriz de Impacto por Cambio

Esta matriz sirve como una guía rápida para evaluar el riesgo y las acciones necesarias al modificar componentes clave del sistema.

## Si cambio X, revisar Y

| Cambio | Impacta en | Riesgo | Verificar antes | Acción recomendada |
|---|---|---|---|---|
| Cambiar campos CRM | Formularios, Journeys, Scoring, Reportes, Integraciones | **Alto** | Mapeo de dependencias en Zoho (workflows, blueprints), MA, Campaigns. | Comunicar al equipo. Planificar cambio. Probar en sandbox si es posible. Actualizar toda la cadena. |
| Cambiar formulario Meta Lead Ads | Integración CRM, Campos CRM, Journey inicial | **Medio** | Que la integración CRM siga funcionando. Que los campos nuevos/modificados existan en CRM. | Pausar campaña. Actualizar mapeo de campos en Zoho. Probar envío. Reactivar. |
| Cambiar landing | Tracking (UTM, GTM, Pixel), Formularios, PageSense, SEO | **Medio** | Que todos los scripts de tracking estén instalados. Que los formularios funcionen. Redirecciones 301 si cambia URL. | Clonar y modificar. Probar en staging. Publicar y verificar tracking y formularios en vivo. |
| Cambiar UTM | Reportes en CRM, Google Analytics, Plataformas Ads | **Alto** | Consistencia de la nomenclatura. Que los sistemas de reporte los lean correctamente. | Usar un generador de UTMs centralizado. No cambiar estructura a mitad de campaña. Validar con equipo de BI/Datos. |
| Cambiar scoring | Segmentación, Derivación a ventas, Journeys | **Alto** | Umbrales de MQL/SQL. Lógica de los journeys que se activan por score. | Modelar el cambio. Revisar impacto en la base actual. Ajustar journeys y alertas a ventas. Comunicar. |
| Cambiar journey | Experiencia del lead, Comunicación, Scoring | **Alto** | Puntos de entrada y salida. Condiciones. Contenido de los emails/SMS. | Mapear el journey actual. Diseñar el nuevo. Probar con leads de test. Implementar y monitorear. |
| Cambiar pipeline EMPRESAS | Proceso comercial B2B, Reportes de venta, Automatizaciones B2B | **Medio** | Etapas del negocio, campos obligatorios por etapa, automatizaciones asociadas. | Validar con el equipo comercial. Ajustar en CRM. Capacitar al equipo sobre el nuevo flujo. |
| Cambiar SalesIQ | Captura de leads web, Experiencia de usuario, Handoff a ventas | **Medio** | Flujo del chatbot, reglas de ruteo, integración con CRM. | Probar el nuevo flujo en un entorno de prueba. Verificar creación de leads en CRM. |
| Cambiar Campaigns | Comunicación con exalumnos/bases, Segmentación | **Bajo/Medio** | Listas de suscriptores, plantillas, automatizaciones simples. | Revisar audiencias afectadas. Probar envíos de test. |
| Cambiar Marketing Automation | Scoring, Journeys, Tracking web | **Alto** | Ver "Cambiar scoring" y "Cambiar journey". | Requiere planificación y pruebas exhaustivas. |
| Cambiar precio/fecha del curso | Landings, Anuncios, Formularios, Equipo de ventas | **Medio** | Que el cambio se refleje en todos los puntos de contacto con el cliente. | Crear checklist de activos a actualizar. Comunicar a ventas. Actualizar todo simultáneamente. |
| Cambiar buyer persona | Anuncios (copy, creatividades), Segmentación, Landings | **Medio** | Alineación de la nueva hipótesis con la oferta. | Documentar la nueva hipótesis. Crear nuevos activos (anuncios, etc.). Lanzar como test A/B. |
| Cambiar oferta de exalumno | Zoho Campaigns, Landings, Equipo de ventas | **Bajo** | Claridad de la oferta y segmento al que aplica. | Actualizar plantillas de email y landing. Informar a ventas. |
| Cambiar integración TrainerCentral/CRM | Flujo de alumnos a CRM, Segmentación de exalumnos | **Medio** | Mapeo de campos, disparadores de la sincronización. | Revisar la configuración de la integración. Probar con un usuario de test. |

## Semáforo de riesgo

- **Bajo**: Cambio documental o de copy sin automatización directa. El impacto es bajo y fácil de revertir.
- **Medio**: Cambio en un componente de cara al público (formulario, landing, campaña). Puede interrumpir la captación de leads o la experiencia de usuario.
- **Alto**: Cambio en la infraestructura central (CRM, scoring, campos, journeys, integraciones). Un error puede tener efectos en cascada, corromper datos o detener operaciones críticas.