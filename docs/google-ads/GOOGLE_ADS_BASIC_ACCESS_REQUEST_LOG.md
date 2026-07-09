# Google Ads Basic Access Request Log

## Estado

- Solicitud de Google Ads API Basic Access enviada el 2026-07-06.
- Basic Access aprobado por Google el 2026-07-08 segun correo recibido por Capacita.
- La solicitud se hizo desde el MCC / Manager de Capacita usado para API Center.
- No se versionan IDs completos de cuentas, credenciales ni archivos locales sensibles.

## Motivo

El pipeline local read-only ya quedo preparado y pudo llegar a Google Ads API, pero la consulta de ideas de keywords contra una cuenta real quedo inicialmente bloqueada porque el acceso anterior solo permitia cuentas de prueba.

Despues de la aprobacion de Basic Access, se ejecuto una primera prueba local read-only de `generate_keyword_ideas.py` contra la cuenta publicitaria real, usando configuracion externa local y sin versionar outputs reales.

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
- PR #16 fue mergeado a main con el log de solicitud de Basic Access.
- Se instalo la libreria local `google-ads`.
- Se creo configuracion local fuera del repo.
- Se regenero ADC/OAuth con scope Google Ads.
- `list_accessible_customers.py` funciono y mostro 2 cuentas accesibles con IDs enmascarados.
- `generate_keyword_ideas.py` funciono despues de Basic Access y genero salida local TSV no versionada.
- El output inicial mostro volumen muy bajo o cero para varias semillas, por lo que la API quedo validada pero el radar requiere ampliar semillas/geografia antes de sacar conclusiones comerciales.

## Siguiente accion

1. Mantener `google-ads.yaml` y scripts `.ps1` locales fuera del repo.
2. No versionar TSV bruto ni IDs completos.
3. Ampliar semillas hacia terminos mas amplios y variantes B2C/B2B.
4. Validar geografia objetivo antes de interpretar volumen bajo como baja demanda real.
5. Construir radar comercial agregado solo con datos anonimizados o resumidos.