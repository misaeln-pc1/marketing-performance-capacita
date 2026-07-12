# Aclaraciones del plan Excel B2C — puente B2B, página histórica y buyer personas

Fecha: 2026-07-12

## Alcance

Este documento complementa `EXCEL_B2C_TWO_PAGE_PLAN_AND_CRO_BASELINE_2026-07-12.md`. No autoriza cambios productivos en landings, Google Ads, PageSense, GTM, Zoho Forms, CRM o Cloudflare.

## 1. Bloque “¿Buscas capacitar a tu equipo?”

### Decisión

No eliminarlo automáticamente.

La evidencia aportada por Misael indica que el bloque ha funcionado como derivación útil para personas que llegan como particulares y luego descubren que su necesidad corresponde a una capacitación grupal o empresarial.

Se conserva como **puente secundario de intención B2C → B2B**, no como mensaje principal de la landing B2C.

### Ubicación y jerarquía

- mantenerlo al final del bloque de alternativas de pago o en una zona inferior de la página;
- no incluirlo en el hero;
- no convertirlo en CTA principal;
- no mezclar su formulario ni su conversión con el formulario B2C;
- dirigirlo a la landing B2B específica;
- registrar su clic como evento secundario separado, con nombre técnico definido por Edge;
- no contabilizarlo como submit B2C ni matrícula individual.

### Copy recomendado

**Título:** `¿La capacitación es para tu equipo?`

**Texto:** `Si necesitas inscribir a varias personas o cotizar una capacitación para tu organización, revisa las opciones para equipos.`

**CTA:** `Ver capacitación para equipos`

No prometer beneficios tributarios, SENCE, franquicia tributaria, gratuidad o condiciones empresariales sin validación vigente y específica.

### Interpretación

Este bloque no convierte la landing B2C en una landing mixta. Funciona como **router de intención**: conserva el recorrido individual y deriva una necesidad distinta hacia su página dueña.

## 2. Qué significa “página histórica de Excel básico”

El baseline Google Ads sanitizado registró que, durante los últimos 30 días observados para la keyword crítica:

- la landing vigente recibió 58 clics y CLP 69.855 de gasto, con 1 conversión registrada;
- una página histórica de Excel básico recibió 11 clics y CLP 14.666 de gasto, con 0 conversiones registradas.

La URL exacta se mantuvo fuera del repositorio público junto con los exports privados.

### “No usar como destino” significa

- no seguir enviando anuncios a esa página antigua mientras no se audite;
- no asumir que es la futura landing básica;
- no borrarla todavía;
- no redirigirla sin revisar su URL, indexación, enlaces, Search Console, sitemap y tráfico orgánico;
- decidir después entre reutilizarla, actualizarla o aplicar 301 hacia la nueva URL.

El problema no es que exista una página antigua. El problema sería publicar una nueva página básica y dejar además la histórica activa, indexable y recibiendo pauta, generando tres destinos potenciales para una misma intención.

### Próxima evidencia requerida

Identificar la URL exacta desde el reporte privado de landing pages de Google Ads o desde la configuración de assets/sitelinks. Después clasificarla como:

1. reutilizar;
2. redirigir 301;
3. mantener por una intención distinta demostrable;
4. retirar como destino pagado.

## 3. Buyer persona en Google Search

### Regla conceptual

La keyword responde principalmente a **qué busca la persona ahora**. El buyer persona responde principalmente a **por qué lo busca, qué problema intenta resolver y qué mensaje le resulta relevante**.

No son equivalentes:

- `curso Excel básico presencial` es intención de búsqueda;
- `BP-001 — Desbordado Operativo` o `BP-002 — Reinserción Laboral` son motivaciones y contextos posibles detrás de esa búsqueda.

Una misma consulta puede provenir de más de un buyer persona. Por eso no se debe inferir automáticamente el buyer persona solo por la keyword.

### Diferencia con Meta

En Meta, el buyer persona condiciona con mayor fuerza la creatividad, el hook, la audiencia y el mensaje que interrumpe al usuario.

En Google Search, la consulta ya expresa intención activa. La arquitectura recomendada es:

1. usar keywords y grupos para separar intención;
2. usar buyer persona para definir promesa, dolor, prueba, CTA y contenido de la landing;
3. mantener un buyer persona primario y una hipótesis por prueba;
4. medir calidad comercial, no solo CPC o CTR.

### Mapeo inicial recomendado

#### Página A — Básico e Intermedio / ruta completa

- intención: curso presencial completo, progresión Básico → Intermedio;
- buyer persona primario candidato: `BP-001 — Desbordado Operativo`;
- dolor central: lentitud, errores, dependencia y aprendizaje fragmentado;
- promesa: trabajar con más orden, rapidez y seguridad mediante práctica guiada;
- CTA: revisar programa, fechas, valor y matrícula.

#### Página B — Básico / desde cero

- intención: comenzar sin conocimientos previos de Excel;
- buyer persona primario candidato: `BP-002 — Reinserción Laboral`;
- dolor central: inseguridad sobre el nivel, no saber por dónde comenzar y necesidad de una ruta clara;
- promesa: comenzar desde cero con acompañamiento y avanzar con confianza;
- CTA: revisar nivel, programa, fechas y valor.

Este mapeo es una aplicación táctica inicial, no redefine los buyer persona canónicos de Global.

### B2B

El bloque de equipos deriva hacia:

- `BP-003 — Coordinador B2B`;
- `BP-004 — Dueño o Jefatura PyME`.

No se los incorpora como buyer persona de la campaña B2C. Se conserva únicamente una salida secundaria hacia la ruta B2B dueña.

## 4. Límite experimental

La arquitectura comercial de lanzamiento variará simultáneamente intención y mensaje principal:

- Página A: ruta completa + BP-001;
- Página B: desde cero + BP-002.

Esto mejora relevancia comercial, pero no permite atribuir causalmente el resultado solo al buyer persona.

Después del primer ciclo, cada página debe probar un mensaje por vez, manteniendo constantes oferta, precio, fecha, formulario, geografía, presupuesto y destino.

## 5. Cambios requeridos al Canvas y al prompt de Work

El Canvas debe corregirse así:

- reemplazar `eliminar B2B` por `mantener puente secundario hacia equipos`;
- añadir buyer persona primario por página;
- aclarar que la página histórica no se borra: se audita antes de reutilizar o redirigir;
- separar conversión B2C de clic al puente B2B;
- mantener el bloque de equipos en ambas páginas solo si conserva jerarquía secundaria y destino B2B independiente.

## Estado de decisión

- Puente B2B: **conservar con jerarquía secundaria y tracking separado**.
- Página histórica básica: **auditar; no usar como destino pagado hasta resolverla**.
- Buyer persona: **incorporar explícitamente en copy, landing y medición de Google Search; no inferirlo solo por keyword**.
