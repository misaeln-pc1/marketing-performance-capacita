# Changelog Agent

## 2026-05-26

- Se preparo auditoria documental V1 de Meta Ads sin usar API, sin tocar campanas reales y sin inventar metricas faltantes.
- Se agrego puente de performance pagada para trazar Meta -> landing/formulario -> Zoho CRM -> contacto -> matricula.
- Se intento validar Google Ads MCP read-only; quedo bloqueado porque no habia herramienta MCP disponible/autenticada.

## 2026-07-05

- Se preparo plan V0.1 para pipeline Google Ads read-only local sin depender de MCP.
- Se agregaron runbook, semillas iniciales y carpeta de output local.
- Se agregaron scripts esqueleto con configuracion externa y guardas de seguridad.
- Se corrigio `generate_keyword_ideas.py` segun el patron oficial del cliente Python.

## 2026-07-06

- PR #14 fue mergeado con el pipeline Google Ads read-only.
- Se valido ejecucion local hasta llamada API read-only.
- Se solicito Google Ads API Basic Access.

## 2026-07-08

- Google aprobo Basic Access.
- `list_accessible_customers.py` mostro dos cuentas accesibles enmascaradas.
- `generate_keyword_ideas.py` genero output TSV local no versionado.
- Se documento que las primeras semillas eran demasiado especificas para concluir demanda.
- `export_campaign_summary.py` permanecio bloqueado.

## 2026-07-10

- Se verifico el merge del contrato corporativo GTM/RevOps en Global PR #88.
- Se abrio issue #19 y se mergeo Marketing PR #20 para alinear el repo con los canonicos.
- Se creo `docs/GTM_CONSUMPTION_BRIDGE.md`.
- Se creo `templates/CAMPAIGN_BRIEF_GTM.md`.
- Se actualizaron README, contexto y carpetas para eliminar propiedad paralela de buyer personas, journey y propuesta de valor.
- Se creo `campaigns/excel-basico-intermedio-presencial-santiago/gtm-baseline-v1.md` como primer consumidor.
- Se registro `BP-001` primario y `BP-002` secundario para el antecedente V3.
- Se detecto que futuros experimentos deben separar productividad y empleabilidad si se desea atribuir resultados por perfil.
- Se abrio issue #21 para preparar los briefs operativos de los buyer personas activos.
- Se creo el indice `campaigns/excel-basico-intermedio-presencial-santiago/briefs/README.md`.
- Se crearon cuatro briefs v1.0.0 para `BP-001` a `BP-004`.
- Se dejo `BP-000` como control y no como audiencia de campana.
- Se separaron los carriles B2C y B2B y se documentaron requisitos previos de activacion.
- Se priorizo `BP-001` como primer desarrollo creativo recomendado y `BP-002` como segunda prueba.
- No se tocaron campanas, landing, CRM, Cloudflare, n8n, WhatsApp, datos reales ni produccion.

## 2026-07-11

- Se ejecuto un diagnostico Google Ads read-only de 90 dias con configuracion y outputs fuera del repo.
- El primer export produjo siete reportes validos y dos errores GAQL acotados.
- PR #29 agrego `export_missing_reports.py` para corregir terminos de busqueda y landing pages.
- La ejecucion corregida produjo 1.825 filas de terminos y 8.482 filas de landing pages, sin errores.
- Se analizaron campanas, keywords, Quality Score, terminos, dispositivos, destinos y conversiones registradas.
- Se confirmo deterioro de `curso excel basico e intermedio` por crecimiento de volumen y baja conversion registrada.
- Se confirmo mezcla de intencion y fuga hacia paginas secundarias.
- Se dejo pendiente Auction Insights nominal, assets/sitelinks, historico 12/24 meses y reconciliacion con Zoho.
- Se abrio Edge #27 para auditar GTM/Google tag y atribucion.
- Se abrio Edge #28 para auditar SEO tecnico, SEO local y visibilidad IA.
- Se abrio Global #101 para evaluar, despues de evidencia, posibles activos transversales.
- Se creo PR #30 para sincronizar `TASK_STATUS.md`, decisiones, reglas locales y mejora continua.

## 2026-07-12

