# REVIEW_REQUEST

## Objetivo de revisión vigente

Validar el Bootstrap y diseño mínimo del **Connected Marketing Analytics Pilot** para Excel B2C presencial Santiago, reutilizando capacidades maduras sin migrar rutas actuales ni ejecutar writes externos.

## Rama

```text
docs/marketing-connected-analytics-pilot-20260814
```

## Alcance del PR

Revisar que:

1. se preserva Google Ads API/PowerShell como fallback y el MCP oficial sólo se evalúa por paridad/ganancia material;
2. se preserva Meta API `ads_read` y el account routing canónico;
3. GA4 queda como capa distinta de Ads y CRM;
4. conversión de plataforma, GA4 key event, Lead/Contact, Deal, CursoAlumno y venta real nunca se presentan como equivalentes;
5. los `DATA_GAP` de downstream no se rellenan por inferencia;
6. las tres skills P0 quedan `ADAPTAR_MINIMO`, sin declarar lifecycle `approved`;
7. el competitive brief usa sólo evidencia pública y no inventa tráfico, ventas, ROAS, presupuestos o conversiones de terceros;
8. el XFER a System Integration exige read-only, sin OAuth nuevo, instalaciones, secretos, PII ni writes;
9. issue #60 recibe Bootstrap PASS, pero la prueba Delta posterior permanece pendiente.

## Archivos creados

```text
docs/analytics/CONNECTED_MARKETING_ANALYTICS_PILOT_2026-08-14.md
SKILLS_USED.md
docs/xfer/XFER__MARKETING__SYSTEM_INTEGRATION__CONNECTED_ANALYTICS_READ_PILOT__20260814__v01__READY.md
```

## Archivos actualizados

```text
docs/BITACORA_XFER.md
DECISIONES.md
TASK_STATUS.md
CHANGELOG_AGENT.md
REVIEW_REQUEST.md
```

## Hallazgos a revisar

### Google Ads

- El histórico conectado llega hasta `2026-08-13`.
- El estado se mantiene **provisional** hasta combinar histórico con una lectura API/MCP fresca equivalente.
- La keyword `curso excel básico e intermedio` sigue concentrando gasto con eficiencia de plataforma inferior al promedio reciente.
- No se propone cambiar negativas, keywords, pujas o campaña.

### Atribución

```text
ADS_PLATFORM_SIGNAL
!= GA4_SITE_SIGNAL
!= CRM_LEAD_OR_CONTACT
!= DEAL
!= CURSOALUMNO
!= VENTA_REAL
```

El mapping CRM de API names permanece `DATA_GAP` hasta validación del repo técnico dueño.

### Competencia

Activa Latam aparece como amenaza directa inicial por superposición de Santiago Centro, propuesta práctica y precio público bajo. EFTEC, INACAP y Pro-Active son comparables complementarios. Reviews, Ads Library validada y tráfico SEO quedan `DATA_GAP` donde no existe evidencia suficiente.

## No se toca

- OAuth o credenciales nuevas;
- instalaciones;
- Google Ads o Meta Ads writes;
- campañas, presupuestos, pujas, anuncios, públicos, keywords o negativas reales;
- GA4/GTM productivo;
- landings/Cloudflare producción;
- CRM writes;
- WhatsApp;
- secretos, PII, IDs completos, exports crudos o binarios.

## Validación esperada

- Sólo Markdown/documentación sanitizada.
- Branch fuera de `main`.
- XFER registrado `READY` v01.
- Skills registradas sin cambiar lifecycle AI OS.
- No PII, secretos, tokens, `.env`, IDs completos ni binarios.
- Ningún ganador MCP declarado antes del micro-piloto.
- `DATA_GAP` explícito para GA4/CRM/Deal/CursoAlumno/venta y creative cuando corresponda.
- Issue #60 no se cierra: Delta pendiente.

## Gate

```text
REQUIERE_REVISION_MISAEL
NO_MERGEAR_TODAVIA
```

No mergear hasta revisión de Misael y validación del diff final.
