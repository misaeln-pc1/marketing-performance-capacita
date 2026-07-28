# Production Standard Meta Ads — Capacita

Fecha de normalizacion: 2026-07-28  
Origen rescatado: PR #8, creado el 2026-05-20  
Estado: `STANDARD_DOCUMENTAL_VIGENTE_SI_SE_MERGEA_PR_LIMPIO`

## Objetivo

Definir el estandar minimo y reutilizable para producir creatividades de Meta Ads de Capacita sin rehacer manualmente tamanos, formatos ni videos por campana.

Este archivo aplica a campanas Meta Ads / Facebook Ads / Instagram Ads del repo `marketing-performance-capacita`.

La finalidad inmediata es evitar errores de formato, recortes, baja legibilidad movil y rechazos por asignar una pieza a placements incompatibles.

## Principio operativo

Cada creatividad debe tratarse como un sistema de piezas por placement, no como una imagen o video unico.

GitHub guarda documentacion, naming, checklist, matriz, estado e indice de ubicacion externa. Los archivos reales de imagen, video y editables viven fuera del repo, en la bodega externa del proyecto o SharePoint/OneDrive.

## Entregables minimos por creatividad

### Imagenes estaticas

Cada creatividad final debe producirse en estos tres formatos:

| Uso | Relacion | Tamano |
|---|---:|---:|
| Feed principal | 4:5 | 1080x1350 |
| Cuadrado / respaldo | 1:1 | 1080x1080 |
| Stories / Reels | 9:16 | 1080x1920 |

### Videos

No usar un unico video 9:16 para todos los placements.

Cada creatividad con video debe producirse en estos formatos:

| Uso | Relacion | Tamano | Formato |
|---|---:|---:|---|
| Stories / Reels | 9:16 | 1080x1920 | MP4 |
| Feed, si se activa Instagram/Facebook Feed | 4:5 | 1080x1350 | MP4 |

Regla critica:

- Video 9:16: usar solo para Stories/Reels o placements verticales compatibles.
- Video 4:5: usar para Feed cuando el video vaya a publicarse en Instagram/Facebook Feed.
- Si Meta rechaza el video por relacion de aspecto, no forzar el placement: corregir formato o separar ubicaciones.
- No producir una sola pieza y confiar en que Meta la adapte correctamente para todos los placements.

## Motion recomendado para video desde imagen estatica

Cuando no exista video real, generar MP4 desde la imagen estatica con motion simple:

- duracion ideal: 10 a 15 segundos;
- movimiento suave de zoom o paneo;
- aparicion limpia de titular, sello y CTA;
- sin cambios de color que degraden la marca;
- sin recortes agresivos;
- sin padding artificial para forzar una relacion de aspecto;
- mantener legibilidad movil;
- exportar en MP4, preferentemente H.264.

## Checklist por creatividad

Por cada anuncio o dolor se debe confirmar:

- [ ] Imagen 4:5 — 1080x1350.
- [ ] Imagen 1:1 — 1080x1080.
- [ ] Imagen 9:16 — 1080x1920.
- [ ] Video 9:16 — 1080x1920 para Stories/Reels.
- [ ] Video 4:5 — 1080x1350 para Feed si se activa placement Feed.
- [ ] Texto legible en movil.
- [ ] CTA visible.
- [ ] Sello o respaldo institucional visible solo si aplica al brief.
- [ ] Sin datos personales reales.
- [ ] Sin promesas prohibidas o ambiguas.
- [ ] Sin mezcla de publicos fuera del alcance de la campana.
- [ ] Previsualizacion en Ads Manager antes de publicar.

## Regla de assets pesados

No subir a GitHub imagenes, videos ni editables reales, aunque sean finales.

Prohibido subir al repo:

- JPG, PNG, WEBP finales o fuente;
- MP4, MOV o videos exportados;
- PSD, AI, Canva u otros editables;
- fuentes;
- capturas con datos personales;
- exportaciones pesadas;
- previews sensibles.

Permitido en GitHub:

- brief;
- matriz creativa;
- checklist;
- naming;
- estado;
- indice de ubicacion externa;
- rutas relativas no sensibles;
- hashes de control cuando aplique.

## Estructura externa sugerida

Usar bodega externa del proyecto:

```text
external-files/marketing-performance-capacita/meta-ads/[campana]/[version]/
  masters/
  exports-static/4x5/
  exports-static/1x1/
  exports-static/9x16/
  exports-video/4x5/
  exports-video/9x16/
  preview/
```

Si el archivo vive en SharePoint/OneDrive, registrar en el documento de campana o manifest:

- nombre del archivo;
- ruta externa;
- hash si existe;
- tamano;
- sensibilidad;
- origen;
- version;
- estado.

## Naming recomendado

Usar nombres consistentes por campana, anuncio, version y formato.

Ejemplo:

```text
meta_excel_v2_AD01_REPORTE_4x5_1080x1350.jpg
meta_excel_v2_AD01_REPORTE_1x1_1080x1080.jpg
meta_excel_v2_AD01_REPORTE_9x16_1080x1920.jpg
meta_excel_v2_AD01_REPORTE_video_4x5_1080x1350.mp4
meta_excel_v2_AD01_REPORTE_video_9x16_1080x1920.mp4
```

Campos minimos recomendados:

```text
meta_[curso]_[campana]_[ad-id]_[concepto]_[formato]_[tamano].[ext]
```

## Validacion minima antes de publicar

Antes de publicar en Meta Ads Manager:

1. Revisar cada formato en vista movil.
2. Confirmar que textos no se cortan en Feed, Stories ni Reels.
3. Confirmar que el video 9:16 no se asigna a Feed si Meta lo rechaza.
4. Confirmar que existe video 4:5 si se quiere publicar video en Feed.
5. Confirmar que el repo solo contiene documentacion e indice, no binarios pesados.
6. Confirmar que la creatividad coincide con la landing y el objetivo de campana.
7. Confirmar que el routing de cuenta publicitaria se obtiene desde el documento vigente `docs/meta-ads/META_ADS_ACCOUNT_ROUTING.md`, no desde supuestos de portafolio.

## Aplicacion a campanas B2C Capacita

En campanas B2C:

- no mezclar empresa, SENCE, OTIC ni franquicia tributaria salvo instruccion expresa;
- no prometer empleo;
- no prometer gratuidad;
- no prometer resultados garantizados;
- si el curso es pagado, el sello o descripcion debe evitar ambiguedad sobre gratuidad;
- si se usa `sin matricula`, acompanarlo con `curso pagado` o equivalente;
- separar B2C y B2B en campana, landing y medicion;
- mantener un buyer persona primario y una hipotesis por prueba.

## Relacion con routing Meta Ads

Este estandar define produccion de creatividades y formatos.

No define:

- cuenta publicitaria;
- business portfolio;
- permisos;
- API;
- export de metricas;
- activacion de campanas;
- presupuesto;
- pujas.

La cuenta/ruta operativa Meta Ads se documenta en:

```text
docs/meta-ads/META_ADS_ACCOUNT_ROUTING.md
```

## Estado de decision

Este documento rescata y actualiza el contenido util de PR #8. PR #8 no debe mergearse como rama antigua; debe quedar como antecedente historico cuando este estandar limpio quede vigente en `main`.