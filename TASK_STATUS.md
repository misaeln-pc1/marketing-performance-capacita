# Estado de Tareas

## Estado Actual

- **Estado:** Se documentó un estándar permanente de producción de assets Meta Ads para evitar rehacer manualmente tamaños y variantes de video en cada campaña.
- **Rama actual de trabajo:** `docs/meta-asset-production-standard`.
- **Estándar creado:** `assets/meta-ads/PRODUCTION_STANDARD_META_ADS.md`.
- **Campaña base de referencia:** Excel Básico-Intermedio Presencial Santiago Centro.
- **Anuncios canónicos Excel v2:** `AD01_DESBORDADO_REPORTE`, `AD02_DESBORDADO_PLANILLAS`, `AD03_PRESENCIAL_GUIADO`, `AD04_REINSERCION_CV`.

## Registro de Actividad

- **Última acción previa:** Se documentó aprendizaje v1, estrategia de calidad v2 y brief `creatives-v2` para Excel Presencial Santiago.
- **Problema operativo detectado:** Cada creatividad necesita múltiples tamaños y una variante de video vertical, lo que generaba fricción si se resolvía manualmente campaña por campaña.
- **Decisión operativa:** Crear un estándar reusable para Meta Ads con 3 tamaños estáticos obligatorios y 1 video 9:16 obligatorio por creatividad.
- **Regla de producción:** Trabajar desde un template maestro con 4 artboards por creatividad: 4:5, 1:1, 9:16 y video 9:16. No reconstruir cada asset desde cero.
- **Regla de repo:** El repo guarda brief, checklist, naming e índice; no guarda PSD, Canva, PNG pesados, videos pesados ni fuentes editables.
- **Actualización Excel v2:** El brief `creatives-v2` queda enlazado al estándar y mantiene el sello: curso presencial pagado, sin matrícula y Santiago Centro.

## Próxima Acción Recomendada

Aplicar el estándar al producir visuales finales de Excel Presencial v2:

1. Crear template maestro fuera del repo.
2. Producir 4 artboards por anuncio/dolor.
3. Exportar 3 JPG estáticos y 1 MP4 vertical por creatividad.
4. Revisar legibilidad móvil y cortes en placements antes de cargar en Meta Ads.

## Pendientes / Bloqueos

- Confirmar herramienta operativa para templates maestros y exports fuera del repo.
- Confirmar ubicación externa para masters y exports pesados.
- Producir/revisar visuales finales v2 desde el brief y el estándar.
- Mantener pendientes de campaña: precio, fecha, duración, política de privacidad, campos Zoho Social y flujo WhatsApp.

## Notas de Alcance

- No crear estructura duplicada de campaña.
- No subir assets binarios pesados.
- No subir datos reales de leads.
- No subir capturas, exportaciones CRM, secretos ni credenciales.
- No modificar campañas reales desde el repositorio.
