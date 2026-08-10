# Meta Ads — routing operativo de cuenta publicitaria

## Estado

- Fecha de registro original: 2026-07-26.
- Última validación: 2026-08-09.
- Estado: `VIGENTE_EN_MAIN` por PR #54, merge SHA `4f9d7f9caf1a5868290dee4ed3cd911b6847aa14`.
- Fuente primaria: revisión visual en Ads Manager / Facturación y auditorías read-only por Work/Codex/API.
- Alcance: impedir que futuros chats, agentes o scripts seleccionen una cuenta o Business Portfolio equivocado al trabajar con Meta Ads de Capacita.
- Sensibilidad: no incluir tokens, secretos, capturas, exports crudos, teléfonos ni IDs completos en GitHub.

## Decisión operativa vigente

La cuenta publicitaria que contiene y entrega la campaña operativa de Excel presencial **NO pertenece a los portfolios comerciales visibles de Capacita**.

La cuenta operativa es una **cuenta publicitaria personal/standalone**, accesible en Meta bajo **`Otros activos`**, controlada directamente por Misael N. J.

Referencia sanitizada vigente:

```text
Cuenta publicitaria operativa Meta Ads: ...2327
```

El identificador completo no se registra en GitHub.

### Regla dura

No inferir la cuenta correcta desde el nombre de un Business Portfolio.

La cuenta correcta debe identificarse primero por su **inventario real de campañas**, especialmente:

```text
META_TRAFFIC_EXCEL_PRESENCIAL_SANTIAGO_B2C_V3
```

junto con:

```text
AS02_2026.06_LANDING_PAGADO_EXCEL_PRESENCIAL
```

y sus anuncios históricos/actuales.

Si una cuenta no contiene ese inventario, no debe usarse para reportería, API, Ads Insights ni configuración de la campaña V3 aunque esté dentro de un portfolio llamado Capacita.

## Separación entre cuenta operativa y portfolios

Validación 2026-08-09:

| Contenedor / portfolio | Relación con cuenta ...2327 | Tratamiento |
|---|---|---|
| `Capacita Spa` | No asociada actualmente | Business sano; candidato futuro para compartir/asignar acceso y crear System User, sin mover propiedad. |
| `Capacita` | No asociada actualmente | No usar como fuente de la campaña V3. |
| `Misael N. J.` | No asociada actualmente | No usar como fuente de la campaña V3. |
| `Otros activos` | Sí; agrupa la cuenta personal ...2327 | Ruta operativa actual para la cuenta que contiene V3. |

Por tanto, estas dos afirmaciones son simultáneamente verdaderas:

1. Existe un Business/portfolio `Capacita Spa` con sus propios activos.
2. La campaña V3 real vive en la cuenta personal ...2327 bajo `Otros activos`, separada de ese portfolio.

No mezclar ambas estructuras.

## Evidencia funcional vigente

La cuenta ...2327 fue confirmada por inventario API y por interfaz como la cuenta que contiene:

- `META_TRAFFIC_EXCEL_PRESENCIAL_SANTIAGO_B2C_V3`;
- `AS02_2026.06_LANDING_PAGADO_EXCEL_PRESENCIAL`;
- los anuncios históricos AD01/AD02/AD03;
- el anuncio de agosto `AD04_BP001_EXCEL_TIEMPO_AGOSTO_V1`.

En la auditoría 2026-08-09:

- cuenta: habilitada por API (`account_status=1`);
- V3: `ACTIVE / ACTIVE`;
- AS02: `ACTIVE / ACTIVE`;
- AD04: publicado y `ACTIVE / ACTIVE`;
- anuncios históricos de junio: pausados;
- Account Quality: sin problemas pendientes ni resueltos visibles en los últimos 90 días;
- restricciones publicitarias visibles: ninguna;
- fondos: disponibles;
- pagos pendientes visibles: ninguno.

### Aclaración sobre límite de gasto

La pantalla de facturación mostró un **límite de gasto diario establecido por Meta**, pero también indicó que el gasto previsto estaba dentro de ese límite.

Eso **no equivale a un bloqueo por límite alcanzado**.

No interpretar automáticamente `límite de gasto diario` como causa de falta de entrega. Verificar siempre el texto/estado actual de facturación y la entrega real.

## Cuenta o activo históricamente bloqueado

Misael recuerda un incidente histórico asociado a WhatsApp y/o una cuenta antigua.

