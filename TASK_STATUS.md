# Estado de Tareas

Fecha de revisión: 2026-07-10

## Estado actual

- **Estado:** alineación operativa Marketing → GTM en ejecución documental.
- **Issue dueño:** [#19](https://github.com/misaeln-pc1/marketing-performance-capacita/issues/19).
- **Rama:** `docs/marketing-gtm-consumption-pilot-v1`.
- **Canónico GTM disponible:** Global PR #88 mergeado.
- **Campaña piloto:** `META_TRAFFIC_EXCEL_PRESENCIAL_SANTIAGO_B2C_V3`.
- **Landing asociada:** `https://capacita.cl/curso-de-excel-presencial-en-santiago`.

## Resultado preparado

- Se creó `docs/GTM_CONSUMPTION_BRIDGE.md`.
- Se creó `templates/CAMPAIGN_BRIEF_GTM.md`.
- Se alinearon README, contexto y carpetas para que Marketing no sea fuente canónica de buyer personas, journey o propuesta de valor.
- Se aplicó el contrato a la campaña Excel V3 en `campaigns/excel-basico-intermedio-presencial-santiago/gtm-baseline-v1.md`.
- Se registró `BP-001` como perfil primario y `BP-002` como secundario para el antecedente V3.
- Se detectó que el copy V3 mezcla ambos perfiles; futuros tests deberían separar productividad y empleabilidad para obtener aprendizaje interpretable.
- No se modificaron campañas, landing, CRM, tracking o producción.

## Regla operativa vigente

Cada campaña nueva o revisada debe:

1. registrar IDs/versiones GTM o documento/sección/versión;
2. separar baseline corporativo de hipótesis táctica;
3. definir público, copy, CTA, destino y medición;
4. documentar claims y datos tácticos por confirmar;
5. devolver evidencia agregada a GTM cuando pueda cambiar el canónico.

## Próxima acción recomendada

Después del merge de este PR:

1. usar `templates/CAMPAIGN_BRIEF_GTM.md` para el siguiente trabajo real de Marketing;
2. definir si el primer test nuevo será:
   - variante `BP-001` productividad;
   - variante `BP-002` empleabilidad;
3. mantener oferta y landing constantes si se quiere aislar el efecto del mensaje;
4. confirmar fecha, precio, cupos, equipamiento y condiciones antes de publicar;
5. ejecutar cualquier cambio real de campaña solo con aprobación explícita.

## Google Ads read-only

Estado preservado:

- Basic Access aprobado.
- `list_accessible_customers.py` validó dos cuentas accesibles enmascaradas.
- `generate_keyword_ideas.py` funcionó en modo read-only y dejó output local no versionado.
- El primer barrido usó semillas demasiado específicas; no permite concluir baja demanda.
- `export_campaign_summary.py` permanece bloqueado hasta aprobar contrato de reporte.

Próxima acción de esa línea:

1. segundo barrido con semillas más amplias;
2. validar geografía;
3. separar presencial/local, curso general, dolor/solución y B2B;
4. documentar solo resumen agregado y anónimo;
5. mantener outputs, credenciales e IDs completos fuera del repo.

## Pendientes y bloqueos

- Confirmar fecha, precio y cupos vigentes antes de publicar.
- Confirmar medición de clics internos, formularios y WhatsApp en la landing.
- Confirmar trazabilidad UTM hacia Zoho CRM.
- No existe todavía unión completa Ads → landing → CRM → matrícula para CPQL/CPA real.
- No hay evidencia suficiente para cambiar los buyer personas canónicos.
- Los campos y workflows Zoho deben definirse posteriormente en `Capacita-Zoho-Deluge-Core`.
- La skill draft de buyer-persona signals en AI OS sigue pendiente de corrección antes de uso.

## Límites

- No trabajar directo en `main`.
- No crear campañas duplicadas.
- No subir PII, exports, capturas sensibles, secretos, credenciales o binarios.
- No modificar campañas, presupuesto, bids, anuncios, landing, CRM o producción desde documentación.
- No inventar métricas, IDs GTM, API names o resultados.
- No copiar canónicos completos cuando basta una referencia versionada.