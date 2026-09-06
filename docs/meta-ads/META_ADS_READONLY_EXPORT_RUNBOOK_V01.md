# Meta Ads read-only export runbook V01

Fecha: 2026-07-29
Revisión y saneamiento: 2026-09-05
Estado: `DOCUMENTAL_TECNICO_RESCATADO_SANITIZADO`
Rama: `feature/marketing-official-read-control-plane-p0`

## Objetivo

Ejecutar un export local y read-only de Meta Ads para la cuenta publicitaria activa de Capacita cuando la cuenta aparece bajo **Otros activos** en Ads Manager y no dentro de los portafolios comerciales visibles.

## Precondiciones

- App Meta: `Capacita Ads API`.
- Token de usuario generado localmente con permiso `ads_read`.
- Cuenta publicitaria confirmada en Ads Manager bajo `Otros activos` con referencia sanitizada `...2327` (`act_<AD_ACCOUNT_ID>`).
- Archivo `.env` privado fuera del repo.
- No usar `ads_management` ni `leads_retrieval` para este export.

## Crear carpeta local

```powershell
New-Item -ItemType Directory -Force "C:\Users\TECH\AppData\Local\Capacita\MetaAds" | Out-Null
```

## Crear `.env` privado

```powershell
notepad "C:\Users\TECH\AppData\Local\Capacita\MetaAds\.env"
```

Contenido (sustituir con los valores reales propios en el entorno privado):

```text
META_GRAPH_VERSION=v25.0
META_ACCESS_TOKEN=PEGAR_TOKEN_LOCAL_AQUI
META_AD_ACCOUNT_ID=act_<AD_ACCOUNT_ID>
META_EXPORT_ROOT=C:\Users\TECH\AppData\Local\Capacita\MetaAds\exports
```

## Ejecutar export

Desde la raíz local del repo:

```powershell
.\scripts\meta_ads_readonly\export_meta_ads_readonly.ps1 `
  -EnvPath "C:\Users\TECH\AppData\Local\Capacita\MetaAds\.env" `
  -DatePreset "last_30d" `
  -TimeIncrement 1
```

## Outputs esperados

Ruta local:

```text
C:\Users\TECH\AppData\Local\Capacita\MetaAds\exports\meta-ads-export-YYYYMMDD-HHMMSS\
```

Archivos:

```text
manifest.json
summary.json
SUMMARY.md
raw-json\00_me.json
raw-json\01_account.json
raw-json\02_campaigns.json
raw-json\03_adsets.json
raw-json\04_ads.json
raw-json\05_insights_campaign.json
raw-json\05_insights_adset.json
raw-json\05_insights_ad.json
raw-json\06_breakdown_*.json
csv\02_campaigns.csv
csv\03_adsets.csv
csv\04_ads.csv
csv\05_insights_campaign.csv
csv\05_insights_adset.csv
csv\05_insights_ad.csv
csv\06_breakdown_*.csv
```

## Almacenamiento canónico de pesados

Para preservación duradera de exports brutos o reportes pesados:
- **Fuente canónica de pesados:** `SharePoint Site / Documentos / CAPACITA/Proyectos/external-files/marketing-performance-capacita`.
- **Acceso local sincronizado:** `OneDrive "Sitio de comunicación - external-files"`.
- **Regla:** No tratar `external-files` como staging ni subir outputs pesados a GitHub.

## Validación PASS

Debe imprimir:

```text
EXPORT_OK
Campaigns: N
Adsets: N
Ads: N
Errors: 0 o errores parciales registrados
Output: <ruta local>
```

Errores parciales en breakdowns no bloquean el export base si campañas, conjuntos, anuncios e insights principales salieron correctamente.

## Seguridad

No subir a GitHub:

- `.env` real;
- token;
- App Secret;
- CSV crudos;
- JSON crudos;
- IDs completos;
- datos personales;
- leads;
- capturas sensibles.

GitHub puede recibir después:

- síntesis agregada;
- procedimiento;
- conteos;
- análisis sanitizado;
- recomendaciones tácticas sin secretos.

## Próximo paso documental después de ejecutar

Crear o actualizar un resumen sanitizado en una rama documental, por ejemplo:

```text
docs/meta-ads/META_ADS_EXPORT_SUMMARY_YYYYMMDD.md
```

Debe incluir:

- periodo;
- campaña activa principal;
- gasto agregado;
- impresiones;
- alcance;
- visitas a landing;
- costo por visita;
- ranking de anuncios;
- errores parciales;
- limitaciones;
- recomendación.

No incluir IDs completos ni token.
