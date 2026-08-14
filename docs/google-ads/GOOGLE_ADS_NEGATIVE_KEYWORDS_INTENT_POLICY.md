# Google Ads — Política canónica de palabras clave negativas por intención

Estado: `PROPUESTO_PARA_MAIN / REGLA_DE_NEGOCIO_APROBADA / IMPLEMENTACION_ADS_NO_EJECUTADA`

Issue: #56

## Propósito

Evitar que futuros chats, agentes o revisiones vuelvan a cuestionar desde cero palabras clave negativas históricas que Capacita utiliza deliberadamente para proteger presupuesto de tráfico sin intención de matrícula.

Este documento define **la lógica de negocio**. No representa el estado vivo de listas o campañas en Google Ads y no autoriza cambios en la plataforma.

## Regla de negocio canónica

Para campañas pagadas de cursos, especialmente Excel B2C presencial, la pregunta principal no es solamente si la persona "quiere aprender Excel".

La pregunta operativa es:

> ¿La búsqueda muestra intención de comprar/asistir a un curso, o busca resolver ahora una tarea puntual mediante una explicación, ejemplo, fórmula, tutorial o recurso?

Capacita **no quiere pagar clics de intención de solución puntual** cuando el usuario busca resolver una necesidad inmediata y no muestra intención suficiente de matricularse. Ese tráfico puede ser atendido por blogs, contenido orgánico u otros recursos abiertos.

## Intención informativa / solución puntual que se negativiza deliberadamente

Existe aprendizaje histórico de campañas: búsquedas sobre temas como los siguientes pueden generar clics pagados de usuarios que quieren una respuesta puntual y no un curso:

- ejemplos de Excel;
- ejercicios o prácticas puntuales;
- atajos;
- funciones o fórmulas;
- BUSCARV u otras funciones específicas;
- SUMAR.SI u otras consultas de sintaxis;
- tablas y tablas dinámicas;
- listas desplegables;
- formatos de Excel;
- manuales;
- tutoriales;
- búsquedas tipo "cómo hacer";
- plantillas o recursos descargables cuando la intención es obtener el recurso y no comprar formación.

Estos conceptos **no deben ser eliminados automáticamente de las negativas** solo porque formen parte del temario de un curso. El criterio es la intención de búsqueda observada, no la relación académica del término con Excel.

## Intención de empleo

Búsquedas orientadas a empleo, vacantes, ofertas laborales o búsqueda de trabajo se consideran una intención distinta de compra de capacitación y pueden excluirse en campañas de cursos.

No obstante, al revisar negativas demasiado amplias debe diferenciarse entre una consulta claramente laboral y una búsqueda comercial válida como "curso Excel para el trabajo".

## Excepción aprobada: "paso a paso"

`paso a paso` **no debe negativizarse globalmente**.

Motivo: puede expresar intención comercial válida para la Landing B / Excel desde cero, por ejemplo "curso Excel paso a paso presencial".

## Regla de preservación de negativas históricas

Una negativa histórica no debe retirarse únicamente por análisis semántico teórico.

Antes de proponer eliminarla o suavizarla, revisar cuando exista evidencia disponible:

1. términos de búsqueda reales que activaron anuncios;
2. tipo de concordancia de la negativa;
3. costo/clics asociados si están disponibles;
4. posibilidad real de bloquear consultas comerciales;
5. grupo o campaña donde se aplica;
6. existencia de una landing específica capaz de capturar la intención.

Si no existe evidencia suficiente, **preservar la decisión histórica y marcar revisión**, en vez de revertirla por defecto.

## Objetivo comercial B2C Excel presencial

Para la familia A/B/C de Excel B2C presencial, el tráfico pagado debe concentrarse en usuarios con intención razonable de asistir o comprar un curso presencial de Excel básico/intermedio en Santiago Centro.

La arquitectura de intención vigente es:

- A: intención general `curso Excel presencial / básico-intermedio`;
- B: intención explícita `desde cero / principiante`;
- C: intención `clases / profesor / aprendizaje acompañado`;
- ninguna: intención informativa puntual, empleo, modalidad no deseada, clases particulares/1 a 1/domicilio, B2B/SENCE u otros fuera de alcance según la lista aplicable.

## Separación entre negativas globales y routing A/B/C

Las negativas destinadas a **eliminar tráfico no deseado de toda la campaña** pueden vivir en listas compartidas o a nivel campaña.

Las negativas destinadas a **enrutar búsquedas entre A/B/C** deben mantenerse a nivel de grupo de anuncios.

Ejemplos:

- A puede excluir `desde cero` para ceder esa intención a B.
- C puede excluir `desde cero` para ceder esa intención a B.
- B puede usar negativas exactas para consultas puramente A o C.

`desde cero`, `profesor`, `clases` u otras señales de routing **no deben convertirse sin revisión en negativas globales de campaña**, porque bloquearían el grupo que debe capturar esa intención.

## Arquitectura modular recomendada de listas

Diseño recomendado — **pendiente de implementación real y validación en Google Ads**:

1. `NEG_EXCEL__SOLUCION_PUNTUAL__V1`
   - intención informativa o de resolución puntual de Excel.

2. `NEG_INTENT__EMPLEO__V1`
   - empleo, vacantes y búsqueda laboral.

3. `NEG_MODALIDAD__NO_PRESENCIAL__V1`
   - online, virtual, remoto, e-learning y equivalentes cuando la campaña sea presencial.

4. `NEG_B2C__EMPRESA_SENCE__V1`
   - empresa, SENCE, OTIC, franquicia e intención B2B expresada de forma suficientemente específica.

5. `NEG_CURSO_GRUPAL__NO_PARTICULAR__V1`
   - clases particulares, profesor particular, 1 a 1 y domicilio para productos grupales.

6. `NEG_EXCEL_BI__FUERA_ALCANCE__V1`
   - contenidos/productos fuera de Excel básico-intermedio, por ejemplo VBA/macros/Excel avanzado/Power BI, cuando corresponda.

La lista histórica `Lista Negativas - Curso Presencial - Excel` debe tratarse como **fuente histórica a clasificar**, no borrarse ni modificarse masivamente sin revisar qué campañas la consumen y sin un plan de sustitución controlado.

## Regla para futuros chats/agentes

Cuando se retome este tema:

1. leer este documento antes de opinar sobre negativas;
2. **no pedir a Misael que vuelva a explicar por qué se negativizan ejemplos, ejercicios, atajos, funciones, fórmulas, tablas, tablas dinámicas, formatos, listas desplegables, empleo u otras señales ya cubiertas aquí**;
3. asumir como vigente el criterio de intención hasta que nueva evidencia de términos de búsqueda justifique revisarlo;
4. separar siempre `negativa para ahorrar tráfico no comprador` de `negativa para routing A/B/C`;
5. cualquier cambio en listas reales de Google Ads requiere autorización explícita y validación de alcance.

## Próximo paso recomendado

Clasificar la lista histórica exportada término por término como:

- `MANTENER`;
- `REFORMULAR`;
- `MOVER_A_LISTA_MODULAR`;
- `REVISAR_CON_EVIDENCIA`;
- `RETIRAR`.

Luego proponer una migración controlada sin tocar Google Ads hasta autorización expresa.
