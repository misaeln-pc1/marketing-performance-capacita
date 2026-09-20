# Incidente Meta/Facebook — perfil restringido y bucle `advanced_protection`

Fecha del incidente documentado: 2026-09-19  
Repo dueño: `misaeln-pc1/marketing-performance-capacita`  
Estado: `HOLD_META_TECH_REPORT / PERIODIC_RECHECK`  
Semáforo: `AMARILLO` operacional; cualquier credencial, pago, permiso o cambio de seguridad sigue siendo `ROJO`.

## Resumen ejecutivo

Misael lleva más de una semana sin poder acceder normalmente a Facebook ni a las superficies de administración Meta asociadas. El síntoma estable es un bucle de redirecciones que termina en:

```text
ERR_TOO_MANY_REDIRECTS
```

El flujo afectado pasa por:

```text
facebook.com/checkpoint/advanced_protection/
```

La evidencia reunida el 2026-09-19 muestra que el perfil de Facebook aparece explícitamente como **`Restringido`** en el Centro de cuentas y que Meta exige completar un **control de seguridad** antes de continuar. El problema es que el propio botón oficial **`IR A FACEBOOK`** conduce nuevamente al flujo roto y termina en el mismo bucle.

No se observó una deshabilitación estándar por política; el asistente de ayuda de Meta indicó que el flujo de recuperación no reconoce la cuenta como “deshabilitada” en los sistemas de apelación estándar y trató el caso como un fallo técnico del control de seguridad/checkpoint.

## Impacto

- Acceso normal a Facebook: bloqueado.
- Ads Manager / Meta Business Suite: bloqueados por el mismo problema de autenticación.
- Instagram personal vinculado: operativo.
- Centro de cuentas de Meta desde Instagram: operativo parcialmente.
- Página de Facebook `Capacita`: sigue apareciendo dentro de “Páginas que administras”.
- Cuenta publicitaria operativa de Meta Ads: no se modificó durante este incidente.
- Riesgo comercial: dificultad para mantener financiada/administrada la campaña Meta Ads si el saldo prepago requiere intervención desde Ads Manager.

La preocupación comercial real al cierre no es gasto ilimitado. La cuenta utiliza fondos limitados/prepagados y el riesgo inmediato es **perder continuidad de leads por no poder agregar fondos o administrar la campaña**.

## Evidencia observada

### 1. Fallo inicial

En escritorio y teléfono:

```text
Facebook / Ads Manager
→ redirección a /checkpoint/advanced_protection/
→ ERR_TOO_MANY_REDIRECTS
```

El fallo persistió durante más de una semana y no fue explicado por pérdida de conectividad.

### 2. Instagram sigue operativo

La aplicación de Instagram continuó funcionando con normalidad. Intentar usar Meta Business Suite autenticando vía Facebook o Instagram también falló.

### 3. Centro de cuentas accesible desde Instagram

Se verificó desde Instagram:

- contraseña actualizada por el propio usuario durante el troubleshooting;
- autenticación en dos pasos activa;
- app autenticadora disponible;
- SMS/WhatsApp disponible como segundo factor;
- códigos de respaldo disponibles;
- dispositivos de confianza existentes;
- teléfono Android actual reconocido por Facebook;
- no se observaron alertas de seguridad recientes en “Correos electrónicos de Meta” durante los últimos 14 días;
- la única “acción recomendada” del chequeo rápido era crear una llave de acceso, no completar Protección avanzada;
- “Protección avanzada” no apareció como opción configurable en esa interfaz.

No se desactivó 2FA, no se eliminaron dispositivos ni se desvincularon perfiles.

### 4. Perfil Facebook marcado como restringido

En el Centro de cuentas, dentro de perfiles:

```text
Misael Novoa Jara
Facebook • Restringido
```

Al abrirlo, Meta mostró:

```text
No se puede editar

Es necesario realizar un control de seguridad de [perfil] en Facebook para continuar.
```

La interfaz ofreció el botón:

```text
IR A FACEBOOK
```

### 5. Passkey / llave de acceso existente

Al seguir el flujo oficial, Android/Google ofreció una llave de acceso ya guardada para `m.facebook.com`.

Importante:

- la llave ya existía;
- no se creó una nueva durante esta sesión;
- Facebook aceptó la autenticación y reconoció el perfil;
- posteriormente apareció la pantalla para guardar la información de inicio de sesión;
- el flujo quedó cargando aproximadamente 15 minutos;
- al repetir el intento, terminó nuevamente en `ERR_TOO_MANY_REDIRECTS`.

