# Google Ads Historical Diagnosis Runbook V01

## Objetivo

Obtener un diagnóstico histórico read-only de Google Ads suficientemente completo para explicar gasto, clics, baja conversión post-click, calidad de keywords, búsquedas reales, landing pages, dispositivos y acciones de conversión.

Este runbook reemplaza la lectura incompleta basada solo en Keyword Ideas. No modifica campañas ni producción.

## Problema observado

Caso reportado por Misael:

- gasto diario aproximado cercano a CLP $20.000;
- 16 a 18 clics;
- 0 a 2 leads aproximados;
- deterioro percibido de la etapa post-click;
- sospecha de mezcla de intención, keywords, competencia, landing y baja calidad.

## Qué considera el export

El exportador genera los siguientes archivos locales:

1. `01_account_context.csv`
   - moneda;
   - zona horaria;
   - rango analizado.
2. `02_campaign_config.csv`
   - campaña;
   - estado;
   - estrategia de puja;
   - presupuesto diario;
   - redes activadas.
3. `03_campaign_daily.csv`
   - gasto, clics, CTR, CPC y conversiones por día;
   - impression share;
   - pérdida por presupuesto;
   - pérdida por Ad Rank;
   - top y absolute top impression percentage.
4. `04_device_network_daily.csv`
   - resultado por dispositivo y red.
5. `05_search_terms_daily.csv`
   - búsquedas reales que activaron anuncios;
   - keyword asociada;
   - tipo de concordancia;
   - estado de targeting;
   - costo y conversiones.
6. `06_keywords_quality_daily.csv`
   - rendimiento histórico por keyword;
   - Quality Score actual;
   - relevancia del anuncio actual;
   - experiencia de landing actual;
   - CTR esperado actual;
   - impression share y pérdida por rank.
7. `07_landing_pages_daily.csv`
   - URL final efectiva;
   - clics, costo y conversiones;
   - desglose por dispositivo.
8. `08_conversion_actions_daily.csv`
   - nombres y categorías de las conversiones contabilizadas.
9. `09_ads_daily.csv`
   - estado y tipo de anuncio;
   - Ad Strength actual;
   - URLs finales;
   - métricas diarias.
10. `10_window_summary.csv`
   - comparación automática de ventanas de 7, 30 y 90 días.
11. `manifest.json`
   - filas generadas;
   - reportes exitosos;
   - errores por consulta, si existen;
   - sin customer ID.

## Consideración sobre competencia

El indicador `competition` de Keyword Planner se mantiene como referencia de planificación, pero no basta para diagnosticar una campaña real.

El diagnóstico histórico usa señales operativas más útiles:

- CPC real;
- Search Impression Share;
- pérdida de impresiones por presupuesto;
- pérdida de impresiones por Ad Rank;
- Quality Score;
- relevancia del anuncio;
- experiencia de landing;
- CTR esperado;
- posición superior y superior absoluta.

No confundir competencia de Keyword Planner con rendimiento o calidad real de la campaña.

## Limitaciones

- Quality Score y sus componentes son valores actuales al momento de la consulta; no constituyen un historial diario real aunque aparezcan junto a métricas históricas.
- Google puede omitir algunos términos de búsqueda por umbrales de privacidad; el total de search terms puede no igualar todos los clics de campaña.
- La API solo muestra conversiones configuradas en Google Ads. Lead contactable, respuesta, cotización y matrícula requieren unión posterior con landing y Zoho CRM.
- La existencia de varias landings no se decide antes del análisis. Primero se identifica qué intención, término y URL pierden dinero o convierten.

## Preflight local

Confirmar que existen fuera del repo:

- `C:\Users\TECH\Documents\Proyectos\0-Origen\google-ads.yaml`;
- Python con librería `google-ads` instalada;
- customer ID real disponible localmente, sin pegarlo en GitHub o chat.

El YAML debe conservar:

```yaml
developer_token: "TOKEN_REAL"
login_customer_id: "ID_MANAGER_MCC_SIN_GUIONES"
use_application_default_credentials: true
use_proto_plus: true
```

## PowerShell — dry run

Este paso no llama la API:

```powershell
cd "C:\Users\TECH\Documents\Proyectos\marketing-performance-capacita"

$cid = "ID_CUENTA_REAL_SIN_GUIONES"
$out = "C:\Users\TECH\Documents\Proyectos\0-Origen\google-ads-diagnosis\dry-run"

python scripts/google_ads_readonly/export_campaign_summary.py `
  --config-path "C:\Users\TECH\Documents\Proyectos\0-Origen\google-ads.yaml" `
  --customer-id $cid `
  --days 90 `
  --output-dir $out
```

Salida esperada:

```text
DRY_RUN: historical diagnosis exporter ready
DATE_RANGE: ...
REPORT_COUNT: 10
OUTPUT_POLICY: external directory only; raw outputs are not versioned
NEXT_STEP: rerun with --execute after review and authorization
```

## PowerShell — ejecución read-only

Ejecutar solo después del merge/revisión del PR y autorización de Misael:

```powershell
cd "C:\Users\TECH\Documents\Proyectos\marketing-performance-capacita"

$cid = "ID_CUENTA_REAL_SIN_GUIONES"
$stamp = Get-Date -Format "yyyyMMdd-HHmmss"
$out = "C:\Users\TECH\Documents\Proyectos\0-Origen\google-ads-diagnosis\$stamp"

New-Item -ItemType Directory -Force $out | Out-Null

python scripts/google_ads_readonly/export_campaign_summary.py `
  --config-path "C:\Users\TECH\Documents\Proyectos\0-Origen\google-ads.yaml" `
  --customer-id $cid `
  --days 90 `
  --output-dir $out `
  --execute

Get-ChildItem $out | Select-Object Name, Length

Compress-Archive `
  -Path "$out\*" `
  -DestinationPath "$out.zip" `
  -Force

Write-Host "DIAGNOSTIC_ZIP: $out.zip"
```

## Entrega para análisis

Compartir en el chat únicamente el ZIP local generado. El exportador:

- no incluye customer ID;
- no incluye credenciales;
- no incluye emails detectables en search terms o URLs;
- reemplaza secuencias largas de números potencialmente sensibles.

No subir el ZIP, CSV ni `manifest.json` al repo público.

## Preguntas que responderá el diagnóstico

1. Qué campañas, días y dispositivos consumen el presupuesto.
2. Qué search terms tienen costo y cero conversiones.
3. Qué keywords tienen baja experiencia de landing, baja relevancia o CTR esperado bajo.
4. Si el problema principal es presupuesto, Ad Rank, concordancia o post-click.
5. Qué URL recibe los clics caros y si convierte.
6. Qué conversiones está contando realmente Google Ads.
7. Si conviene separar campaña, grupo de anuncios o landing por intención.
8. Qué negativas iniciales están respaldadas por gasto real.

## Guardrails

- Solo SELECT/GAQL read-only.
- No modifica campañas, pujas, presupuestos, anuncios, keywords o conversiones.
- No sube outputs al repo.
- No imprime IDs completos.
- No usa MCP.
- Si una consulta falla, continúa con las restantes y registra el error en `manifest.json`.
