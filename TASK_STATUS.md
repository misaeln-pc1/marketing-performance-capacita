# Estado de Tareas

Fecha de revisión: 2026-07-10

## Estado actual

- **Estado:** paquete de briefs por buyer persona preparado para revisión.
- **Issue dueño:** [#21](https://github.com/misaeln-pc1/marketing-performance-capacita/issues/21).
- **Rama:** `docs/marketing-buyer-persona-briefs-v1`.
- **Contrato Marketing → GTM:** mergeado mediante PR #20.
- **Canónico GTM:** Global PR #88 mergeado.
- **Oferta base:** Excel presencial Santiago.

## Resultado preparado

Se creó `campaigns/excel-basico-intermedio-presencial-santiago/briefs/` con:

- `README.md`: índice, separación B2C/B2B y orden recomendado;
- `BRIEF_BP001_DESBORDADO_OPERATIVO_V1.md`;
- `BRIEF_BP002_REINSERCION_LABORAL_V1.md`;
- `BRIEF_BP003_COORDINADOR_B2B_V1.md`;
- `BRIEF_BP004_JEFATURA_PYME_V1.md`.

`BP-000` permanece como salida de control para evidencia insuficiente y no se utiliza como audiencia de campaña.

## Preparación por brief

| Brief | Estado | Próxima acción |
|---|---|---|
| `BP-001 — Desbordado Operativo` | Listo para desarrollo creativo B2C | Confirmar oferta, producir pieza y validar tracking. |
| `BP-002 — Reinserción Laboral` | Listo para desarrollo creativo B2C | Confirmar nivel/diploma, producir pieza y validar claims. |
| `BP-003 — Coordinador B2B` | Listo documentalmente | Confirmar landing, formulario, oferta grupal, SLA y cotización. |
| `BP-004 — Dueño o Jefatura PyME` | Listo documentalmente | Confirmar oferta B2B, diagnóstico comercial, landing y pipeline. |

## Regla operativa vigente

Cada experimento debe:

1. tener un buyer persona primario;
2. conservar ID y versión GTM;
3. separar B2C y B2B;
4. definir una hipótesis principal;
5. mantener constantes oferta y landing cuando se quiera comparar mensajes;
6. medir hasta calidad comercial, cotización o matrícula;
7. devolver evidencia agregada a GTM sin redefinir el canónico desde Marketing.

## Orden recomendado para comenzar

1. `BP-001`: productividad, errores y autonomía en el trabajo actual.
2. `BP-002`: actualización de competencias y confianza laboral.
3. `BP-003`: coordinación de capacitación para equipos.
4. `BP-004`: decisión empresarial e impacto operativo.

No activar conjuntamente los cuatro briefs. El paquete entrega opciones disponibles; la ejecución debe seleccionar un brief y una hipótesis por prueba.

## Próxima acción después del merge

1. Seleccionar `BP-001` como primer desarrollo creativo recomendado.
2. Confirmar fecha, precio, cupos, nivel, equipamiento, materiales y condiciones.
3. Preparar un solo concepto creativo y sus formatos necesarios.
4. Validar landing, UTM, formulario/WhatsApp y entrada a Zoho.
5. Solicitar autorización antes de modificar o activar campañas reales.
6. Preparar `BP-002` como segunda prueba manteniendo oferta y destino constantes cuando sea viable.

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

- Confirmar fecha, precio, cupos y oferta vigente antes de publicar.
- Confirmar medición de clics internos, formularios y WhatsApp en la landing.
- Confirmar trazabilidad UTM hacia Zoho CRM.
- No existe todavía unión completa Ads → landing → CRM → matrícula para CPQL/CPA real.
- Los briefs B2B no deben activarse sin landing/ruta empresarial y proceso de cotización.
- `BP-003` y `BP-004` siguen con madurez de evidencia `hypothesis`.
- No hay evidencia suficiente para cambiar buyer personas canónicos.
- Los campos y workflows Zoho deben definirse posteriormente en `Capacita-Zoho-Deluge-Core`.
- La skill draft de buyer-persona signals en AI OS sigue pendiente de corrección antes de uso.

## Límites

- No trabajar directo en `main`.
- No crear campañas duplicadas.
- No mezclar B2C/B2B en una campaña o medición común.
- No subir PII, exports, capturas sensibles, secretos, credenciales o binarios.
- No modificar campañas, presupuesto, bids, anuncios, landing, CRM o producción desde documentación.
- No inventar métricas, IDs GTM, API names o resultados.
- No garantizar empleo, productividad, ahorro, ROI o eliminación de errores.
