# Production Standard Meta Ads — Capacita

## Objetivo

Definir el estándar mínimo y reutilizable para producir creatividades de Meta Ads de Capacita sin rehacer manualmente tamaños, formatos ni videos por campaña.

Este archivo aplica a campañas Meta Ads / Facebook Ads / Instagram Ads del repo `marketing-performance-capacita`.

## Principio operativo

Cada creatividad debe tratarse como un sistema de piezas por placement, no como una imagen suelta.

GitHub guarda documentación, naming, checklist, matriz, estado e índice de ubicación. Los archivos reales de imagen/video/editables viven fuera del repo, preferentemente en Drive/local respaldado.

## Entregables mínimos por creatividad

### Imágenes estáticas

Cada creatividad final debe producirse en estos tres formatos:

| Uso | Relación | Tamaño |
|---|---:|---:|
| Feed principal | 4:5 | 1080x1350 |
| Cuadrado / respaldo | 1:1 | 1080x1080 |
| Stories / Reels | 9:16 | 1080x1920 |

### Videos

No usar un único video 9:16 para todos los placements.

Cada creatividad con video debe producirse en estos formatos:

| Uso | Relación | Tamaño | Formato |
|---|---:|---:|---|
| Stories / Reels | 9:16 | 1080x1920 | MP4 |
| Feed, si se activa Instagram/Facebook Feed | 4:5 | 1080x1350 | MP4 |

Regla crítica:

- Video 9:16: usar solo para Stories/Reels o placements verticales compatibles.
- Video 4:5: usar para Feed cuando el video vaya a publicarse en Instagram/Facebook Feed.
- Si Meta rechaza el video por relación de aspecto, no forzar el placement: corregir formato o separar ubicaciones.

## Motion recomendado para video desde imagen estática

Cuando no exista video real, generar MP4 desde la imagen estática con motion simple:

- duración ideal: 10–15 segundos;
- movimiento suave de zoom o paneo;
- aparición limpia de titular/sello/CTA;
- sin cambios de color, recortes agresivos ni padding artificial;
- mantener legibilidad móvil;
- exportar en MP4, preferentemente H.264.

## Checklist por creatividad

Por cada anuncio o dolor se debe confirmar:

- [ ] Imagen 4:5 — 1080x1350.
- [ ] Imagen 1:1 — 1080x1080.
- [ ] Imagen 9:16 — 1080x1920.
- [ ] Video 9:16 — 1080x1920 para Stories/Reels.
- [ ] Video 4:5 — 1080x1350 para Feed si se activa placement Feed.
- [ ] Texto legible en móvil.
- [ ] Sello visible definido en el brief de campaña.
- [ ] Sin datos personales reales.
- [ ] Sin promesas prohibidas o ambiguas.
- [ ] Sin mezcla de públicos fuera del alcance de la campaña.
- [ ] Previsualización en Ads Manager antes de publicar.

## Regla de assets pesados

No subir a GitHub imágenes ni videos reales, aunque sean finales.

Prohibido subir al repo:

- JPG, PNG, WEBP finales o fuente;
- MP4, MOV o videos exportados;
- PSD, AI, Canva u otros editables;
- fuentes;
- capturas con datos personales;
- exportaciones pesadas.

Permitido en GitHub:

- brief;
- matriz creativa;
- checklist;
- naming;
- estado;
- índice de ubicación en Drive/local.

## Estructura sugerida fuera del repo

Mantener los archivos reales fuera del repo, por ejemplo:

```text
/meta-ads/[campaña]/[versión]/
  masters/
  exports-static/4x5/
  exports-static/1x1/
  exports-static/9x16/
  exports-video/4x5/
  exports-video/9x16/
  preview/
```

## Naming recomendado

Usar nombres consistentes por campaña, anuncio, versión y formato.

Ejemplo:

```text
meta_excel_v2_AD01_REPORTE_4x5_1080x1350.jpg
meta_excel_v2_AD01_REPORTE_1x1_1080x1080.jpg
meta_excel_v2_AD01_REPORTE_9x16_1080x1920.jpg
meta_excel_v2_AD01_REPORTE_video_4x5_1080x1350.mp4
meta_excel_v2_AD01_REPORTE_video_9x16_1080x1920.mp4
```

## Validación mínima antes de publicar

Antes de publicar en Meta Ads Manager:

1. Revisar cada formato en vista móvil.
2. Confirmar que textos no se cortan en Feed, Stories ni Reels.
3. Confirmar que el video 9:16 no se asigna a Feed si Meta lo rechaza.
4. Confirmar que existe video 4:5 si se quiere publicar video en Feed.
5. Confirmar que el repo solo contiene documentación e índice, no binarios pesados.

## Aplicación a campañas B2C Capacita

En campañas B2C:

- no mezclar empresa, SENCE, OTIC ni franquicia tributaria salvo instrucción expresa;
- no prometer empleo, gratuidad ni resultados garantizados;
- si el curso es pagado, el sello o descripción debe evitar ambigüedad sobre gratuidad;
- si se usa “sin matrícula”, acompañarlo con “curso pagado” o equivalente.
