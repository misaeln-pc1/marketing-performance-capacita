# Estándar de producción de assets Meta Ads

## Objetivo

Evitar rehacer manualmente tamaños y variantes de video en cada campaña. Cada creatividad debe producirse desde un template maestro y exportarse en los formatos mínimos necesarios para Meta Ads.

## Tamaños estáticos obligatorios

Por cada creatividad aprobada, producir:

| Formato | Tamaño | Uso |
|---|---:|---|
| 4:5 | 1080x1350 px | Feed principal y placements verticales controlados |
| 1:1 | 1080x1080 px | Feed cuadrado y variantes de compatibilidad |
| 9:16 | 1080x1920 px | Stories, Reels y placements verticales full screen |

## Variante video obligatoria

Por cada creatividad aprobada, producir una variante de video:

- Formato: 9:16.
- Resolución: 1080x1920 px.
- Archivo final: MP4.
- Codec video: H.264.
- Audio: AAC opcional.
- Duración recomendada: 10-15 s.
- Movimiento: motion simple desde imagen estática.

El video no debe cambiar la promesa, el dolor ni la oferta del asset estático. Solo debe agregar movimiento básico para adaptar la pieza a placements de video.

## Regla de producción

- Trabajar desde un template maestro por campaña o línea creativa.
- Crear 4 artboards por creatividad:
  - 4:5.
  - 1:1.
  - 9:16.
  - video 9:16.
- No reconstruir cada asset desde cero.
- Mantener el mismo titular, sello/filtro visual y criterio de cumplimiento entre variantes.
- Ajustar composición por formato para evitar cortes de texto, rostros, sellos o llamadas visuales importantes.

## Regla de repo

Este repositorio solo guarda:

- brief;
- checklist;
- naming;
- índice;
- criterios de cumplimiento;
- referencias a ubicación externa si corresponde.

No subir al repo:

- PSD;
- Canva;
- PNG pesados;
- videos pesados;
- fuentes editables;
- archivos de trabajo;
- duplicados de exports.

Las fuentes, masters y exports finales pesados deben quedar fuera del repo, preferentemente en Drive u otra ubicación operativa definida por el equipo.

## Estructura recomendada fuera del repo

Usar una estructura simple para masters y exports:

```text
/masters/
/exports-static/4x5/
/exports-static/1x1/
/exports-static/9x16/
/exports-video/9x16/
```

## Excel Presencial v2

Para Excel Presencial Santiago v2, mantener el sello:

> Curso presencial pagado · sin matrícula · Santiago Centro

Prohibiciones específicas:

- No prometer empleo.
- No sugerir gratuidad.
- No mezclar B2C con empresa/SENCE/OTIC.

## Checklist de salida por creatividad

Cada creatividad debe tener:

- 1 JPG 4:5.
- 1 JPG 1:1.
- 1 JPG 9:16.
- 1 MP4 9:16.

## Prueba mínima

Antes de publicar o entregar a carga en Meta Ads:

- Revisar visualmente en móvil.
- Revisar cortes en placements.
- Confirmar legibilidad de titular y sello.
- Confirmar que no haya datos personales reales.
- Confirmar que no haya promesas no permitidas ni señales de gratuidad.
