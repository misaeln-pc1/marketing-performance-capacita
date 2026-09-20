# Meta/Facebook — investigación externa sobre Advanced Protection — 2026-09-20

## Alcance

Complementa el incidente canónico:

`docs/incidents/META_FACEBOOK_RESTRICTED_ADVANCED_PROTECTION_LOOP_2026-09-19.md`

No reemplaza sus guardrails ni autoriza pagos, cambios de seguridad, permisos, ownership o Ads.

## Hallazgo principal

Meta documenta que Facebook Protect pasó a llamarse **Protección avanzada / Advanced Protection** y que algunas cuentas pueden quedar obligadas a completar ese flujo.

Entre el 15 y el 20 de septiembre de 2026 aparecieron múltiples reportes independientes con una secuencia prácticamente idéntica al incidente Capacita:

```text
LOGIN_OR_OTP_ACCEPTED
→ CHECKPOINT_ADVANCED_PROTECTION
→ BLANK/META_LOGO/ERR_TOO_MANY_REDIRECTS
→ MULTIPLE_DEVICES_FAIL
→ INSTAGRAM_STILL_WORKS_IN_MANY_CASES
```

Esto refuerza, sin demostrar causa raíz, la hipótesis de un fallo/desincronización del checkpoint de Meta.

```text
LEADING_HYPOTHESIS=ADVANCED_PROTECTION_CHECKPOINT_STATE_DESYNC_OR_PLATFORM_BUG
CONFIDENCE=MEDIUM_HIGH
ROOT_CAUSE_OFFICIALLY_CONFIRMED=NO
```

## Ruta gratuita prioritaria

Antes de pagar, inspeccionar desde la app oficial de Instagram:

```text
Instagram
→ Centro de cuentas
→ Contraseña y seguridad
→ Protección avanzada / Advanced Protection
```

Objetivo:

- verificar si aparece el Facebook afectado;
- ver si el estado figura pendiente, activado o requiere acción;
- comprobar si el flujo puede iniciarse desde Instagram o si vuelve a exigir Facebook.

Durante esta inspección:

```text
PASSWORD_WRITE=0
2FA_WRITE=0
PASSKEY_WRITE=0
DEVICE_WRITE=0
PAYMENT_WRITE=0
```

## Micro-piloto candidato — Meta Verified desde Instagram

Meta documenta que Meta Verified para creadores exige Protección avanzada en el perfil elegible y que suscriptores activos disponen de soporte por chat/email desde la app, con ID de caso.

La señal comunitaria contemporánea es mixta:

- varios usuarios con el mismo checkpoint informaron recuperación tras activar Meta Verified desde un Instagram ya vinculado y completar el flujo de Protección avanzada/2FA;
- otros usuarios, incluso ya verificados, siguieron bloqueados.

Por tanto:

```text
PILOT=IG_META_VERIFIED_ADVANCED_PROTECTION_RESYNC
STATUS=PROPOSED_NOT_AUTHORIZED
PRIMARY_OBJECTIVE=TRY_SECURITY_STATE_RESYNC
SUPPORT_FOR_BLOCKED_FACEBOOK=NOT_GUARANTEED
RISK=YELLOW_MONEY_AND_SECURITY
```

### Fase A — sin pago

1. usar sólo la app oficial de Instagram;
2. confirmar que Instagram y Facebook están en el mismo Centro de cuentas;
3. revisar si Meta Verified para creador/personal puede iniciarse sin autenticar el Facebook bloqueado;
4. revisar precio o prueba visible;
5. detenerse antes de confirmar suscripción o modificar seguridad.

### Fase B — sólo con autorización expresa de Misael

1. activar la suscripción desde la superficie oficial elegible;
2. no desactivar 2FA;
3. no borrar passkeys ni dispositivos;
4. si Meta ofrece completar Protección avanzada desde Instagram, seguir sólo el flujo oficial sin reducir seguridad;
5. probar Facebook una sola vez;
6. si persiste el bucle, detener el piloto.

## Soporte humano

Meta indica que no existe un número telefónico público general para soporte de Facebook.

El soporte de Meta Verified está disponible para suscriptores activos desde la app compatible y genera un ID de caso. No asumir que una suscripción sólo de Instagram garantiza resolución del Facebook restringido.

```text
PUBLIC_FACEBOOK_PHONE_SUPPORT=NO
META_VERIFIED_IG_HUMAN_SUPPORT=AVAILABLE_IF_ACTIVE_SUBSCRIBER
CROSS_PROFILE_FACEBOOK_SUPPORT=NOT_GUARANTEED
```

