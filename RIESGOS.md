# Riesgos — Marketing Performance Capacita

Registro mínimo de riesgos transversales. Los riesgos específicos permanecen en el documento/campaña dueña; este archivo no los duplica.

## Estado — 2026-09-05

| ID | Riesgo | Semáforo | Control mínimo | Estado |
|---|---|---:|---|---|
| MKT-R01 | Recomendaciones genéricas o reactivas sin consultar datos disponibles | Amarillo | aplicar `MARKETING_PROACTIVE_OPPORTUNITY_SCAN_V01.md`; exigir evidencia o `DATA_GAP` y `NEXT_BEST_ACTION` | mitigación propuesta en rama |
| MKT-R02 | Confundir conversión Ads o clic con lead, Deal, matrícula o venta | Amarillo | separar capas Ads/web/CRM/pipeline/operación/comercial | vigente |
| MKT-R03 | Tratar clic en CTA como prueba del dolor o buyer persona real | Amarillo | registrar `pain_signal` y `bp_hypothesis` como señales; validar con comportamiento/downstream | mitigación propuesta |
| MKT-R04 | Proliferación de categorías, eventos y campos difíciles de mantener | Amarillo | limitar a 3–5 pain signals por oferta/familia; IDs versionados; reuse antes de crear | mitigación propuesta |
| MKT-R05 | Herramienta conectada con capacidad WRITE usada por inferencia | Rojo | READ por defecto; nuevo OAuth/scope, writes, costos y producción requieren autorización | control obligatorio |
| MKT-R06 | Datos personales, secretos, IDs completos o exports crudos en GitHub | Rojo | sólo agregados sanitizados; pesados/sensibles en SharePoint canónico | control obligatorio |
| MKT-R07 | Repo público expone estrategia, performance o aprendizaje comercial sensible | Amarillo | revisión separada de visibilidad y clasificación; no cambiar permisos sin decisión explícita | pendiente de decisión |
| MKT-R08 | Estado fragmentado entre `main`, instrucciones, issues y PRs abiertos | Amarillo | Bootstrap/Delta; canónico por frente; no asumir PR abierto como vigente; consolidar #60/#62 | abierto |
| MKT-R09 | Landings hermanas demasiado parecidas o, al corregir, pérdida de coherencia de marca | Amarillo | matriz de diferenciación controlada; misma familia, activo/mensaje/ejemplo propio | mitigación propuesta |
| MKT-R10 | Sobreanálisis, exceso de herramientas o demora en publicar/aprender | Amarillo | consultar sólo fuentes pertinentes; detener por bajo beneficio marginal; prueba mínima reversible | control obligatorio |
| MKT-R11 | Recomendación de keywords negativas elimina intención válida | Amarillo | aplicar política canónica de intención y diferenciar Ads de SEO/canibalización | vigente |
| MKT-R12 | Dependencia de planes, conectores o herramientas no disponibles | Verde/Amarillo | registrar `NO_ACCESS/PLAN_LIMIT`; mantener fallback validado; no inventar datos | vigente |

## Riesgo de visibilidad del repositorio

Hecho verificado: este repositorio es público. La gobernanza Global recomienda repos privados para estrategia, CRM y datos comerciales. No se cambia la visibilidad desde este trabajo porque implica permisos/administración y requiere decisión explícita.

Criterio de revisión:

- mantener públicos sólo procedimientos, plantillas y evidencia sanitizada que no revele ventaja comercial material;
- no versionar performance granular, nombres/IDs sensibles, audiencias privadas, exports o decisiones de precio no públicas;
- evaluar migración a privado por separado, con impacto en integraciones, enlaces y acceso.

## Regla de escalamiento

- **Verde:** lectura, documentación y análisis sanitizado/reversible.
- **Amarillo:** datos agregados, tracking, assets, XFER, SharePoint o estrategia que condiciona inversión.
- **Rojo:** PII, secretos, permisos, writes, campañas/presupuestos reales, producción, pagos, borrado/renombrado o merge/main.

Un riesgo rojo bloquea la acción externa, no el análisis ni la preparación documental segura.
