# Relaciones entre Proyectos e Infraestructura

Este documento contiene un mapa visual que ilustra cómo los diferentes proyectos y sistemas se conectan e influyen entre sí.

## Diagrama de Flujo

```mermaid
flowchart LR
    subgraph "Fuentes de Captación"
        F1[Meta Ads]
        F2[Google Ads]
        F3[Web / SEO]
        F4[Exalumnos]
        F5[Empresas / SENCE]
        F6[TrainerCentral]
    end

    subgraph "Puntos de Captura"
        C1[Meta Lead Forms]
        C2[Landings]
        C3[Zoho Forms]
        C4[SalesIQ Chat]
    end

    subgraph "Core Lógica Comercial (Zoho)"
        Z1[Zoho CRM]
        Z2[Zoho Marketing Automation]
        Z3[Zoho Campaigns]
        Z4[PageSense]
    end

    subgraph "Activos Compartidos"
        A1[Campos CRM]
        A2[Scoring]
        A3[Journeys]
        A4[UTM Tracking]
        A5[Reportes]
    end

    subgraph "Salida / Venta"
        S1[Venta Humana / WhatsApp]
        S2[Pipeline EMPRESAS]
        S3[Continuidad Formativa]
    end

    F1 --> C1; F2 --> C2; F3 --> C2;
    C2 --> C3; C1 & C3 & C4 --> Z1;
    Z1 -- Contiene --> A1; Z1 -- Alimenta --> A5; Z1 -- Dispara --> S1 & S2 & S3;
    Z2 -- Gestiona --> A2 & A3; Z2 -- Sincroniza con --> Z1;
    Z3 -- Lee/Escribe --> Z1; Z3 -- Ejecuta --> A3;
    F1 & F2 & F3 -- Usan --> A4 -- Registra en --> Z1;
    Z4 -- Optimiza --> C2;
    F4 --> Z3; F5 --> Z1; F6 --> Z1;
    A2 & A3 --> S1;
```

## Lectura del mapa

Este mapa no pretende mostrar cada detalle técnico, sino las **dependencias lógicas** entre los componentes del sistema.

Su propósito principal es servir como una herramienta de **análisis de impacto**. Antes de modificar un componente (ej: un campo en Zoho CRM), se puede consultar este mapa para identificar rápidamente qué otros sistemas o proyectos (ej: Formularios, Journeys, Reportes) se verán afectados.

Esto ayuda a prevenir errores en cascada y asegura que los cambios se realicen de manera controlada, comunicando a los responsables de las áreas impactadas.