## Continuidad comercial

No existe evidencia documental actual de otro administrador autorizado de la cuenta standalone `...2327`.

```text
OTHER_ADMIN=NOT_VERIFIED
SAFE_EXTERNAL_TOPUP_ROUTE=NOT_VERIFIED
```

No usar referencias bancarias históricas, no reclamar/mover propiedad y no crear una cuenta nueva como sustituto por reflejo.

Si aparece otro administrador ya autorizado, primero validar en READ:

```text
VERIFY_AD_ACCOUNT=...2327
VERIFY_CAMPAIGN_INVENTORY=V3
VERIFY_STATUS
VERIFY_PREPAID_BALANCE
```

Cualquier pago o cambio de permisos requiere autorización específica.

## Fuentes

Oficiales:

- https://www.facebook.com/help/1052552578831700?locale=es_LA
- https://www.facebook.com/help/2419286908233223
- https://www.facebook.com/help/178774494481770
- https://www.facebook.com/help/search/?locale=es_LA&query=contact+phone+numbers

Señal comunitaria auxiliar:

- https://www.reddit.com/r/facebook/comments/1wh6lvc/locked_out_of_facebook_messenger_meta_ads_for_15/
- https://www.reddit.com/r/facebook/comments/1win8cg/facebook_locked_advanced_protection_checkpoint/
- https://www.reddit.com/r/facebook/comments/1w2yuwc/facebook_account_locked_on_advanced_protection/
- https://www.reddit.com/r/facebook/comments/1vru3dg/facebook_account_locked_in_advanced_protection/

## Decisión

Este delta **complementa** el baseline vigente.

Siguiente acción recomendada:

```text
READ_ONLY_INSPECTION_INSTAGRAM_ADVANCED_PROTECTION
```

Sólo si esa ruta no resuelve y la interfaz de Meta Verified es utilizable sin Facebook, evaluar el piloto pagado mediante gate humano.


## Resultado del micro-check gratuito desde Instagram — 2026-09-20

Evidencia visual revisada desde la app oficial de Instagram / Centro de cuentas, sin subir capturas ni PII al repo.

Hallazgos:

```text
INSTAGRAM_ACCOUNTS_CENTER=PASS
FACEBOOK_PROFILE_STATUS=RESTRICTED
INSTAGRAM_PROFILE_STATUS=NORMAL
THREADS_PROFILE_STATUS=NORMAL
FACEBOOK_STILL_LINKED_TO_META_ACCOUNT=YES
FACEBOOK_PAGES_ADMIN_RELATIONSHIP_VISIBLE=YES
SECURITY_CHECKUP_RECOMMENDATION=CREATE_PASSKEY_ONLY
EXISTING_PASSKEY_ALREADY_CONFIRMED=YES
ADVANCED_PROTECTION_CONTROL_VISIBLE_IN_IG_ACCOUNTS_CENTER=NO
FREE_IG_ADVANCED_PROTECTION_ROUTE=NOT_EXPOSED
```

La pantalla de seguridad muestra como controles visibles:

- comprobación rápida de seguridad;
- información de contacto;
- contraseña;
- autenticación en dos pasos;
- selfie de verificación;
- inicio de sesión guardado;
- llave de acceso;
- dónde iniciaste sesión;
- correos electrónicos de Meta.

No aparece un control separado de `Protección avanzada / Advanced Protection / Facebook Protect`.

La comprobación rápida de seguridad propone únicamente crear una nueva llave de acceso. Esa acción no se ejecuta porque ya existe una passkey funcional y el incidente falla después de autenticar.

Además, el perfil Facebook sigue administrando páginas dentro del Centro de cuentas. No ejecutar `Quitar de esta cuenta de Meta`, `Desactivación o eliminación` ni cambios de vínculo durante el incidente.

### Decisión del delta

```text
READ_ONLY_INSPECTION_INSTAGRAM_ADVANCED_PROTECTION=COMPLETE
RESULT=NO_ADVANCED_PROTECTION_CONTROL_EXPOSED
NEXT_CANDIDATE=IG_META_VERIFIED_ADVANCED_PROTECTION_RESYNC
STATUS=PROPOSED_NOT_AUTHORIZED
```

La ruta gratuita específica de Protección avanzada desde Instagram queda agotada con la interfaz actual. El siguiente candidato, si Misael decide continuar, es revisar la elegibilidad/flujo de Meta Verified desde Instagram **hasta antes de confirmar cualquier pago o cambio de seguridad**.
