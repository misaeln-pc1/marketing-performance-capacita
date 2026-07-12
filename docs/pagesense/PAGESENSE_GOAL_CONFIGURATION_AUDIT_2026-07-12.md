# Auditoría de configuración de goals PageSense — 2026-07-12

## Alcance

Confirmar qué mide realmente cada goal revisado mediante capturas privadas de configuración y contrastarlo con la arquitectura pública sanitizada de las landings.

Los screenshots originales permanecen fuera del repositorio. Este documento conserva sólo la conclusión operativa.

## Resultado confirmado

Los tres objetivos revisados son de tipo **Pulsaciones en elementos**. Ninguno demuestra por sí solo un submit aceptado por Zoho Forms ni la creación de un lead.

### `enviar Pre`

- Página: landing B2C de Excel presencial.
- Tipo: pulsación en elementos.
- Elementos: dos selectores asociados a botones, entre ellos la clase del botón submit del formulario.
- Interpretación correcta: clic o intento sobre botón/elemento.
- Interpretación incorrecta: formulario aceptado, lead creado o matrícula.

La configuración explica la discrepancia entre cientos de goals/clics y cerca de 30 envíos implícitos en Form Analytics.

### `inicio`

- Página: home de Capacita.
- Tipo: pulsación en elementos.
- Elementos: cinco selectores repetidos asociados a elementos del home.
- No mide carga de página, inicio de sesión ni inicio de formulario.
- El nombre `inicio` es ambiguo y no debe usarse dentro del funnel comercial de la landing B2C.

### `Enviar Empresa-Excel`

- Página: landing B2B de Excel para empresas.
- Tipo: pulsación en elemento.
- Elemento: botón de envío identificado por su conjunto de clases CSS.
- Interpretación correcta: clic o intento de envío.
- Interpretación incorrecta: propuesta enviada o lead B2B confirmado.

El selector basado en la cadena completa de clases es además frágil ante cambios de diseño, orden de clases o framework.

## Contraste con arquitectura Edge

### B2C Excel presencial

La landing vigente mantiene temporalmente un flujo legacy con POST directo a Zoho Forms. El campo de redirección está vacío en el HTML actual y no existe un evento frontend confirmado posterior a la aceptación.

Consecuencia: el clic puede medirse, pero el éxito real requiere identificar la página/mensaje de confirmación de Zoho o migrar el flujo mediante un cambio técnico controlado.

### B2B Excel empresas

La landing B2B usa el endpoint Edge `/api/forms/lead`. La arquitectura documentada establece que el éxito termina en una redirección a la landing con `?lead=ok#registro`.

Consecuencia: el goal primario B2B debería basarse en esa condición de éxito o en un custom event disparado después de confirmarla, no en el clic del botón.

## Clasificación de goals

| Goal actual | Clasificación | Uso permitido |
|---|---|---|
| `enviar Pre` | click/intent B2C | Diagnóstico secundario |
| `inicio` | click ambiguo en home | No usar en funnel comercial |
| `Enviar Empresa-Excel` | click/intent B2B | Diagnóstico secundario |

## Recomendación mínima

1. No borrar los goals actuales: conservar continuidad histórica y reclasificarlos como métricas secundarias de interacción.
2. No usarlos como conversiones primarias en PageSense, Google Ads ni dashboard comercial.
3. Crear goals nuevos de éxito sólo cuando exista evidencia inequívoca:
   - B2B: URL con `lead=ok` o custom event posterior a la confirmación.
   - B2C: confirmar primero el destino/mensaje posterior al submit Zoho o aprobar una migración técnica separada.
4. Mantener separados:
   - clic CTA;
   - inicio de formulario;
   - intento de submit;
   - submit confirmado;
   - lead recibido en Zoho CRM;
   - matrícula.

## Riesgo

**Amarillo.** Cambiar PageSense, GTM, el flujo del formulario o la redirección afecta medición e integración productiva. Requiere issue técnico dueño en Capacita Edge, prueba controlada, evidencia y autorización previa.

## Próximo gate

- Verificar en una prueba controlada qué URL o mensaje aparece tras un envío B2C exitoso, sin exponer PII.
- Definir el evento canónico de submit confirmado.
- Reconciliar una muestra agregada con Zoho CRM.
- Recién después activar A/B o Split URL de la variante con énfasis básico.
