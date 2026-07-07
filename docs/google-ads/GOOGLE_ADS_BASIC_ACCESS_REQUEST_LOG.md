# Google Ads Basic Access Request Log

## Estado

- Solicitud de Google Ads API Basic Access enviada el 2026-07-06.
- La solicitud se hizo desde el MCC / Manager de Capacita usado para API Center.
- No se versionan IDs completos de cuentas, credenciales ni archivos locales sensibles.

## Motivo

El pipeline local read-only ya quedo preparado y pudo llegar a Google Ads API, pero la consulta de ideas de keywords contra una cuenta real quedo bloqueada porque el acceso actual solo permite cuentas de prueba.

## Alcance declarado

- Herramienta interna de Capacita.
- Usuarios internos solamente.
- Campaign type: Search.
- Capabilities: Reporting y Keyword Planning Services.
- Sitio web: https://capacita.cl.
- Uso: lectura agregada, reporting y keyword research para planificacion comercial de cursos presenciales Santiago Centro.

## Fuera de alcance declarado

- No crear campanas.
- No modificar campanas.
- No cambiar presupuestos, bids, anuncios, assets, conversiones ni configuracion de cuenta.
- No usar App Conversion Tracking ni Remarketing API.
- No exponer la herramienta a clientes o publico general.

## Estado tecnico validado

- PR #14 fue mergeado a main.
- Se instalo la libreria local `google-ads`.
- Se creo configuracion local fuera del repo.
- Se regenero ADC/OAuth con scope Google Ads.
- La primera lectura read-only funciono.
- La consulta de ideas de keywords quedo pendiente hasta que Google apruebe Basic Access.

## Siguiente accion

1. Esperar respuesta de Google.
2. Mientras tanto, usar Keyword Planner manual si se necesita radar comercial inmediato.
3. Cuando Basic Access sea aprobado, repetir la prueba local read-only y exportar resultados locales no versionados.