Secuencia observada:

```text
PROFILE_RESTRICTED
→ SECURITY_CHECK_REQUIRED
→ IR_A_FACEBOOK
→ PASSKEY_ACCEPTED
→ PROFILE_IDENTIFIED
→ POST_LOGIN_FLOW
→ ERR_TOO_MANY_REDIRECTS
```

Esto separa el problema de una contraseña incorrecta, ausencia de 2FA o falta de dispositivo reconocido.

## Investigación de posible cambio previo de seguridad

Misael recordó que alrededor de una semana antes había trabajado en integraciones Ads/MCP y había usado PIN/passkey.

Se revisó el historial GitHub de Marketing:

- el incidente de passkey documentado el 2026-09-13 pertenecía a **Google Ads / Google OAuth**, no a Facebook;
- ese flujo quedó en `HOLD_OAUTH_INTERACTIVE_PASSKEY`;
- el procedimiento documentó explícitamente que no se creó una nueva passkey durante ese intento;
- la solución Google Ads READ terminó usando Service Account + OpenAI Secure MCP Tunnel;
- el roadmap de esa fecha mantenía `META_ADS_READ=NOT_STARTED` y `META_ADS_WRITE=NOT_STARTED`.

Conclusión: no existe evidencia en el repo de que el setup de MCP/Google haya modificado seguridad de Facebook/Meta.

## Relación con la cuenta Meta Ads operativa

Fuente vigente:

`docs/meta-ads/META_ADS_ACCOUNT_ROUTING.md`

La cuenta publicitaria operativa de Capacita es una cuenta personal/standalone bajo `Otros activos`, con referencia sanitizada:

```text
...2327
```

No pertenece actualmente a los Business Portfolios visibles de Capacita.

Campaña de referencia:

```text
META_TRAFFIC_EXCEL_PRESENCIAL_SANTIAGO_B2C_V3
```

No modificar esta identificación por memoria ni por nombre de portfolio.

Durante este incidente:

```text
ADS_WRITES=0
BUDGET_WRITES=0
PAYMENT_WRITES=0
ACCOUNT_PERMISSION_WRITES=0
META_SECURITY_SETTINGS_WRITES=0
```

El usuario sí actualizó voluntariamente su contraseña durante el diagnóstico.

## Intento desde Instagram para administrar publicidad

Desde el perfil de Instagram operativo se abrió:

```text
Herramientas
→ Herramientas publicitarias
```

La interfaz mostró:

```text
Administrar anuncios
No tienes anuncios.
```

Conclusión: ese perfil de Instagram no expone la cuenta publicitaria operacional ni su facturación. No usar esa superficie para inferir que la campaña Meta Ads real no existe.

## Soporte Meta

Se utilizó el Asistente de ayuda de Meta desde Instagram.

El asistente:

1. inicialmente sugirió pasos genéricos de login/cookies;
2. luego reconoció que el caso no aparecía como cuenta “deshabilitada” en el sistema estándar de apelación;
3. caracterizó el problema como fallo técnico del proceso de control de seguridad;
4. indicó que no podía restablecer manualmente el checkpoint ni generar un número de caso;
5. recomendó reportar el incidente desde Instagram porque Facebook no era accesible.

Misael envió finalmente el reporte mediante Instagram el 2026-09-19.

Estado al cierre:

```text
INSTAGRAM_BUG_REPORT=SENT
META_CASE_NUMBER=NONE
META_RESPONSE_PENDING=YES
FACEBOOK_ACCESS=BLOCKED
PROFILE_STATUS=RESTRICTED
CHECKPOINT_LOOP=REPRODUCIBLE
```

Las capturas originales permanecen en el historial del chat y no se versionan en este repositorio público.

## Qué NO hacer al retomar

Hasta recibir respuesta de Meta o evidencia nueva:

- no repetir cambios de contraseña sin necesidad;
- no desactivar 2FA;
- no eliminar dispositivos de confianza;
- no borrar la passkey existente;
- no crear otra passkey por reflejo;
- no desvincular Facebook, Instagram, Threads ni la página Capacita;
- no reclamar/mover la cuenta publicitaria a un Business;
- no cambiar permisos/propiedad;
- no asumir que borrar cookies resolverá un checkpoint ya reproducido después de autenticación correcta;
- no trabajar directo en `main`.

## Próximo paso al retomar

Prioridad 1:

