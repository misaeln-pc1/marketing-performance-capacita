# Incidente Meta/Facebook — perfil restringido y bucle `advanced_protection`

Fecha del incidente documentado: 2026-09-19  
Repo dueño: `misaeln-pc1/marketing-performance-capacita`  
Estado: `HOLD_META_SUPPORT / RECOVERY_PENDING`  
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

