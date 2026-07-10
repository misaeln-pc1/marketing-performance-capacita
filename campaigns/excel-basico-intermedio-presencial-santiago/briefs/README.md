# Paquete de briefs por buyer persona — Excel presencial Santiago

Fecha: 2026-07-10  
Versión local: 1.0.0  
Estado: listo para desarrollo creativo; no activa campañas ni producción  
Issue: #21

## Propósito

Convertir los buyer personas corporativos de GTM/RevOps en cuatro aplicaciones tácticas separadas para Marketing, evitando mezclar dolores, compradores y métricas incompatibles.

Fuente canónica:

- `misaeln-pc1/capacita-global-control/docs/gtm-revops/BUYER_PERSONAS.md` v1.0.0;
- `BUYER_PERSONA_SIGNAL_MODEL.md` v1.0.0;
- `VALUE_PROPOSITIONS.md` v0.2.1;
- `CUSTOMER_JOURNEY.md` v0.2;
- `CONSUMPTION_CONTRACT.md` v1.0.1.

Marketing no redefine estos documentos. Cada brief registra una aplicación local, una hipótesis y una ruta de aprendizaje.

## Personas activas

| ID | Persona | Tipo | Brief | Preparación |
|---|---|---|---|---|
| `BP-001` | Desbordado Operativo | B2C / usuario de empresa | `BRIEF_BP001_DESBORDADO_OPERATIVO_V1.md` | Prioridad 1; listo para creatividad B2C. |
| `BP-002` | Reinserción Laboral | B2C | `BRIEF_BP002_REINSERCION_LABORAL_V1.md` | Prioridad 2; listo para creatividad B2C. |
| `BP-003` | Coordinador B2B | B2B comprador para terceros | `BRIEF_BP003_COORDINADOR_B2B_V1.md` | Listo documentalmente; validar landing y cotización grupal. |
| `BP-004` | Dueño o Jefatura PyME | B2B decisor | `BRIEF_BP004_JEFATURA_PYME_V1.md` | Listo documentalmente; validar oferta y diagnóstico comercial. |
| `BP-000` | No clasificado / evidencia insuficiente | Control | Sin campaña propia | No es audiencia; se usa para no forzar clasificación. |

## Orden recomendado

1. Lanzar o desarrollar primero `BP-001`, porque la oferta Excel presencial y la landing actual ya contienen elementos de productividad, práctica y reducción de errores.
2. Preparar después `BP-002` manteniendo la misma oferta y destino cuando se quiera comparar solo el mensaje.
3. No mezclar `BP-001` y `BP-002` en una misma pieza si el objetivo es aprender qué dolor convierte.
4. Activar `BP-003` y `BP-004` únicamente con ruta B2B separada, formulario/cotización adecuados y oferta grupal confirmada.

## Arquitectura de campañas recomendada

```text
B2C
├── BP-001 Productividad y errores
└── BP-002 Empleabilidad y actualización

B2B
├── BP-003 Coordinación, evidencia y baja fricción
└── BP-004 Impacto operativo y decisión de inversión
```

No usar una campaña mixta B2C/B2B. No comparar resultados B2C y B2B como si tuvieran el mismo ciclo de venta.

## Variables que deben permanecer constantes en un test de mensaje

- curso;
- modalidad;
- fecha;
- precio;
- landing;
- presupuesto;
- duración;
- geografía;
- formato creativo, cuando sea posible.

La variable principal debe ser el mensaje asociado al buyer persona.

## Datos tácticos obligatorios antes de publicar

- fecha vigente;
- valor y medios de pago;
- cupos;
- dirección y modalidad;
- equipamiento disponible;
- materiales y diploma aplicables;
- CTA y formulario funcionando;
- parámetros UTM;
- trazabilidad mínima hacia lead contactable, cotización y matrícula.

## Regla de aprendizaje

Cada campaña debe conservar:

```yaml
buyer_persona_id: BP-XXX
buyer_persona_version: 1.0.0
brief_version: 1.0.0
hypothesis: texto
result_status: pending | supported | rejected | inconclusive
```

Los resultados agregados se documentan en Marketing. Solo se propone cambiar GTM cuando exista evidencia repetida que afecte la definición corporativa.

## Límites

- No contiene datos personales ni exports.
- No modifica campañas reales.
- No modifica landing, Cloudflare, CRM o automatizaciones.
- No garantiza empleo, productividad, ahorro, rentabilidad ni resultados académicos.
- No usa edad, género u otros atributos sensibles para segmentar o clasificar.
