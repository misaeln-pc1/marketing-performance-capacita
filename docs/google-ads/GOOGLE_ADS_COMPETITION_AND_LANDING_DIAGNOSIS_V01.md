# Diagnóstico de competencia y landing pages Google Ads V01

## Objetivo

Completar la evidencia necesaria antes de decidir si Search de Excel requiere una landing, varias landings, nuevos grupos de anuncios, campañas separadas, keywords negativas o cambios de puja.

Este protocolo no autoriza cambios en Google Ads. Es documental y read-only.

## Capas de evidencia

### 1. Google Ads API — automatizada y read-only

Usar el diagnóstico de 90 días y `export_missing_reports.py` para obtener:

- términos reales de búsqueda;
- keyword activadora y concordancia;
- campaña y grupo de anuncios;
- dispositivo y red;
- gasto, clics, CPC, conversiones registradas y CPA;
- URL expandida de destino;
- participación de impresiones de campaña y keyword;
- pérdida por ranking y presupuesto;
- tasas de parte superior y primera posición absoluta;
- Quality Score, CTR esperado, relevancia del anuncio y experiencia de landing.

Estas señales permiten evaluar presión de ranking, mezcla de intención, conversión post-click, dispositivo, red, keyword y destino.

### 2. Auction Insights — export manual privado

Los competidores nominales, como Superprof, deben evaluarse mediante Estadísticas de subasta en la interfaz de Google Ads.

Exportar CSV privados para 7, 30 y 90 días en:

- campaña `EXCEL-PRE-STGO`;
- grupo de anuncios presencial cuando exista separación suficiente;
- keywords de gasto alto, especialmente `curso excel básico e intermedio`, `curso excel presencial` y `clases de excel presencial`.

Columnas esperadas:

- dominio visible;
- participación de impresiones;
- tasa de superposición;
- tasa de posición superior;
- tasa de parte superior;
- tasa de primera posición absoluta;
- porcentaje de ranking superior;
- periodo;
- dispositivo cuando esté disponible.

Auction Insights requiere actividad suficiente. Los CSV con competidores permanecen privados y no se versionan en este repositorio público.

## Regla de decisión de landing

No crear seis landing pages únicamente porque existen seis clusters de keywords.

Una hipótesis de landing distinta se justifica solo cuando el cluster reúne:

1. intención materialmente diferente;
2. gasto o clics suficientes para evaluar;
3. patrón estable en términos de búsqueda;
4. promesa, prueba, CTA u objeciones diferentes;
5. volumen suficiente para una prueba controlada;
6. medición separada y oferta/destino constantes dentro de la prueba.

Intenciones candidatas a evaluar después de revisar la evidencia:

- Excel presencial Santiago Centro;
- Excel básico desde cero;
- Excel básico e intermedio;
- clases particulares o profesor a domicilio;
- Excel para empresas.

`Clases particulares / profesor a domicilio` no debe mezclarse con la oferta de curso en sala salvo que el servicio exista, esté autorizado y la landing, el anuncio y la operación cumplan esa promesa.

## Matriz de interpretación

| Evidencia | Acción probable a evaluar |
|---|---|
| Gasto alto, baja conversión y consultas irrelevantes | negativas o concordancia más estricta antes de crear landing |
| Gasto alto, intención coherente y experiencia de landing débil | prueba de landing dedicada |
| CPC alto, alta participación y poca pérdida por ranking | competencia no parece causa principal |
| CPC creciente más mayor superposición/posición superior de competidores | hipótesis competitiva gana soporte |
| Conversiones Google mayores que leads CRM | reconciliar tracking/CRM antes de cambiar medios |
| Intención B2B distinta | campaña, landing y medición separadas de B2C |

## Evidencia requerida antes de decisiones de activación

- informe corregido de términos de búsqueda;
- informe corregido de landing pages;
- comparación API 7/30/90;
- Auction Insights privado 7/30/90;
- comparación CRM agregada sin PII;
- propuesta de negativas;
- matriz conservar / pausar / aislar;
- recomendación de experimento de landing con un buyer persona primario y una hipótesis.

## Seguridad

No versionar:

- exports crudos de Google Ads;
- CSV de Auction Insights;
- customer IDs completos;
- tokens, OAuth o YAML;
- exports CRM o PII.

Solo pueden volver a GitHub hallazgos agregados, sanitizados y trazables.