# Plan de Accion

## Fase 1: base visual y mapa

**Objetivo:** dejar una estructura editable para entender la maquina completa antes de implementar herramientas.

**Tareas**
- Crear mapa mental compatible con Markmap.
- Crear flujo maestro en Mermaid.
- Documentar reglas de trabajo y limites.

**Entregables**
- `MAPA_MENTAL.md`
- `FLUJO_MAESTRO.md`
- `README.md`

**Definition of Done**
- El mapa se puede abrir visualmente.
- El flujo muestra la arquitectura completa.
- El subproyecto queda explicado sin crear app ni dependencias.

## Fase 2: campos CRM

**Objetivo:** definir los campos minimos necesarios para capturar fuente, intencion, segmento y estado comercial.

**Tareas**
- Levantar campos CRM existentes.
- Identificar campos faltantes.
- Separar campos B2C y B2B cuando corresponda.
- Definir estados minimos de lead.

**Entregables**
- Lista de campos base.
- Pendientes de configuracion CRM.
- Decisiones sobre pipeline Standard y EMPRESAS.

**Definition of Done**
- Existe una propuesta de campos clara.
- Los campos permiten medir fuente, score, estado y siguiente accion.
- No hay integraciones reales todavia.

## Fase 3: scoring

**Objetivo:** crear un modelo simple para priorizar intencion y calidad comercial.

**Tareas**
- Validar senales positivas y negativas.
- Definir umbrales frio, tibio, MQL y SQL.
- Decidir donde vivira el scoring.
- Separar regla de empresa para pipeline EMPRESAS.

**Entregables**
- Matriz de scoring inicial.
- Umbrales operativos.
- Criterio de contacto humano.

**Definition of Done**
- El score permite decidir a quien contactar.
- Las senales B2C y B2B no quedan mezcladas.
- El modelo se puede ajustar sin reescribir todo.

## Fase 4: journeys

**Objetivo:** definir recorridos automaticos simples para cada tipo de lead.

**Tareas**
- Priorizar el primer journey real.
- Diseñar journey de lead nuevo Meta Ads.
- Diseñar ruta empresa.
- Diseñar reactivacion de exalumnos.
- Definir salida a venta humana.

**Entregables**
- Journey lead nuevo.
- Journey empresa.
- Journey exalumno o reactivacion.

**Definition of Done**
- Cada journey tiene entrada, condiciones, mensajes y salida.
- La venta humana solo se activa con senal clara.
- No se implementan automatizaciones productivas aun.

## Fase 5: medicion

**Objetivo:** medir calidad comercial, no solo volumen de leads.

**Tareas**
- Definir reporte minimo.
- Vincular fuente, anuncio, landing y resultado.
- Separar metricas B2C y B2B.
- Definir costo por matriculado.

**Entregables**
- Lista de metricas minimas.
- Criterios de MQL, SQL y matricula.
- Vista inicial de reporte.

**Definition of Done**
- Se puede saber que fuente trae mejores leads.
- Se mide conversion por calidad e intencion.
- El reporte minimo cabe en una vista simple.

## Fase 6: optimizacion

**Objetivo:** ajustar captacion, landing, scoring y journeys con evidencia.

**Tareas**
- Revisar datos de PageSense.
- Probar variantes de landing.
- Ajustar creatividades.
- Ajustar scoring segun conversion real.
- Revisar mensajes de journeys.

**Entregables**
- Backlog de optimizacion.
- Hipotesis A/B.
- Ajustes priorizados.

**Definition of Done**
- Cada cambio responde a una metrica o aprendizaje.
- Las mejoras no rompen la arquitectura base.
- El sistema sigue simple y editable.
