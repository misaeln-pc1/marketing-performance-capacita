# Procedimiento de análisis de estatus de Google Ads V01

## Propósito

Definir el procedimiento obligatorio cada vez que Misael solicite un **análisis de estatus**, **revisión de rendimiento**, **diagnóstico actual** o **informe de campaña** de Google Ads.

El análisis consolidado debe usar dos fuentes complementarias:

1. export fresco y read-only obtenido mediante PowerShell / Google Ads API;
2. hoja histórica automatizada de Google Drive llamada exactamente `Historial_Rendimiento_GoogleAds`.

Este procedimiento no autoriza cambios en campañas, presupuestos, pujas, anuncios, keywords, conversiones ni configuración de cuenta.

## Activadores

Aplicar este procedimiento cuando la solicitud incluya, entre otras, expresiones como:

- analizar el estado de Google Ads;
- revisar cómo está funcionando la campaña;
- entregar estatus de campaña;
- diagnosticar rendimiento;
- comparar últimos 7, 30, 90 días u otro periodo;
- identificar deterioro, fuga, competencia, calidad o conversión.

## Fuentes obligatorias

### Fuente A — PowerShell / Google Ads API

Fuente primaria para una fotografía fresca y read-only de la cuenta en la fecha de análisis.

Debe incluir, según la pregunta:

- contexto y configuración de campañas;
- campaña diaria;
- dispositivo y red;
- keywords y Quality Score;
- términos de búsqueda;
- landing pages efectivas;
- anuncios;
- acciones de conversión;
- señales competitivas propias y agregadas;
- manifest con periodo, filas, estado y errores.

Reglas:

- ejecutar fuera del repo;
- usar únicamente consultas read-only;
- cerrar el periodo en el último día completo;
- conservar CSV, ZIP, YAML, IDs y credenciales fuera de GitHub;
- verificar manifest antes de analizar.

### Fuente B — Google Drive

Fuente histórica operativa para continuidad, tendencia y comparación longitudinal.

Nombre exacto:

`Historial_Rendimiento_GoogleAds`

Pestañas conocidas:

- `Change_Log`;
- `Log_Diario_Salud_Competitiva`;
- `Log_Diario_Locations`;
- `Log_Diario_ConversionActions`;
- `Log_Diario_Campaigns`;
- `Log_Diario_Ads`;
- `Log_Diario_Terminos_Busqueda`;
- `Log_Diario_Calidad`;
- `Log_Diario_Landing_Pages`.

Reglas:

- buscar el archivo por nombre exacto al iniciar cada análisis;
- comprobar que el conector tenga acceso;
- registrar fecha/hora de última actualización visible;
- validar cobertura temporal y pestañas disponibles;
- no copiar IDs completos, URLs sensibles ni filas crudas al repo público.

## Declaración obligatoria de acceso

Antes de entregar conclusiones, declarar explícitamente:

```text
PowerShell / Google Ads API: disponible | no disponible | incompleto
Google Drive — Historial_Rendimiento_GoogleAds: disponible | no disponible | incompleto
Periodo común analizado: AAAA-MM-DD a AAAA-MM-DD
Estado del análisis: completo | provisional | bloqueado
```

### Si Google Drive no está disponible

Aunque exista export de PowerShell, indicar de forma explícita:

> No tengo acceso en esta ejecución a `Historial_Rendimiento_GoogleAds`. El análisis usa solo el export fresco de Google Ads y se considera provisional porque no puedo validar continuidad histórica ni discrepancias contra la fuente automatizada.

No presentar el resultado como análisis consolidado completo.

### Si PowerShell no está disponible

Aunque Google Drive sea accesible, indicar:

> No se recibió o no se validó un export fresco por PowerShell / Google Ads API. El análisis usa el historial automatizado y se considera provisional porque no puedo confirmar el estado actual de la cuenta en la fecha de corte.

### Si ambas fuentes faltan

Declarar el análisis bloqueado y no inferir estado actual.

## Jerarquía de fuentes

| Pregunta | Fuente principal | Fuente complementaria |
|---|---|---|
| Estado actual de cuenta | PowerShell / API | Drive |
| Tendencia histórica | Drive | PowerShell / API |
| Configuración vigente | PowerShell / API | Change Log |
| Términos y destinos actuales | PowerShell / API | logs diarios Drive |
| Evolución de CPC, CPA, QS e impression share | Drive | export fresco |
| Competidores nominales | Auction Insights manual privado | señales agregadas API/Drive |
| Leads, contactabilidad y matrícula | Zoho agregado | Google Ads y web |

