# CONSUMPTION ACK — Marketing Performance Skill Refresh V01

## Estado

```text
DATE=2026-09-13
CONSUMER=misaeln-pc1/marketing-performance-capacita
AI_OS_BASELINE=V4.2 ACTIVA_VALIDADA
ACK_TYPE=INITIAL_BASELINE_BUNDLE
ACK_COUNT=13
PER_USE_LOG=NO
SEMVER_CHANGE_REQUESTED=NO
PARALLEL_LOCAL_RADAR=NO
```

Este bundle registra la primera decisión material de consumo para los bindings del refresh. No es un log de ejecuciones y no promueve ninguna skill a `approved/reusable`.

## ACK-01 — Google Ads campaign audit

```yaml
skill_or_capability: google-ads-campaign-audit-capacita
aios_version: 0.1.0
consumer_repo: misaeln-pc1/marketing-performance-capacita
decision: MIX
consumption_profile: MIX
local_status: in_use_local
evidence_level: OBSERVED
scope_used: [campaign-read, keywords, search-terms, landings, conversions, recommendations]
scope_not_used: [campaign-writes, new-oauth, final-attribution-without-downstream]
local_delta_summary: local negative-intent policy + validated Google Ads READ fast path + local campaign contracts
conditions_where_it_works: [read evidence is available, commercial objective is explicit]
known_limits: [tracking/CRM gaps can keep conclusions provisional, Campaign Leadership V01 not yet validated]
reusable_feedback_found: true
evidence: [SKILLS_USED.md, Google Ads diagnosis baseline, negative keywords intent policy]
```

## ACK-02 — Meta Ads campaign audit

```yaml
skill_or_capability: meta-ads-campaign-audit-capacita
aios_version: 0.1.0
consumer_repo: misaeln-pc1/marketing-performance-capacita
decision: MIX
consumption_profile: MIX
local_status: in_use_local
evidence_level: OBSERVED
scope_used: [campaign-adset-ad analysis, creative, audience, placements, landing/downstream coherence]
scope_not_used: [ads-writes, lead-pii, quality inference from CTR/CPC alone]
local_delta_summary: account routing + asset standards + candidate Campaign Leadership contract
conditions_where_it_works: [read sources available, account routing resolved]
known_limits: [downstream evidence can be incomplete, V3.2/Campaign Leadership remains candidate]
reusable_feedback_found: true
evidence: [SKILLS_USED.md, META_ADS_ACCOUNT_ROUTING.md, Marketing issue #91]
```

## ACK-03 — Paid Ads performance bridge

```yaml
skill_or_capability: paid-ads-performance-bridge-capacita
aios_version: 0.1.0
consumer_repo: misaeln-pc1/marketing-performance-capacita
decision: MIX
consumption_profile: MIX
local_status: in_use_local
evidence_level: OBSERVED
scope_used: [ads-web-crm-sale layer separation, normalized metrics, attribution gaps]
scope_not_used: [always-live unified pipeline, final ROAS/CPA without verified downstream]
local_delta_summary: connected READ sources + GTM/RevOps ownership + local campaign contracts
conditions_where_it_works: [source/period definitions are explicit]
known_limits: [full attribution depends on authorized downstream reconciliation]
reusable_feedback_found: true
evidence: [SKILLS_USED.md, MARKETING_PROACTIVE_OPPORTUNITY_SCAN_V01.md]
```

## ACK-04 — Page visibility orchestrator

```yaml
skill_or_capability: marketing-page-visibility-review-capacita
aios_version: 0.1.0
consumer_repo: misaeln-pc1/marketing-performance-capacita
decision: ADOPTAR
consumption_profile: PARTIAL
local_status: in_use_local
evidence_level: OBSERVED
scope_used: [local visibility protocol orchestration, proportional modules, P0/P1/P2, do-not-change, handoff]
scope_not_used: [run-all-modules, production publishing, Edge/Cloudflare changes]
local_delta_summary: local MARKETING_PAGE_VISIBILITY_PROTOCOL_V01 remains authoritative for page contract
conditions_where_it_works: [page objective and indexability decision are known]
known_limits: [few real cases; not enough to claim VALIDATED]
reusable_feedback_found: false
evidence: [SKILLS_USED.md, docs/seo-ai/README.md, TASK_STATUS.md]
```