```text
REVISAR_RESPUESTA_META
→ identificar si Meta entrega número de caso, instrucción específica o cambio de estado
→ repetir sólo la validación mínima necesaria
→ confirmar si PROFILE_STATUS deja de ser RESTRICTED
→ confirmar acceso a Ads Manager
```

Prioridad 2, continuidad comercial:

```text
VERIFICAR_ESTADO_REAL_CAMPAÑA
→ verificar saldo/fondos prepago
→ confirmar ACTIVE vs ENDED
→ agregar fondos sólo desde superficie autorizada y cuenta correcta
→ confirmar entrega
```

Si existe otro administrador autorizado de la cuenta publicitaria, puede evaluarse como fallback para mantener la operación sin esperar la recuperación del perfil, siempre sin compartir contraseñas y con autorización explícita para cualquier cambio de dinero/permisos.

## Criterio de cierre del incidente

No cerrar hasta tener evidencia de al menos una de estas condiciones:

- acceso normal a Facebook restaurado y checkpoint completado; o
- Meta entrega resolución/diagnóstico oficial y una ruta funcional de recuperación; o
- existe un fallback administrativo seguro y validado para Ads mientras el perfil sigue restringido, con el incidente de seguridad todavía abierto.


## Aclaración de seguimiento — 2026-09-20

El Asistente de ayuda de Meta aclaró explícitamente que los reportes enviados mediante **Reportar un problema** por fallos técnicos:

- no generan una respuesta personal;
- no generan confirmación por correo;
- no tienen seguimiento individual visible;
- se utilizan como señal técnica para mejorar/corregir la plataforma.

La **Bandeja de ayuda** aplica principalmente a reportes de normas/contenido y no sirve como tracker del bug técnico de este incidente.

Por tanto, la estrategia de seguimiento cambia de:

```text
ESPERAR_RESPUESTA_META
```

a:

```text
TECH_REPORT_SENT
→ NO_INDIVIDUAL_RESPONSE_EXPECTED
→ PERIODIC_RECHECK_PROFILE_STATUS
→ PERIODIC_RECHECK_SECURITY_CHECK_FLOW
→ RETOMAR SOLO SI HAY CAMBIO
```

Comprobación mínima recomendada al retomar:

1. Instagram → Centro de cuentas → perfiles.
2. Verificar si Facebook sigue mostrando `Restringido`.
3. Sólo si cambió el estado, probar `IR A FACEBOOK` una vez.
4. No repetir cambios de contraseña, cookies, 2FA o passkey sin evidencia nueva.


## Escalamiento comercial y soporte pagado — 2026-09-20

Ante la gravedad comercial del bloqueo, se investigaron rutas de soporte pagado dentro de Meta desde Instagram.

### Ofertas observadas en la interfaz

Se observaron al menos estas ofertas:

```text
Business Standard
Desde $5.600/mes por perfil
Ayuda mejorada: chat o correo electrónico con representantes
Beneficio de prueba visible
```

y:

```text
Business Plus
Desde $18.990/mes por perfil
Ayuda mejorada
"Resuelve los problemas más rápido"
Beneficio de prueba visible
```

Business Plus además mostraba beneficios adicionales de visibilidad/perfil en Facebook e Instagram. No se documenta aquí ninguna promesa de SLA porque la interfaz observada no mostró un tiempo garantizado de resolución.

### Bloqueo circular del soporte pagado

Al intentar avanzar para obtener el plan/soporte, la interfaz volvió a exigir autenticación mediante Facebook.

Resultado:

```text
NEED_HUMAN_SUPPORT
→ META_BUSINESS_PLAN_FLOW
→ AUTH_VIA_FACEBOOK_REQUIRED
→ FACEBOOK_PROFILE_RESTRICTED
→ SECURITY_CHECK_REQUIRED
→ CHECKPOINT_LOOP
```

Por tanto, la vía pagada no quedó validada como acceso efectivo a soporte humano para este incidente.

### Cobertura de perfil observada

Al revisar la selección/asignación del plan desde la superficie disponible, la interfaz mostraba principalmente el perfil de Instagram y solicitaba asignar una categoría. No quedó demostrado que la suscripción pudiera aplicarse al perfil Facebook restringido ni que habilitara soporte para él sin superar antes el mismo login bloqueado.

Decisión provisional:

- no contratar Business Standard/Plus sólo por expectativa de soporte;
- primero exigir evidencia de que el plan cubre el perfil Facebook afectado y no depende del mismo checkpoint roto;
- no interpretar beneficios de mayor exposición como solución al incidente de autenticación;
- no confundir soporte para Instagram/WhatsApp con soporte garantizado para el perfil Facebook restringido.