- Se separo el alcance de PR #29: quedo limitado a Google Ads y diagnostico agregado.
- Los seis documentos SEO/GEO se trasladaron sin perdida a la rama `docs/marketing-seo-geo-baseline-v01`.
- Se abrio PR #31 para la metodologia SEO, Local SEO y visibilidad en motores generativos.
- Se agrego `docs/google-ads/GOOGLE_ADS_DIAGNOSIS_BASELINE_2026-07-11.md` con hallazgos sanitizados.
- Se alineo `REPO_RULES.md` con GTM/RevOps como fuente canonica.
- Se actualizaron `TASK_STATUS.md` y `DECISIONES.md` con el estado real y la secuencia vigente.
- PR #29, PR #30 y PR #31 quedaron mergeados.
- Se valido acceso al archivo de Drive `Historial_Rendimiento_GoogleAds` y sus pestanas operativas.
- Se definio `GOOGLE_ADS_STATUS_ANALYSIS_PROCEDURE_V01.md`: todo estatus recurrente debe combinar PowerShell/API fresco y Drive; si falta una fuente, el analisis se declara provisional.
- No se modificaron plataformas Ads, GTM, WordPress, Cloudflare, Zoho, campanas ni produccion.

## 2026-07-28

- Se preparo consolidacion documental minima para tres landings Excel B2C pagadas sin mergear completo PR #35.
- Se creo `docs/landing-pages/EXCEL_B2C_PAID_LANDINGS_MINIMUM_BASELINE_2026-07-28.md`.
- Se creo XFER de respuesta Marketing -> Edge `v02` para consumir Edge XFER `v05` como `CONSUMED_WITH_CHANGES`.
- Se creo `docs/BITACORA_XFER.md` para registrar el XFER producido y el XFER externo consumido.
- Se actualizaron `TASK_STATUS.md`, `DECISIONES.md` y `REVIEW_REQUEST.md` con el estado vigente del frente PR #35 / issue #43 / Edge PR #36.
- PR #46 fue mergeado en `main` con SHA `4404ddbe2c6b6d0ec209cc7dc11e0480da85771d`.
- Se preparo PR limpio desde `main` para rescatar PageSense/CRO sin mergear PR #34 antiguo.
- Se agregaron `docs/pagesense/PAGESENSE_CRO_REPORTING_BASELINE_V01.md` y `docs/pagesense/PAGESENSE_GOAL_CONFIGURATION_AUDIT_2026-07-12.md`.
- Se documento que goals de clic no son submits confirmados ni leads, y que la URL de redireccion B2C con nombre/correo es riesgo rojo de privacidad.
- PR #47 fue mergeado en `main` con SHA `1faf07729b3c3208465d4aabebd91437b1069dab` y PR #34 quedo cerrado como `SUPERSEDED`.
- Se cerro PR #28 como `SUPERSEDED/PARCIAL`, se cerro issue #27 como cierre administrativo y se creo issue #48 para residuales manuales Google Ads.
- Se preparo PR limpio desde `main` para normalizar el XFER comercial de Learning Games `GAME-EXCEL-BASICO-BLOCKS-001`, sin mergear PR #41 draft.
- Se agrego `docs/xfer/GAME-EXCEL-BASICO-BLOCKS-001/MARKETING_BRIEF.md` y se registro en `docs/BITACORA_XFER.md`.
- PR #49 fue mergeado en `main` con SHA `2863380d8db9e763c5964d4f09c319dbb7c6686b`, PR #41 quedo cerrado como `SUPERSEDED` y issue #40 como `completed`.
- Se cerro PR #39 como intento bloqueado por `ACCESS_TOKEN_SCOPE_INSUFFICIENT` y se creo issue #50 para reintento futuro Office Ads con OAuth `adwords`, sin ejecucion hasta nueva autorizacion.
- Se preparo PR limpio desde `main` para actualizar `assets/meta-ads/PRODUCTION_STANDARD_META_ADS.md` rescatando PR #8 y agregando video 4:5 para Feed, bodega externa y reglas B2C vigentes.
- No se modificaron campanas, Google Ads, Meta Ads, Edge, Cloudflare, Worker, DNS, sitemap, GTM, PageSense, Turnstile, Zoho, APIs, scripts, exports ni produccion.

## 2026-08-09

