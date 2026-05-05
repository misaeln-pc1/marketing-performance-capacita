# Reglas del Repositorio

## 1. Nomenclatura de Campañas
Seguir siempre el formato: `[CIUDAD]-[PRODUCTO]-[CANAL]-[MES][AÑO]`
*Ejemplo:* `SCL-EXCEL-META-MAY26`

## 2. Gestión de Archivos
* **Markdown:** Todo documento estratégico o de texto debe ser `.md`.
* **Kebab-case:** Nombres de archivos en minúsculas separados por guiones (ej: `plan-de-medios.md`).
* **No Binarios:** No subir videos o imágenes pesadas al repo. Usar links a Drive en la carpeta `/assets`.
* **Sin Carpetas Inútiles:** No crear carpetas o archivos que no tengan un propósito inmediato (no hacer sobreingeniería).

## 3. Estructura de Datos
* Las propuestas de valor se definen en `core/value-propositions/` y se invocan en los anuncios para asegurar coherencia.
* **No duplicar sistemas:** No duplicar la funcionalidad o almacenamiento de Zoho CRM, Google Drive ni plataformas Ads en este repositorio.

## 4. Seguridad y Privacidad
* **No subir datos personales:** Jamás incluir emails reales, teléfonos, u otra PII (Personally Identifiable Information).
* **No subir credenciales:** Prohibido subir `.env`, secretos, tokens, llaves API o archivos similares de autenticación.