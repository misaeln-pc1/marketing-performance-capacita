# Meta Ads — routing operativo de cuenta publicitaria

## Estado

- Fecha de registro: 2026-07-26.
- Fuente primaria: revisión visual guiada por Misael en Meta Business Settings / Ads Manager.
- Alcance: documentación operativa para evitar seleccionar el portafolio equivocado al preparar lectura read-only con Marketing API / Ads Insights.
- Sensibilidad: no incluir tokens, secretos, capturas, exports ni PII en GitHub.

## Decisión operativa

Para lectura de campañas Meta Ads de Capacita, no asumir que la cuenta publicitaria activa está dentro de los tres portafolios comerciales visibles.

La cuenta publicitaria usada para las campañas aparece en Ads Manager como **activo aparte / otros activos**, no como cuenta propia disponible dentro de estos portafolios:

| Portafolio visible | Señal observada | Uso para reportería actual |
|---|---:|---|
| `Capacita Spa` | muestra una cuenta publicitaria propia sin campañas activas observadas en la revisión | No usar como primera opción para el export actual |
| `Capacita` | 0 cuentas publicitarias | No usar |
| `Misael Novoa Jara` | 0 cuentas publicitarias | No usar |
| `Otros activos` | 1 cuenta publicitaria con campañas históricas visibles | Usar para lectura read-only actual |

## Cuenta objetivo

- Cuenta objetivo operativa: cuenta publicitaria visible en Ads Manager bajo **Otros activos**.
- Identificador completo: no se registra en GitHub público por regla de seguridad del repo.
- Sufijo visible para validación humana: `...9327`.
- En la URL de Ads Manager se observa el parámetro `act=` correspondiente a esa cuenta.

## Evidencia funcional observada

Al seleccionar la cuenta bajo **Otros activos**, Ads Manager muestra campañas históricas y campañas con error de pago/fondos. En cambio, al seleccionar los portafolios `Capacita`, `Capacita Spa` o `Misael Novoa Jara`, no se observa el mismo inventario operativo de campañas.

## Regla para API / Ads Insights

Antes de generar token o ejecutar export read-only:

1. seleccionar/confirmar la cuenta publicitaria desde Ads Manager;
2. validar que el `act_...` corresponda a la cuenta bajo **Otros activos**;
3. no usar automáticamente la cuenta propia del portafolio `Capacita Spa` solo porque aparece dentro de Business Settings;
4. usar únicamente permisos de lectura (`ads_read`) para el piloto;
5. no usar `ads_management`, `leads_retrieval` ni permisos de escritura;
6. no subir tokens, App Secret, capturas, CSV crudos ni IDs completos al repo.

## Implicación práctica

La ruta operativa correcta para el trabajo actual es:

```text
Ads Manager → selector de cuenta publicitaria → Otros activos → cuenta publicitaria activa con campañas históricas
```

No es:

```text
Business Settings → Capacita Spa → cuenta publicitaria propia visible
```

salvo que en una revisión posterior se confirme que esa cuenta fue migrada, reclamada o que las campañas reales fueron movidas.

## Próximo paso recomendado

Para el script read-only de Ads Insights, solicitar el `act_...` completo localmente en PowerShell mediante entrada segura o variable `.env` privada. GitHub solo debe registrar la decisión de routing y resultados agregados sanitizados.