## ACK-05 — SEO demand/SERP research

```yaml
skill_or_capability: seo-demand-serp-research-capacita
aios_version: 0.1.0
consumer_repo: misaeln-pc1/marketing-performance-capacita
decision: MIX
consumption_profile: PARTIAL
local_status: evaluating
evidence_level: OBSERVED
scope_used: [demand, search-intent, SERP, cannibalization, real-source-first]
scope_not_used: [CPC-as-demand, fanout-pages-by-keyword]
local_delta_summary: combine with Ads, GTM and local visibility protocol
conditions_where_it_works: [GSC/SERP or equivalent evidence exists]
known_limits: [source availability varies by case]
reusable_feedback_found: false
evidence: [SKILLS_USED.md, SEO_GEO_TECHNICAL_RESEARCH_BASELINE_V01.md]
```

## ACK-06 — AEO / AI readability

```yaml
skill_or_capability: aeo-ai-readability-capacita
aios_version: 0.1.0
consumer_repo: misaeln-pc1/marketing-performance-capacita
decision: ADAPTAR_MINIMO
consumption_profile: PARTIAL
local_status: evaluating
evidence_level: OBSERVED
scope_used: [answer-first clarity, recoverable content, fact consistency, render/markdown support]
scope_not_used: [mandatory-llms-txt, mandatory-faq-schema, artificial-chunking, guaranteed-uplift]
local_delta_summary: preserve CRO and authorized commercial facts
conditions_where_it_works: [render/content and page objective are available]
known_limits: [insufficient evidence for VALIDATED]
reusable_feedback_found: false
evidence: [SKILLS_USED.md, docs/seo-ai/README.md, TASK_STATUS.md]
```

## ACK-07 — GEO / AI Search benchmark

```yaml
skill_or_capability: geo-ai-search-benchmark-capacita
aios_version: 0.1.0
consumer_repo: misaeln-pc1/marketing-performance-capacita
decision: ADAPTAR_MINIMO
consumption_profile: PARTIAL
local_status: evaluating
evidence_level: OBSERVED
scope_used: [reproducible benchmark pattern, observation-vs-interpretation, Promptfoo synthetic benchmark]
scope_not_used: [synthetic-as-real-ranking, single-run-causality]
local_delta_summary: technical runner is external to Marketing repo
conditions_where_it_works: [benchmark question set and surface semantics are explicit]
known_limits: [REAL_AI_SEARCH_RANKING_NOT_VALIDATED]
reusable_feedback_found: false
evidence: [SKILLS_USED.md, docs/seo-ai/README.md, TASK_STATUS.md]
```

## ACK-08 — AI crawler/retrieval access audit

```yaml
skill_or_capability: ai-crawler-retrieval-access-audit-capacita
aios_version: 0.1.0
consumer_repo: misaeln-pc1/marketing-performance-capacita
decision: MIX
consumption_profile: PARTIAL
local_status: evaluating
evidence_level: OBSERVED
scope_used: [crawl, sitemap/robots/access evidence, search-retrieval-vs-training separation]
scope_not_used: [production-robots-waf-cloudflare changes, bypass]
local_delta_summary: SiteOne/advertools provide runtime; Edge owns implementation
conditions_where_it_works: [public URL and safe read evidence available]
known_limits: [technical crawl does not prove generative visibility]
reusable_feedback_found: false
evidence: [SKILLS_USED.md, docs/seo-ai/README.md, TASK_STATUS.md]
```

## ACK-09 — Entity/authority corroboration

```yaml
skill_or_capability: entity-authority-corroboration-capacita
aios_version: 0.1.0
consumer_repo: misaeln-pc1/marketing-performance-capacita
decision: MIX
consumption_profile: PARTIAL
local_status: evaluating
evidence_level: PLANNED
scope_used: [selected-for-material-local-or-institutional-pages]
scope_not_used: [full-two-case-validation, synthetic-authority, fake-reviews-or-backlinks]
local_delta_summary: invoke only when entity/GBP/schema/corroboration can change the decision
conditions_where_it_works: [authorized institutional facts and relevant page context exist]
known_limits: [PENDING_FIRST_MATERIAL_LOCAL_VALIDATION]
reusable_feedback_found: false
evidence: [SKILLS_USED.md, docs/seo-ai/README.md]
```

