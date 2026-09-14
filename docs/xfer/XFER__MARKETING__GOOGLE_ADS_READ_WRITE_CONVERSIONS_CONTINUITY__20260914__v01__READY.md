# XFER — Google Ads READ / WRITE / Conversion Feedback Continuity

Fecha: 2026-09-14
Repo: `misaeln-pc1/marketing-performance-capacita`
Estado: `READY / CONTINUITY_BASELINE`

## 1. Objetivo

Evitar reinvestigar o repetir configuración si cambia el chat/agente. Este documento consolida el estado validado de Google Ads READ, las decisiones de alcance para Google Ads WRITE y el nuevo frente futuro de closed-loop conversion feedback desde CRM.

Antes de reabrir cualquiera de estos frentes, leer en este orden:

1. `TASK_STATUS.md`
2. `DECISIONES.md`
3. `docs/ads-connectivity/ADS_MCP_SECURE_CONNECTION_RUNBOOK_V01_2026-09-13.md`
4. Issue `#106` — Google Ads WRITE
5. Issue `#107` — Closed-loop conversions
6. Este XFER

No volver a OAuth/ADC/passkey ni reconstruir READ desde cero salvo evidencia verificable de ruptura.

---

## 2. Google Ads READ — estado vivo validado

Arquitectura validada:

```text
ChatGPT
-> OpenAI Secure MCP Tunnel
-> Google Ads MCP oficial
-> Service Account READ
-> Google Ads API
```

Estado:

```text
PRIMARY_PATH=DIRECT_MCP
LOCAL_LAUNCHER_REPRODUCIBLE=PASS
TUNNEL_REAL_TO_GOOGLE_ADS_MCP=PASS
WORKSPACE_TUNNEL_BINDING=PASS
CHATGPT_GOOGLE_ADS_TOOLS=PASS
GOOGLE_ADS_MCP_AUTH=PASS
GOOGLE_ADS_ACCOUNT_ACCESS=1
LIVE_READ_QUERY=PASS
CUSTOMER_COUNT=1
ADS_WRITES=0
GA4_CONFIG_WRITES=0
SECRETS_IN_GITHUB=0
```

Issue de implementación READ: `#104` cerrado como completado.
PR histórico/implementación: `#103` permanece Draft mientras se reconcilia su alcance documental.

Canónico operativo:
`docs/ads-connectivity/ADS_MCP_SECURE_CONNECTION_RUNBOOK_V01_2026-09-13.md`

Reglas:
- la Service Account READ sigue siendo sólo lectura;
- no promoverla silenciosamente a WRITE;
- secretos locales nunca a GitHub/chat;
- si falla el túnel, seguir runbook por capas: API directa -> MCP directo -> tunnel stub -> tunnel + MCP -> ChatGPT tool -> consulta mínima.

---

## 3. Google Ads WRITE — decisión de arquitectura

Issue canónico: `#106`.

Arquitectura objetivo:

```text
ChatGPT
-> OpenAI Secure MCP Tunnel separado: `Capacita-Google-Ads-WRITE`
-> MCP local WRITE controlado
-> Service Account WRITE separada
-> Google Ads API Mutate endpoints explícitamente whitelisteados
```

Motivo del MCP local: el MCP oficial de Google Ads validado para READ expone herramientas de lectura; no se debe fingir WRITE sobre ese servidor.

Principio:

```text
IDENTITY_READ != IDENTITY_WRITE
CONFIGURAR != GASTAR
GENERIC_MUTATE=PROHIBIDO
```

### 3.1 Familias de campaña incluidas en la misma identidad/túnel WRITE

No crear claves/túneles diferentes por tipo de campaña.

Incluidas para soporte técnico futuro:
- Search
- Shopping
- Demand Gen
- Display
- Video

`Performance Max`: **PENDIENTE_DE_DECISION_MISAEL**. No asumir incluido ni excluido hasta decisión explícita.

### 3.2 Capacidades permitidas

Mediante tools específicas y whitelisteadas, con `validate_only` antes de `apply`:
- crear campañas en estado `PAUSED`;
- editar campañas existentes sin presupuesto, bidding ni activación;
- ad groups / asset groups cuando aplique;
- keywords y match types;
- negativas y criterios negativos;
- anuncios/creatividades mutables;
- final URLs, paths y tracking permitido;
- assets y asociaciones: sitelinks, callouts, imágenes, etc.;
- targeting soportado: ubicación, idioma, horarios, audiencias, demografía, placements;
- pausar recursos reversibles;
- recomendaciones/experimentos sólo si se crean tools específicas y nunca con auto-apply silencioso.

### 3.3 Capacidades excluidas / sólo Misael

Bloqueadas por diseño dentro del MCP WRITE general:

```text
CAMPAIGN_ENABLE=USER_ONLY
BUDGET=USER_ONLY
BIDDING=USER_ONLY
BILLING_PAYMENTS=EXCLUDED
USER_ACCESS_PERMISSIONS_ACCOUNT_ADMIN=EXCLUDED
GENERIC_MUTATE=PROHIBITED
```

Adicionalmente, por seguridad, `ENABLE_*` de ad groups/ads/keywords nuevos queda bloqueado por defecto hasta decisión explícita, porque dentro de una campaña activa puede iniciar delivery/gasto.

### 3.4 Controles obligatorios WRITE

```text
VALIDATE_ONLY_DEFAULT=true
DRY_RUN_FIRST=true
BEFORE_AFTER_DIFF=REQUIRED
EXPLICIT_APPLY_AUTHORIZATION=REQUIRED
POST_WRITE_READ_VERIFY=REQUIRED
AUDIT_LOG_SANITIZED=REQUIRED
PARTIAL_FAILURE_DEFAULT=false
```