La auditoría 2026-08-09 no identificó un WABA restringido ni demostró que ese incidente esté relacionado con ...2327.

Regla:

```text
No inferir "WhatsApp bloqueado = cuenta publicitaria ...2327 bloqueada".
```

Estado actual:

- activo histórico bloqueado: `NO IDENTIFICADO`;
- relación con ...2327: `NO DEMOSTRADA`;
- impacto actual sobre V3: no hay evidencia visible de restricción.

Si en el futuro aparece un activo restringido, documentarlo por tipo: perfil, Business, cuenta publicitaria, Page, Instagram, WABA o número WhatsApp. No propagar la restricción por asociación sin evidencia.

## Corrección de referencia histórica

La referencia antigua aproximada:

```text
...9327
```

queda **SUPERSEDED / NO USAR PARA IDENTIFICAR LA CUENTA V3**.

La referencia sanitizada confirmada por inventario real es:

```text
...2327
```

Ante conflicto entre memoria, sufijo antiguo o nombre de portfolio, manda el inventario de campañas de la cuenta.

## Ruta correcta para trabajo actual

```text
Ads Manager
→ selector de cuenta publicitaria
→ Otros activos
→ cuenta personal ...2327
→ validar que contiene META_TRAFFIC_EXCEL_PRESENCIAL_SANTIAGO_B2C_V3
```

No usar por defecto:

```text
Business Settings
→ Capacita Spa
→ cualquier cuenta publicitaria propia del portfolio
```

salvo que una futura migración/asignación autorizada cambie formalmente la relación de activos y quede documentada en este archivo.

## Regla para API / Ads Insights

Antes de ejecutar cualquier lectura API:

1. identificar la cuenta por inventario real, no por nombre del portfolio;
2. confirmar sufijo sanitizado vigente `...2327`;
3. usar el `act_...` completo únicamente en entorno local/privado;
4. usar por defecto solo `ads_read` para reportería;
5. no guardar tokens, App Secret ni IDs completos en GitHub;
6. mantener exports crudos fuera del repo.

## Tokens y acceso permanente

Los tokens humanos usados anteriormente eran temporales y expiraron. Su expiración bloquea la **lectura API**, no la entrega de las campañas en Ads Manager.

No confundir:

```text
token API vencido ≠ campaña Meta pausada/bloqueada
```

### Arquitectura futura recomendada

Business candidato sano:

```text
Capacita Spa
```

Pero ...2327 no pertenece actualmente a ese Business.

Ruta futura, solo con autorización específica:

```text
cuenta personal ...2327
→ compartir/asignar acceso formal a Capacita Spa
→ conservar propiedad personal existente
→ crear System User en Capacita Spa
→ asignar acceso read-only a ...2327
→ generar token permanente/read-only
```

No reclamar ni mover propiedad mientras no exista una razón específica, evidencia y aprobación humana.

- Compartir/asignar: riesgo amarillo/rojo según permisos efectivos.
- Reclamar/mover propiedad: riesgo rojo.

## Checklist obligatorio para futuros chats/agentes

Antes de afirmar cuál es la cuenta Meta Ads operativa:

- [ ] ¿La cuenta contiene `META_TRAFFIC_EXCEL_PRESENCIAL_SANTIAGO_B2C_V3`?
- [ ] ¿Contiene `AS02_2026.06_LANDING_PAGADO_EXCEL_PRESENCIAL`?
- [ ] ¿La referencia sanitizada coincide con `...2327` o existe evidencia nueva posterior?
- [ ] ¿Se distinguió cuenta personal `Otros activos` de los Business Portfolios?
- [ ] ¿Se evitó inferir una restricción desde un WhatsApp/activo distinto?
- [ ] ¿Se verificó Account Quality/facturación antes de afirmar un bloqueo?
- [ ] ¿Se distinguió estado API/token de estado real de entrega publicitaria?

Si cualquiera falla, el estado debe declararse `NO VERIFICADO` y no se debe recomendar cambios estructurales.

## Vigencia

Esta actualización reemplaza la referencia antigua `...9327` y consolida la evidencia 2026-08-09.

Una migración futura de ...2327 hacia un Business, una transferencia de propiedad o un cambio de cuenta operativa constituye cambio material y debe actualizar este documento mediante PR antes de convertirse en nueva fuente vigente.
