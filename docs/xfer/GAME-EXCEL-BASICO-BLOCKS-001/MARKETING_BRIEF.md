# Marketing brief XFER - GAME-EXCEL-BASICO-BLOCKS-001

Fecha: 2026-07-25  
Estado: `READY_DOCUMENTAL`  
Repo origen: `misaeln-pc1/Capacita-Learning-Games-Diagnostics`  
Issue maestro: https://github.com/misaeln-pc1/Capacita-Learning-Games-Diagnostics/issues/6  
Issue XFER: https://github.com/misaeln-pc1/marketing-performance-capacita/issues/40

## Alcance y control

Este brief resuelve solo la vision comercial documental del piloto **Bloques de Excel: detecta y corrige errores**.

No activa campanas, presupuesto, plataformas Ads, landing productiva, Zoho, Edge, Supabase, workflows ni tracking real. Los eventos y senales descritos son contrato conceptual para Learning Games y requieren autorizacion posterior antes de implementacion tecnica.

## Fuentes leidas

- `README.md`
- `PROJECT_CONTEXT.md`
- `TASK_STATUS.md`
- `AGENTS.md`
- `DECISIONES.md`
- `docs/GTM_CONSUMPTION_BRIDGE.md`
- `templates/CAMPAIGN_BRIEF_GTM.md`
- `campaigns/excel-basico-intermedio-presencial-santiago/gtm-baseline-v1.md`
- `docs/google-ads/GOOGLE_ADS_DIAGNOSIS_BASELINE_2026-07-11.md`
- Issue maestro Learning Games #6
- Issue XFER Marketing #40

Archivos no encontrados en raiz del repo al momento del preflight: `RIESGOS.md`, `PROMPTS_BASE.md`, `briefs/README.md`.

## Baseline GTM consumido

```yaml
canonical_baseline:
  buyer_personas:
    - id: BP-001
      name: Desbordado Operativo
      version: 1.0.0
      role: primary
    - id: BP-002
      name: Reinsercion Laboral
      version: 1.0.0
      role: secondary
  value_propositions:
    - document: VALUE_PROPOSITIONS.md
      section: A) Capacitacion practica y guiada
      version: 0.2.1
    - document: VALUE_PROPOSITIONS.md
      section: C) Productividad laboral y seguridad operativa
      version: 0.2.1
    - document: VALUE_PROPOSITIONS.md
      section: D) Empleabilidad / reinsercion laboral
      version: 0.2.1
    - document: VALUE_PROPOSITIONS.md
      section: E) Recursos incluidos y cero friccion logistica
      version: 0.2.1
  journey_stage:
    document: CUSTOMER_JOURNEY.md
    section: 1. Visitante / audiencia fria
    version: 0.2
  expected_transition:
    document: CUSTOMER_JOURNEY.md
    section: 3. Lead identificado
    version: 0.2
  source_date: 2026-07-10
```

Marketing no redefine buyer personas ni scoring canónico. Esta es una aplicacion local para el piloto.

## 1. Buyer persona principal

`BP-001 - Desbordado Operativo`.

Persona que usa Excel en tareas administrativas u operacionales, siente lentitud, comete errores frecuentes, necesita resolver trabajo real y valora una experiencia practica, guiada y de baja friccion.

Motivo de seleccion: el juego detecta errores tipicos y brechas operativas, por lo que conecta directamente con productividad, seguridad al trabajar y necesidad de practica inmediata.

## 2. Buyer persona secundario

`BP-002 - Reinsercion Laboral`.

Persona que necesita actualizar competencias, comprobar su nivel y mostrar una ruta confiable de aprendizaje. Puede enganchar con el juego como diagnostico rapido antes de cotizar o pedir orientacion.

Uso recomendado: lectura secundaria, no mezclar mensajes de productividad y empleabilidad en una misma prueba si luego se busca medir respuesta por perfil.

## 3. Dolores comerciales

| Dolor | Lectura comercial |
|---|---|
| Me demoro demasiado en planillas simples | Necesidad de productividad inmediata. |
| Me equivoco en formulas, referencias o filtros | Riesgo de errores laborales y baja confianza. |
| No se si mi nivel es realmente basico | Necesidad de diagnostico y ruta sugerida. |
| He aprendido mirando tutoriales, pero no ordenadamente | Necesidad de estructura y practica guiada. |
| Me cuesta demostrar que se Excel | Necesidad de capacitacion certificable o ruta formal. |

## 4. Objeciones frecuentes

