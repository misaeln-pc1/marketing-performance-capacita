# Marketing brief XFER — GAME-EXCEL-BASICO-BLOCKS-001

Fecha: 2026-07-28  
Estado: `READY`  
Productor: `Marketing Performance`  
Consumidor: `Capacita-Learning-Games-Diagnostics`  
Caso: `GAME-EXCEL-BASICO-BLOCKS-001`  
Origen de solicitud: Marketing issue #40 / Learning Games issue #6  
Versión normalizada: `v02`  

## 1. Alcance y control

Este brief resuelve solo la visión comercial documental del piloto **Bloques de Excel: detecta y corrige errores**.

No activa campañas, presupuesto, plataformas Ads, landing productiva, Zoho, Edge, Supabase, workflows ni tracking real. Los eventos y señales descritos son contrato conceptual para Learning Games y requieren autorización posterior antes de cualquier implementación técnica.

## 2. Fuentes y baseline consumido

Fuentes locales y de coordinación consideradas:

- `README.md`.
- `PROJECT_CONTEXT.md`.
- `TASK_STATUS.md`.
- `AGENTS.md`.
- `DECISIONES.md`.
- `docs/GTM_CONSUMPTION_BRIDGE.md`.
- `templates/CAMPAIGN_BRIEF_GTM.md`.
- `campaigns/excel-basico-intermedio-presencial-santiago/gtm-baseline-v1.md`.
- `docs/google-ads/GOOGLE_ADS_DIAGNOSIS_BASELINE_2026-07-11.md`.
- Learning Games issue #6.
- Marketing issue #40.
- Antecedente histórico PR #41.

Baseline GTM consumido como aplicación local:

```yaml
canonical_baseline:
  buyer_personas:
    - id: BP-001
      name: Desbordado Operativo
      version: 1.0.0
      role: primary
    - id: BP-002
      name: Reinserción Laboral
      version: 1.0.0
      role: secondary
  value_propositions:
    - document: VALUE_PROPOSITIONS.md
      section: A) Capacitación práctica y guiada
      version: 0.2.1
    - document: VALUE_PROPOSITIONS.md
      section: C) Productividad laboral y seguridad operativa
      version: 0.2.1
    - document: VALUE_PROPOSITIONS.md
      section: D) Empleabilidad / reinserción laboral
      version: 0.2.1
    - document: VALUE_PROPOSITIONS.md
      section: E) Recursos incluidos y cero fricción logística
      version: 0.2.1
  journey_stage:
    document: CUSTOMER_JOURNEY.md
    section: 1. Visitante / audiencia fría
    version: 0.2
  expected_transition:
    document: CUSTOMER_JOURNEY.md
    section: 3. Lead identificado
    version: 0.2
```

Marketing no redefine buyer personas ni scoring canónico. Esta es una aplicación local para el piloto.

## 3. Buyer persona principal

`BP-001 — Desbordado Operativo`.

Persona que usa Excel en tareas administrativas u operacionales, siente lentitud, comete errores frecuentes, necesita resolver trabajo real y valora una experiencia práctica, guiada y de baja fricción.

Motivo de selección: el juego detecta errores típicos y brechas operativas, por lo que conecta directamente con productividad, seguridad al trabajar y necesidad de práctica inmediata.

## 4. Buyer persona secundario

`BP-002 — Reinserción Laboral`.

Persona que necesita actualizar competencias, comprobar su nivel y mostrar una ruta confiable de aprendizaje. Puede enganchar con el juego como diagnóstico rápido antes de cotizar o pedir orientación.

Uso recomendado: lectura secundaria. No mezclar mensajes de productividad y empleabilidad en una misma prueba si luego se busca medir respuesta por perfil.

## 5. Dolores comerciales

| Dolor | Lectura comercial |
|---|---|
| Me demoro demasiado en planillas simples | Necesidad de productividad inmediata. |
| Me equivoco en fórmulas, referencias o filtros | Riesgo de errores laborales y baja confianza. |
| No sé si mi nivel es realmente básico | Necesidad de diagnóstico y ruta sugerida. |
| He aprendido mirando tutoriales, pero no ordenadamente | Necesidad de estructura y práctica guiada. |
| Me cuesta demostrar que sé Excel | Necesidad de capacitación certificable o ruta formal. |

## 6. Objeciones frecuentes

- “Solo necesito algo puntual, no un curso completo”.
- “Puedo aprender gratis en YouTube”.
- “No tengo tiempo”.
- “No sé si estoy en nivel básico o intermedio”.
- “Me da vergüenza partir desde cero”.
- “Quiero precio, fecha y modalidad antes de hablar con alguien”.

