# Google Ads History Diagnosis Contract V0.1

## Objetivo

Construir un historial read-only de Google Ads para diagnosticar por que hay gasto y clicks sin leads suficientes, antes de modificar campanas reales.

Problema observado:

- Gasto diario reportado cercano a CLP $20.000.
- Clicks diarios reportados aprox. 16-18.
- Leads recibidos: 0-2 aprox.
- Sospecha: mezcla de intenciones, keywords amplias mal filtradas, landing no alineada, baja calidad post-click o competencia/CPC alto.

## Decision

No tomar decisiones solo con Keyword Planner / Keyword Ideas.

El siguiente diagnostico debe usar historico real de Google Ads, separado por:

1. terminos de busqueda reales;
2. keywords compradas;
3. campanas y grupos;
4. landing/final URLs;
5. dispositivo;
6. fecha;
7. costo, clicks, CTR, CPC y conversiones cuando existan.

## Fuentes Google Ads API permitidas

Solo consultas read-only mediante GAQL:

- `search_term_view` para terminos reales buscados por usuarios.
- `keyword_view` para rendimiento de keywords compradas.
- `expanded_landing_page_view` para rendimiento por URL final.
- `campaign` para resumen diario por campana.

## Campos minimos del diagnostico

### Search terms

- fecha;
- campana;
- grupo de anuncio;
- termino de busqueda;
- estado del termino;
- impresiones;
- clicks;
- CTR;
- CPC promedio;
- costo;
- conversiones;
- tasa de conversion.

### Keywords

- fecha;
- campana;
- grupo de anuncio;
- keyword;
- tipo de concordancia;
- estado;
- impresiones;
- clicks;
- CTR;
- CPC promedio;
- costo;
- conversiones;
- tasa de conversion.

### Landing pages

- fecha;
- URL final expandida;
- impresiones;
- clicks;
- CTR;
- CPC promedio;
- costo;
- conversiones;
- tasa de conversion.

### Campaign daily

- fecha;
- campana;
- canal;
- impresiones;
- clicks;
- CTR;
- CPC promedio;
- costo;
- conversiones;
- tasa de conversion.

## Salidas locales esperadas

Los CSV brutos deben quedar solo en local, no versionados:

- `automation/google-ads-readonly/output/google_ads_history/search_terms.csv`
- `automation/google-ads-readonly/output/google_ads_history/keywords.csv`
- `automation/google-ads-readonly/output/google_ads_history/landing_pages.csv`
- `automation/google-ads-readonly/output/google_ads_history/campaign_daily.csv`

## Analisis comercial posterior

Con esos archivos, construir resumen agregado:

- top gasto sin conversion;
- top clicks sin conversion;
- terminos basura para negativas;
- keywords caras sin lead;
- keywords buenas con costo razonable;
- landing con gasto alto y conversion baja;
- separacion recomendada por landing / grupo de anuncio;
- decision: pausar, negativizar, separar landing, ajustar copy o mantener.

## Hipotesis a validar

1. **Keyword demasiado amplia:** clicks llegan por personas que buscan gratis/online/general y no curso presencial pagado.
2. **Landing no alineada:** el anuncio promete una intencion y la landing mezcla otra.
3. **Grupo de anuncios mezclado:** keywords de distintas intenciones llevan a la misma landing/copy.
4. **CPC alto por competencia:** costo alto pero sin conversion por baja calidad post-click.
5. **Tracking incompleto:** puede haber leads no atribuidos si Zoho/formulario/UTM no esta bien conectado.
6. **Presencial como filtro tardio:** Google captura busqueda general, pero el usuario descubre tarde que es presencial o pagado.

## Guardrails

- No modificar campanas reales.
- No cambiar presupuestos.
- No cambiar bids.
- No crear ni pausar keywords.
- No subir CSV brutos.
- No subir IDs completos.
- No subir nombres de leads ni PII.
- No subir `google-ads.yaml`, token, OAuth JSON, refresh token ni access token.
- No usar MCP para esta linea.

## Criterio de exito

El diagnostico es exitoso si permite responder:

1. que terminos consumen plata;
2. que keywords compradas activan esos terminos;
3. que landing recibe esos clicks;
4. que gasto no convierte;
5. que negativas son obvias;
6. que separacion por landing/grupo tiene sentido;
7. que prueba Search conviene hacer sin aumentar riesgo de gasto.