# ADS MCP SECURE CONNECTION RUNBOOK V01

Fecha baseline: 2026-09-13  
Repo: `misaeln-pc1/marketing-performance-capacita`  
Rama: `feature/marketing-google-official-permanent-read`
Estado: `VALIDATED_READ_PASS` — Google Ads MCP oficial conectado a ChatGPT mediante OpenAI Secure MCP Tunnel y validado con una consulta READ viva.

## 1. Objetivo

Documentar el procedimiento real, los aciertos, errores y comandos que funcionaron al construir una conexión segura entre ChatGPT y una plataforma Ads, para no repetir investigación ni trabajo manual en futuros frentes.

Baseline que se quiere reutilizar:

```text
ChatGPT web
  -> OpenAI Secure MCP Tunnel / MCP remoto oficial cuando aplique
  -> MCP/adapter de la plataforma
  -> identidad técnica separada READ o WRITE
  -> API oficial de Ads
```

Frentes previstos:

1. Google Ads READ — actual.
2. Google Ads WRITE — posterior, identidad separada.
3. Meta Ads READ — posterior.
4. Meta Ads WRITE — posterior, gate independiente.

La metodología es reusable; la arquitectura exacta NO se debe copiar ciegamente. Si Meta entrega un MCP remoto oficial, puede no necesitar tunnel local.

---

## 2. Principios que quedaron validados

1. **Probar la API antes del MCP.** Si la identidad técnica no puede leer la cuenta directamente, no tiene sentido depurar MCP/tunnel.
2. **Probar el MCP antes del tunnel.** Confirmar que el servidor local inicia con las mismas credenciales.
3. **Probar el tunnel con stub antes de unirlo al MCP real.** Aísla fallos de red/control-plane de fallos Google/Meta.
4. **Separar READ y WRITE.** Una identidad READ no debe promoverse silenciosamente a WRITE.
5. **No persistir secretos en GitHub.** GitHub sólo guarda nombres, rutas esperadas, estado y procedimiento.
6. **PowerShell env vars son por proceso.** Abrir otra ventana puede borrar el contexto y producir errores engañosos.
7. **Un error de shutdown no implica fallo de inicio.** Ctrl+C en un MCP stdio puede imprimir `CancelledError` / `KeyboardInterrupt` aunque el servidor haya arrancado correctamente.

---

## 3. Estado validado — Google Ads READ

```text
GOOGLE_ADS_SERVICE_ACCOUNT=PASS
ACCESSIBLE_CUSTOMERS=1
GOOGLE_ADS_SCOPE_ADWORDS=PASS
GOOGLE_ADS_MCP_OFFICIAL_START=PASS
OPENAI_SECURE_MCP_TUNNEL_STUB_READYZ=PASS
LOCAL_LAUNCHER_REPRODUCIBLE=PASS
TUNNEL_REAL_TO_GOOGLE_ADS_MCP=PASS
WORKSPACE_TUNNEL_BINDING=PASS
CHATGPT_GOOGLE_ADS_TOOLS=PASS
GOOGLE_ADS_MCP_AUTH=PASS
GOOGLE_ADS_ACCOUNT_ACCESS=1
LIVE_READ_QUERY=PASS
ADS_WRITES=0
SECRETS_IN_GITHUB=0
```

### Identidad Google READ

- Google Cloud project: `capacitacl-210323`
- Service Account: creada específicamente para Google Ads MCP READ.
- IAM de proyecto: no se asignaron roles innecesarios.
- La Service Account fue agregada como usuario en Google Ads con nivel **Solo lectura**.
- JSON local:

```text
C:\Users\TECH\secrets\google-ads-mcp-service-account.json
```

El contenido del JSON nunca debe copiarse a GitHub, chat, Drive ni documentación.

### Herramientas locales validadas

```text
pipx = 1.12.0
OpenAI tunnel-client = 0.0.14
Tunnel client dir = C:\Tools\OpenAI\tunnel-client
```

---

## 4. Procedimiento que funcionó — Google Ads READ

### Fase A — Crear identidad técnica

Google Cloud:

1. `IAM & Admin -> Service Accounts`.
2. Crear una Service Account dedicada al frente READ.
3. No asignar roles de proyecto si no son necesarios.
4. `Keys -> Add key -> Create new key -> JSON`.
5. Mover el archivo a una carpeta local fuera del repo.

Baseline local usado:

```text
C:\Users\TECH\secrets\google-ads-mcp-service-account.json
```

Google Ads:

1. `Access and security -> Users`.
2. Agregar el email técnico de la Service Account.
3. Para READ: permiso **Solo lectura**.
4. No reutilizar esta identidad para WRITE.

### Fase B — Verificar archivo local

```powershell
Test-Path "C:\Users\TECH\secrets\google-ads-mcp-service-account.json"
```

