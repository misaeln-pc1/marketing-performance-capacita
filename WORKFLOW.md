# Workflow Operativo

## Principio

Marketing no espera una lista exhaustiva de análisis de Misael. Ante un frente material debe identificar qué evidencia necesita, consultarla cuando exista acceso READ y entregar la siguiente mejor acción.

```text
CONTEXTO
→ DECISION
→ DATOS
→ DIAGNOSTICO
→ PRIORIDAD
→ HANDOFF/EJECUCION
→ VALIDACION
→ APRENDIZAJE
```

## Flujo estándar

### 0. Recuperar baseline

1. Aplicar Bootstrap o Delta según corresponda.
2. Leer `TASK_STATUS.md`, `DECISIONES.md` y el canónico específico.
3. Confirmar objetivo, alcance, campaña/página y decisión que debe habilitarse.
4. Identificar PR/issues abiertos para no duplicar ni pisar trabajo.

### 1. Definir la decisión de negocio

Antes de investigar, formular:

- qué se intenta mejorar o decidir;
- resultado comercial esperado;
- audiencia e intención;
- restricciones vigentes;
- ventana y baseline comparable;
- qué no debe cambiar.

Una solicitud como “revisa esta landing” no se reduce a una inspección visual: activa análisis de intención, diferenciación, CRO, medición y riesgos según los protocolos vigentes.

### 2. Ejecutar Opportunity Scan

Aplicar:

```text
docs/analytics/MARKETING_PROACTIVE_OPPORTUNITY_SCAN_V01.md
```

Seleccionar las fuentes pertinentes disponibles. Preferir conectores, APIs o herramientas READ ya autorizadas sobre copia/pega manual. Registrar fuente, ventana, cobertura y data gaps.

No consultar herramientas irrelevantes sólo para completar una lista. Detener la exploración cuando nueva evidencia tenga bajo beneficio marginal.

### 3. Diagnosticar y priorizar

Separar:

```text
HECHO
INTERPRETACION
HIPOTESIS
RECOMENDACION
```

No colapsar Ads, web, CRM, Deal, CursoAlumno y venta. Priorizar cada oportunidad por:

- impacto esperado;
- esfuerzo;
- confianza de la evidencia;
- riesgo/dependencia;
- reversibilidad;
- tiempo hasta aprendizaje.

### 4. Emitir paquete de decisión

Toda salida material incluye:

```text
EVIDENCIA
HALLAZGO
P0/P1/P2
ACCION_EXACTA
IMPACTO
ESFUERZO
CONFIANZA
RIESGO
DUENO
METRICA
VALIDACION
DO_NOT_CHANGE
NEXT_BEST_ACTION
```

No cerrar con consejos genéricos ni trasladar a Misael el trabajo analítico que Marketing puede resolver.

### 5. Derivar o ejecutar según frontera

- **ChatGPT / Atlas:** define criterio, consulta fuentes, analiza, prioriza, documenta y revisa.
- **Antigravity u otro agente:** modifica documentación o implementación acotada en rama mediante un único prompt operativo.
- **Capacita Edge:** implementa HTML/CSS, activos web, SEO técnico y tracking frontend.
- **Misael:** autoriza writes, campañas, presupuesto, producción, permisos y merge/main.

El handoff debe contener repo, rama, carpeta, objetivo, lecturas, cambios exactos, permitidos, prohibidos, `DO_NOT_CHANGE`, validación, evidencia, commit, push, PR y DoD.

### 6. Ejecución en rama

El agente ejecutor:

1. confirma baseline y alcance;
2. modifica sólo archivos autorizados;
3. actualiza la evidencia que no tenga otro PR abierto como dueño;
4. ejecuta validaciones aplicables;
5. prepara `REVIEW_REQUEST.md` o equivalente;
6. reporta `git status`, diff, SHA y PR.

No trabajar en `main` ni modificar plataformas externas por inferencia.

### 7. Revisión Marketing

Marketing valida:

- correspondencia con intención, buyer persona y propuesta;
- uso de evidencia y ausencia de afirmaciones inventadas;
- diferenciación de campaña/landing;
- CRO, tracking y medición;
- coherencia con canónicos;
- ausencia de PII, secretos y binarios;
- cumplimiento de `DO_NOT_CHANGE`;
- resultado visual/técnico cuando corresponda.

Si hay una falla, emitir corrección concreta. No reiniciar todo el análisis.

### 8. Activación y medición

Una campaña, landing o cambio productivo sólo se activa con autorización y gate del repo dueño.

Después de publicar/activar, comparar contra baseline y separar:

```text
ADS_SIGNAL
WEB_SIGNAL
CRM_SIGNAL
PIPELINE_SIGNAL
COMMERCIAL_RESULT
```

Registrar aprendizaje, no sólo métricas.

### 9. Cierre

Cerrar con:

- estado/gate;
- qué cambió y dónde;
- fuentes y ventana;
- evidencia y validación;
- riesgos/data gaps;
- SHA/PR o evidencia de plataforma;
- qué no se tocó;
- siguiente acción.

No declarar completado sin evidencia.

## Fast path

Para una corrección manual menor a dos minutos, reversible y sin riesgo, ejecutar la ruta simple y documentar sólo lo necesario. No crear una automatización, skill o estructura nueva si aumenta mantenimiento sin mejorar medición o recurrencia.
