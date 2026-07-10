# Puente de consumo Marketing → GTM / RevOps

Fecha: 2026-07-10  
Versión: 1.0.0  
Estado: vigente para operación documental  
Issue: `#19`

## Propósito

Permitir que Marketing trabaje directamente en campañas, anuncios, targeting, copies, activos y performance sin duplicar ni redefinir el conocimiento comercial transversal de Capacita.

```text
GTM / RevOps define el modelo corporativo vigente.
Marketing selecciona y prueba una aplicación táctica.
Los resultados de campaña alimentan una revisión futura del canónico.
```

## Fuentes canónicas

Las definiciones corporativas viven en:

`misaeln-pc1/capacita-global-control/docs/gtm-revops/`

Fuentes mínimas para una campaña:

| Tema | Fuente canónica | Estado actual |
|---|---|---|
| Contrato de consumo | `CONSUMPTION_CONTRACT.md` | v1.0.1 |
| Buyer personas | `BUYER_PERSONAS.md` | v1.0.0; IDs `BP-000` a `BP-004` |
| Señales de clasificación | `BUYER_PERSONA_SIGNAL_MODEL.md` | v1.0.0 piloto |
| Propuestas de valor | `VALUE_PROPOSITIONS.md` | v0.2.1; sin IDs normalizados todavía |
| Customer journey | `CUSTOMER_JOURNEY.md` | v0.2; sin IDs normalizados todavía |
| Segmentación | `SEGMENTATION_RULES.md` | v0.1 inicial |
| Scoring, nurturing y touch | documentos homónimos | iniciales; no automatizar sin validación |

## Qué pertenece a Marketing

Marketing conserva y versiona:

- brief y objetivo de campaña;
- selección de buyer personas para esa campaña;
- hipótesis táctica;
- público y targeting de plataforma;
- copy, creatividades y CTA;
- presupuesto o propuesta de test documental;
- métricas y resultados agregados;
- aprendizajes, objeciones y nuevas señales observadas.

Marketing no conserva como verdad propia:

- definiciones corporativas paralelas de buyer persona;
- una segunda versión del journey;
- propuestas de valor transversales redefinidas;
- scoring o nurturing global inventado para una campaña;
- reglas técnicas de Zoho, Edge, n8n o WhatsApp.

## Contrato mínimo para una campaña

Cada campaña nueva o revisada debe registrar:

```yaml
canonical_baseline:
  buyer_personas:
    - id: BP-001
      version: 1.0.0
  value_propositions:
    - document: VALUE_PROPOSITIONS.md
      section: C) Productividad laboral y seguridad operativa
      version: 0.2.1
  journey_stage:
    document: CUSTOMER_JOURNEY.md
    section: 1. Visitante / audiencia fría
    version: 0.2
  source_date: 2026-07-10

local_application:
  campaign_id: CAMPAIGN_ID
  objective: OBJETIVO
  channel: CANAL
  tactical_hypothesis: HIPOTESIS
  primary_cta: CTA
  owner_repo: misaeln-pc1/marketing-performance-capacita
```

### Regla para bloques sin ID

Mientras propuesta de valor, journey u otro bloque no tenga IDs normalizados, usar obligatoriamente:

- documento;
- sección exacta;
- versión.

No inventar IDs desde Marketing.

## Adaptación permitida

Marketing puede:

- elegir uno o más buyer personas activos;
- priorizar dolores y objeciones pertinentes;
- adaptar lenguaje, formato, creatividad y canal;
- probar variantes A/B;
- crear segmentación táctica de plataforma;
- documentar aprendizajes y resultados agregados.

Marketing no puede:

- cambiar el significado de un buyer persona dentro del brief;
- presentar inferencias como hechos declarados;
- utilizar atributos sensibles para clasificación o targeting no autorizado;
- prometer resultados, empleabilidad, certificaciones o beneficios no verificables;
- copiar evidencia privada de Global, CRM o ventas al repo público;
- modificar automáticamente campañas históricas cuando cambia el canónico.

## Versionado y campañas históricas

- La campaña conserva la versión canónica con la que fue diseñada.
- Un cambio de GTM no reescribe automáticamente campañas anteriores.
- Las campañas activas se revisan solo si el cambio afecta promesa, clasificación, riesgo o performance esperada.
- Las nuevas campañas usan la versión canónica vigente.

## Retroalimentación hacia GTM

Cuando una campaña produzca evidencia que pueda cambiar una definición corporativa:

1. conservar datos y análisis agregados en Marketing;
2. identificar ID o documento/sección/versión afectada;
3. registrar evidencia, alcance y posible impacto;
4. crear o enlazar issue en `capacita-global-control`;
5. GTM/RevOps decide mantener, refinar, deprecar o versionar;
6. Marketing evalúa si migra campañas activas.

Una observación aislada puede quedar como hipótesis táctica. No modifica por sí sola el canónico.

## Relación con otros repos

| Necesidad | Repo dueño |
|---|---|
| Landing, formulario y eventos frontend | `capacita-edge` |
| Campos, API names y Deluge | `Capacita-Zoho-Deluge-Core` |
| Workflows y mensajería | `whatsapp-n8n-zoho-capacita` |
| Skills y procedimientos reutilizables | `capacita-ai-operating-system` |
| Definiciones corporativas | `capacita-global-control/docs/gtm-revops/` |

Marketing documenta la necesidad y enlaza la ejecución; no duplica código ni implementación.

## Repositorio público

En este repo solo se permiten:

- referencias y versiones canónicas;
- hipótesis de campaña sanitizadas;
- resultados agregados;
- copies y configuraciones documentales no sensibles.

No incluir datos personales, conversaciones privadas, exports CRM, secretos, IDs completos de cuentas, métricas financieras confidenciales ni evidencia privada de Global.

## Definition of Done de una campaña

Una campaña está documentalmente lista cuando:

- referencia baseline canónico y versiones;
- distingue definición corporativa de hipótesis táctica;
- define público, oferta, CTA, canal y métrica;
- identifica claims permitidos y datos tácticos por confirmar;
- establece cómo devolverá aprendizaje a GTM;
- no modifica plataformas, CRM, landing o producción sin autorización específica.