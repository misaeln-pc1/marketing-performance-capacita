# automation

Documentación de necesidades de tracking, atribución y automatización comercial asociadas a campañas.

## Marketing puede documentar

- eventos y UTMs requeridos;
- trazabilidad campaña → landing → CRM → matrícula;
- condición comercial que debería gatillar un seguimiento;
- métricas esperadas;
- requerimientos para Zoho, SalesIQ, n8n o WhatsApp;
- pruebas read-only autorizadas.

## Fuentes y ejecución

- GTM/RevOps define scoring, nurturing, touch strategy y criterios comerciales.
- `Capacita-Zoho-Deluge-Core` implementa campos y código Zoho/Deluge.
- `whatsapp-n8n-zoho-capacita` implementa workflows y mensajería.
- `capacita-edge` implementa formularios y eventos frontend.
- Marketing mide el resultado de campaña y documenta la necesidad, sin duplicar la implementación.

## No incluir

- tokens, client secrets, refresh/access tokens, cookies o `.env`;
- datos personales o conversaciones privadas;
- workflows productivos exportados sin control;
- API names inventados;
- reglas comerciales paralelas a GTM;
- mutaciones de plataformas reales sin autorización.