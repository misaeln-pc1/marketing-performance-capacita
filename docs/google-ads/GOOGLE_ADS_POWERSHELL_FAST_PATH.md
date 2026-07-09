# Google Ads PowerShell Fast Path

## Proposito

Dejar documentada la ruta rapida que ya funciono para ejecutar Google Ads API read-only desde Windows PowerShell, sin repetir errores de configuracion, encoding o permisos.

## Estado validado

- Google Ads API Basic Access aprobado.
- Pipeline local Python read-only validado.
- `list_accessible_customers.py` funciono y mostro 2 cuentas accesibles con IDs enmascarados.
- `generate_keyword_ideas.py` funciono contra la cuenta publicitaria real.
- Se genero output local TSV y radar local CSV.
- No se versionan outputs brutos, tokens, YAML ni customer IDs completos.

## Archivos locales sensibles

Estos archivos viven fuera del repo y no deben subirse a GitHub:

- `C:\Users\TECH\Documents\Proyectos\0-Origen\google-ads.yaml`
- `C:\Users\TECH\Documents\Proyectos\0-Origen\run-google-ads-keywords.ps1`

## YAML correcto

El archivo `google-ads.yaml` debe tener solo esta estructura:

```yaml
developer_token: "TOKEN_REAL"
login_customer_id: "ID_MANAGER_MCC_SIN_GUIONES"
use_application_default_credentials: true
use_proto_plus: true
```

Reglas:

- `developer_token`: token aprobado en API Center.
- `login_customer_id`: ID del Manager/MCC, sin guiones.
- No agregar `customer_id` ni `target_customer_id` al YAML.
- No pegar este archivo en chats, PRs ni repositorios.

## Cuentas observadas

`list_accessible_customers.py` mostro 2 cuentas accesibles:

- cuenta publicitaria real: `996-***-7322`;
- Manager/MCC: `746-***-6623`.

Uso correcto:

- En YAML, `login_customer_id` = MCC `746...` sin guiones.
- En `generate_keyword_ideas.py`, `--customer-id` = cuenta real `996...` sin guiones.

## Runner local que funciono

El archivo local `run-google-ads-keywords.ps1` debe ejecutar el script desde el repo, usando config externa y customer ID de la cuenta real.

Ejecucion:

```powershell
powershell -ExecutionPolicy Bypass -File "C:\Users\TECH\Documents\Proyectos\0-Origen\run-google-ads-keywords.ps1"
```

Salida esperada:

```text
KEYWORD_IDEAS_READY
keyword_idea_text	avg_monthly_searches	competition	low_top_of_page_bid_micros	high_top_of_page_bid_micros
...
```

## Errores resueltos

### 1. `DEVELOPER_TOKEN_NOT_APPROVED`

Causa:

- Token solo tenia acceso de prueba.

Solucion:

- Google aprobo Basic Access.

### 2. `USER_PERMISSION_DENIED`

Causa probable:

- Faltaba o no se estaba usando correctamente `login_customer_id` del MCC.

Solucion validada:

- YAML con `login_customer_id` del MCC sin guiones.
- Verificar que Python lo carga:

```powershell
cd "C:\Users\TECH\Documents\Proyectos\marketing-performance-capacita"

@'
from google.ads.googleads.client import GoogleAdsClient
config_path = r"C:\Users\TECH\Documents\Proyectos\0-Origen\google-ads.yaml"
client = GoogleAdsClient.load_from_storage(path=config_path)
login_customer_id = getattr(client, "login_customer_id", None)
if login_customer_id:
    login_customer_id = str(login_customer_id)
    print("OK: Python cargo login_customer_id:", login_customer_id[:3] + "***" + login_customer_id[-4:])
else:
    print("ERROR: Python NO cargo login_customer_id")
'@ | python
```

### 3. `Seeds file is empty`

Causa:

- PowerShell 5.1 puede guardar CSV con BOM o codificacion que rompe la cabecera `keyword_seed`.

Solucion rapida:

- Reescribir el CSV con UTF-8 sin BOM usando .NET:

```powershell
cd "C:\Users\TECH\Documents\Proyectos\marketing-performance-capacita"

$csvPath = "automation\google-ads-readonly\keyword_seeds_presencial_santiago.csv"

$content = @"
keyword_seed
curso excel básico e intermedio
curso excel presencial
excel presencial
excel santiago
curso de excel presencial santiago
curso excel presencial santiago
Excel de Santiago
Curso Excel de Santiago
excel curso
curso excel on line
"@

$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
[System.IO.File]::WriteAllText((Resolve-Path $csvPath), $content, $utf8NoBom)
```

### 4. `UnicodeDecodeError` al leer TSV

Causa:

- PowerShell 5.1 guarda la redireccion `>` como UTF-16 LE con BOM.

Solucion:

- Leer el TSV con `encoding="utf-16"` al transformarlo en radar CSV.

## Keywords reales usadas como semillas

Estas semillas vinieron desde Google Ads real del dia:

```csv
keyword_seed
curso excel básico e intermedio
curso excel presencial
excel presencial
excel santiago
curso de excel presencial santiago
curso excel presencial santiago
Excel de Santiago
Curso Excel de Santiago
excel curso
curso excel on line
```

## Resultado local validado

- `generate_keyword_ideas.py` funciono.
- Radar local generado:
  - `automation/google-ads-readonly/output/radar_keyword_ideas_presencial_santiago_v01.csv`
- Filas procesadas: 1676.

## Lectura operativa

No repetir el flujo manual largo. La via rapida es:

1. Confirmar que `google-ads.yaml` existe fuera del repo.
2. Confirmar que `run-google-ads-keywords.ps1` existe fuera del repo.
3. Editar semillas si corresponde.
4. Ejecutar el runner.
5. Transformar TSV a CSV leyendo UTF-16 si el output viene de PowerShell 5.1.
6. Documentar solo resumen sanitizado.

## Guardrails

- No subir YAML.
- No subir token ni refresh token.
- No subir customer IDs completos.
- No subir TSV/CSV bruto.
- No ejecutar `export_campaign_summary.py` hasta aprobar contrato.
- No modificar campañas reales.