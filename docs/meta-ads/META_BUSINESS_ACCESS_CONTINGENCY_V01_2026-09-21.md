# Meta — continuidad de acceso y eliminación de punto único de falla

Fecha: 2026-09-21  
Repo: `misaeln-pc1/marketing-performance-capacita`  
Issue: #112  
Estado: `DRAFT_NO_VIGENTE / PENDIENTE_EJECUCION_CONTROLADA`

## 1. Objetivo

Evitar que un bloqueo futuro del perfil Facebook de Misael deje simultáneamente sin acceso a:

- Página Capacita;
- Instagram vinculado;
- Meta Business Suite;
- Ads Manager;
- facturación/pagos;
- soporte Meta;
- continuidad de campañas.

## 2. Arquitectura objetivo

```text
CAPACITA SPA
│
├─ Admin humano primario: Misael
│  ├─ cuenta Facebook real actual
│  ├─ email/teléfono propios
│  └─ 2FA + backup codes propios
│
├─ Admin humano secundario: PERSONA_REAL_DE_MAXIMA_CONFIANZA
│  ├─ cuenta Facebook personal real propia
│  ├─ email/teléfono independientes
│  └─ 2FA + backup codes independientes
│
├─ Business Portfolio: Capacita Spa
│  ├─ Página Facebook Capacita
│  ├─ Instagram operativo
│  ├─ cuenta Ads empresarial futura
│  └─ personas/permisos auditados
│
└─ Cuenta Ads histórica ...2327
   └─ mantener operativa mientras exista transición; no mover ownership por reflejo
```

## 3. Qué NO es redundancia

No usar como contingencia:

- otro correo conectado al mismo Facebook;
- otra passkey del mismo usuario;
- otro dispositivo del mismo usuario;
- segundo perfil adicional bajo la misma cuenta;
- segunda cuenta personal duplicada “Misael 2”;
- credenciales compartidas con terceros;
- System User como sustituto de un administrador humano.

Todos esos casos mantienen o crean un punto único de falla distinto.

## 4. Fase 0 — inventario READ

Antes de modificar permisos:

```text
VERIFY_PAGE_CAPACITA_OWNER_AND_ACCESS
VERIFY_BUSINESS_PORTFOLIO_CAPACITA_SPA
VERIFY_INSTAGRAM_LINK
VERIFY_AD_ACCOUNT_2327_CURRENT_OWNER
VERIFY_CURRENT_PEOPLE_AND_PARTNERS
VERIFY_PAYMENT_METHODS
VERIFY_RECOVERY_EMAILS_AND_PHONES
```

Evidencia esperada: inventario sanitizado, sin IDs completos ni datos de pago.

Semáforo: Verde/Amarillo READ.

## 5. Fase 1 — segundo administrador humano

Elegir **una persona real de máxima confianza**, por ejemplo un familiar directo o futuro responsable administrativo formal.

Requisitos:

- cuenta Facebook personal propia y legítima;
- nombre real;
- acceso estable a su correo y teléfono;
- 2FA activado con su propio autenticador;
- códigos de recuperación almacenados por esa persona;
- compromiso de no compartir contraseña.

### Permiso objetivo

Para verdadera contingencia, el segundo administrador debe tener acceso suficiente para:

- entrar a la Página;
- operar Business Suite;
- administrar anuncios;
- mantener cuentas vinculadas;
- abrir soporte;
- restaurar acceso a Misael o agregar otro admin si Misael queda bloqueado.

Meta documenta que sólo quienes tienen **full control** de una Página pueden gestionar accesos y que full control permite también administrar cuentas vinculadas y anuncios.

**Riesgo:** una persona con full control también puede retirar otros accesos o borrar la Página. Por eso sólo debe asignarse a alguien de máxima confianza.

Semáforo: Rojo por permisos. Requiere autorización explícita antes de ejecutar.

## 6. Fase 2 — Business Portfolio como plano de control

Objetivo:

```text
PERSONA
≠
ACTIVO
```

La Página, Instagram y futuras cuentas Ads deben quedar administrables desde el Business Portfolio de Capacita, con al menos dos administradores humanos independientes.

No mover activos si hoy no es necesario. Primero verificar el estado real y después agregar redundancia.

