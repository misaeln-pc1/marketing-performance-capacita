# Google Ads Historical Diagnosis Contract V01

## Proposito

Definir el siguiente paso seguro despues del radar Keyword Ideas V0: construir historial real de Google Ads para diagnosticar gasto, clics, terminos de busqueda, landing, conversiones y calidad post-click.

## Problema comercial observado

El usuario reporto un caso reciente aproximado:

- gasto diario cercano a CLP $20.000;
- 16 a 18 clics;
- 0 a 2 leads aproximados;
- percepcion de alza en tasa/costo post-click;
- sospecha de mezcla entre keywords, landing e intencion de busqueda.

Esto no se puede resolver solo con Keyword Ideas. Se requiere historial real.

## Hipotesis a validar

1. Keywords demasiado amplias consumen presupuesto sin lead.
2. Terminos `gratis`, `online`, `sena`, plantillas u otros pueden activar anuncios no alineados con sala presencial.
3. La landing puede no coincidir con la intencion real de busqueda.
4. Puede requerirse separar landing por intencion:
   - Excel basico desde cero;
   - Excel presencial Santiago Centro;
   - Excel empresas;
   - Excel certificado.
5. Puede haber problema de concordancia, negativas insuficientes o Quality Score bajo.
6. Puede haber clics moviles de baja calidad o mala trazabilidad hacia Zoho CRM.

## Reporte historico read-only requerido

El reporte debe obtenerse solo en modo lectura, con salida local no versionada.

Columnas minimas deseadas:

- fecha;
- campaign name;
- ad group name;
- keyword text;
- search term;
- match type;
- final URL o landing;
- device;
- network;
- impressions;
- clicks;
- CTR;
- cost;
- average CPC;
- conversions;
- conversion rate;
- cost per conversion;
- quality score si esta disponible;
- campaign status;
- ad group status;
- keyword status.

## Preguntas que debe responder

1. Que terminos reales estan consumiendo presupuesto.
2. Que keywords generan clics sin conversion.
3. Que search terms tienen alta friccion o mala intencion.
4. Que landing recibe los clics caros.
5. Si hay diferencias fuertes por dispositivo.
6. Si hay diferencia entre keywords generales y keywords presenciales.
7. Que negativas iniciales son evidentes.
8. Si se justifica separar landing por intencion.

## Guardrails

- No ejecutar cambios en campanas reales.
- No activar, pausar ni editar anuncios.
- No modificar presupuestos ni bids.
- No subir exports brutos.
- No subir customer IDs completos.
- No subir datos personales ni CRM.
- No ejecutar `export_campaign_summary.py` hasta aprobar contrato tecnico GAQL.
- No usar MCP.

## Salida versionable permitida

Solo se permite versionar resumen agregado y sanitizado, por ejemplo:

- top terminos por costo sin conversion;
- grupos de intencion;
- negativas candidatas;
- recomendaciones de landing;
- estructura propuesta de grupos de anuncios;
- supuestos y limites.

No versionar CSV/TSV bruto.

## Siguiente accion

Preparar PR tecnico-documental para habilitar un script read-only de export historico, o un runbook local equivalente, con GAQL aprobado antes de ejecucion.