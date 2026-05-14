# Flujo Maestro

```mermaid
flowchart LR
    captacion[Captacion] --> captura[Captura]
    captura --> crm[CRM SSOT]
    crm --> scoring[Scoring]
    scoring --> segmentacion[Segmentacion]
    segmentacion --> journeys[Journeys]
    journeys --> venta[Venta humana]
    venta --> medicion[Medicion]
    medicion --> optimizacion[Optimizacion]
    optimizacion --> captacion

    segmentacion --> b2c[B2C / particulares]
    b2c --> b2cCaliente[Particular caliente]
    b2c --> b2cTibio[Particular tibio]
    b2cCaliente --> whatsapp[WhatsApp humano]
    b2cTibio --> nutricion[Nutricion automatizada]
    whatsapp --> matricula[Matricula]
    nutricion --> scoring

    segmentacion --> b2b[B2B / empresas]
    b2b --> empresaScore[Empresa +50]
    empresaScore --> pipelineEmpresas[Pipeline EMPRESAS]
    pipelineEmpresas --> propuesta[Propuesta comercial]
    propuesta --> dealEmpresa[Deal empresa]

    segmentacion --> exalumnos[Exalumnos]
    exalumnos --> continuidad[Continuidad formativa]
    exalumnos --> crossSell[Cross-sell / up-sell]
    continuidad --> journeys
    crossSell --> venta

    segmentacion --> frios[Leads frios / no respuesta]
    frios --> bajoContacto[Journey de bajo contacto]
    bajoContacto --> reactivacion[Reactivacion]
    reactivacion --> scoring
    bajoContacto --> baja[Baja / no contactar]
```

## Lectura rapida

El flujo principal mantiene a Zoho CRM como fuente unica de verdad. Las rutas separan particulares, empresas, exalumnos y leads frios para evitar que venta humana persiga contactos sin senal suficiente.
