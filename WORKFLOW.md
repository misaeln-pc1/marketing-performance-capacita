# Workflow Operativo

El flujo de trabajo estándar en este repositorio es el siguiente:

1. **ChatGPT define arquitectura/criterio:** Establece el plan de acción, estructura y revisión.
2. **Antigravity ejecuta sobre rama:** Realiza los cambios operativos solicitados en una rama específica.
3. **Antigravity actualiza `TASK_STATUS.md`:** Registra el progreso, acciones y estado de la tarea.
4. **Antigravity prepara `REVIEW_REQUEST.md`:** Genera un resumen de los cambios para revisión.
5. **ChatGPT revisa:** Evalúa la solicitud de revisión y los cambios realizados.
6. **Se corrige:** Antigravity aplica las correcciones solicitadas por ChatGPT (si las hay).
7. **Se mergea o se cierra la tarea:** Una vez aprobado, los cambios se integran y finaliza el ciclo.
