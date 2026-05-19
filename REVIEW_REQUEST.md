# Solicitud de Revisión (Review Request)

## ¿Qué se hizo?

Se documentó el aprendizaje de la campaña Meta Ads / Facebook Ads v1 para Excel Básico–Intermedio Presencial Santiago Centro y se preparó una estrategia v2 enfocada en calidad de leads.

## Rama

`docs/meta-excel-quality-v2`

## Archivos creados

- `campaigns/excel-basico-intermedio-presencial-santiago/lead-quality-learnings-v1.md`
- `campaigns/excel-basico-intermedio-presencial-santiago/meta-ads-quality-test-v2.md`
- `campaigns/excel-basico-intermedio-presencial-santiago/zoho-crm-measurement-v2.md`

## Archivos modificados

- `TASK_STATUS.md`
- `REVIEW_REQUEST.md`

## Decisiones registradas

- La campaña v1 generó volumen, pero baja respuesta/contactabilidad.
- El problema principal se interpreta como baja intención del formulario instantáneo, no como falla total de atracción.
- Se mantiene la lógica de 4 anuncios por dolor:
  1. `AD01_DESBORDADO_REPORTE`.
  2. `AD02_DESBORDADO_PLANILLAS`.
  3. `AD03_APRENDER_CON_GUIA`.
  4. `AD04_CV_REINSERCION_LABORAL`.
- El dolor/persona debe inferirse desde el anuncio cuando sea posible.
- La v2 debe comparar dos rutas:
  - Lead Form filtrado.
  - Click a WhatsApp.
- El filtro fuerte debe moverse a imagen/copy: curso presencial, pagado, sin matrícula, Santiago Centro.
- La métrica prioritaria deja de ser CPL bruto y pasa a ser costo por lead respondido y costo por matrícula.
- Para una prueba limpia, se recomienda revisar/desactivar anuncios multianunciante si Meta lo permite.
- No se recomienda cargar todas las métricas de Meta en cada lead de Zoho CRM; Zoho debe registrar atribución básica, intención y resultado comercial.

## Revisión solicitada

Validar que la estrategia v2:

- no duplique estructura existente;
- reutilice la campaña Excel presencial ya creada;
- no mezcle B2C con empresa/SENCE/OTIC;
- no avance hacia CRM técnico profundo;
- no proponga automatizaciones complejas antes de confirmar qué datos entrega Zoho Social;
- no incluya datos personales, secretos, capturas ni archivos pesados;
- mantenga foco en ads, leads, buyer persona, customer journey y aprendizaje comercial.

## Riesgos o dudas

- Falta confirmar precio vigente.
- Falta confirmar duración vigente.
- Falta confirmar próxima fecha.
- Falta activar/validar medio de pago Meta.
- Falta confirmar política de privacidad de Meta Lead Ads.
- Falta verificar qué campos Zoho Social transfiere realmente a Zoho CRM.
- Falta definir si WhatsApp será manual, Zoho Desk, Zoho CRM, n8n u otro flujo.
- Falta decidir presupuesto por conjunto para comparar Form vs WhatsApp sin sesgo de asignación automática.

## Decisión solicitada

- [ ] APROBADO
- [ ] APROBADO CON OBSERVACIONES
- [ ] CORREGIR ANTES DE MERGE