## ACK-10 — Search Intelligence toolchain capability

```yaml
skill_or_capability: capacita-search-intelligence-toolchain
aios_version: AI_OS_PR_56_REGISTRY_HANDOFF
consumer_repo: misaeln-pc1/marketing-performance-capacita
decision: ADOPTAR
consumption_profile: PARTIAL
local_status: accepted_local
evidence_level: VALIDATED
scope_used: [SiteOne, advertools, Promptfoo-synthetic]
scope_not_used: [SerpBear-runtime, paid-provider, credentials, local-duplicate-install]
local_delta_summary: runtime remains in dedicated technical repo
conditions_where_it_works: [read-only public-page analysis, sanitized outputs]
known_limits: [SERPBEAR_PENDING_PROVIDER_SECURITY_REVIEW, synthetic-benchmark-not-real-ai-ranking]
reusable_feedback_found: false
evidence: [toolchain merge fb5c4a9df255953fa6bad59a8866ddf610474d1b, AI OS PR #56, docs/seo-ai/README.md]
```

## ACK-11 — Marketing event taxonomy pattern

```yaml
skill_or_capability: marketing-event-taxonomy-attribution-capacita
aios_version: 0.1.0
consumer_repo: misaeln-pc1/marketing-performance-capacita
decision: EXTRAER_PATRON
consumption_profile: PATTERN_ONLY
local_status: evaluating
evidence_level: PLANNED
scope_used: [stable-event-ids, signal-vs-identity, pain-signal/bp-hypothesis/cta/page-variant design]
scope_not_used: [full-game-taxonomy, real-GA4-Meta-Zoho-activation]
local_delta_summary: Marketing owns page/campaign taxonomy; technical implementation remains with owner repo
conditions_where_it_works: [event purpose and privacy boundary are explicit]
known_limits: [real tracking not validated by this binding]
reusable_feedback_found: false
evidence: [SKILLS_USED.md, MARKETING_PROACTIVE_OPPORTUNITY_SCAN_V01.md]
```

## ACK-12 — Buyer persona signal pattern

```yaml
skill_or_capability: buyer-persona-signal-map-capacita
aios_version: 0.1.0
consumer_repo: misaeln-pc1/marketing-performance-capacita
decision: EXTRAER_PATRON
consumption_profile: PATTERN_ONLY
local_status: evaluating
evidence_level: PLANNED
scope_used: [behavior-as-signal-not-identity, buyer-persona-as-hypothesis]
scope_not_used: [game-specific-logic, definitive-person-labeling]
local_delta_summary: GTM/RevOps retains canonical buyer persona; Marketing applies only evidence-based hypothesis
conditions_where_it_works: [signal origin is explicit and non-sensitive]
known_limits: [no sensitive-attribute inference, click-is-not-persona-proof]
reusable_feedback_found: false
evidence: [SKILLS_USED.md, MARKETING_PROACTIVE_OPPORTUNITY_SCAN_V01.md]
```

## ACK-13 — Generic Meta audit evaluated/not used

```yaml
skill_or_capability: meta-ads-campaign-audit
aios_version: 0.1.0
consumer_repo: misaeln-pc1/marketing-performance-capacita
decision: RECHAZAR_LOCAL
consumption_profile: EVALUATED_NOT_USED
local_status: rejected_local
evidence_level: OBSERVED
scope_used: []
scope_not_used: [direct-consumption]
local_delta_summary: meta-ads-campaign-audit-capacita@0.1.0 covers the same core with broader campaign/adset/ad, creative, audience, placement, UTM and CRM detail
conditions_where_it_works: []
known_limits: [AI OS must decide whether another consumer justifies both library entries]
reusable_feedback_found: true
evidence: [SKILLS_USED.md, documentary comparison 2026-09-13]
```

## Reusable feedback routing

Two material reusable deltas were found:

1. `Campaign Leadership`: compare the local observed gap against the current Paid Ads skill family and existing external candidates in AI OS #40. Do not create/version automatically.
2. `meta-ads-campaign-audit` duplication: AI OS should compare/deprecate/justify both entries to reduce impact-check noise.

These deltas will be routed **once** to AI OS #40 after this consumer PR exists. No separate local radar or duplicate AI OS issue is required.
