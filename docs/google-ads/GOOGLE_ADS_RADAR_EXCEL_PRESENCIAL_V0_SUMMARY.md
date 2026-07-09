# Google Ads Radar Excel Presencial V0 Summary

## Estado

- Radar local generado desde `generate_keyword_ideas.py` usando Google Ads API Basic Access.
- Output bruto local no versionado: `automation/google-ads-readonly/output/keyword_ideas_presencial_santiago.tsv`.
- Radar local no versionado: `automation/google-ads-readonly/output/radar_keyword_ideas_presencial_santiago_v01.csv`.
- Filas procesadas localmente: 1676.
- No se versionan archivos TSV/CSV de salida, customer IDs completos, tokens, YAML ni credenciales.

## Lectura comercial inicial

El radar confirma demanda capturable para Excel, pero la demanda estrictamente presencial/local aparece baja en volumen mensual cuando se usa como keyword exacta o muy especifica.

La estrategia inicial no debe depender solo de keywords con `presencial` o `santiago`. Conviene capturar demanda general de Excel y filtrar en anuncio/landing con propuesta presencial.

## Top senales sanitizadas observadas

| Keyword / idea | Busquedas mensuales aprox. | Competencia | Lectura |
|---|---:|---|---|
| curso de excel | 40 | MEDIUM | Mejor semilla general inicial. |
| excel basico | 30 | MEDIUM | Buena entrada para publico principiante. |
| excel desde cero | 20 | LOW | Buena entrada B2C / reinsercion / desbordado operativo. |
| curso de excel desde cero | 20 | MEDIUM | Alta claridad de intencion formativa. |
| curso excel presencial | 10 | UNSPECIFIED | Senal presencial directa, bajo volumen. |
| curso de excel presencial | 10 | LOW | Senal presencial directa, usable como grupo especifico. |
| clases de excel | 10 | MEDIUM | Intencion amplia, puede funcionar con filtro presencial. |
| curso excel avanzado | 10 | MEDIUM | Posible segmento posterior, no foco inicial. |
| curso de excel gratis | 10 | MEDIUM | Baja calidad / excluir o negativizar. |
| curso excel online | 10 | MEDIUM | No foco sala / evaluar como negativa si la landing es solo presencial. |

## Implicancia para campana

### Grupo recomendado 1: Excel general con filtro presencial

Objetivo: capturar volumen general y filtrar por anuncio/landing.

Keywords candidatas:

- `curso de excel`
- `curso excel`
- `excel basico`
- `excel desde cero`
- `clases de excel`

Mensaje recomendado:

- Excel presencial en Santiago Centro.
- Sala equipada.
- Notebook disponible.
- Profesor en vivo.
- Cupos limitados.

### Grupo recomendado 2: Presencial local exacto

Objetivo: capturar intencion explicita aunque el volumen sea bajo.

Keywords candidatas:

- `curso excel presencial`
- `curso de excel presencial`
- `curso excel presencial santiago`
- `curso de excel presencial santiago`
- `curso excel santiago centro`

Mensaje recomendado:

- Curso presencial de Excel en Santiago Centro.
- Cerca del metro.
- Aprendizaje practico con computador.

### Grupo recomendado 3: Excluir / baja calidad inicial

Negativas candidatas si la campana busca sala presencial pagada:

- `gratis`
- `online`
- `on line`
- `sena`
- `certificado gratis`

No negativizar `certificado` completo todavia, porque puede existir intencion pagada valida.

## Riesgos

- Volumen bajo no implica ausencia de demanda; puede reflejar geo estrecho, semillas especificas o limitaciones de historico.
- Keywords amplias pueden traer leads que quieren online o gratis; se mitiga con copy presencial y negativas.
- CPC alto/bajo en cero no debe interpretarse como gratis; puede ser falta de estimacion suficiente.

## Proxima accion recomendada

1. Crear una version local filtrada del radar con solo keywords accionables.
2. Separar keywords por grupo de anuncios:
   - Excel general;
   - Excel presencial local;
   - negativas iniciales.
3. No tocar campanas reales hasta validar estructura y presupuesto de test.
4. Preparar propuesta de campanha Search pequena con presupuesto controlado y medicion hacia landing/formulario/Zoho CRM.

## Guardrails

- No subir outputs brutos.
- No subir IDs completos.
- No tocar campanas reales desde este repo.
- No activar campana sin revisar fecha, precio, cupos y landing.
- No usar MCP para esta linea.