- Se revalidó la arquitectura real de Meta Ads con auditoría visual y API read-only.
- La cuenta operativa que contiene `META_TRAFFIC_EXCEL_PRESENCIAL_SANTIAGO_B2C_V3` quedó confirmada como cuenta personal/standalone bajo `Otros activos`, referencia sanitizada `...2327`.
- Se confirmó que `...2327` no pertenece actualmente a los Business Portfolios `Capacita Spa`, `Capacita` ni `Misael N. J.`.
- La referencia histórica aproximada `...9327` quedó marcada como `SUPERSEDED` y no debe volver a usarse para identificar V3.
- Se documentó que el incidente histórico recordado de WhatsApp no tiene relación demostrada con `...2327`; no se deben propagar restricciones entre activos sin evidencia.
- Account Quality de `...2327` no mostró restricciones publicitarias visibles en la revisión; V3, AS02 y AD04 estaban activos.
- Se corrigió la interpretación del límite de gasto diario: el panel indicaba gasto previsto dentro del límite, por lo que no se considera un bloqueo por límite alcanzado.
- Se registró `Capacita Spa` como candidato futuro para un System User permanente solo mediante compartir/asignar acceso a `...2327`, sin reclamar ni mover propiedad salvo aprobación específica.
- Archivo canónico actualizado en rama documental: `docs/meta-ads/META_ADS_ACCOUNT_ROUTING.md`.
- No se modificaron Meta Ads, permisos, propiedad, tokens, System Users, WhatsApp, campañas, presupuesto ni producción.

## 2026-08-13

- PR #58 fue mergeado con la política canónica de palabras clave negativas por intención para Google Ads B2C Excel presencial; issue #56 quedó completado e issue #57 cerrado como duplicado.
- Se detectó que la política mergeada conservaba estado `PROPUESTO_PARA_MAIN`; se corrige documentalmente a `VIGENTE_EN_MAIN` sin tocar Google Ads.
- Auditoría de continuidad detectó `TASK_STATUS.md`, `DECISIONES.md`, `CHANGELOG_AGENT.md` y `REVIEW_REQUEST.md` desactualizados respecto del trabajo de agosto.
- Se incorporó en `AGENTS.md` una regla anti-reinicio: recuperar decisiones y documento canónico del frente antes de recomendar y analizar solo el delta.
- Se corrigió la fuente general de archivos pesados: SharePoint/OneDrive Empresa como bodega definitiva; `external-files/marketing-performance-capacita` como staging local; Google Drive/R2 solo cuando exista uso específico documentado.
- PR #35 y #45 quedan clasificados como antecedentes históricos que no gobiernan el contexto actual; PR #52 se conserva abierto para revisión técnica específica.
- No se modificaron campañas, presupuestos, anuncios, keywords, negativas reales, cuentas Ads, APIs, scripts, producción, PII, secretos ni archivos pesados.

## 2026-08-22

- Misael definió como obligatorio aplicar a toda página o landing nueva/revisada una metodología integral SEO, Local SEO cuando aplique, AEO, GEO/AI Search, AI-readability/citabilidad, demanda/keywords, intención, buyer persona, propuesta de valor, journey/CTA, competencia, CRO, medición e impacto comercial.
- Se abrió issue `#63 [INSTRUCCIONES]` para consolidar la definición sin duplicar los canónicos SEO/GEO existentes.
- Se creó `docs/seo-ai/MARKETING_PAGE_VISIBILITY_PROTOCOL_V01.md` como gate reusable y se referenció desde `AGENTS.md`, `DECISIONES.md` y `docs/seo-ai/README.md`.
- Se dejó explícito que el protocolo es obligatorio, pero no convierte automáticamente en indexables las landings paid-only con `noindex` vigente.
- Se separó acceso de crawlers de AI-readability/citabilidad y crawlers de búsqueda/recuperación de crawlers de entrenamiento.
- Misael autorizó explícitamente el merge a `main` de este cambio documental.
- No se modificaron campañas, Google Ads, Meta Ads, landings productivas, Edge, Cloudflare, robots, WAF, canonical, sitemap, redirects, CRM, GTM, PageSense, Turnstile, credenciales, scopes ni producción.

## 2026-09-05

