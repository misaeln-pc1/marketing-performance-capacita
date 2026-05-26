# Google Ads MCP Read-Only Audit

## 1. Estado de conexión MCP

Estado: bloqueado.

No hay una herramienta Google Ads MCP disponible en esta sesión de Codex. La búsqueda de herramientas disponibles no expuso un conector Google Ads, y no se encontró configuración MCP local del repo en `.mcp.json`.

## 2. Qué se intentó

- Crear rama de trabajo desde `main` actualizado.
- Buscar herramientas disponibles relacionadas con Google Ads MCP, Google Ads API, GAQL y cuentas/campañas.
- Revisar configuración MCP local del repositorio.
- Confirmar que no hay herramienta invocable de Google Ads en el entorno actual.

## 3. Consultas ejecutadas

No se ejecutaron consultas Google Ads.

Consultas read-only planificadas, bloqueadas por falta de MCP:

- listar cuentas accesibles;
- obtener metadata de `campaign`;
- ejecutar GAQL mínima de campañas.

GAQL mínima prevista:

```sql
SELECT
  campaign.id,
  campaign.name,
  campaign.status
FROM campaign
LIMIT 10
```

## 4. Error o bloqueo

Bloqueo: Google Ads MCP no está disponible o no está autenticado en este entorno.

No se solicitó ni guardó:

- developer token;
- OAuth client secret;
- refresh token;
- customer IDs sensibles;
- `.env`;
- credenciales locales.

## 5. Cuenta/campañas anonimizadas

No disponible. No se pudo listar cuentas ni campañas.

## 6. Periodo revisado

No aplica. La conexión falló antes de ejecutar consultas read-only.

## 7. Métricas agregadas

No se obtuvieron métricas. No se inventaron datos.

| Métrica | Estado |
| --- | --- |
| Gasto | No disponible |
| Impresiones | No disponible |
| Clicks | No disponible |
| CTR | No disponible |
| CPC | No disponible |
| Conversiones | No disponible |
| CPA | No disponible |
| Presupuesto | No disponible |
| Estado de campaña | No disponible |

## 8. Datos faltantes para CPQL/CPA real

- Acceso read-only a Google Ads MCP.
- Cuenta Google Ads accesible en modo lectura.
- Periodo de análisis autorizado.
- Exportación agregada de conversiones.
- Definición de lead calificado.
- Datos agregados de Zoho CRM para contacto, calificación y matrícula.
- Mapeo UTM/GCLID desde campaña a CRM.

## 9. Riesgos de tracking

- Sin conexión read-only no se puede validar si las campañas tienen conversiones configuradas.
- Sin CRM agregado no se puede calcular CPQL.
- Sin trazabilidad `gclid`, `utm_campaign`, `utm_content` o equivalente, CPA/CPQL pueden quedar desacoplados de resultados comerciales.
- Sin conversiones auditadas, Google Ads podría optimizar por señales incompletas.

## 10. Recomendaciones sin ejecutar cambios

- Habilitar Google Ads MCP en modo solo lectura antes de reintentar.
- Confirmar autenticación sin guardar secretos en el repo.
- Definir customer/account access fuera del repositorio.
- Ejecutar primero consultas read-only de cuentas y campañas.
- Exportar solo resultados agregados y anonimizados.
- No modificar bids, presupuestos, assets, anuncios, conversiones ni estados.

## 11. Confirmación de seguridad

- No se tocó ninguna campaña Google Ads.
- No se usó Google Ads API.
- No hubo mutaciones.
- No se guardaron secretos, tokens, `.env`, developer tokens ni credenciales.
- No se subieron datos personales.
- No se obtuvieron ni inventaron métricas.
