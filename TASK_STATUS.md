# Estado de Tareas

Fecha de revisión: 2026-07-12

## Prioridad activa

Completar un diagnóstico basado en evidencia antes de modificar campañas, landings, presupuesto, pujas, keywords o tracking productivo.

La línea activa integra:

- Google Ads histórico y términos reales de búsqueda;
- landing pages efectivas;
- señales de competencia y Auction Insights;
- Quality Score, dispositivo y red;
- atribución Ads → web → formularios/WhatsApp → Zoho;
- SEO técnico, SEO local y visibilidad en motores generativos;
- definición posterior de un dashboard de mejora continua.

## Estado Google Ads

- Basic Access de Google Ads API aprobado.
- Pipeline local read-only validado.
- PR #26 mergeado con export histórico de campañas.
- Primera ejecución de 90 días completada y analizada localmente.
- Siete reportes se generaron correctamente.
- Los reportes de términos de búsqueda y landing pages fallaron por compatibilidad GAQL.
- PR #29 está abierto para recuperar esos dos reportes y documentar el análisis de competencia.
- Ningún output real, customer ID, YAML, token, ZIP o CSV debe versionarse.

## Hallazgos preliminares

Los datos iniciales muestran deterioro reciente del rendimiento de Excel presencial y gasto relevante en términos o campañas con baja conversión registrada. Estos hallazgos son preliminares porque la medición web puede estar incompleta y faltan los términos reales y landing pages efectivas.

No se aprueba todavía:

- crear seis landing pages;
- separar campañas por intuición;
- aumentar presupuesto;
- modificar bids;
- pausar keywords o campañas sin completar la evidencia.

## Bloque 0 — medición y atribución

Issue técnico dueño en Capacita Edge:

- `misaeln-pc1/capacita-edge#27` — auditar cobertura GTM/Google tag y atribución Ads → formularios → Zoho.

Debe validar:

- presencia de GTM/Google tag en todas las rutas relevantes;
- persistencia de `gclid`, `gbraid`, `wbraid` y UTM;
- formularios, WhatsApp, llamadas y páginas de confirmación;
- eventos duplicados o ausentes;
- comparación agregada entre conversiones Google Ads, leads creados, leads contactables y resultados comerciales.

La falta de tracking completo puede subestimar conversiones, pero no invalida gasto, clics, CPC, términos de búsqueda, impression share o Auction Insights.

## SEO, SEO local y visibilidad IA

Issue técnico dueño en Capacita Edge:

- `misaeln-pc1/capacita-edge#28` — auditar rastreo, indexación y visibilidad en motores generativos.

Debe revisar WordPress, Cloudflare Pages, robots, headers, canonicals, sitemap, enlaces internos, Search Console, Bing, bots verificados, entidad local, datos estructurados y páginas históricas o duplicadas.

Marketing desarrollará la metodología y consumirá evidencia agregada. La implementación productiva pertenece a Capacita Edge.

## Buyer persona y activos transversales

Los buyer persona, propuestas de valor y customer journey se consumen desde los canónicos GTM/RevOps de Global. Marketing no los redefine.

Regla de mejora continua:

1. un concepto nace como hipótesis o aplicación local;
2. se documenta, prueba y mide en el repo dueño;
3. se conserva local mientras no exista evidencia suficiente;
4. cuando demuestra estabilidad y reutilización transversal, se propone a Global/Atlas;
5. Global decide adoptar, devolver para más evidencia, mantener local o rechazar;
6. un activo adoptado debe tener versión, dueño, consumidores, límites y mecanismo de actualización.

Punto de revisión global creado:

- `misaeln-pc1/capacita-global-control#101` — evaluar conceptos reutilizables descubiertos en Marketing Performance.

Candidatos iniciales a observar:

- taxonomía de intención de búsqueda;
- modelo SEO/GEO y visibilidad IA;
- benchmark de consultas generativas;
- mapa de entidad y autoridad digital;
- modelo de atribución Ads → web → Zoho;
- matriz de decisión de landing pages;
- dashboard de crecimiento y mejora continua.

Ninguno se considera canónico todavía.

## Secuencia inmediata

1. Ejecutar el export corregido del PR #29.
2. Obtener `05_search_terms_daily.csv` y `07_landing_pages_daily.csv`.
3. Analizar términos, intención, gasto, conversiones registradas y landing efectiva.
4. Exportar Auction Insights 7/30/90 días en archivos privados.
5. Completar baseline de tracking actual mediante Edge #27.
6. Completar auditoría SEO/GEO mediante Edge #28.
7. Consolidar hipótesis causales y alternativas.
8. Decidir cambios de campaña o landing solo con evidencia y autorización.
9. Definir contrato de datos del dashboard recurrente.

## Reglas operativas vigentes

- Un buyer persona primario y una hipótesis por prueba.
- Separar B2C y B2B en campaña, landing y medición.
- Mantener constantes oferta, destino y variables relevantes al comparar mensajes.
- No mezclar resultados registrados por Google con resultados comerciales sin reconciliación con Zoho.
- No modificar campañas, landings, tracking o producción sin autorización expresa.
- No subir PII, secretos, IDs completos, exports crudos, capturas sensibles ni binarios.
- No trabajar directo en `main`.

## Definition of Done del diagnóstico

- términos reales recuperados;
- landing pages efectivas recuperadas;
- competencia evaluada con señales API y Auction Insights;
- tracking auditado y sus limitaciones documentadas;
- SEO/visibilidad IA con baseline técnico;
- diferencias Google Ads → formularios → Zoho cuantificadas en agregado;
- hipótesis clasificadas como confirmadas, debilitadas o pendientes;
- alternativas de campaña y landing comparadas;
- decisión documentada con evidencia, riesgos, rollback y autorización.
