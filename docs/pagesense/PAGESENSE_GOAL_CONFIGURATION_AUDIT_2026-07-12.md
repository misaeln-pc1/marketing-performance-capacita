# Auditoría de configuración de goals PageSense — 2026-07-12

## Alcance

Confirmar qué mide realmente cada goal revisado mediante capturas privadas de configuración y contrastarlo con la arquitectura pública sanitizada de las landings y con la configuración posterior al envío de Zoho Forms.

Los screenshots originales permanecen fuera del repositorio. Este documento conserva solo la conclusión operativa.

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

El selector basado en la cadena completa de clases es frágil ante cambios de diseño, orden de clases o framework.

## Configuración posterior al envío confirmada

### Formulario principal B2C del héroe

Zoho Forms está configurado para redirigir, después de un envío aceptado, a una página de agradecimiento de `capacita.cl` con un identificador del producto.

La redirección actual incorpora además nombre y correo mediante parámetros de URL.

Conclusiones:

- la visita a la página de agradecimiento sí puede convertirse en un goal de submit confirmado;
- el identificador del formulario/producto permite separar el formulario principal de otras acciones;
- nombre y correo no deben viajar en query string.

**Riesgo rojo de privacidad:** los datos personales en URL pueden quedar expuestos en historial del navegador, analytics, logs, referrers, capturas, herramientas de sesión y sistemas de terceros.

Mitigación mínima:

- conservar solo un identificador no personal del formulario/origen;
- eliminar nombre y correo de la URL de redirección;
- validar que la página de agradecimiento no replique datos personales en HTML ni `dataLayer`;
- probar un submit controlado antes de usar el nuevo goal en Google Ads o PageSense.

### Formulario secundario de descarga de temario

Zoho Forms muestra una página de agradecimiento interna y envía el temario por correo. No redirige actualmente a una página propia diferenciada de `capacita.cl`.

Conclusiones:

- su submit puede estar disponible para GA/Pixel si el tracking interno está correctamente configurado;
- PageSense en la landing no puede asumir ese éxito desde el clic del botón;
- esta acción debe clasificarse como lead magnet o conversión secundaria, no como lead comercial principal;
- para una medición unificada conviene redirigir posteriormente a una URL propia y distinta, sin datos personales.

Ejemplo conceptual sanitizado:

```text
/gracias/?id=descarga_temario_excel&origen=temario
```

## Contraste con arquitectura Edge

### B2C Excel presencial

La landing vigente mantiene temporalmente un flujo legacy con POST directo a Zoho Forms. La configuración interna de Zoho ya confirma una URL de éxito posterior al submit.

Consecuencia: el goal primario B2C debe basarse en la página de agradecimiento más el identificador no personal del formulario, no en el clic del botón.

### B2B Excel empresas

La landing B2B usa el endpoint Edge `/api/forms/lead`. La arquitectura documentada establece que el éxito termina en una redirección a la landing con `?lead=ok#registro`.

Consecuencia: el goal primario B2B debería basarse en esa condición de éxito o en un custom event disparado después de confirmarla, no en el clic del botón.

## Clasificación de goals y formularios

| Elemento | Clasificación | Uso permitido |
|---|---|---|
| `enviar Pre` | click/intent B2C | Diagnóstico secundario |
| `inicio` | click ambiguo en home | No usar en funnel comercial |
| `Enviar Empresa-Excel` | click/intent B2B | Diagnóstico secundario |
| éxito formulario héroe B2C | submit confirmado técnico | Conversión primaria técnica; reconciliar con CRM |
| descarga de temario | lead magnet/submit secundario | Conversión secundaria |
| matrícula o deal ganado | resultado comercial | Fuente Zoho CRM, no PageSense |

## Recomendación mínima

1. No borrar los goals actuales: conservar continuidad histórica y reclasificarlos como métricas secundarias de interacción.
2. No usarlos como conversiones primarias en PageSense, Google Ads ni dashboard comercial.
3. Corregir primero la redirección B2C para eliminar datos personales de la URL.
4. Crear un goal nuevo de éxito B2C basado en la página de agradecimiento y el identificador no personal del formulario.
5. Mantener la descarga de temario como conversión secundaria y medirla por una ruta/identificador propio cuando se apruebe.
6. Crear el goal B2B sobre `lead=ok` o custom event posterior a la confirmación.
7. Mantener separados: clic CTA, inicio de formulario, intento de submit, submit confirmado, lead recibido en Zoho CRM y matrícula.

## Riesgo

- **Rojo:** nombre y correo presentes en URL de redirección B2C. Deben retirarse antes de usar esa URL como objetivo o compartirla con herramientas adicionales.
- **Amarillo:** cambiar PageSense, GTM, el flujo del formulario o la redirección afecta medición e integración productiva. Requiere issue técnico dueño en Capacita Edge, prueba controlada, evidencia y autorización previa.

## Próximo gate

- corregir la URL de redirección B2C sin PII;
- ejecutar un submit controlado y confirmar la URL final;
- definir el goal canónico de submit confirmado;
- revisar la medición de la descarga de temario como conversión secundaria;
- reconciliar una muestra agregada con Zoho CRM;
- recién después activar A/B o Split URL de la variante con énfasis básico.