## Mapa consolidado de rutas intentadas

```text
FACEBOOK_WEB                  = FAIL_ERR_TOO_MANY_REDIRECTS
FACEBOOK_MOBILE_FLOW          = FAIL_CHECKPOINT_LOOP
FACEBOOK_PASSKEY              = AUTH_PASS / POST_LOGIN_FAIL
META_BUSINESS_SUITE_FACEBOOK  = FAIL
META_BUSINESS_SUITE_INSTAGRAM = FAIL
INSTAGRAM_APP                 = PASS
INSTAGRAM_ACCOUNTS_CENTER     = PASS_PARTIAL
INSTAGRAM_AD_TOOLS            = NO_REAL_META_ADS_ACCOUNT_VISIBLE
META_AI_HELP_ASSISTANT        = INFORMATION_ONLY / NO_CASE
INSTAGRAM_TECH_BUG_REPORT     = SENT / NO_INDIVIDUAL_RESPONSE
META_HELP_INBOX               = NOT_TRACKER_FOR_TECH_BUG
META_BUSINESS_STANDARD        = SUPPORT_OFFER_VISIBLE / ACCESS_NOT_VALIDATED
META_BUSINESS_PLUS            = SUPPORT_OFFER_VISIBLE / ACCESS_NOT_VALIDATED
PAID_SUPPORT_FLOW             = BLOCKED_BY_FACEBOOK_AUTH_LOOP
```

## Problema comercial asociado

La cuenta publicitaria opera con fondos limitados/prepagados. Al cierre:

- el saldo se habría agotado recientemente;
- el objetivo de Misael es mantener la campaña generando leads;
- la necesidad inmediata no es pausar gasto, sino poder **agregar fondos / mantener continuidad comercial**;
- Instagram personal no expone la cuenta publicitaria standalone real;
- el acceso a Ads Manager/facturación sigue bloqueado por el perfil restringido.

Antes de cualquier pago futuro:

```text
VERIFY_AD_ACCOUNT=...2327
VERIFY_CAMPAIGN_INVENTORY=V3
VERIFY_STATUS=ACTIVE|ENDED|OTHER
VERIFY_PREPAID_BALANCE
THEN_ADD_FUNDS_IF_AUTHORIZED
```

No transferir dinero usando datos bancarios/referencias históricas fuera de una superficie oficial y validada de la cuenta correcta.

## Hipótesis y hechos separados

### Hechos verificados

- Facebook muestra el perfil como `Restringido`.
- Meta exige control de seguridad.
- El flujo oficial `IR A FACEBOOK` termina en bucle.
- La passkey existente autentica correctamente al usuario.
- 2FA y dispositivo de confianza están activos.
- Instagram funciona.
- Ads Manager/Business Suite no son utilizables por el bloqueo.
- El reporte técnico por Instagram fue enviado.
- Meta indicó que ese tipo de reporte no genera respuesta individual.
- Las ofertas Business Standard/Plus muestran soporte mejorado, pero el flujo observado vuelve a requerir Facebook.

### No demostrado todavía

- causa raíz interna exacta del checkpoint;
- que Meta haya abierto un ticket técnico individual;
- que Business Standard o Plus permitan soporte humano para el Facebook restringido sin autenticarse primero en ese Facebook;
- que otro administrador autorizado tenga acceso a la cuenta publicitaria standalone;
- estado vivo actual de campaña/saldo después del bloqueo;
- que la restricción tenga relación causal con algún cambio previo de seguridad.

## Estado de continuidad recomendado

```text
INCIDENT_OPEN=YES
TECH_REPORT_SENT=YES
INDIVIDUAL_META_REPLY_EXPECTED=NO
PAID_SUPPORT_AVAILABLE_IN_UI=YES
PAID_SUPPORT_USABLE_FOR_BLOCKED_FACEBOOK=NOT_VERIFIED
ADS_ADMIN_ACCESS=BLOCKED
COMMERCIAL_CONTINUITY_RISK=YES
```

Siguiente investigación útil al retomar:

1. identificar una vía de soporte humano que no requiera el mismo login Facebook bloqueado;
2. verificar si existe otro administrador real de la cuenta publicitaria standalone;
3. verificar si una superficie comercial/partner/agency puede abrir caso por esa cuenta sin compartir credenciales;
4. recuperar acceso o un fallback seguro antes de rediseñar ownership;
5. una vez estable, reducir dependencia de un único perfil personal para administración y facturación.
