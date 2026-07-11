# Google Ads competition and landing diagnosis V01

## Objective

Complete the evidence needed before deciding whether Excel Search requires one landing page, several landing pages, new ad groups, separate campaigns, negative keywords, or bid changes.

This protocol does not authorize changes in Google Ads. It is read-only and documentary.

## Evidence layers

### 1. Google Ads API — automated read-only

Use the existing 90-day diagnosis plus `export_missing_reports.py` to obtain:

- actual user search terms;
- triggering keyword and match type;
- campaign and ad group;
- device and network;
- spend, clicks, CPC, conversions and CPA;
- actual expanded landing URL;
- campaign and keyword impression share;
- impression share lost by rank and budget;
- top and absolute-top impression rates;
- Quality Score, expected CTR, ad relevance and landing-page experience.

These signals can show whether CPC deterioration is associated with rank pressure, intent mixing, low post-click conversion, device, network, keyword, or landing mismatch.

### 2. Auction Insights — manual private export

Named competitors such as Superprof must be evaluated with Google Ads Auction Insights in the Google Ads interface.

Export private CSV files for 7, 30 and 90 days at:

- campaign level for `EXCEL-PRE-STGO`;
- ad-group level for the Excel presencial ad groups;
- keyword level for high-spend terms, especially `curso excel básico e intermedio`, `curso excel presencial`, `clases de excel presencial` and related terms.

Requested columns:

- display URL domain;
- impression share;
- overlap rate;
- position above rate;
- top of page rate;
- absolute top of page rate;
- outranking share;
- time period;
- device segment when available.

Auction Insights requires sufficient activity and does not include Search Partners in the same way as Google Search. Keep the export private; do not version competitor-level CSVs in this public repository.

## Landing-page decision rule

Do not create six landing pages merely because six keyword clusters exist.

A distinct landing-page hypothesis is justified only when a cluster has all of the following:

1. materially different user intent;
2. enough spend or clicks to evaluate;
3. a stable query pattern in the search-term report;
4. a different promise, proof, CTA or objection set;
5. enough volume to support a controlled test;
6. separate measurement and a constant offer/destination within the test.

Initial candidate intents to test after evidence review:

- Excel presencial Santiago Centro;
- Excel básico desde cero;
- Excel básico e intermedio;
- clases particulares / profesor a domicilio;
- Excel para empresas.

`Clases particulares / profesor a domicilio` must not be mixed with the classroom-course offer unless the service is actually available and the landing, ad and operational delivery match that promise.

## Decision matrix

| Evidence | Likely action |
|---|---|
| High spend, low conversion, irrelevant queries | negatives or tighter match before new landing |
| High spend, coherent intent, weak landing experience | dedicated landing test |
| High CPC, high impression share, low rank loss | competition is not the main cause |
| Rising CPC plus higher overlap/position-above competitor rates | competition hypothesis gains support |
| Good Google conversions but fewer CRM leads | tracking/CRM reconciliation before media changes |
| Distinct B2B intent | separate campaign, landing and measurement from B2C |

## Required outputs before activation decisions

- corrected search-term report;
- corrected landing-page report;
- 7/30/90-day API comparison;
- 7/30/90-day Auction Insights private export;
- aggregated CRM comparison without PII;
- proposed negative keywords;
- retain/pause/isolate keyword matrix;
- landing-page experiment recommendation with one primary persona and one hypothesis.

## Security

Do not commit:

- raw Google Ads exports;
- Auction Insights competitor CSVs;
- customer IDs;
- tokens, OAuth files or YAML;
- CRM exports or PII.

Only sanitized, aggregated findings may return to GitHub.