- "Solo necesito algo puntual, no un curso completo".
- "Puedo aprender gratis en YouTube".
- "No tengo tiempo".
- "No se si estoy en nivel basico o intermedio".
- "Me da verguenza partir desde cero".
- "Quiero precio, fecha y modalidad antes de hablar con alguien".

Respuesta comercial sugerida: el juego no debe vender de inmediato como primer golpe; debe entregar valor, mostrar brechas concretas y luego ofrecer una ruta corta y clara.

## 5. Promesa del juego

En pocos minutos, el usuario identifica errores frecuentes de Excel Basico, recibe una lectura simple de sus brechas y obtiene una recomendacion de siguiente paso sin exponer sus respuestas crudas al CRM.

Promesa permitida: diagnostico orientativo y ruta sugerida.  
Promesa prohibida: certificacion, empleabilidad, resultado laboral, aumento salarial o dominio garantizado.

## 6. Mensaje de entrada

Texto sugerido:

> Detecta errores tipicos de Excel Basico y descubre que deberias reforzar primero. Juega unos minutos, corrige bloques y recibe una recomendacion simple para avanzar.

Variante `BP-001`:

> Si tus planillas te hacen perder tiempo, prueba este mini juego y detecta que errores te estan frenando.

Variante `BP-002`:

> Si quieres actualizar tu Excel y no sabes por donde partir, usa este diagnostico rapido para ubicar tu nivel.

## 7. Resultado comercial esperado

Resultado esperado del piloto: aumentar calidad de leads y claridad de intencion antes del contacto comercial.

El juego debe ayudar a separar:

- usuarios curiosos sin intencion inmediata;
- usuarios con brechas reales y disposicion a recibir orientacion;
- usuarios listos para cotizar un curso o pedir contacto.

No se debe medir exito solo por inicio del juego o clics. La metrica util es avance hacia lead contactable, cotizacion, inscripcion o aprendizaje agregado, siempre sin datos personales en GitHub.

## 8. CTA principal

**Recibir mi diagnostico y ruta recomendada**.

Condicion: pedir datos solo al final, despues de entregar valor. El formulario debe explicar que se enviara una recomendacion relacionada con cursos de Excel Capacita.

## 9. CTA secundario

**Cotizar curso de Excel Basico**.

Uso recomendado: mostrarlo al finalizar o cuando el usuario declara intencion alta. No interrumpir el juego al inicio.

## 10. Senales de intencion comercial

| Senal | Lectura | Uso permitido |
|---|---|---|
| Completa el juego | Interes suficiente para terminar la experiencia | Scoring agregado del juego. |
| Repite intentos tras feedback | Disposicion a aprender | Nurturing educativo. |
| Errores en formulas/referencias | Dolor tecnico de alta friccion laboral | Recomendacion de modulo o curso. |
| Errores en filtros/ordenamiento | Brecha operativa en manejo de registros | Recomendacion practica. |
| Click en CTA principal | Interes en recibir resultado | Solicitar opt-in y contacto. |
| Click en cotizar | Intencion comercial alta | Derivacion comercial posterior autorizada. |
| Abandona antes de entregar contacto | Interes bajo o friccion alta | Solo analitica agregada/anonima, no Zoho. |

## 11. Lead frio, tibio y caliente

| Estado | Criterio documental | Accion recomendada |
|---|---|---|
| Frio | Inicia o juega parcialmente, sin opt-in ni contacto | No enviar a Zoho. Usar solo estadistica anonima/agregada si existe base legal y tecnica. |
| Tibio | Completa el juego, desbloquea resultado o deja email con opt-in, pero no cotiza | Enviar resumen de ruta y contenido educativo de Excel Basico. |
| Caliente | Deja contacto, acepta comunicacion y hace clic en cotizar/WhatsApp o solicita informacion concreta | Enviar a ruta comercial con resumen no crudo: curso recomendado, nivel, score/rango y consentimiento. |

Los umbrales numericos finales deben definirse en Learning Games y validarse antes de integracion real.

## 12. Datos que NO se deben enviar a Zoho

No enviar a Zoho:

- respuestas crudas por reto;
- historial completo de aciertos/errores;
- tiempos por bloque o microinteracciones;
- sesiones anonimas sin contacto;
- IP, user agent crudo, huella de navegador o datos tecnicos invasivos;
- eventos de juego sin opt-in;
- leads incompletos o no contactables;
- datos de menores o atributos sensibles;
- capturas, grabaciones, archivos, textos libres no revisados;
- inferencias de buyer persona como si fueran hechos.