Google Ads es fuente de verdad para métricas de plataforma. Drive es una réplica histórica operativa y no reemplaza la cuenta. Zoho es fuente de verdad para resultados comerciales reales.

## Reconciliación mínima entre PowerShell y Drive

Comparar, para el periodo común:

1. campañas incluidas y estado;
2. fechas disponibles y días faltantes;
3. clics, impresiones, costo, CPC y CTR;
4. conversiones, CVR y CPA registrados;
5. impression share y pérdida por ranking/presupuesto;
6. keywords, concordancia y Quality Score;
7. términos de búsqueda e intención;
8. landing pages efectivas y URLs sospechosas;
9. anuncios, destino y desalineaciones;
10. acciones de conversión;
11. ubicaciones cuando sean relevantes;
12. cambios documentados en `Change_Log`.

## Manejo de discrepancias

Si los valores difieren:

- no promediar automáticamente;
- comprobar periodo, zona horaria, último día completo, filtros y atribución;
- revisar si Drive cargó datos después del export;
- revisar duplicados por `Key_Unica` y fechas de carga;
- separar conversiones de `all_conversions`;
- registrar la discrepancia y su causa conocida o pendiente;
- usar el export fresco para el estado puntual y Drive para tendencia, salvo evidencia contraria.

Una discrepancia no resuelta debe aparecer como bloqueo o limitación del informe.

## Evidencia adicional que no cubren las dos fuentes

### Auction Insights

Los dominios competidores, overlap, position-above y outranking se obtienen manualmente desde Google Ads. El archivo permanece privado.

### Tracking y atribución

GTM/Google tag, formularios, WhatsApp y navegación entre páginas se validan mediante `misaeln-pc1/capacita-edge#27`.

### Resultado comercial

Leads, contactabilidad, cotizaciones y matrículas se reconcilian con Zoho en agregado y sin PII.

## Formato obligatorio del informe

1. **Estado de acceso a fuentes.**
2. **Fecha de corte y periodo común.**
3. **Resumen ejecutivo.**
4. **Cambios versus 7/30/90 días o baseline acordado.**
5. **Campañas, keywords, términos, landings, dispositivos y conversiones.**
6. **Discrepancias PowerShell ↔ Drive.**
7. **Hipótesis confirmadas, debilitadas y pendientes.**
8. **Datos faltantes o limitaciones.**
9. **Próxima acción recomendada.**
10. **Cambios productivos:** siempre `no ejecutados`, salvo autorización expresa independiente.

## Change Log

Antes de atribuir un resultado a una campaña, revisar `Change_Log` para identificar:

- fecha exacta del cambio;
- categoría;
- cambio realizado;
- hipótesis;
- métrica objetivo;
- impacto observado;
- responsable.

No comparar periodos como equivalentes si hubo cambios relevantes en campañas, landings, pujas, tracking, geo, anuncios u oferta.

## Seguridad

No versionar en GitHub:

- exports crudos;
- ZIP o CSV reales;
- IDs completos de cuenta, campaña, grupo, keyword o conversión;
- recursos `customers/...`;
- URLs con parámetros sensibles;
- YAML, OAuth, tokens o credenciales;
- datos personales o exports CRM.

GitHub conserva únicamente procedimiento, síntesis agregada, decisiones, riesgos y evidencia mínima sanitizada.

## Definition of Done

Un análisis de estatus se considera **completo** solo si:

- el export PowerShell/API fue validado;
- `Historial_Rendimiento_GoogleAds` fue localizado y leído;
- existe un periodo común comparable;
- se revisó `Change_Log`;
- las discrepancias fueron explicadas o declaradas;
- las limitaciones de tracking y Zoho fueron señaladas;
- Auction Insights se marcó como pendiente cuando se requieran competidores nominales;
- no se expusieron secretos, IDs completos, PII ni outputs crudos;
- no se ejecutaron cambios productivos sin autorización.

## Estado parcial permitido

Se puede entregar un análisis provisional con una sola fuente cuando exista urgencia, pero debe etiquetarse claramente como **provisional**, indicar la fuente ausente y enumerar qué conclusiones no pueden cerrarse.
