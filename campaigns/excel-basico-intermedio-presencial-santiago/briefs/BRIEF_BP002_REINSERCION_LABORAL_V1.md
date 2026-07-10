# Brief BP-002 — Reinserción Laboral

Fecha: 2026-07-10  
Versión del brief: 1.0.0  
Estado: listo para desarrollo creativo; activación pendiente de validaciones tácticas  
Campaign ID recomendado: `META_TRAFFIC_EXCEL_PRESENCIAL_BP002_V1`

## 1. Baseline canónico

```yaml
canonical_baseline:
  buyer_persona:
    id: BP-002
    name: Reinserción Laboral
    version: 1.0.0
    role: primary
  value_propositions:
    - document: VALUE_PROPOSITIONS.md
      section: A) Capacitación práctica y guiada
      version: 0.2.1
    - document: VALUE_PROPOSITIONS.md
      section: B) Experiencia presencial confiable en ubicación céntrica
      version: 0.2.1
    - document: VALUE_PROPOSITIONS.md
      section: D) Empleabilidad / reinserción laboral
      version: 0.2.1
  journey_stage:
    document: CUSTOMER_JOURNEY.md
    section: 1. Visitante / audiencia fría
    version: 0.2
  expected_transition:
    document: CUSTOMER_JOURNEY.md
    section: 3. Lead identificado
    version: 0.2
  source_date: 2026-07-10
```

## 2. Objetivo

Captar consultas y cotizaciones de personas que necesitan actualizar, recuperar o demostrar competencias de Excel para postular, cambiar de trabajo, retomar funciones administrativas o sentirse mejor preparadas ante nuevas oportunidades.

Objetivo de negocio: lead contactable con interés real en nivel, programa, fecha, valor o inscripción.

## 3. Problema concreto

- Siente que su nivel de Excel quedó desactualizado.
- No sabe qué nivel necesita ni por dónde comenzar.
- Ha aprendido de forma informal y le falta una ruta ordenada.
- Ve Excel como requisito frecuente en trabajos administrativos.
- Busca formación práctica y una evidencia de participación o aprobación cuando corresponda.

No inferir desempleo, edad, situación económica o capacidad de aprendizaje.

## 4. Hipótesis táctica

Si el mensaje reduce la inseguridad de “no saber suficiente” y presenta una ruta presencial, práctica y clara, aumentará la intención de revisar el nivel, el programa y las condiciones del curso.

Variable principal del test: actualización laboral y confianza para enfrentar tareas o postulaciones que requieren Excel.

## 5. Promesa táctica

**Actualiza tu manejo de Excel con una ruta práctica y guiada para enfrentar con mayor confianza tareas y oportunidades laborales.**

No prometer empleo, contratación, ascenso, renta o éxito en postulaciones.

## 6. Arquitectura de mensaje

### Dolor principal

“Sabes que Excel aparece en muchas ofertas y tareas, pero no tienes seguridad sobre tu nivel actual.”

### Transformación esperada

Pasar de una preparación fragmentada o insegura a una práctica estructurada con objetivos claros.

### Soporte de credibilidad

- programa y nivel informados;
- práctica guiada;
- profesor en vivo cuando corresponda;
- modalidad presencial y ubicación accesible;
- evaluación y diploma/certificado solo según condiciones vigentes.

### CTA principal

`Revisar nivel, fechas y valor`

### CTA comercial alternativo

`Cotizar mi cupo`

## 7. Rutas creativas iniciales

### Ruta A — Actualización

**Hook:** ¿Hace tiempo que no usas Excel y necesitas actualizarte?

**Texto base:** Retoma y fortalece tus habilidades con práctica guiada, un programa claro y clases presenciales en Santiago Centro. Revisa nivel, fechas y valor.

**Título:** Actualiza tu Excel

### Ruta B — Confianza

**Hook:** Que una oferta pida Excel no debería dejarte fuera antes de intentarlo.

**Texto base:** Aprende y practica herramientas de Excel útiles para tareas administrativas y laborales, con acompañamiento durante el proceso.

