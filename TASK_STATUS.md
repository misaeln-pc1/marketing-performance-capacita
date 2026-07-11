# Estado de Tareas

Fecha de revisión: 2026-07-12

## Prioridad activa

Completar el diagnóstico basado en evidencia antes de modificar campañas, landings, presupuestos, pujas, keywords, conversiones o tracking productivo.

La línea activa integra:

- Google Ads histórico y términos reales de búsqueda;
- landing pages efectivas;
- competencia y Auction Insights;
- Quality Score, dispositivo, red, assets y sitelinks;
- atribución Ads → web → formularios/WhatsApp → Zoho;
- SEO técnico, SEO local y visibilidad en motores generativos;
- contrato futuro de datos para dashboard y mejora continua.

## Estado Google Ads

- Basic Access de Google Ads API aprobado.
- Pipeline local read-only validado.
- PR #26 mergeado con export histórico.
- Export de 90 días completado para 2026-04-12 a 2026-07-10.
- Los siete reportes iniciales válidos fueron analizados localmente.
- PR #29 corrigió los dos reportes faltantes:
  - `05_search_terms_daily.csv`: 1.825 filas, `ok`;
  - `07_landing_pages_daily.csv`: 8.482 filas, `ok`.
- La evidencia agregada y sanitizada quedó en `docs/google-ads/GOOGLE_ADS_DIAGNOSIS_BASELINE_2026-07-11.md` dentro de PR #29.
- Los CSV, ZIP, URLs completas, IDs, YAML, tokens y credenciales permanecen fuera del repo.

## Hallazgos confirmados

- `curso excel básico e intermedio` aumentó fuertemente su volumen y participación de gasto con baja conversión registrada.
- Esa keyword mezcla intenciones: básico, intermedio, desde cero, clases, gratis e informativas.
- `EXCEL-PRE-STGO` concentra múltiples intenciones en un solo grupo y un único anuncio responsive activo.
- Existe tráfico pagado hacia páginas secundarias con desempeño considerablemente inferior a la landing principal.
- `EXCEL-EMPRESA` presenta gasto relevante y conversión registrada muy débil; requiere auditoría B2B y de objetivos compartidos.
- La campaña presencial conserva alta participación de impresiones y poca pérdida por ranking/presupuesto; la competencia no está confirmada como causa principal.

## Hipótesis pendientes

- presión de precio por competidores específicos, incluido Superprof;
- necesidad real de una landing específica para básico–intermedio;
- origen exacto de la fuga hacia páginas secundarias mediante assets o sitelinks;
- submedición por cobertura incompleta de GTM/Google tag;
- mezcla B2C/B2B en conversiones o `landing_code`;
- canibalización entre páginas vigentes e históricas;
- problemas de rastreo, entidad, autoridad o SEO local que afectan visibilidad en motores generativos.

No se aprueba todavía:

- crear seis landing pages;
- separar campañas por intuición;
- aumentar presupuesto o pujas;
- pausar campañas o keywords;
- agregar negativas;
- modificar conversiones;
- cambiar GTM, WordPress, Cloudflare, Zoho o producción.

## Competencia y Auction Insights

La API permite obtener señales competitivas propias y agregadas, pero no el informe nominal con dominios competidores.

Próxima descarga manual privada:

1. campaña `EXCEL-PRE-STGO`, 90 días;
2. después 30 y 7 días;
3. repetir para:
   - `curso excel básico e intermedio`;
   - `curso excel presencial`;
   - `clases de excel presencial`.

No subir Auction Insights al repo público. Analizar en privado y versionar solo hallazgos agregados.

## Bloque 0 — medición y atribución

Issue técnico dueño:

- `misaeln-pc1/capacita-edge#27` — cobertura GTM/Google tag y atribución Ads → formularios → Zoho.

Debe validar:

- cobertura en todas las rutas relevantes;
- persistencia de `gclid`, `gbraid`, `wbraid` y UTM;
- navegación entre WordPress, Cloudflare Pages, dominios y subdominios;
- formularios, WhatsApp, llamadas y confirmaciones;
- eventos duplicados o ausentes;
- objetivos primarios/secundarios y posibles conversiones compartidas;
- comparación agregada Google Ads → formularios → leads Zoho → resultados comerciales.

La submedición puede afectar conversiones, CVR y CPA; no invalida gasto, clics, CPC, términos, Quality Score o señales de subasta.

## SEO, SEO local y visibilidad IA

- PR #31 separa la metodología SEO/GEO del PR Google Ads.
- Edge issue #28 conserva la auditoría técnica dueña.
- Marketing define consultas, intención, benchmark, medición agregada e impacto comercial.
- Capacita Edge implementa robots, headers, sitemap, canonicals, structured data, Cloudflare, frontend y eventos.

El baseline debe distinguir rastreo, indexación, duplicidad, entidad local, autoridad externa y variabilidad de motores generativos. La ausencia de Capacita en una respuesta aislada no prueba bloqueo de bots ni ranking estable.

## Buyer persona y activos transversales

Los buyer persona, propuestas de valor y customer journey se consumen desde Global/Atlas. Marketing no los redefine.

Ciclo de mejora continua:

1. hipótesis o aplicación local;
2. prueba y evidencia en el repo dueño;
3. aprendizaje estable y reutilizable;
4. candidato transversal;
5. revisión en Global/Atlas;
6. adopción versionada, permanencia local o rechazo.

Punto de revisión:

- `misaeln-pc1/capacita-global-control#101`.

Ningún candidato nuevo se considera canónico todavía.

## PR y ramas activas

| PR | Rama | Alcance | Estado esperado |
|---|---|---|---|
| #29 | `fix/marketing-google-ads-missing-reports-v02` | Exportador corregido, protocolo Google Ads y baseline agregado | revisar y mergear antes de cerrar la recuperación de reportes |
| #30 | `docs/marketing-continuous-learning-routing-v01` | estado, decisiones, reglas locales y trazabilidad | revisar y mergear después de validar diff |
| #31 | `docs/marketing-seo-geo-baseline-v01` | metodología SEO/Local SEO/visibilidad IA | revisar separado; no condiciona extracción Ads |

## Secuencia inmediata

1. Validar y mergear PR #29 si diff y checks permanecen limpios.
2. Validar y mergear PR #30 para sincronizar estado y gobernanza.
3. Revisar PR #31 como línea documental independiente.
4. Descargar Auction Insights de campaña 90 días y analizar formato.
5. Completar 7/30/90 y keywords priorizadas.
6. Exportar assets/sitelinks read-only y ampliar histórico a 12/24 meses si responde a una decisión concreta.
7. Ejecutar auditoría Edge #27.
8. Ejecutar auditoría Edge #28.
9. Reconciliar Google Ads, formularios y Zoho en agregado.
10. Construir matriz conservar / negativizar / pausar / aislar / separar / nueva landing.
11. Solicitar autorización antes de cualquier cambio productivo.

## Reglas operativas vigentes

- Un buyer persona primario y una hipótesis por prueba.
- Separar B2C y B2B en campaña, landing y medición.
- Mantener constantes oferta, destino y variables relevantes al comparar mensajes.
- No mezclar conversiones registradas por Google con resultados comerciales sin reconciliación.
- No trabajar directo en `main`.
- No subir PII, secretos, IDs completos, exports crudos, capturas sensibles ni binarios.
- No inventar métricas, claims, IDs o resultados.

## Definition of Done del diagnóstico

- términos reales y landing pages recuperados;
- competencia evaluada con señales API y Auction Insights;
- assets/sitelinks explicados cuando afecten destinos;
- tracking auditado y limitaciones documentadas;
- SEO/visibilidad IA con baseline técnico;
- diferencias Google Ads → formularios → Zoho cuantificadas en agregado;
- hipótesis clasificadas como confirmadas, debilitadas o pendientes;
- alternativas de campaña y landing comparadas;
- decisión documentada con evidencia, riesgos, rollback y autorización.