Todo `apply_*` debe corresponder a un plan de cambio explícito y aprobado. No permitir que una autorización para keywords esconda cambios de budget, bidding o status.

El setup de #106 debe terminar antes del primer write real en:

```text
VALIDATE_ONLY_MUTATE=PASS
REAL_ADS_WRITES=0
REQUIERE_REVISION_MISAEL
NO_MERGEAR_TODAVIA
```

---

## 4. Conversiones y PII — separación conceptual

### 4.1 PII

PII = información que puede identificar a una persona, por ejemplo:
- email;
- teléfono;
- nombre;
- identificadores de cliente.

Puede intervenir en Enhanced Conversions, Customer Match u otros flujos de atribución/medición. No es necesaria para configurar campañas y no debe pasar por ChatGPT innecesariamente.

Reglas:

```text
PII_IN_GITHUB=0
PII_IN_CHAT_UNNECESSARY=0
PII_UPLOADS_IN_GENERAL_CAMPAIGN_MCP=0
```

### 4.2 Configuración de conversiones

Modificar conversion actions/goals, primary/secondary, valores o atribución puede alterar la señal de optimización de Google aunque no use PII.

Estado actual:

```text
CONVERSION_CONFIG_READ=ALLOWED
CONVERSION_CONFIG_VALIDATE=ALLOWED_WHEN_IMPLEMENTED
CONVERSION_CONFIG_APPLY=HOLD_DECISION_MISAEL
```

No mezclar silenciosamente configuración de conversiones con cambios rutinarios de campañas.

---

## 5. Closed-loop conversion feedback — nuevo frente

Issue canónico: `#107`.

Objetivo futuro: devolver a Google resultados comerciales reales desde Zoho CRM para que la medición/optimización distinga cantidad de leads de calidad comercial.

Arquitectura conceptual:

```text
Google Ads click/lead
-> landing Capacita
-> identificador de atribución permitido
-> Zoho CRM
-> hito comercial validado
-> pipeline automático
-> Google Ads / Data Manager
```

Este frente es distinto de #106:

```text
CAMPAIGN_CONFIGURATION_MCP != CONVERSION_FEEDBACK_PIPELINE
```

El pipeline final debe operar automáticamente sin depender de que ChatGPT esté abierto.

### 5.1 Señales candidatas, aún no canónicas

```text
Lead
-> Lead calificado
-> Matrícula
-> Venta real
```

Pendiente decidir con evidencia:
- `PRIMARY_CONVERSION`;
- secondary/observation;
- valor monetario, si corresponde;
- idempotencia/deduplicación;
- reversos/cancelaciones;
- diferencias B2C/B2B.

### 5.2 DATA_GAP del frente conversion feedback

Antes de implementar se debe verificar:
1. campos/estados reales en Zoho para lead, calificado, matrícula y venta;
2. identificador de atribución que efectivamente llega a landing/CRM: GCLID/GBRAID/WBRAID u otro;
3. acciones de conversión vigentes en Google Ads;
4. definición exacta de `VENTA_REAL` B2C/B2B;
5. deduplicación/idempotencia y manejo de cancelaciones.

Hasta entonces:

```text
DESIGN_ONLY=YES
CRM_WRITES=0
GOOGLE_CONVERSION_UPLOADS=0
```

Nota de riesgo: aunque enviar una venta a Google no modifica directamente el presupuesto ni el bidding, sí puede influir indirectamente en Smart Bidding. Por eso la calidad de señal requiere gobernanza propia.

---

## 6. Secuencia vigente

```text
A. Google Ads READ = PASS_VERIFIED
B. Google Ads WRITE = #106 -> construir hasta VALIDATE_ONLY_MUTATE=PASS, sin write real
C. Primer write real = sólo instrucción concreta posterior de Misael
D. Meta Ads READ
E. Meta Ads WRITE
F. Closed-loop conversions = #107, cuando se priorice y se resuelvan DATA_GAP CRM/atribución
```

#107 puede diseñarse en paralelo documentalmente, pero no debe bloquear #106 ni mezclarse técnicamente con él.

---

## 7. Do not reopen / no repetir

No volver a discutir desde cero salvo nueva evidencia:
- READ ya funciona por Secure MCP Tunnel + Service Account;
- la identidad READ no se promueve a WRITE;
- WRITE usa túnel/app/Service Account separados;
- presupuesto, bidding, billing/pagos, activación, usuarios/permisos/cuentas y mutate genérico están fuera del MCP WRITE general;
- Search/Shopping/Demand Gen/Display/Video comparten una sola identidad/túnel WRITE;
- feedback CRM->Google va en un frente separado (#107), no dentro del MCP de campañas;
- secretos y PII no se versionan.

---

## 8. Gate actual

```text
GOOGLE_ADS_READ=PASS_VERIFIED
GOOGLE_ADS_WRITE=#106_IN_DESIGN/IMPLEMENTATION
CLOSED_LOOP_CONVERSIONS=#107_BACKLOG_DOCUMENTED
PERFORMANCE_MAX=PENDING_DECISION_MISAEL
CONVERSION_CONFIG_APPLY=PENDING_DECISION_MISAEL
REAL_ADS_WRITES=0
CRM_WRITES=0
GOOGLE_CONVERSION_UPLOADS=0
SECRETS_IN_GITHUB=0
NO_MERGEAR_TODAVIA
```

## NEXT_BEST_ACTION

Continuar #106 usando este perímetro y el runbook READ; detener el setup en `VALIDATE_ONLY_MUTATE=PASS` para revisión de Misael antes de cualquier cambio real en Google Ads.