Esperado:

```text
True
```

### Fase C — Cargar variables Google en la sesión actual

```powershell
$env:GOOGLE_APPLICATION_CREDENTIALS="C:\Users\TECH\secrets\google-ads-mcp-service-account.json"
$env:GOOGLE_PROJECT_ID="capacitacl-210323"
$env:GOOGLE_CLOUD_PROJECT="capacitacl-210323"
```

`GOOGLE_PROJECT_ID` es la variable relevante para el Google Ads MCP oficial actual. `GOOGLE_CLOUD_PROJECT` se mantiene por compatibilidad con otras herramientas Google.

### Fase D — Probar Google Ads API directamente

Comando validado:

```powershell
python -c "import google.auth; from google.ads.googleads.client import GoogleAdsClient; creds,_=google.auth.default(scopes=['https://www.googleapis.com/auth/adwords']); c=GoogleAdsClient(credentials=creds,use_proto_plus=True); r=c.get_service('CustomerService').list_accessible_customers(); print('GOOGLE_ADS_SERVICE_ACCOUNT=PASS'); print('ACCESSIBLE_CUSTOMERS=',len(r.resource_names))"
```

Resultado real:

```text
GOOGLE_ADS_SERVICE_ACCOUNT=PASS
ACCESSIBLE_CUSTOMERS= 1
```

### Fase E — Probar Google Ads MCP oficial localmente

Comando usado:

```powershell
pipx run --spec "git+https://github.com/googleads/google-ads-mcp.git" google-ads-mcp
```

Resultado observado:

```text
Starting MCP server 'Google Ads Server' with transport 'stdio'
```

Esto significa **servidor iniciado y esperando cliente**, no proceso bloqueado.

Para detenerlo:

```text
Ctrl + C
```

Puede aparecer un traceback terminando en:

```text
asyncio.exceptions.CancelledError
KeyboardInterrupt
```

En este contexto es shutdown manual esperado; no clasificar como fallo del MCP si antes apareció `Starting MCP server...`.

### Fase F — Crear y probar OpenAI Secure MCP Tunnel con stub

Se creó en ChatGPT/OpenAI un tunnel dedicado llamado `Capacita-Google-Ads`.

Se creó una Runtime API key restringida exclusivamente a permisos de tunnel:

```text
Tunnels: Read + Use
Resto: None
```

La clave real NO se documenta.

Carga segura por sesión:

```powershell
$env:CONTROL_PLANE_API_KEY = [System.Net.NetworkCredential]::new("", (Read-Host "Pega la clave OpenAI" -AsSecureString)).Password
```

El Tunnel ID puede cargarse en la sesión como:

```powershell
$env:CONTROL_PLANE_TUNNEL_ID="<TUNNEL_ID_EXISTENTE>"
```

El ID no es una credencial de autenticación, pero no es necesario versionarlo en GitHub; preferir recuperarlo de la configuración local estable que genere #104.

Prueba del tunnel con MCP stub que dio PASS:

```powershell
cd C:\Tools\OpenAI\tunnel-client
.\tunnel-client.exe run --embedded-mcp-stub --control-plane.tunnel-id $env:CONTROL_PLANE_TUNNEL_ID --health.listen-addr 127.0.0.1:0 --health.url-file "$env:TEMP\tunnel-client-health.url"
```

En una segunda PowerShell:

```powershell
$u = Get-Content "$env:TEMP\tunnel-client-health.url"
Invoke-WebRequest -UseBasicParsing "$u/readyz" | Select-Object StatusCode, Content
```

Resultado real:

```text
StatusCode 200
Content    ready
```

Interpretación:

```text
PC -> OpenAI Secure MCP Tunnel = PASS
Runtime key = PASS
Tunnel ID = PASS
Embedded MCP = PASS
```

### Fase G — Unir tunnel real + Google Ads MCP real

Launcher versionado y validado:

```text
scripts/google_ads_mcp_read/Start-CapacitaGoogleAdsMcpRead.ps1
```

