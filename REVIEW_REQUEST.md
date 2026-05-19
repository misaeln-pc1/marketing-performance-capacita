# Solicitud de Revisión (Review Request)

## ¿Qué se hizo?

Se creó un estándar reusable de producción de assets Meta Ads para Capacita y se conectó el brief de Excel Presencial v2 con ese estándar.

## Rama

`docs/meta-asset-production-standard`

## Archivos creados

- `assets/meta-ads/PRODUCTION_STANDARD_META_ADS.md`

## Archivos modificados

- `assets/meta-ads/excel-presencial-santiago/creatives-v2/README.md`
- `TASK_STATUS.md`
- `REVIEW_REQUEST.md`

## Decisiones registradas

- Cada creatividad Meta Ads debe producirse en 3 formatos estáticos obligatorios:
  1. 4:5 - 1080x1350.
  2. 1:1 - 1080x1080.
  3. 9:16 - 1080x1920.
- Cada creatividad debe incluir 1 variante video obligatoria:
  - 9:16.
  - 1080x1920.
  - MP4.
  - H.264.
  - AAC opcional.
  - 10-15 s recomendado.
  - Motion simple desde imagen estática.
- La producción debe partir desde un template maestro con 4 artboards por creatividad.
- No se debe reconstruir cada asset desde cero.
- El repo solo guarda brief, checklist, naming e índice.
- No se suben PSD, Canva, PNG pesados, videos pesados ni fuentes editables.
- Para Excel Presencial v2 se mantiene el sello: `Curso presencial pagado · sin matrícula · Santiago Centro`.
- Para Excel Presencial v2 se mantienen las prohibiciones: no prometer empleo, no sugerir gratuidad y no mezclar B2C con empresa/SENCE/OTIC.

## Revisión solicitada

Validar que el estándar:

- sea reusable para futuras campañas Meta Ads;
- evite rehacer manualmente tamaños y video en cada campaña;
- no cree estructura duplicada dentro del repo;
- mantenga el repo liviano y documental;
- no habilite subida de binarios pesados ni fuentes editables;
- sea suficiente como checklist operativo para producir 3 JPG y 1 MP4 por creatividad.

## Riesgos o dudas

- Falta definir herramienta operativa para el template maestro.
- Falta definir ubicación externa final para masters y exports pesados.
- Falta producir y revisar los assets finales de Excel Presencial v2 usando este estándar.

## Decisión solicitada

- [ ] APROBADO CON OBSERVACIONES
- [ ] CORREGIR ANTES DE MERGE
