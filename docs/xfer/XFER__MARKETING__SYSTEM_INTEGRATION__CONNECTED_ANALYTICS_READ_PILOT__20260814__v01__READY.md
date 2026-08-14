# XFER — Marketing → System Integration — Connected Analytics Read Pilot

```yaml
producer: Marketing Performance / Campañas & Growth
consumer: System Integration / Capacita
case: CONNECTED_ANALYTICS_READ_PILOT
version: v01
date: 2026-08-14
status: READY
sensitivity: sanitized_metadata_only
```

## Prompt operativo único para System Integration

Actúa como proyecto **System Integration / Capacita** y ejecuta exclusivamente el micro-piloto técnico read-only requerido por Marketing.

### Lugar y ownership

1. Resuelve primero tu repo dueño real y aplica el Context Gate vigente de Global.
2. Trabaja sólo en una rama fuera de `main` del repo dueño de System Integration.
3. Lee como baseline obligatorio:
   - Global/CURRENT vigente y routing aplicable;
   - AI OS `docs/research/CAPACITA_CONVERSATIONAL_BUSINESS_MARKETING_CONTROL_PLANE_2026-08.md`;
   - AI OS `docs/handoffs/SYSTEM_INTEGRATION_MCP_CONTROL_PLANE_HANDOFF_2026-08.md`;
   - AI OS `docs/handoffs/MARKETING_CONNECTED_ANALYTICS_SKILLS_HANDOFF_2026-08.md`;
   - AI OS `docs/registry/CONVERSATIONAL_CONTROL_PLANE_CAPABILITIES_UPSTREAM_2026-08.md`;
   - issue AI OS #40 y PR #41 merge SHA `40ec5d26ec86d71a176dcf0c6bb526aa4c85aed7`;
   - Marketing `docs/analytics/CONNECTED_MARKETING_ANALYTICS_PILOT_2026-08-14.md` desde la rama/PR de este XFER.
4. No copies catálogos completos de AI OS al repo técnico.

### Objetivo

Validar si las capacidades oficiales reducen copy/paste y mantenimiento **sin migrar todavía** las rutas read-only actuales de Marketing.

Ejecuta tres frentes, en este orden:

#### A. Google Ads — paridad METHOD_A vs METHOD_B

```text
METHOD_A = API/POWERSHELL ACTUAL
METHOD_B = GOOGLE ADS MCP OFICIAL
```

Usa la misma cuenta Capacita, identificada de forma sanitizada, mismas ventanas de 7 y 30 días completos, misma zona horaria, moneda CLP y mismos filtros.

Responder exactamente las mismas preguntas:

1. campañas activas;
2. gasto 7/30 días;
3. performance por campaña;
4. search terms;
5. keywords;
6. Quality Score cuando esté disponible;
7. landing pages;
8. device/network;
9. conversion actions;
10. datos faltantes;
11. tiempo/corrección manual;
12. mantenimiento.

Para cada tarea reporta:

```text
METHOD_A_RESULT
METHOD_B_RESULT
PARITY=PASS|FAIL|DATA_GAP
MANUAL_CORRECTIONS_A=<count/description>
MANUAL_CORRECTIONS_B=<count/description>
WINNER_BY_TASK=METHOD_A|METHOD_B|MIX|NO_WINNER
REASON=<evidence>
```

Reglas:

- no asumir que MCP reemplaza la API actual;
- cualquier divergencia de significado/agregación no explicada = `PARITY=FAIL`;
- `FALLBACK=METHOD_A`;
- `NO_MIGRATION_IF_NO_MATERIAL_GAIN=YES`;
- no modificar campañas, budgets, bids, ads, keywords, negatives, conversion actions o estados;
- no crear scripts alternativos sólo para hacer ganar a un método.

#### B. Google Analytics MCP — capacidad existente

Sin crear OAuth ni credenciales nuevas:

1. verifica si existe conexión/auth ya utilizable;
2. si existe, confirma sólo lectura y consulta de forma sanitizada:
   - cuentas/propiedades;
   - metadata de propiedad;
   - usuarios/sesiones;
   - source/medium/campaign;
   - landing pages;
   - key events;
   - funnels/drop-off;
   - realtime cuando la herramienta lo soporte;
   - custom dimensions/metrics existentes;
   - Google Ads links;
3. no crees eventos, dimensiones, vínculos o configuración;
4. si el acceso requiere OAuth nuevo, instalación o secreto nuevo, detente y devuelve `GA4_MCP=HOLD_NEW_AUTH_REQUIRED`.

