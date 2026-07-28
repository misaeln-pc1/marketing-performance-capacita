# REVIEW_REQUEST

## Objetivo de revision vigente

Revisar el PR documental limpio que actualiza el estandar de produccion de assets Meta Ads desde `main` y reemplaza al PR #8 antiguo como fuente a mergear.

Este PR no activa campanas, Ads Manager, API, publicaciones ni produccion. Solo consolida reglas documentales para producir creatividades Facebook/Instagram.

## PR en revision

- Rama: `docs/marketing-meta-ads-production-standard-clean-20260728`.
- Alcance:
  - actualizacion de `assets/meta-ads/PRODUCTION_STANDARD_META_ADS.md`;
  - rescate de contenido util de PR #8;
  - incorporacion de video 4:5 para Feed si se activa Feed;
  - incorporacion de bodega externa `external-files/marketing-performance-capacita/meta-ads/...`;
  - actualizacion de estado, decisiones y changelog;
  - clasificacion de PR #8 como antecedente historico/superseded despues del merge.

## Archivos esperados

```text
assets/meta-ads/PRODUCTION_STANDARD_META_ADS.md
TASK_STATUS.md
DECISIONES.md
CHANGELOG_AGENT.md
REVIEW_REQUEST.md
```

## Validacion solicitada

Confirmar que el PR:

1. no toca Meta Ads Manager, campanas, presupuesto, pujas, anuncios, audiencias, formularios ni produccion;
2. no contiene binarios, imagenes, videos, editables, fuentes, PII, secretos ni exports crudos;
3. mantiene GitHub solo para documentacion, checklist, naming, estado e indice de ubicacion externa;
4. exige imagenes 4:5, 1:1 y 9:16 por creatividad;
5. exige video 9:16 para Stories/Reels;
6. exige video 4:5 para Feed si se activa Instagram/Facebook Feed;
7. prohíbe usar un unico video 9:16 para todos los placements;
8. alinea la bodega externa con `external-files/marketing-performance-capacita/meta-ads/...`;
9. conserva reglas B2C: no mezclar empresa/SENCE/OTIC, no prometer empleo, gratuidad ni resultados garantizados;
10. distingue el estandar de creatividades del routing de cuenta Meta Ads, que sigue en `docs/meta-ads/META_ADS_ACCOUNT_ROUTING.md`.

## Gates

```text
REQUIERE_REVISION_MISAEL
NO_MERGEAR_TODAVIA
```

Si el diff es correcto y sigue siendo documental, el siguiente paso sera pedir autorizacion de merge con la frase acordada.

## No hacer desde esta revision

- No cerrar PR #8 todavia.
- No modificar Meta Ads Manager.
- No subir assets reales.
- No crear campanas ni anuncios.
- No ejecutar APIs.
- No mergear sin autorizacion expresa.
- No tocar produccion ni plataformas.