# Baseline sanitizado de diagnóstico Google Ads — 2026-07-11

## Estado

- Periodo observado: 2026-04-12 a 2026-07-10.
- Fuente: export local Google Ads API read-only.
- Reportes corregidos:
  - `05_search_terms_daily.csv`: 1.825 filas, estado `ok`;
  - `07_landing_pages_daily.csv`: 8.482 filas, estado `ok`.
- Outputs crudos, URLs completas, IDs, YAML, credenciales y CSV permanecen fuera del repo.
- Este documento no autoriza cambios en campañas, presupuestos, pujas, anuncios, keywords, conversiones o landings.

## Resumen ejecutivo

El deterioro observado no tiene una única causa demostrada. La evidencia actual sostiene cuatro frentes simultáneos:

1. una keyword de alto gasto aumentó fuertemente su volumen con baja conversión registrada;
2. un solo grupo de anuncios mezcla varias intenciones de búsqueda;
3. parte del tráfico pagado termina en páginas secundarias con desempeño débil;
4. la medición puede mezclar B2C/B2B o perder atribución después de la navegación.

La competencia puede influir en el CPC, pero todavía falta Auction Insights nominal para evaluar dominios específicos.

## Campañas observadas — 90 días

| Campaña | Gasto CLP | Clics | Conversiones principales registradas | CVR registrada | CPA registrado |
|---|---:|---:|---:|---:|---:|
| `EXCEL-PRE-STGO` | 632.218 | 670 | 100 | 14,93% | 6.322 |
| `EXCEL-EMPRESA` | 302.602 | 284 | 2 | 0,70% | 151.301 |

`EXCEL-EMPRESA` concentró aproximadamente 32% del gasto observado y cerca de 2% de las conversiones registradas. Esto justifica auditoría prioritaria, pero no autoriza pausarla.

## Deterioro de `EXCEL-PRE-STGO`

| Bloque aproximado | Gasto CLP | Clics | Conversiones registradas | CVR registrada | CPA registrado |
|---|---:|---:|---:|---:|---:|
| 12 abr–11 may | 189.200 | 213 | 40,67 | 19,09% | 4.652 |
| 12 may–10 jun | 199.031 | 216 | 33,33 | 15,43% | 5.971 |
| 11 jun–10 jul | 243.987 | 241 | 26 | 10,79% | 9.384 |

La caída principal está en la conversión post-click. El CPC aumentó, pero no explica por sí solo que el CPA registrado aproximadamente se duplicara.

## Keyword crítica: `curso excel básico e intermedio`

| Ventana | Clics | Gasto CLP | CPC medio CLP | Conversiones registradas | CPA registrado CLP | Participación en gasto de campaña |
|---|---:|---:|---:|---:|---:|---:|
| 90 días | 99 | 120.996 | 1.222 | 4 | 30.249 | 19,1% |
| 30 días | 71 | 87.109 | 1.227 | 2 | 43.555 | 35,7% |
| 7 días | 28 | 35.638 | 1.273 | 2 | 17.819 | 51,9% |

### Interpretación

- El CPC se mantuvo cercano a CLP 1.200 dentro del periodo.
- No se confirmó una subida abrupta del CPC de esta keyword en los 90 días.
- Sí se confirmó un fuerte aumento de impresiones, clics y participación de gasto.
- La tasa de conversión registrada cayó a medida que creció el volumen.

Para validar la referencia histórica de CPC cercano a CLP 400 se requiere un export de 12 o 24 meses.

### Mezcla de intención

La keyword activó búsquedas relacionadas con:

- Excel básico;
- Excel intermedio;
- básico e intermedio;
- Excel desde cero;
- clases de Excel;
- cursos para principiantes;
- opciones gratuitas;
- tutoriales y búsquedas informativas.

Esto confirma mezcla de intención. Una landing dedicada sigue siendo una hipótesis y no una conclusión.

## Landing pages efectivas

### Keyword crítica — últimos 30 días

| Destino agregado | Clics | Gasto CLP | Conversiones registradas |
|---|---:|---:|---:|
| Landing vigente de Excel presencial Santiago | 58 | 69.855 | 1 |
| Página histórica de Excel básico | 11 | 14.666 | 0 |

Enviar tráfico a la página histórica no mejoró el desempeño registrado.

### Fuga general de destino — 90 días

| Ruta agregada | Clics | Gasto CLP | Conversiones registradas | CPA registrado CLP |
|---|---:|---:|---:|---:|
| Landing principal | 600 | 560.091 | 92,83 | 6.033 |
| Otras páginas | 43 | 45.393 | 1,5 | 30.262 |

