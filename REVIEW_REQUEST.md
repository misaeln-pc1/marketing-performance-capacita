# REVIEW_REQUEST

## Objetivo de revisión vigente

Revisar y consolidar la corrección definitiva del routing de cuenta Meta Ads para evitar que futuros chats, agentes o scripts vuelvan a confundir la cuenta operativa V3 con cuentas pertenecientes a Business Portfolios distintos.

## Rama

```text
docs/marketing-meta-ads-account-routing-20260809
```

## Hallazgo principal

La cuenta publicitaria que contiene la campaña operativa:

```text
META_TRAFFIC_EXCEL_PRESENCIAL_SANTIAGO_B2C_V3
```

es una cuenta personal/standalone accesible bajo `Otros activos`, referencia sanitizada:

```text
...2327
```

No pertenece actualmente a los Business Portfolios:

- `Capacita Spa`;
- `Capacita`;
- `Misael N. J.`.

La referencia histórica aproximada `...9327` queda `SUPERSEDED` y no debe usarse para identificar V3.

## Archivos modificados

```text
docs/meta-ads/META_ADS_ACCOUNT_ROUTING.md
DECISIONES.md
CHANGELOG_AGENT.md
REVIEW_REQUEST.md
```

## Reglas que deben quedar firmes

1. Identificar la cuenta operativa por inventario real de campañas, no por nombre de Business Portfolio.
2. La ruta actual de V3 es `Otros activos → cuenta personal ...2327`.
3. No inferir que una restricción histórica de WhatsApp afecta a la cuenta ...2327 sin evidencia por activo.
4. Account Quality de ...2327 no mostró restricciones publicitarias visibles en la auditoría 2026-08-09.
5. Un token API vencido afecta lectura API, no implica que la campaña esté pausada o bloqueada.
6. El límite de gasto diario mostrado por Meta no debe interpretarse como bloqueo si el panel indica que el gasto previsto está dentro del límite.
7. `Capacita Spa` es solo candidato futuro para System User: primero habría que compartir/asignar acceso a ...2327 sin mover propiedad.
8. Reclamar o mover propiedad sigue siendo riesgo rojo y requiere decisión específica.

## No se toca

- Meta Ads Manager;
- campañas;
- anuncios;
- presupuesto;
- fondos;
- facturación;
- Business Portfolios;
- permisos;
- System Users;
- tokens;
- WhatsApp;
- activos físicos o archivos externos.

## Validación esperada

- Solo Markdown.
- Sin IDs completos.
- Sin tokens, secretos, teléfonos, PII, capturas ni exports crudos.
- `...2327` queda como referencia sanitizada vigente para V3.
- `...9327` queda explícitamente superseded.
- No existe ninguna instrucción de reclamar/mover propiedad.
- El documento canónico único de routing sigue siendo `docs/meta-ads/META_ADS_ACCOUNT_ROUTING.md`.

## Feedback scan

`AGENT_FEEDBACK.md` no existe en `main`. El hallazgo relevante fue la desactualización del `REVIEW_REQUEST.md` anterior; este cambio lo reemplaza con la revisión vigente de routing Meta Ads.

## Gate

```text
LISTO_PARA_MERGE
REQUIERE_REVISION_MISAEL
```

Si el diff es correcto, el siguiente paso es autorización explícita de merge.
