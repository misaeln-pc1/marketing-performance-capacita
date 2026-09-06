# Meta Ads read-only API — Ruta A por usuario

Fecha: 2026-07-29
Revisión y saneamiento: 2026-09-05
Estado: `PROCEDIMIENTO_OPERATIVO_VALIDADO_SANITIZADO`
Alcance: lectura read-only de Meta Ads / Ads Insights para la cuenta publicitaria activa que aparece como **Otros activos**.

## 1. Problema que resuelve

La cuenta publicitaria activa de Capacita no aparece dentro de los tres portafolios comerciales visibles revisados previamente.

No asumir como fuente operativa:

- `Capacita Spa`;
- `Capacita`;
- `Misael Novoa Jara`.

La ruta operativa documentada previamente sigue siendo:

```text
Ads Manager -> selector de cuenta publicitaria -> Otros activos -> cuenta publicitaria activa con campañas históricas (...2327)
```

Referencia interna:

```text
docs/meta-ads/META_ADS_ACCOUNT_ROUTING.md
```

## 2. Decisión operativa

Mientras la cuenta no esté asignada formalmente a un Business/portfolio que permita usar System User, la ruta automatizable inmediata es:

```text
User Access Token del usuario que ya ve la cuenta en Ads Manager
+ permiso ads_read
+ cuenta publicitaria activa bajo Otros activos (...2327)
+ export local read-only
```

Esto no es la solución estructural definitiva, pero sí permite obtener información real por API sin hacer export manual recurrente.

## 3. Qué NO hacer

No usar esta ruta para:

- modificar campañas;
- publicar anuncios;
- cambiar presupuestos;
- cambiar pujas;
- cambiar audiencias;
- leer leads con PII;
- descargar formularios Lead Ads con datos personales;
- subir tokens, App Secret, CSV crudos, capturas sensibles o IDs completos al repo.

No agregar en esta fase:

```text
ads_management
leads_retrieval
```

## 4. Permisos validados

Permisos mínimos validados para Ruta A:

```text
ads_read
public_profile
```

`public_profile` aparece por defecto en el token de usuario. La lectura de performance usa `ads_read`.

## 5. URL de acceso para generar/probar token

```text
https://developers.facebook.com/tools/explorer/
```

Configuración visual esperada:

- App: `Capacita Ads API`.
- Usuario o página: token de usuario.
- Permiso: `ads_read`.
- Graph API version: versión vigente mostrada por Meta.

## 6. Validaciones mínimas en Graph API Explorer

### 6.1 Validar usuario/token

```text
GET /me?fields=id,name
```

Resultado esperado:

```text
Respuesta JSON con id y name del usuario autorizado.
```

No guardar el `user_id` en GitHub público.

### 6.2 Validar cuenta publicitaria activa

Usar el `act_...` completo solo en entorno local o privado. En GitHub registrar solo referencia sanitizada (`...2327`).

```text
GET /act_<AD_ACCOUNT_ID>?fields=id,name,account_status,currency,timezone_name
```

Resultado validado en chat:

```text
id: act_<sanitizado_...2327>
account_status: 1
currency: CLP
timezone_name: America/Santiago / America/Los_Angeles
```

Interpretación:

- el token puede leer la cuenta publicitaria activa;
- la cuenta responde desde API;
- Ruta A queda validada para lectura inicial.

### 6.3 Validar campañas

```text
GET /act_<AD_ACCOUNT_ID>/campaigns?fields=id,name,status,effective_status,objective,created_time,updated_time&limit=100
```

Resultado validado en chat:

- token con `ads_read` respondió correctamente;
- campaña activa encontrada: `META_TRAFFIC_EXCEL_PRESENCIAL_SANTIAGO_B2C_V3`;
- campaña anterior encontrada: `META_LEADS_EXCEL_PRESENCIAL_SANTIAGO_B2C_V1`, pausada;
- se observaron campañas históricas de Excel desde años anteriores;
- la respuesta incluyó paginación.

No versionar IDs completos de campañas en GitHub público.

## 7. Próximas llamadas read-only recomendadas

### 7.1 Conjuntos de anuncios

```text
GET /act_<AD_ACCOUNT_ID>/adsets?fields=id,name,campaign_id,campaign{name},status,effective_status,optimization_goal,billing_event,daily_budget,lifetime_budget,created_time,updated_time&limit=100
```

### 7.2 Anuncios

```text
GET /act_<AD_ACCOUNT_ID>/ads?fields=id,name,campaign_id,campaign{name},adset_id,adset{name},status,effective_status,created_time,updated_time&limit=100
```

### 7.3 Insights por anuncio — últimos 30 días

```text
GET /act_<AD_ACCOUNT_ID>/insights?level=ad&date_preset=last_30d&fields=campaign_name,adset_name,ad_name,spend,impressions,reach,clicks,inline_link_clicks,actions,cpc,ctr,cpm
```

### 7.4 Insights diarios por anuncio

```text
GET /act_<AD_ACCOUNT_ID>/insights?level=ad&date_preset=last_30d&time_increment=1&fields=date_start,date_stop,campaign_name,adset_name,ad_name,spend,impressions,reach,clicks,inline_link_clicks,actions,cpc,ctr,cpm
```

## 8. Export local y almacenamiento canónico

Los resultados crudos locales deben guardarse fuera del repo:

```text
C:\Users\TECH\AppData\Local\Capacita\MetaAds\exports\meta-ads-export-YYYYMMDD-HHMMSS\
```

Para retención pesada y canónica:
- **Bodega canónica:** `SharePoint Site / Documentos / CAPACITA/Proyectos/external-files/marketing-performance-capacita`.
- **Acceso local sincronizado:** `OneDrive "Sitio de comunicación - external-files"`.
- **Regla:** No tratar `external-files` como staging.

Archivo `.env` local sugerido:

```text
META_GRAPH_VERSION=v25.0
META_ACCESS_TOKEN=<NO_VERSIONAR_LOCAL_ONLY>
META_AD_ACCOUNT_ID=act_<NO_VERSIONAR_EN_GITHUB>
META_EXPORT_ROOT=C:\Users\TECH\AppData\Local\Capacita\MetaAds\exports
```

## 9. Reglas de sanitización

GitHub puede guardar:

- procedimiento;
- nombres de campañas si no contienen PII;
- estados agregados;
- métricas agregadas;
- manifest sanitizado;
- resumen de hallazgos.

GitHub no debe guardar:

- token;
- App Secret;
- IDs completos de usuario, cuenta, campaña, conjunto, anuncio o lead;
- CSV/JSON crudos;
- datos personales;
- capturas sensibles.

## 10. Ruta B pendiente

La solución estructural futura es regularizar acceso Business/System User.

Precondición:

```text
la cuenta publicitaria activa debe estar asignada, compartida o reclamada formalmente por el Business/portfolio correcto.
```

Mientras no ocurra eso, un System User creado dentro de un portfolio que no posee ni tiene asignada la cuenta no podrá leer `act_<AD_ACCOUNT_ID>` aunque tenga permisos.

## 11. Definition of Done para usar Ruta A

- [ ] Token de usuario generado sin exponerlo.
- [ ] Permiso `ads_read` presente.
- [ ] `/me` responde correctamente.
- [ ] `/act_<AD_ACCOUNT_ID>` responde con `account_status`, `currency` y `timezone_name`.
- [ ] `/campaigns` lista campañas reales.
- [ ] Exports crudos quedan fuera del repo.
- [ ] Resumen GitHub queda sanitizado.
- [ ] No se ejecutan cambios de campañas, presupuesto, anuncios ni audiencias.
