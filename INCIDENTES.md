# INCIDENTES

## 2026-07-10 — placeholder vacío creado y eliminado en rama de diagnóstico Google Ads

- **Rama:** `feature/marketing-google-ads-history-v01`.
- **Incidente:** se creó accidentalmente `docs/google-ads/.placeholder` vacío durante una llamada de herramienta incorrecta.
- **Corrección:** archivo eliminado inmediatamente antes de abrir PR.
- **Impacto:** ninguno en `main`; sin código, datos, secretos ni outputs afectados.
- **Prevención:** usar `create_issue` para problemas y no reutilizar acciones de archivos como sustituto.
