# Solicitud de Revisión (Review Request)

## ¿Qué se hizo?

Se documentó el aprendizaje de la campaña Meta Ads / Facebook Ads v1 para Excel Básico-Intermedio Presencial Santiago Centro, se preparó una estrategia v2 enfocada en calidad de leads, se corrigió el naming canónico de anuncios y se agregó el brief/matriz de creatividades v2.

## Rama

`docs/meta-excel-quality-v2`

## Archivos creados

- `campaigns/excel-basico-intermedio-presencial-santiago/lead-quality-learnings-v1.md`
- `campaigns/excel-basico-intermedio-presencial-santiago/meta-ads-quality-test-v2.md`
- `campaigns/excel-basico-intermedio-presencial-santiago/zoho-crm-measurement-v2.md`
- `assets/meta-ads/excel-presencial-santiago/creatives-v2/README.md`

## Archivos modificados

- `TASK_STATUS.md`
- `REVIEW_REQUEST.md`
- `campaigns/excel-basico-intermedio-presencial-santiago/lead-quality-learnings-v1.md`
- `campaigns/excel-basico-intermedio-presencial-santiago/meta-ads-quality-test-v2.md`
- `campaigns/excel-basico-intermedio-presencial-santiago/zoho-crm-measurement-v2.md`

## Decisiones registradas

- La campaña v1 generó volumen, pero baja respuesta/contactabilidad.
- El problema principal se interpreta como baja intención del formulario instantáneo, no como falla total de atracción.
- Se mantiene la lógica de 4 anuncios por dolor:
  1. `AD01_DESBORDADO_REPORTE`.
  2. `AD02_DESBORDADO_PLANILLAS`.
  3. `AD03_PRESENCIAL_GUIADO`.
  4. `AD04_REINSERCION_CV`.
- Se corrige la trazabilidad para usar como canónicos los nombres existentes en `creatives-v1`.
- El dolor/persona debe inferirse desde el anuncio cuando sea posible.
- La v2 debe comparar dos rutas:
  - Lead Form filtrado.
  - Click a WhatsApp.
- El filtro fuerte debe moverse a imagen/copy: curso presencial pagado, sin matrícula y Santiago Centro.
- `sin matrícula` no debe usarse aislado; siempre debe ir junto a `curso pagado` o `pagado`.
- Se agrega brief/matriz `creatives-v2` para producir visuales finales sin subir fuentes pesadas ni binarios.
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
- mantenga foco en ads, leads, buyer persona, customer journey y aprendizaje comercial;
- use naming canónico consistente con `creatives-v1`;
- incluya un brief `creatives-v2` suficiente para producir piezas finales sin sugerir gratuidad ni prometer empleo.

## Riesgos o dudas

- Falta confirmar precio vigente.
- Falta confirmar duración vigente.
- Falta confirmar próxima fecha.
- Falta activar/validar medio de pago Meta.
- Falta confirmar política de privacidad de Meta Lead Ads.
- Falta verificar qué campos Zoho Social transfiere realmente a Zoho CRM.
- Falta definir si WhatsApp será manual, Zoho Desk, Zoho CRM, n8n u otro flujo.
- Falta decidir presupuesto por conjunto para comparar Form vs WhatsApp sin sesgo de asignación automática.
- Falta producir/revisar visuales finales v2 a partir del brief.

## Decisión solicitada

- [ ] APROBADO CON OBSERVACIONES
- [ ] CORREGIR ANTES DE MERGE
