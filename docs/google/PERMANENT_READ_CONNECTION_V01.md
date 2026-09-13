# Permanent Google READ Connection V01

Issue: `#102`
Branch: `feature/marketing-google-official-permanent-read`
Estado: `IMPLEMENTATION_IN_PROGRESS`

## Objetivo

Establecer una conexión oficial, reutilizable y sin dependencia de trials para que Marketing pueda leer Google Ads y GA4 de forma consistente.

## Decisión de arquitectura

```text
PRIMARY_AUTH = Google OAuth / Application Default Credentials (ADC)
GOOGLE_ADS = official Google Ads API
GA4 = official Google Analytics Admin + Data APIs
THIRD_PARTY_TRIALS = OPTIONAL_ONLY
SECRETS_IN_GITHUB = 0
ADS_WRITES = 0
GA4_WRITES = 0
```

Se reutiliza el fast path existente de `#85/#86`; este frente no crea otro control plane.

## Cambio oficial de Google — septiembre 2026

Google retiró los developer tokens para Google Ads API el 2026-09-09. El acceso se asocia ahora al proyecto Google Cloud que posee el OAuth client o service account. Los headers `developer-token` legacy pueden seguir siendo enviados por código antiguo, pero el servidor los ignora.

Consecuencia: **no crear un proyecto OAuth nuevo al azar**. Debe reutilizarse el proyecto Google Cloud que heredó el acceso Google Ads API, salvo que Google Cloud Console confirme explícitamente acceso para otro proyecto.

## Autenticación elegida para el baseline actual

Para el entorno Windows/local ya existente se mantiene `single-user OAuth + ADC`, porque el fast path actual ya está diseñado para ADC y el último bloqueo observado fue `ACCESS_TOKEN_SCOPE_INSUFFICIENT`.

Scopes autorizados:

```text
https://www.googleapis.com/auth/adwords
https://www.googleapis.com/auth/analytics.readonly
https://www.googleapis.com/auth/cloud-platform
```

La credencial ADC se guarda por `gcloud` fuera del repo. El OAuth client JSON también debe permanecer fuera de GitHub.

> Un refresh token es persistente y las librerías Google renuevan access tokens automáticamente. Google aún puede revocar el refresh token por seguridad o si el usuario revoca consentimiento. `PERMANENTE` significa infraestructura propia/reutilizable, no token eterno.

## Instalación única

Script:

```text
scripts/google_official_read/setup_google_read.ps1
```

Entradas privadas locales:

- OAuth Desktop Client JSON del proyecto Google Cloud que conserva acceso Google Ads API.
- `google-ads.yaml` existente fuera del repo con `use_application_default_credentials: true` y routing de cuenta cuando corresponda.

El script:

1. verifica `gcloud` y Python;
2. instala/actualiza sólo librerías oficiales Google necesarias;
3. abre **un único consentimiento Google** para Ads + GA4 READ;
4. guarda ADC fuera del repo;
5. ejecuta un health check unificado READ-only.

## Health check

```text
scripts/google_official_read/check_google_read.py
```

Criterio mínimo:

```text
GOOGLE_ADS_AUTH=PASS
GOOGLE_ADS_ACCESSIBLE_CUSTOMERS=>0
GA4_AUTH=PASS
GA4_PROPERTIES=>0
```

Si falta configuración o permisos, devuelve `HOLD`; nunca inventa datos ni intenta writes.

## Acceso desde ChatGPT

La autenticación local resuelve el acceso oficial de los runners de Capacita, pero un chat web no puede ejecutar arbitrariamente procesos del PC local. Para que ChatGPT consuma resultados sin plugins pagados, el patrón objetivo es:

```text
OFFICIAL GOOGLE APIs
→ runner READ reproducible
→ snapshot agregado/sanitizado
→ superficie ya conectada a ChatGPT
→ Marketing analiza
```

La superficie preferida es Google Drive/Sheets ya conectada, reutilizando el modelo `Historial_Rendimiento_GoogleAds` si sigue vigente. SharePoint queda como bodega canónica para archivos pesados, no como requisito para consultas tabulares frecuentes.

Este bridge no reemplaza la fuente oficial: sólo transporta snapshots READ al chat.

## DO_NOT_CHANGE

- no conectar otro trial como ruta primaria;
- no guardar OAuth client secrets, refresh tokens o ADC en GitHub;
- no usar Ads writes;
- no usar GA4 Admin writes;
- no cambiar presupuestos, pujas, anuncios, keywords, negativas o conversiones;
- no crear un Google Cloud project nuevo si el actual ya heredó el acceso Ads API.

## Estado esperado de cierre

```text
GOOGLE_OFFICIAL_AUTH=PASS
GOOGLE_ADS_READ=PASS
GA4_READ=PASS
CHATGPT_READ_BRIDGE=PASS
THIRD_PARTY_TRIAL_DEPENDENCY=NO
NO_MERGEAR_TODAVIA hasta evidencia viva
```