Respuesta comercial sugerida: el juego no debe vender de inmediato como primer golpe. Debe entregar valor, mostrar brechas concretas y luego ofrecer una ruta corta y clara.

## 7. Promesa del juego

En pocos minutos, el usuario identifica errores frecuentes de Excel Básico, recibe una lectura simple de sus brechas y obtiene una recomendación de siguiente paso sin exponer sus respuestas crudas al CRM.

Promesa permitida: diagnóstico orientativo y ruta sugerida.  
Promesa prohibida: certificación, empleabilidad, resultado laboral, aumento salarial o dominio garantizado.

## 8. Mensaje de entrada

Texto base:

> Detecta errores típicos de Excel Básico y descubre qué deberías reforzar primero. Juega unos minutos, corrige bloques y recibe una recomendación simple para avanzar.

Variante `BP-001`:

> Si tus planillas te hacen perder tiempo, prueba este mini juego y detecta qué errores te están frenando.

Variante `BP-002`:

> Si quieres actualizar tu Excel y no sabes por dónde partir, usa este diagnóstico rápido para ubicar tu nivel.

## 9. Resultado comercial esperado

Resultado esperado del piloto: aumentar calidad de leads y claridad de intención antes del contacto comercial.

El juego debe ayudar a separar:

- usuarios curiosos sin intención inmediata;
- usuarios con brechas reales y disposición a recibir orientación;
- usuarios listos para cotizar un curso o pedir contacto.

No se debe medir éxito solo por inicio del juego o clics. La métrica útil es avance hacia lead contactable, cotización, inscripción o aprendizaje agregado, siempre sin datos personales en GitHub.

## 10. CTA principal y secundario

CTA principal:

```text
Recibir mi diagnóstico y ruta recomendada
```

Condición: pedir datos solo al final, después de entregar valor. El formulario debe explicar que se enviará una recomendación relacionada con cursos de Excel Capacita.

CTA secundario:

```text
Cotizar curso de Excel Básico
```

Uso recomendado: mostrarlo al finalizar o cuando el usuario declara intención alta. No interrumpir el juego al inicio.

## 11. Señales de intención comercial

| Señal | Lectura | Uso permitido |
|---|---|---|
| Completa el juego | Interés suficiente para terminar la experiencia | Scoring agregado del juego. |
| Repite intentos tras feedback | Disposición a aprender | Nurturing educativo. |
| Errores en fórmulas/referencias | Dolor técnico de alta fricción laboral | Recomendación de módulo o curso. |
| Errores en filtros/ordenamiento | Brecha operativa en manejo de registros | Recomendación práctica. |
| Click en CTA principal | Interés en recibir resultado | Solicitar opt-in y contacto. |
| Click en cotizar | Intención comercial alta | Derivación comercial posterior autorizada. |
| Abandona antes de entregar contacto | Interés bajo o fricción alta | Solo analítica agregada/anónima, no Zoho. |

## 12. Lead frío, tibio y caliente

| Estado | Criterio documental | Acción recomendada |
|---|---|---|
| Frío | Inicia o juega parcialmente, sin opt-in ni contacto | No enviar a Zoho. Usar solo estadística anónima/agregada si existe base legal y técnica. |
| Tibio | Completa el juego, desbloquea resultado o deja email con opt-in, pero no cotiza | Enviar resumen de ruta y contenido educativo de Excel Básico. |
| Caliente | Deja contacto, acepta comunicación y hace clic en cotizar/WhatsApp o solicita información concreta | Enviar a ruta comercial con resumen no crudo: curso recomendado, nivel, score/rango y consentimiento. |

Los umbrales numéricos finales deben definirse en Learning Games y validarse antes de integración real.

## 13. Datos que NO se deben enviar a Zoho

No enviar a Zoho:

- respuestas crudas por reto;
- historial completo de aciertos/errores;
- tiempos por bloque o microinteracciones;
- sesiones anónimas sin contacto;
- IP, user agent crudo, huella de navegador o datos técnicos invasivos;
- eventos de juego sin opt-in;
- leads incompletos o no contactables;
- datos de menores o atributos sensibles;
- capturas, grabaciones, archivos, textos libres no revisados;
- inferencias de buyer persona como si fueran hechos.

Si hay opt-in, Zoho podría recibir solo un resumen controlado: curso de interés, rango de nivel, brecha principal, CTA elegido, fuente/UTM permitida, consentimiento y versión de política. Esa definición queda fuera de este brief y requiere aprobación técnica/legal posterior.

