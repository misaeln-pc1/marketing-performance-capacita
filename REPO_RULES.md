# Reglas del Repositorio

## 1. Nomenclatura de Campañas

Seguir por defecto el formato: `[CIUDAD]-[PRODUCTO]-[CANAL]-[MES][AÑO]`.

Ejemplo: `SCL-EXCEL-META-MAY26`.

Cuando una plataforma o campaña histórica use otra convención, conservar su baseline y documentar la equivalencia antes de renombrar.

## 2. Gestión de Archivos

- **Markdown:** los documentos estratégicos u operativos deben ser `.md` cuando no exista una plantilla externa obligatoria.
- **Kebab-case:** usar nombres en minúsculas separados por guiones cuando no exista un nombre canónico previo.
- **No binarios:** no subir videos, imágenes, editables, fuentes o exports pesados. GitHub conserva manifest, hash, síntesis y ruta lógica; los originales viven fuera del repo.
- **Sin carpetas inútiles:** no crear carpetas o archivos sin propósito operativo inmediato.

## 3. Fuentes de verdad y datos

- Buyer personas, propuestas de valor, segmentación transversal y customer journey se consumen desde GTM/RevOps en `misaeln-pc1/capacita-global-control`.
- Toda campaña nueva o revisada aplica `docs/GTM_CONSUMPTION_BRIDGE.md` y `templates/CAMPAIGN_BRIEF_GTM.md`.
- `core/` es un índice de aplicación local y referencias; no es fuente canónica paralela de propuestas de valor.
- No duplicar funcionalidad o almacenamiento de Zoho CRM, Google Drive, Capacita Edge ni plataformas Ads.
- Los resultados reales de Ads y CRM se documentan solo en forma agregada y sanitizada.

## 4. Seguridad y privacidad

- No subir datos personales, correos, teléfonos, exports CRM ni conversaciones privadas.
- No subir `.env`, secretos, tokens, llaves API, OAuth JSON, YAML sensible ni IDs completos.
- No subir CSV/TSV/ZIP crudos, capturas sensibles ni outputs reales de plataformas.

## 5. Cambios y producción

- No trabajar directo en `main`.
- No modificar campañas, presupuestos, pujas, anuncios, keywords, conversiones, landings, tracking, CRM o producción sin autorización explícita.
- Mantener un buyer persona primario y una hipótesis por prueba.
- Separar B2C y B2B en campaña, landing y medición.
- No declarar una campaña lista para activar sin oferta, CTA, destino, tracking, claims, autorización y evidencia.