## 7. Fase 3 — cuenta Ads

### Estado actual

```text
META_ADS_CURRENT=...2327
TYPE=PERSONAL_STANDALONE
CAMPAIGN=V3
```

### Estrategia recomendada

No transferir ownership de golpe.

```text
ETAPA_A
mantener ...2327 activa

ETAPA_B
dar acceso formal al Business/segundo admin si Meta lo permite sin cambiar ownership

ETAPA_C
crear cuenta Ads empresarial nueva dentro de Capacita Spa

ETAPA_D
probar una campaña pequeña/controlada

ETAPA_E
migrar futuras campañas gradualmente

ETAPA_F
mantener ...2327 como histórico/fallback hasta comprobar estabilidad
```

Así se elimina la dependencia futura de una cuenta Ads personal sin arriesgar la campaña actual de una vez.

## 8. Fase 4 — pagos

Objetivo: evitar que la ausencia de un único usuario impida financiar campañas.

Checklist:

- método de pago empresarial primario;
- segundo método válido si Meta lo admite;
- administrador secundario con permiso suficiente para revisar facturación;
- datos bancarios nunca almacenados en GitHub;
- prueba READ de facturación desde sesión secundaria.

Dinero = Rojo. Cualquier alta/cambio/cobro requiere autorización explícita.

## 9. Fase 5 — recuperación independiente

Cada administrador mantiene:

- correo propio;
- teléfono propio;
- app autenticadora propia;
- passkey propia si corresponde;
- backup codes propios;
- dispositivo de confianza propio.

Además, Capacita mantiene:

- correo corporativo de recuperación/verificación;
- dominio corporativo controlado;
- documentos legales de empresa accesibles sólo en repositorio privado autorizado;
- Meta Verified Business como canal de soporte mientras aporte valor.

## 10. Runbook de incidente

### Si Misael queda bloqueado

```text
1. NO tocar contraseña/2FA de Misael por reflejo
2. Admin secundario entra con su propia cuenta
3. Verifica Página + Business + Ads
4. Mantiene campaña/facturación sólo si está autorizado
5. Abre soporte Meta
6. Confirma que Misael sigue listado
7. No cambia ownership salvo necesidad real
8. Documenta caso/ticket
```

### Si el segundo admin queda bloqueado

Misael ejecuta el mismo flujo en sentido inverso.

### Si ambos quedan bloqueados

Escalar por:
- Meta Verified Business;
- soporte empresarial oficial;
- documentación societaria y de dominio;
- runbook de recuperación del Business.

## 11. Simulacro trimestral READ

Cada 90 días:

```text
ADMIN_PRIMARY_LOGIN=PASS
ADMIN_SECONDARY_LOGIN=PASS
PAGE_ACCESS_BOTH=PASS
BUSINESS_SUITE_BOTH=PASS
ADS_READ_BOTH=PASS
BILLING_READ_AUTHORIZED=PASS
INSTAGRAM_LINK=PASS
RECOVERY_CHANNELS_CURRENT=PASS
```

No modificar campañas ni pagos durante el simulacro.

## 12. Prioridad recomendada

```text
P0  Designar segundo administrador real
P1  Inventario READ de activos/accesos
P2  Dar acceso redundante a Página/Business
P3  Validar sesión independiente
P4  Diseñar cuenta Ads empresarial futura
P5  Redundancia de pagos
P6  Simulacro trimestral
```

## 13. Decisiones pendientes de Misael

1. Quién será la persona real de confianza.
2. Si tendrá full control o un esquema escalonado hasta validar.
3. Cuándo migrar nuevas campañas hacia una cuenta Ads empresarial.
4. Cuánto tiempo mantener Meta Verified Business después de estabilizar la contingencia.

## 14. Definition of Done

```text
NO_DUPLICATE_MISAEL_ACCOUNT=PASS
SECOND_REAL_HUMAN_ADMIN=VALIDATED
PAGE_REDUNDANCY=PASS
BUSINESS_REDUNDANCY=PASS
ADS_CONTINUITY_PATH=PASS
RECOVERY_INDEPENDENCE=PASS
PAYMENT_CONTINGENCY=DEFINED
QUARTERLY_DRILL=DEFINED
```