**Título:** Prepárate con más confianza

### Ruta C — Ruta clara

**Hook:** Ver tutoriales sueltos no siempre te dice qué aprender primero.

**Texto base:** Avanza con una ruta ordenada, ejercicios prácticos y orientación para elegir el nivel que corresponde.

**Título:** Una ruta clara para aprender Excel

Estas rutas deben revisarse para evitar que la publicidad sugiera garantía de empleo.

## 8. Público y targeting táctico

| Dimensión | Decisión inicial | Estado |
|---|---|---|
| Alcance | B2C individual | Definido |
| Geografía | Santiago / Región Metropolitana para presencial | Confirmar cobertura |
| Interés | Excel, empleabilidad, administración, actualización profesional | Hipótesis de plataforma |
| Intención | Aprender, actualizar, certificar participación o prepararse | Señal preferida |
| Exclusión conceptual | Capacitación para equipos o decisión empresarial | Derivar a `BP-003` o `BP-004` |
| Atributos sensibles | No usar edad, género, desempleo inferido u otros | Prohibido |

No segmentar usando supuestos sobre vulnerabilidad o situación laboral personal.

## 9. Destino y requisitos de landing

La landing debe mostrar:

- nivel y requisitos de entrada;
- qué aprenderá la persona;
- metodología práctica;
- modalidad y ubicación;
- fechas y duración;
- valor y formas de pago;
- diploma/certificado aplicable;
- mecanismo para consultar qué nivel corresponde.

Una evaluación diagnóstica puede ser un apoyo futuro, pero no debe bloquear el acceso a información básica.

## 10. Claims

| Claim | Estado |
|---|---|
| Actualizar conocimientos de Excel | Permitido. |
| Practicar tareas aplicables a contextos laborales | Permitido si el temario lo respalda. |
| Diploma o certificado | Confirmar denominación y condiciones. |
| Mejorar confianza al usar Excel | Permitido como expectativa, no garantía. |
| Conseguir empleo | Prohibido como promesa. |
| Asegurar una entrevista o ascenso | Prohibido. |
| Curso reconocido por todas las empresas | Prohibido sin evidencia. |
| Aprender desde cero | Confirmar que el nivel ofertado lo permita. |

## 11. Medición

| Etapa | Métrica prioritaria | Fuente |
|---|---|---|
| Exposición | alcance, frecuencia | Ads |
| Interés | visita a programa/nivel | Ads / analítica |
| Acción | consulta de nivel, formulario o WhatsApp | Edge / formulario |
| Calidad | lead contactable y respuesta | CRM / ventas |
| Resultado | cotización, inscripción y matrícula | CRM / operación |

Aprendizaje clave: verificar si las consultas corresponden realmente a actualización laboral o si el mensaje atrae interés genérico sin intención de compra.

## 12. Datos pendientes antes de activar

- nivel exacto del curso;
- si existe diagnóstico previo;
- fecha, precio, cupos y duración;
- diploma/certificado aplicable;
- equipamiento y materiales;
- URL final y UTM;
- seguimiento de consultas por nivel;
- trazabilidad en Zoho.

## 13. Definition of Done

- [x] Buyer persona y versiones registrados.
- [x] Una hipótesis principal definida.
- [x] Promesa, CTA y rutas creativas preparadas.
- [x] Claims laborales limitados de forma explícita.
- [x] Métricas de calidad comercial definidas.
- [ ] Oferta y nivel confirmados.
- [ ] Creatividad producida y revisada.
- [ ] Landing y tracking validados.
- [ ] Autorización de activación real.

## 14. Aprendizaje hacia GTM

Registrar de forma agregada:

- motivo declarado para estudiar;
- nivel percibido y nivel recomendado;
- objeciones sobre precio, tiempo o dificultad;
- tasa de respuesta y matrícula;
- porcentaje reclasificado como `BP-001` o `BP-000`;
- señales que se repitan y puedan mejorar el modelo corporativo.

No modificar `BP-002` desde Marketing. Toda propuesta requiere issue en Global y evidencia agregada.
