# Google Ads Keyword Ideas First Run Log

## Estado

- Fecha de ejecucion local reportada: 2026-07-08.
- Basic Access ya aprobado por Google.
- Ejecucion local read-only exitosa contra `KeywordPlanIdeaService.GenerateKeywordIdeas`.
- Output bruto guardado localmente fuera de versionamiento.
- No se versionan customer IDs completos, tokens, YAML, refresh tokens, OAuth JSON ni TSV bruto.

## Evidencia sanitizada

La ejecucion local mostro:

- `KEYWORD_IDEAS_READY`.
- Columnas disponibles:
  - `keyword_idea_text`;
  - `avg_monthly_searches`;
  - `competition`;
  - `low_top_of_page_bid_micros`;
  - `high_top_of_page_bid_micros`.
- Varias semillas iniciales devolvieron `avg_monthly_searches = 0` y `competition = UNSPECIFIED`.
- Algunas ideas iniciales devolvieron volumen bajo aproximado, por ejemplo 10 busquedas mensuales, sin competencia/bids especificados.

## Lectura comercial inicial

La API quedo validada. El resultado inicial no debe interpretarse todavia como baja demanda real, porque las semillas son muy especificas y el filtro geografico puede estar estrechando demasiado el universo.

Riesgo de lectura equivocada:

- `curso excel presencial santiago` y variantes muy especificas pueden tener bajo volumen aunque exista demanda capturable por terminos mas amplios.
- La demanda puede estar en keywords como `curso excel`, `curso excel online`, `excel basico`, `clases excel`, `capacitacion excel`, `curso power bi`, `power bi curso`, `curso office`, etc.
- El modificador `presencial` puede bajar volumen, pero puede ser util para intencion comercial de sala.

## Siguiente barrido recomendado

Crear un segundo set de semillas por capas:

1. **Alta intencion presencial local**
   - curso excel presencial
   - curso excel santiago
   - curso excel santiago centro
   - curso power bi presencial

2. **Intencion curso sin modalidad**
   - curso excel
   - curso excel basico
   - curso excel intermedio
   - curso excel avanzado
   - curso power bi
   - curso office

3. **Dolor / solucion**
   - aprender excel
   - clases de excel
   - capacitacion excel
   - excel para trabajo
   - excel para empresas

4. **B2B / empresa**
   - capacitacion excel empresas
   - curso excel empresas
   - capacitacion power bi empresas
   - cursos office empresas

## Guardrails

- No ejecutar `export_campaign_summary.py` todavia.
- No subir el TSV bruto.
- No subir outputs con IDs completos.
- No cambiar campanas reales.
- No usar MCP para esta linea.
- No sacar conclusiones de inversion hasta validar geo, semillas y agregacion.