#### C. Meta Ads — conector/agente oficial vs API `ads_read`

Baseline de Marketing:

```text
CURRENT_FALLBACK=API_ADS_READ
ACCOUNT_ROUTING=CANONICAL_MARKETING_ROUTING
WRITE=FORBIDDEN
```

1. verifica si existe hoy un conector/MCP oficial Meta ya disponible y autenticado en tu entorno;
2. no crees auth nueva;
3. si existe, compara read-only:
   - account inventory/routing;
   - campaign/adset/ad status;
   - gasto 7/30;
   - impresiones/alcance/frecuencia;
   - clicks/landing page views cuando estén disponibles;
   - metadata de anuncio/creative;
   - errores, pasos manuales y mantenimiento;
4. no habilites `ads_management`, no publiques, no cambies presupuestos, audiencias, pujas o estados;
5. si el acceso oficial requiere instalación, OAuth nuevo, scopes de write o no puede resolver el routing correcto, devuelve `META_OFFICIAL_CONNECTOR=HOLD` y conserva `API_ADS_READ`.

### Gap CRM a resolver o enrutar

Marketing necesita una fuente canónica/verificada de los **API names reales** para atribución agregada en Zoho CRM, sin PII:

- UTM source/medium/campaign/content/term si existen;
- presencia de click ID;
- landing/landing_code si existe;
- lead/contact status;
- relación a Deal;
- relación a CursoAlumno cuando corresponda.

No inventes API names. Si System Integration no es dueño del mapping, crea/enruta una instrucción al repo técnico dueño y reporta el issue/PR correspondiente. No hagas CRM writes.

### Límites duros

No ejecutar:

- OAuth nuevo;
- instalaciones nuevas;
- Ads WRITE;
- CRM WRITE;
- GTM/Cloudflare/landing productiva;
- WhatsApp;
- secretos o credenciales en GitHub/chat;
- PII;
- exports crudos o binarios en GitHub;
- merge a `main`.

Si cualquiera de esos puntos es necesario para continuar, detener ese subfrente y reportarlo como gap; continuar sólo con los subfrentes independientes que sigan siendo read-only y autorizados.

### Evidencia y validación

Antes de commit/push, exige y conserva evidencia de:

```text
git status --short --branch
git diff --stat
git diff --check
```

Además valida:

- ausencia de PII;
- ausencia de secretos/tokens/OAuth JSON/`.env`;
- ausencia de customer/ad account IDs completos en documentación pública;
- ausencia de binarios/exports crudos;
- resultados agregados y sanitizados;
- cada query/herramienta utilizada identificada;
- cualquier `DATA_GAP` explícito.

Si falla `git diff --check`, aparece PII/secreto/binario o el scope deja de ser read-only: **no commit, no push**.

### Commit / push / PR

Si las validaciones pasan:

1. commit intencional en la rama de System Integration;
2. push;
3. PR no draft;
4. no merge;
5. enlaza este XFER y la evidencia AI OS/Marketing;
6. devuelve SHA y PR.

### DoD de retorno a Marketing

Entrega un único reporte con:

```text
GOOGLE_ADS_MCP_AUTH=PASS|HOLD
GOOGLE_ADS_MCP_PARITY=PASS|FAIL|PARTIAL|HOLD
WINNER_BY_TASK=[...]
FALLBACK=METHOD_A
NO_MIGRATION_IF_NO_MATERIAL_GAIN=YES

GA4_MCP=PASS|PARTIAL|HOLD
GA4_AVAILABLE_READS=[...]
GA4_GAPS=[...]

META_OFFICIAL_CONNECTOR=PASS|PARTIAL|HOLD
META_WINNER_BY_TASK=[...]
META_FALLBACK=API_ADS_READ

CRM_ATTRIBUTION_FIELD_MAPPING=PASS|ROUTED|HOLD
CRM_OWNER=...
CRM_EVIDENCE=...

EXTERNAL_WRITES=0
NEW_OAUTH=NO
INSTALLATIONS=0
PII_IN_GITHUB=NO
SECRETS_IN_GITHUB=NO

BRANCH=...
SHA=...
PR=...
MERGE_GATE=REQUIERE_REVISION_MISAEL|REQUIERE_CHECKS
```

No declares migración ni cierre E2E comercial. Marketing decidirá el `Delta` después de recibir esta evidencia.