- Agente: Google Antigravity.
- Rama: `feature/marketing-official-read-control-plane-p0`.
- PR: `#86` (existente).
- Tarea: Task Hub #215 (Issue padre: Marketing #85).
- Fase 0 (Rescate sanitizado de PR #52 en PR #86; PR #52 histórico intacto):
  - Se rescató el contenido útil de PR #52 sin mergear, sin borrar, sin cerrar y sin tocar su rama histórica.
  - Se sanitizaron completamente IDs reales de cuenta publicitaria, tokens y rutas.
  - Se crearon `docs/meta-ads/META_ADS_READONLY_LOCAL_ENV_TEMPLATE.env.example`, `docs/meta-ads/META_ADS_READONLY_EXPORT_RUNBOOK_V01.md`, `docs/meta-ads/META_ADS_READONLY_API_ROUTE_A_PROCEDURE_V01.md` y `scripts/meta_ads_readonly/export_meta_ads_readonly.ps1`.
  - Se corrigió la referencia canónica de archivos pesados a SharePoint (`SharePoint Site / Documentos / CAPACITA/Proyectos/external-files/marketing-performance-capacita`) y OneDrive como acceso sincronizado local.
- Fase 1 (Control Plane Oficial READ y Guard de Negativas):
  - Inventario del entorno completado sin imprimir secretos: Git, PowerShell 5.1, Python 3.14.3, scripts Google Ads, MCPs configurados, variables por nombre.
  - Calibración de estados honestos tras revisión formal ID `5123538405`: `OFFLINE_CORE=PASS`, `LIVE_ADAPTER=IMPLEMENTED_HOLD_AUTH`, `LIVE_SNAPSHOT=HOLD_DATA_GAP`, `METHOD_COMPARISON=DESIGN_ONLY`, `LIVE_PARITY=NOT_RUN`, `METHOD_A=BASELINE_FALLBACK`.
  - Google Ads Fast Path (METHOD_A) auditado: smoke-read ejecutado con `ACCESS_TOKEN_SCOPE_INSUFFICIENT` por falta de scope `adwords` en ADC; queda registrado como `HOLD_WITH_EVIDENCE` y retenido como fallback.
  - Google Ads MCP oficial (METHOD_B) evaluado contra METHOD_A en 13 preguntas; paridad `NOT_RUN` en ejecución live; queda en `HOLD_WITH_EVIDENCE`.
  - Diseñado e implementado el Guard de Palabras Clave Negativas (`core/negative_guard/` y `scripts/google_ads_readonly/run_negative_guard.py`):
    - Adaptador READ de estado vivo (`GoogleAdsNegativeReadAdapter`) para 6 entidades de negativas (customer negative, shared set, shared criterion, campaign shared set, campaign criterion, ad group criterion) con filtrado de status `REMOVED`/`UNKNOWN`, enmascaramiento seguro de IDs y fail-closed a `HOLD_DATA_GAP`.
    - Contrato de campaña fail-closed (`CampaignContract`, `CampaignRegistry`) con tipado estricto (audiencia, producto, modalidad) y rechazo explícito de entidades o intenciones desconocidas.
    - Idempotencia persistente cross-process (`RecommendationLedger`) almacenada fuera de git / tempdir con clave `manifest_hash + recommendation_hash`.
    - Normalización diacrítica/Unicode (NFKD) para tildes y precedencia estricta de B2B sobre routing.
    - Snapshot completo (Schema 1.1.0) con attachments de shared sets, estados activos, razón de hold y validación de round-trip.
    - CLI fail-closed requiriendo `--candidates-json` o `--demo` explícito, devolviendo exit code 2 machine-readable en `HOLD_DATA_GAP`.
  - Script PowerShell de Meta Ads blindado para `Set-StrictMode -Version Latest` mediante `Get-PropSafe` y validado con prueba mock (`tests/test_meta_script_mock.ps1`, `META_SCRIPT_RUNTIME=MOCK_PASS`).
  - GA4, GSC y Meta Ads evaluados en READ y documentados con estado `HOLD_WITH_EVIDENCE`.
  - Diseñada allowlist READ agregada para Zoho CRM Data Insights, marcando nombres de campos como `CONCEPTUAL_UNVERIFIED` hasta lectura de metadata real.
  - Creada suite de pruebas ampliada a 13 tests unitarios (`tests/test_negative_guard.py`: 100% OK en 0.026s) y runner de validación integral sobre el diff real `origin/main...HEAD` (`scripts/run_offline_validations.py`).
  - Cero writes en Google Ads, Meta Ads, CRM o producción (`ADS_WRITES=0`, `CRM_WRITES=0`, `PRODUCTION_WRITES=0`).
  - Validación de seguridad: `SECRETS_IN_GITHUB=0`, `PII_IN_GITHUB=0`, `FULL_IDS_IN_NEW_DIFF=0`, `git diff --check` limpio.
- Estado final de entrega: PR #86 actualizado con corrección exhaustiva de hallazgos P0/P1 del Review ID `5123538405`.

## 2026-09-05 (Revisión Formal P0 - Review ID 5123583986)

- Agente: Google Antigravity.
- Rama: `feature/marketing-official-read-control-plane-p0`.
- PR: `#86`.
- Review ID Resuelto: `5123583986`.
- Tarea: Task Hub #215 (Issue padre: Marketing #85).
- Correcciones implementadas y validadas:
  1. Google Ads Account-Level Negatives: Reemplazado el GAQL inválido de `customer_negative_criterion` por la API oficial basada en `negative_keyword_list.shared_set`, soportando tipos `NEGATIVE_KEYWORDS` y `ACCOUNT_LEVEL_NEGATIVE_KEYWORDS`, y recuperando términos reales desde `shared_criterion` con tipo `KEYWORD`.
  2. Filtro estricto de tipos: En `shared_criterion`, `campaign_criterion` y `ad_group_criterion` se exige `type = 'KEYWORD'`, descartando criterios sin texto, con match type `UNKNOWN`, o cuyo parent/shared set esté en estado `REMOVED` o `UNKNOWN`.
  3. Campaign Mapping: Clave principal migrada a `campaign_id_hash`, con comprobación secundaria por nombre/familia; fail-closed ante ID no registrado, nombre incompatible, cero matches o colisiones. Retiradas campañas Meta del registro de Google Ads.
  4. Alineación B2C/B2B y Matriz A/B/C: Permitido `B2B_SENCE` como intención excluible en B2C Excel según política canónica. Implementada matriz estricta de routing A/B/C (A y C ceden a B; B bloquea exclusión de 'desde cero'; 'profesor/clases' solo en destinos válidos; fail-closed `HOLD_REVIEW` en grupos no configurados).
  5. Compatibilidad de Producto y Modalidad: Validación real que impide aplicar taxonomía Excel a Power BI (`PRODUCT_MISMATCH -> HOLD_REVIEW`), protege términos propios del producto activo, prohíbe negativizar online en modalidad ONLINE o MIXTA, y arroja `HOLD_REVIEW` si el producto es `UNKNOWN`.
  6. Protected Terms Match-Aware y Scope-Aware: Eliminado substring ingenuo. Términos aislados (`presencial`, `curso excel presencial`) generan `CONFLICT`; frases compuestas con modificador (`curso excel presencial gratis`, `curso excel presencial empleo`, `curso excel para empresas`) son evaluadas por intención y aceptadas como `CANDIDATE`.
  7. Ledger Fail-Closed y Concurrencia Atómica: Corrupción genera `HOLD_REVIEW` (no `{}`). Implementado lock atómico con archivo `.lock`. Prueba de subprocesos concurrentes confirmada con `PROCESS_1_RECOMMENDATIONS > 0` y `PROCESS_2_RECOMMENDATIONS = 0`.
  8. Hashes e Identificadores: Recálculo obligatorio de `state_hash` y detección de manipulación (`HOLD_REVIEW`). Preservación de sentinels (`none`, `unknown`, `global`, `n/a`) sin hashear. Clave HMAC dinámica fuera de Git.
  9. Código Productivo Meta Ads: Módulo importable `MetaAdsExportHelpers.psm1` con helpers de extracción y sanitización estricta (`Sanitize-MetaText`, `Sanitize-MetaUri`). Eliminación de código duplicado en tests (`test_meta_script_mock.ps1`).
  10. Security Validation y Suite de Pruebas: Verificación estricta de `origin/main`, diff real y archivos modificados analizados; 16 tests unitarios pasando al 100% en `test_negative_guard.py`; validación limpia de whitespace en Git.
  11. Documentación: Deduplicación de títulos en especificación técnica, eliminación de referencias restantes a staging en control plane, y actualización de `REVIEW_REQUEST.md`, `AGENT_FEEDBACK.md` y PR #86.
- Guardrails operativos estrictamente cumplidos: `ADS_WRITES=0`, `CRM_WRITES=0`, `PRODUCTION_WRITES=0`, `MERGE=0`.
- Declaración oficial de estado: `OFFLINE_CORE=PASS`, `LIVE_ADAPTER=IMPLEMENTED_HOLD_AUTH`, `LIVE_SNAPSHOT=HOLD_DATA_GAP`, `LIVE_PARITY=NOT_RUN`.
- Estado: PR #86 listo para re-revisión formal. No hacer merge.

## 2026-09-06 (Re-revisión P0 y Reconciliación con main)

- Agente: Gemini / Google Antigravity.
- Rama: `feature/marketing-official-read-control-plane-p0`.
- PR: `#86`.
- Tarea: Task Hub #215 (Issue padre: Marketing #85).
- HEAD inicial bootstrap: `2bdd3c8870dda3d80edb83bf8bdde1a8597a6313`.
- Correcciones P0 implementadas y validadas:
  1. HMAC Fail-Closed: Eliminado todo fallback público/fijo de `CAPACITA_HMAC_KEY`. Requerida clave externa; fail-closed ante clave ausente para IDs reales. Implementada validación regex estricta `^hash_[0-9a-f]{12}$` para valores pre-hasheados, rechazando `alias_*` y strings ambiguos. Preservados sentinels canónicos (`none`, `unknown`, `global`, `n/a`).
  2. Ledger Atómico: Reemplazado patrón `is_recorded() -> record()` por `claim_once(...)` interproceso bajo un único lock atómico con recarga de disco y validación de corrupción (`HOLD_CORRUPT`). Verificado mediante test obligatorio con 2 subprocesos concurrentes (`test_21`).
  3. Tratamiento Estricto de PAUSED: Solo `ENABLED` es considerado activo en `active_items()`. Los criterios `PAUSED` no bloquean como activa y emiten señal diferenciada `EXISTS_PAUSED` / `REVIEW_REACTIVATION` a través de los 4 alcances (`CUSTOMER`, `SHARED_SET`, `CAMPAIGN`, `AD_GROUP`), verificado en `test_22`.
  4. Google Ads Live Executor Cableado: Implementado `core/negative_guard/live_executor.py` con `GoogleAdsClient.load_from_storage` y `search_stream` (SELECT-only), transformando filas a diccionarios para `GoogleAdsNegativeReadAdapter`. Configuración externa privada vía `--runtime-config-path` (`google_ads_config_path`, `customer_id`, `campaign_contract_path`, `ledger_path`). Mappings demo confinados a tests y mapping operacional privado para live (`LIVE_EXECUTOR_WIRED=IMPLEMENTED_HOLD_AUTH`, `LIVE_API_CALL=NOT_RUN`, `LIVE_SNAPSHOT=HOLD_DATA_GAP`).
  5. Meta Ads Error Sanitization: Script productivo `export_meta_ads_readonly.ps1` no expone URLs, tokens ni query strings en excepciones fatales. Implementado test end-to-end `test_meta_e2e_sanitization.ps1` que valida `TOKEN_IN_STDOUT=0`, `TOKEN_IN_STDERR=0`, `TOKEN_IN_MANIFEST=0`.
  6. Manifest Hash Tamper Detection: Recálculo y comparación de `manifest_hash` al deserializar snapshot; manipulación genera `HOLD_REVIEW` con `MANIFEST_HASH_TAMPER_DETECTED`. Preservada detección a nivel de item `state_hash`.
  7. Reconciliación con main: Merge limpio de `origin/main` (PR #88) integrando handoff Marketing → Edge (`MARKETING_EDGE_SLOT_PUBLICATION_HANDOFF_V01.md`), `VENUE_ID`, `CAMPAIGN_LAUNCH_ALLOWED=YES` y reconciliando `TASK_STATUS.md` sin pérdida de contexto ni contradicciones semánticas.
- Pruebas: 25 tests unitarios en Python (`test_negative_guard.py`) 100% OK; 2 tests en PowerShell 100% OK; runner `run_offline_validations.py` 100% OK.
- Guardrails: `ADS_WRITES=0`, `CRM_WRITES=0`, `PRODUCTION_WRITES=0`, `MERGE=0`.
- Estado: PR #86 en estado `DRAFT_READY_FOR_FINAL_REVIEW`.

