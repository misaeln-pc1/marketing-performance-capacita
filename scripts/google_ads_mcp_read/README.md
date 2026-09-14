# Google Ads MCP READ local

Launcher local reproducible para conectar el Google Ads MCP oficial al OpenAI Secure MCP Tunnel usando la Service Account READ ya configurada en este PC.

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass `
  -File .\scripts\google_ads_mcp_read\Start-CapacitaGoogleAdsMcpRead.ps1
```

El launcher recupera el Tunnel ID no secreto desde el estado local, valida la credencial sin mostrarla y fija las variables del proyecto. Si `CONTROL_PLANE_API_KEY` no existe en el proceso, la solicita con entrada oculta y la conserva sólo mientras vive el proceso.

Acciones disponibles:

```powershell
# Preparar o reconstruir el perfil local sin usar red ni pedir la API key.
.\scripts\google_ads_mcp_read\Start-CapacitaGoogleAdsMcpRead.ps1 -Action Prepare

# Ejecutar preflight real del túnel y MCP.
.\scripts\google_ads_mcp_read\Start-CapacitaGoogleAdsMcpRead.ps1 -Action Doctor

# Consultar salud de un proceso ya iniciado.
.\scripts\google_ads_mcp_read\Start-CapacitaGoogleAdsMcpRead.ps1 -Action Status
```

El proceso principal queda en primer plano. Se detiene con `Ctrl+C`. No realiza writes en Google Ads y no configura GA4.