En los últimos 30 días, páginas distintas de la landing principal recibieron 18 clics y CLP 22.149 sin conversiones registradas.

Posibles orígenes pendientes de validar:

- sitelinks;
- assets;
- rutas complementarias;
- expansión u otra configuración.

Se requiere un informe read-only adicional de assets y sitelinks.

## Estructura actual

`EXCEL-PRE-STGO` presenta:

- un solo grupo de anuncios;
- un anuncio responsive activo;
- 28 keywords de frase habilitadas;
- múltiples intenciones dentro del mismo grupo.

Esto dificulta alinear `consulta → keyword → anuncio → landing → oferta → conversión`.

No se ha decidido todavía cuántas campañas, grupos o landings deben existir.

## Clases particulares y Superprof

- No se observaron términos con `Superprof`, `particular` o `a domicilio`.
- Se observó un clic en `profesor de excel` dentro de la campaña empresarial.
- El cluster relacionado con clases no mostró evidencia suficiente para justificar una landing de clases particulares.
- `clases de excel presencial` mantiene Quality Score alto y señales de relevancia favorables.

Los términos de búsqueda no identifican los dominios que participaron en la subasta. Superprof y otros competidores requieren Auction Insights manual privado.

## Competencia — señales propias agregadas

`EXCEL-PRE-STGO`, últimos 30 días aproximados:

- Search Impression Share: 96,4%;
- pérdida por presupuesto: 0%;
- pérdida por ranking: 3,5%;
- tasa de parte superior: 93,3%;
- primera posición absoluta: 75,4%.

La campaña entra en casi todas las subastas disponibles, no está limitada por presupuesto y pierde pocas impresiones por ranking. Esto debilita la hipótesis de que los competidores estén expulsando a Capacita, pero no descarta presión de precio.

## Tracking y atribución

Las URLs pagadas incluyen parámetros UTM y `landing_code`. Se observó el mismo `landing_code` agregado en tráfico B2C y B2B, por lo que debe validarse su función antes de modificarlo.

Además, una acción de conversión observada en la campaña empresarial utiliza un nombre asociado al curso presencial B2C. Esto justifica auditar objetivos compartidos y separación de medición.

Hipótesis pendiente:

```text
Google Ads
→ landing etiquetada
→ navegación interna
→ página o formulario sin cobertura completa
→ lead en Zoho
→ conversión no atribuida o fuente perdida
```

La posible submedición afecta conversiones, CVR y CPA; no invalida gasto, clics, CPC, términos, Quality Score o señales de subasta.

## Cobertura y límites

- El reporte de términos visibles cubre una parte relevante, pero no la totalidad de clics y gasto debido a umbrales de privacidad de Google.
- El reporte de landing pages tiene una cobertura sustancialmente mayor.
- Las conversiones registradas siguen siendo provisionales hasta reconciliar Google Ads, formularios y Zoho.
- Los resultados no prueban causalidad de competencia, landing o tracking por separado.

## Estado de hipótesis

| Hipótesis | Estado |
|---|---|
| La competencia explica el aumento de CPC | Posible, no confirmada |
| Superprof aumenta el costo | Pendiente de Auction Insights |
| La keyword básico–intermedio deteriora la campaña | Confirmada |
| El CPC de esa keyword subió fuertemente dentro de 90 días | No confirmado |
| El volumen de esa keyword creció fuertemente | Confirmado |
| La keyword mezcla intenciones | Confirmado |
| Se necesita una landing específica | Plausible, no demostrada |
| Se necesitan seis landings | No aprobado |
| Hay clics hacia páginas secundarias débiles | Confirmado |
| Un solo grupo mezcla demasiadas intenciones | Confirmado |
| GTM incompleto puede submedir conversiones | Plausible, pendiente de auditoría |
| B2C y B2B pueden estar mezclados en tracking | Evidencia suficiente para auditar |

## Próxima evidencia requerida

1. Auction Insights privados 7/30/90 para campaña y keywords priorizadas.
2. Informe read-only de assets y sitelinks.
3. Histórico 12/24 meses para tendencia de CPC.
4. Auditoría GTM/Google tag y atribución mediante `capacita-edge#27`.
5. Reconciliación agregada Google Ads → formularios → Zoho.
6. Matriz final conservar / negativizar / pausar / aislar / separar / nueva landing.

## Regla de decisión

No modificar campañas o landings hasta clasificar las hipótesis principales, conservar un buyer persona primario por prueba, separar B2C/B2B y contar con autorización explícita y rollback.