Si hay opt-in, Zoho podria recibir solo un resumen controlado: curso de interes, rango de nivel, brecha principal, CTA elegido, fuente/UTM permitida, consentimiento y version de politica. Esa definicion queda fuera de este brief y requiere aprobacion tecnica/legal posterior.

## 13. Eventos comerciales sugeridos

Eventos conceptuales para una fase futura, no implementados en este PR:

| Evento | Proposito | Riesgo/control |
|---|---|---|
| `game_start` | Medir inicio de experiencia | Anonimo/agregado; no Zoho. |
| `challenge_answered` | Calcular avance y feedback | No guardar respuesta literal en CRM. |
| `concept_error_detected` | Identificar brecha por concepto | Guardar codigo de concepto o categoria, no texto crudo. |
| `game_completed` | Separar curiosos de usuarios comprometidos | Agregado hasta opt-in. |
| `result_unlocked` | Medir valor percibido | No forzar contacto antes del valor. |
| `cta_primary_clicked` | Medir interes por diagnostico/ruta | Requiere consentimiento si conecta con identidad. |
| `quote_cta_clicked` | Senal comercial alta | Derivar solo con opt-in/contacto. |
| `contact_submitted` | Conversion a lead identificado | Validar consentimiento, fuente y dedupe antes de Zoho. |

## 14. Recomendacion de nurturing

| Segmento | Nurturing recomendado |
|---|---|
| Frio | No email si no dejo contacto. Usar aprendizaje agregado para mejorar juego y copy. |
| Tibio con opt-in | Enviar resultado resumido, 2 o 3 tips para corregir la brecha principal y una invitacion suave a revisar curso de Excel Basico. |
| Caliente | Contacto comercial rapido con referencia a su brecha principal y CTA elegido, sin mencionar respuestas especificas ni datos invasivos. |

Secuencia sugerida para tibio:

1. Resultado y ruta: "Tu principal brecha esta en formulas/referencias/filtros".
2. Recurso educativo: mini guia de errores tipicos de Excel Basico.
3. CTA: cotizar curso o hablar con un asesor.

## 15. Riesgos comerciales o de privacidad

| Riesgo | Semaforo | Mitigacion minima |
|---|---:|---|
| Enviar eventos crudos a Zoho | Rojo | Solo resumen con opt-in; eventos crudos quedan fuera del CRM. |
| Prometer certificacion o empleabilidad no verificada | Rojo | Usar lenguaje de diagnostico orientativo y ruta sugerida. |
| Mezclar B2C y B2B en la misma lectura | Amarillo | Mantener este piloto como B2C salvo decision separada. |
| Declarar buyer persona como hecho | Amarillo | Tratarlo como hipotesis o senal, no etiqueta definitiva. |
| Sobreoptimizar por clics del juego | Amarillo | Medir lead contactable y aprendizaje agregado, no solo interaccion. |
| Pedir datos al inicio y bajar engagement | Verde/Amarillo | Captura al final, despues de entregar valor. |

## 16. Recomendacion final para Learning Games

Avanzar con el piloto documental usando `BP-001` como perfil primario y `BP-002` como lectura secundaria. La experiencia debe comenzar anonima, entregar feedback inmediato, pedir datos solo al final y enviar a futuras integraciones solo un resumen comercial controlado.

Para la primera version, Learning Games deberia producir tres salidas separadas:

1. `technical_score`: desempeno por concepto/categoria.
2. `commercial_intent`: frio/tibio/caliente como hipotesis provisional.
3. `recommended_next_step`: ver tips, recibir diagnostico o cotizar.

No implementar tracking real, Zoho, Edge, Supabase, Ads ni automatizaciones sin una decision posterior con riesgos, campos, consentimiento, dedupe y rollback.

## Callback sugerido

```yaml
CALLBACK_XFER:
  source_repo: marketing-performance-capacita
  target_repo: Capacita-Learning-Games-Diagnostics
  game_id: GAME-EXCEL-BASICO-BLOCKS-001
  status: READY
  output_file: docs/xfer/GAME-EXCEL-BASICO-BLOCKS-001/MARKETING_BRIEF.md
  branch: docs/marketing-xfer-game-excel-basico-blocks-001
  risks:
    - Verde documental en este PR.
    - Amarillo futuro si se implementan tracking, CRM, campañas o datos identificables.
  pending:
    - Definir umbrales numericos de scoring antes de cualquier integracion real.
    - Validar consentimiento, campos y dedupe antes de enviar resumen a Zoho.
  recommendation: Usar el brief como insumo comercial para Learning Games; no ejecutar sistemas productivos todavia.
```