## 14. Eventos comerciales sugeridos

Eventos conceptuales para una fase futura, no implementados en este PR:

| Evento | Propósito | Riesgo/control |
|---|---|---|
| `game_start` | Medir inicio de experiencia | Anónimo/agregado; no Zoho. |
| `challenge_answered` | Calcular avance y feedback | No guardar respuesta literal en CRM. |
| `concept_error_detected` | Identificar brecha por concepto | Guardar código de concepto o categoría, no texto crudo. |
| `game_completed` | Separar curiosos de usuarios comprometidos | Agregado hasta opt-in. |
| `result_unlocked` | Medir valor percibido | No forzar contacto antes del valor. |
| `cta_primary_clicked` | Medir interés por diagnóstico/ruta | Requiere consentimiento si conecta con identidad. |
| `quote_cta_clicked` | Señal comercial alta | Derivar solo con opt-in/contacto. |
| `contact_submitted` | Conversión a lead identificado | Validar consentimiento, fuente y dedupe antes de Zoho. |

## 15. Recomendación de nurturing

| Segmento | Nurturing recomendado |
|---|---|
| Frío | No email si no dejó contacto. Usar aprendizaje agregado para mejorar juego y copy. |
| Tibio con opt-in | Enviar resultado resumido, 2 o 3 tips para corregir la brecha principal y una invitación suave a revisar curso de Excel Básico. |
| Caliente | Contacto comercial rápido con referencia a su brecha principal y CTA elegido, sin mencionar respuestas específicas ni datos invasivos. |

Secuencia sugerida para tibio:

1. Resultado y ruta: “Tu principal brecha está en fórmulas/referencias/filtros”.
2. Recurso educativo: mini guía de errores típicos de Excel Básico.
3. CTA: cotizar curso o hablar con un asesor.

## 16. Riesgos comerciales o de privacidad

| Riesgo | Semáforo | Mitigación mínima |
|---|---:|---|
| Enviar eventos crudos a Zoho | Rojo | Solo resumen con opt-in; eventos crudos quedan fuera del CRM. |
| Prometer certificación o empleabilidad no verificada | Rojo | Usar lenguaje de diagnóstico orientativo y ruta sugerida. |
| Mezclar B2C y B2B en la misma lectura | Amarillo | Mantener este piloto como B2C salvo decisión separada. |
| Declarar buyer persona como hecho | Amarillo | Tratarlo como hipótesis o señal, no etiqueta definitiva. |
| Sobreoptimizar por clics del juego | Amarillo | Medir lead contactable y aprendizaje agregado, no solo interacción. |
| Pedir datos al inicio y bajar engagement | Verde/Amarillo | Captura al final, después de entregar valor. |

## 17. Recomendación final para Learning Games

Avanzar con el piloto documental usando `BP-001` como perfil primario y `BP-002` como lectura secundaria. La experiencia debe comenzar anónima, entregar feedback inmediato, pedir datos solo al final y enviar a futuras integraciones solo un resumen comercial controlado.

Para la primera versión, Learning Games debería producir tres salidas separadas:

1. `technical_score`: desempeño por concepto/categoría.
2. `commercial_intent`: frío/tibio/caliente como hipótesis provisional.
3. `recommended_next_step`: ver tips, recibir diagnóstico o cotizar.

No implementar tracking real, Zoho, Edge, Supabase, Ads ni automatizaciones sin una decisión posterior con riesgos, campos, consentimiento, dedupe y rollback.

## 18. Callback XFER sugerido

```yaml
CALLBACK_XFER:
  source_repo: marketing-performance-capacita
  target_repo: Capacita-Learning-Games-Diagnostics
  game_id: GAME-EXCEL-BASICO-BLOCKS-001
  status: READY
  output_file: docs/xfer/GAME-EXCEL-BASICO-BLOCKS-001/MARKETING_BRIEF.md
  branch: docs/marketing-xfer-game-excel-basico-blocks-clean-20260728
  risks:
    - Verde documental en este PR.
    - Amarillo futuro si se implementan tracking, CRM, campañas o datos identificables.
  pending:
    - Definir umbrales numéricos de scoring antes de cualquier integración real.
    - Validar consentimiento, campos y dedupe antes de enviar resumen a Zoho.
    - Learning Games debe consumir la versión vigente desde main después del merge.
  recommendation: Usar el brief como insumo comercial para Learning Games; no ejecutar sistemas productivos todavía.
```