Acceso local de un paso:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\google_ads_mcp_read\Start-CapacitaGoogleAdsMcpRead.ps1
```

El launcher:

1. recupera el Tunnel ID desde estado local sin pedirlo de nuevo;
2. valida el JSON de Service Account sin imprimirlo;
3. genera el perfil local del tunnel fuera del repo;
4. solicita la Runtime API key con entrada oculta y la mantiene sólo en memoria del proceso;
5. ejecuta `doctor` antes de iniciar;
6. publica salud local y PID para `Status`;
7. usa `python -m pipx` para evitar fallos del wrapper `pipx.exe` observados en Windows.

Smoke directo, sanitizado y versionado:

```text
scripts/google_ads_mcp_read/probe_official_mcp.py
```

Resultado real:

```text
GOOGLE_ADS_MCP_INIT=PASS
GOOGLE_ADS_MCP_READ_TOOLS=PASS
GOOGLE_ADS_MCP_AUTH=PASS
GOOGLE_ADS_ACCOUNT_ACCESS=1
```

El tunnel se asoció al workspace ChatGPT autorizado y la aplicación privada `Capacita Google Ads READ` quedó conectada sin OAuth interactivo. ChatGPT detectó las tres herramientas READ del MCP oficial y ejecutó `customers_list_accessible_customers`.

Resultado vivo sanitizado:

```text
WORKSPACE_TUNNEL_BINDING=PASS
CHATGPT_GOOGLE_ADS_TOOLS=PASS
LIVE_READ_QUERY=PASS
CUSTOMER_COUNT=1
ADS_WRITES=0
GA4_CONFIG_WRITES=0
```

No registrar el identificador de cliente devuelto por la herramienta.

DoD de #104:

```text
LOCAL_LAUNCHER_REPRODUCIBLE=PASS
TUNNEL_REAL_TO_GOOGLE_ADS_MCP=PASS
GOOGLE_ADS_MCP_AUTH=PASS
GOOGLE_ADS_ACCOUNT_ACCESS=1
SECRETS_IN_GITHUB=0
ADS_WRITES=0
```

---

## 5. Errores encontrados y cómo evitarlos

### Error 1 — Reusar ADC/OAuth personal sin scope correcto

Configuración histórica:

```text
C:\local-only\google-ads.yaml
use_application_default_credentials=True
```

Prueba septiembre 2026:

```text
ACCESS_TOKEN_SCOPE_INSUFFICIENT
```

**Lección:** no asumir que un ADC que funcionó meses antes conserva scopes válidos.

### Error 2 — Reautorizar ADC por navegador/passkey

`gcloud auth application-default login` llegó a un bloqueo de autenticación/passkey en Google.

**Decisión:** no repetir esta ruta para Google Ads READ. Se reemplazó por Service Account dedicada.

### Error 3 — Depurar MCP antes de validar API

La ruta correcta fue:

```text
Service Account -> Google Ads API = PASS
THEN
Google Ads MCP = PASS
THEN
Tunnel
```

Esto elimina ambigüedad sobre dónde está el fallo.

### Error 4 — Ejecutar `--help` y esperar salida inmediata

En la versión probada, el entrypoint del Google Ads MCP inició el servidor incluso usando el intento con `--help`.

**Lección:** el indicador real es `Starting MCP server...`; detener con Ctrl+C cuando sólo se quiere smoke test.

### Error 5 — Interpretar Ctrl+C como error de ejecución

El traceback `CancelledError / KeyboardInterrupt` fue provocado por cierre manual.

**Lección:** separar `START_FAIL` de `MANUAL_SHUTDOWN`.

### Error 6 — Perder variables al abrir otra PowerShell

Se cargaron variables en una ventana y luego se continuó en otra. Resultado:

```text
TUNNEL_ID_LOADED=False
```

El comando posterior produjo:

```text
invalid tunnel ID "--mcp-command"
```

porque `$env:CONTROL_PLANE_TUNNEL_ID` estaba vacío y el parser tomó el siguiente flag como valor.

**Lección crítica:** antes de iniciar tunnel/MCP verificar sin revelar secretos:

```powershell
"API_KEY_LOADED=$([bool]$env:CONTROL_PLANE_API_KEY)"
"TUNNEL_ID_LOADED=$([bool]$env:CONTROL_PLANE_TUNNEL_ID)"
"GOOGLE_CREDS_LOADED=$([bool]$env:GOOGLE_APPLICATION_CREDENTIALS)"
"GOOGLE_PROJECT_LOADED=$([bool]$env:GOOGLE_PROJECT_ID)"
```

Todo debe ser `True` antes del launcher.

### Error 7 — Variable Google incompleta

Primero se configuró `GOOGLE_CLOUD_PROJECT`; posteriormente se confirmó que el MCP oficial espera también `GOOGLE_PROJECT_ID`.

**Baseline:** cargar ambas.

### Warning técnico — grpcio / PQC

La prueba directa emitió:

```text
grpcio < 1.83.0 does not support Post-Quantum Cryptography (PQC)
```

No bloqueó la conexión actual, pero el warning indica enforcement desde octubre de 2026.

**Acción técnica pendiente:** antes de octubre de 2026 validar/actualizar `grpcio >= 1.83.0` en el entorno que ejecute Google Ads API/MCP.

---

## 6. Patrón de secretos y archivos

### Se puede documentar/versionar

- nombres de variables;
- rutas esperadas;
- nombres de Service Accounts;
- project ID;
- estado PASS/FAIL;
- comandos que referencian variables;
- arquitectura;
- versiones de herramientas;
- errores sanitizados.

### Nunca versionar ni pegar en chat

```text
OpenAI Runtime API secret
Google Service Account private_key
JSON completo de Service Account
OAuth client_secret
refresh_token
access_token
```

Carpeta local de secretos actual:

```text
C:\Users\TECH\secrets\
```

El repo debe contener sólo referencias a esa carpeta, nunca sus archivos.

---

## 7. Plantilla reusable para cualquier Ads READ

```text
A. Elegir plataforma + objetivo READ
B. Crear identidad técnica dedicada
C. Conceder mínimo permiso en la cuenta Ads
D. Guardar secreto fuera del repo
E. Probar API oficial directamente
F. Probar MCP/adapter local o remoto
G. Si requiere tunnel: probar stub
H. Unir MCP real + tunnel
I. Validar tools desde ChatGPT
J. Ejecutar una consulta mínima sin writes
K. Documentar evidencia y cierre
```

No avanzar de fase si la anterior no tiene evidencia PASS.

---

## 8. Replicación futura — Google Ads WRITE

No ejecutar todavía.

Baseline aprobado:

```text
IDENTITY_READ != IDENTITY_WRITE
```

Propuesta de identidad futura:

```text
capacita-google-ads-write
```

La cuenta WRITE debe:

1. crearse separada de READ;
2. tener su propio JSON fuera del repo;
3. recibir sólo el permiso Google Ads necesario para editar;
4. probar autenticación y acceso antes de cualquier operación mutate;
5. usar un adapter/tool WRITE separado del MCP READ actual si el MCP oficial vigente continúa siendo read-only;
6. implementar `DRY_RUN / VALIDATE_ONLY` si la API lo permite;
7. exigir autorización explícita de Misael antes de cada cambio material.

No debe habilitarse WRITE modificando silenciosamente la Service Account READ actual.

---

## 9. Replicación futura — Meta Ads READ / WRITE

Aplicar la misma metodología, no necesariamente el mismo tunnel.

Antes de implementar:

```text
1. validar capability oficial Meta vigente;
2. determinar si MCP es remoto Meta-hosted o requiere componente local;
3. crear identidad/token con mínimo scope READ;
4. validar cuenta accesible;
5. validar una consulta READ;
6. sólo después diseñar WRITE;
7. separar READ/WRITE cuando la plataforma lo permita;
8. mantener aprobación humana para cambios materiales.
```

No asumir que Meta necesita OpenAI Secure MCP Tunnel sólo porque Google lo necesitó.

---

## 10. Checklist de diagnóstico rápido

Ante una futura caída, probar en este orden:

```text
[1] ¿Existe el archivo secreto local?
[2] ¿Las variables de la PowerShell actual están cargadas?
[3] ¿La API directa responde?
[4] ¿El MCP inicia localmente?
[5] ¿El tunnel stub da readyz=200?
[6] ¿El tunnel real logra iniciar el MCP?
[7] ¿ChatGPT ve las tools?
[8] ¿La consulta mínima devuelve la cuenta esperada?
```

Esto evita reconstruir todo el sistema cuando sólo falló una capa.

---

## 11. Evidencia / issues relacionados

- Issue #102 — conexión permanente oficial Google Ads + GA4.
- Issue #104 — finalizar Google Ads MCP READ sin trabajo manual repetitivo.
- Issue #105 — roadmap Google Ads WRITE -> Meta Ads READ/WRITE.
- PR #103 — conserva la evidencia histórica del reporting bridge rechazado y añade la ruta primaria MCP directa validada en #104.

---

## 12. Gate actual

```text
GOOGLE_ADS_READ_API=PASS
GOOGLE_ADS_MCP_LOCAL=PASS
OPENAI_TUNNEL_STUB=PASS
LOCAL_LAUNCHER_REPRODUCIBLE=PASS
REAL_MCP_TUNNEL_INTEGRATION=PASS
WORKSPACE_TUNNEL_BINDING=PASS
CHATGPT_GOOGLE_ADS_TOOLS=PASS
LIVE_READ_QUERY=PASS
GOOGLE_ADS_ACCOUNT_ACCESS=1
SECRETS_IN_GITHUB=0
ADS_WRITES=0
GA4_CONFIG_WRITES=0
GOOGLE_ADS_WRITE=NOT_STARTED
META_ADS_READ=NOT_STARTED
META_ADS_WRITE=NOT_STARTED
NO_MERGEAR_TODAVIA
ISSUE_104=PASS_READY_TO_CLOSE
```

`NEXT_BEST_ACTION`: usar este documento como baseline para los frentes independientes de Google Ads WRITE y Meta Ads READ/WRITE, cada uno con su propia autorización y gate.
