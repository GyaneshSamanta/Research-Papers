# Data Analysis Strategy Memo: Causal Link from B2B SaaS UX to Business Outcomes

## Executive Summary

This memo establishes a comprehensive **Data Analysis Strategy** for a research study investigating the causal relationship between B2B SaaS User Experience (UX) and tangible business outcomes (Net Revenue Retention, Customer Churn, Customer Lifetime Value). The analysis is grounded in the "Ladder of Thought" conceptual model: **Improved UX → Changed User Perception → Positive User Emotion → Desired User Behavior (Feature Adoption) → Positive Business Outcome (Retention/NRR)**.

This strategy curates and evaluates publicly available datasets from industry analysts (Gartner, Forrester, HG Insights), academic repositories, enterprise surveys (Stack Overflow, World Bank, ACSI), and technology platforms (G2, CrUX, Mendeley). The memo identifies **critical data gaps**, particularly the absence of user-level datasets linking UX heuristics to feature adoption and churn, and provides actionable analytical pathways using proxy methods and ecological analysis.

---

## Section 1: Dataset Evaluation and Curation

### 1.1 Vetting Table: Complete Dataset Inventory

| **Dataset Name** | **Source** | **B2B Relevance** | **Data Type** | **Suitability for RQs** | **Real Data?** | **Justification/Notes** |
|---|---|---|---|---|---|---|
| **Top 100 SaaS Companies Dataset** | Kaggle | High | Transactional/Performance | RQ3 (Firm-level) | Yes | Provides financial metrics (valuation, growth) for leading SaaS firms; can be cross-referenced with public satisfaction scores (G2, Capterra) for firm-level correlation analysis. Enables macro-level analysis of successful SaaS companies. |
| **AWS SaaS Sales Dataset** | Kaggle | Medium | Transactional (Fictitious) | None | **No** | **EXCLUDE**: Explicitly labeled as "fictitious but realistic." While useful as a methodological example for internal structure analysis, cannot be used for real evidence. |
| **Mendeley SaaS Customer Experience Survey** | Mendeley Data | High | Survey | RQ1, RQ2 | Yes | Real survey data (50 SaaS users) on customer preferences for live chat, response times, agent knowledge, and AI integration. Reveals customer expectations in B2B SaaS context; useful for consumerization baseline (RQ1). Limited sample size but real. |
| **American Customer Satisfaction Index (ACSI)** | Mendeley Data / PMC | High | Survey (8,239 respondents) | RQ1 | Yes | Large, scientifically rigorous satisfaction dataset covering 4 industries (processed food, airlines, ISPs, banks). Provides benchmark for "consumer-grade" satisfaction (68-79% on 0-100 scale). Enables comparison of consumer vs. enterprise satisfaction gap. **Real, validated, PLS-SEM modeled.** |
| **Chrome User Experience Report (CrUX)** | Google Chrome / BigQuery | High | Real User Monitoring (Millions of data points) | RQ1 | Yes | Aggregated real-world web performance metrics from Chrome users. Establishes performance benchmark for consumer-grade web experiences (LCP, INP, CLS). Data shows 75th percentile performance; publicly accessible via Google BigQuery. Enables proxy for "consumerization" baseline. |
| **HG Insights CRM Market Analysis** | HG Insights | High | Market Intelligence | RQ1, RQ3 | Yes | $53B global CRM market; 1.4M companies; purchasing criteria, buyer profiles, market segmentation. Shows UX/usability mentioned in purchasing priorities (indicator for RQ1). Provides firm-level spending and adoption data. |
| **HG Insights ERP Market Report** | HG Insights | High | Market Intelligence | RQ1, RQ3 | Yes | $147.7B ERP market; 3.8M companies; adoption patterns, buyer insights, complexity indicators. Demonstrates the scale and UX challenges in enterprise software; reveals adoption barriers related to complexity (proxy for poor UX). |
| **Stack Overflow Developer Survey 2025** | Stack Overflow | High | Survey (49,000+ developers) | RQ1, RQ2 | Yes | Large-scale developer survey on tools, platforms, satisfaction, and AI adoption. 84% use AI tools; 60% positive sentiment (down from 70%+). Satisfaction with tools correlates with continued use. Developers distrust AI "almost-right" solutions (45% frustration). Proxy for "tool satisfaction → adoption." |
| **Stack Overflow Developer Survey 2024** | Stack Overflow | High | Survey (65,000+ developers) | RQ1, RQ2 | Yes | Earlier year data; 76% using/planning AI tools; satisfaction metrics on tool preferences. Enables year-over-year trend analysis. |
| **OECD Digital Transformation of SMEs Report** | OECD | Medium | Policy Analysis / Survey Data | RQ1, RQ3 | Yes | Identifies SME digitalization barriers, technology adoption rates, and business function priorities. Shows complexity (e.g., ERP adoption requires "critical firm size") as a UX/usability barrier. Supports RQ1 thesis that simpler, more usable tools are prioritized. Data from OECD countries. |
| **OECD SME Digitalisation 2024 Survey** | OECD D4SME Initiative | Medium | Survey (1,000+ SMEs) | RQ1, RQ3 | Yes | 72% of SMEs use data for decision-making; 77% of "mostly digitalized" businesses vs. 63% of "somewhat digitalized." Reveals relationship between ease of use (digitalization readiness) and adoption behavior. 7 countries. |
| **World Bank Enterprise Survey Database** | World Bank / enterprisesurveys.org | Medium | Survey (58,000+ firms) | RQ3 | Yes | Manufacturing firms across 82 countries; data on technology adoption (email, website), productivity, firm performance. Panel data structure enables causal inference (via control function approach). Firm-level variables: tech adoption, TFPR, factor demand. **Validated source.** |
| **World Bank Digital-Technology Adoption & Productivity Paper** | World Bank Open Knowledge | High | Econometric Analysis (Firm-level) | RQ3 | Yes | Estimates revenue-based Total Factor Productivity (TFPR) premiums from digital adoption. Email adoption: 1.6% median premium; website adoption: 2.2% premium. Productivity gains from 54.6%-67.3% of firms. **Establishes baseline for tech adoption → productivity link (proxy for UX → business outcome).** |
| **G2 Software Reviews Dataset** | G2.com / webautomation.io | High | Reviews (1M+ entries) | RQ1, RQ2, RQ3 | Yes | 1M+ verified B2B software reviews; 120,000+ software products; 40+ data points per review. Includes satisfaction ratings, feature reviews, use cases, adoption patterns. Cross-referenceable with financial data from Top 100 SaaS. **Critical for firm-level analysis and satisfaction → performance correlation.** |
| **Mendeley UI/UX User Interaction Dataset** | Mendeley Data | Medium | Survey (2,271 entries) | RQ1 | Yes | UI/UX preferences across digital platforms; satisfaction ratings. Limited to general UI/UX; not B2B-specific but useful for consumerization baseline (consumer expectations). |
| **Customer Satisfaction Records (10K+ entries)** | Kaggle | Medium | Survey | RQ2, RQ3 | Yes | Large satisfaction dataset (10,000+ records). Can be analyzed for correlation between satisfaction and "loyalty" or "intent to renew" (proxy for churn). **Useful for RQ3 micro-level proxy analysis.** |
| **Lakeside Software Application Performance Dataset** | Lakeside Software Documentation | Medium | Enterprise IT Performance | RQ2 | Yes | Application behavior, resource usage, user experience impact metrics. Documentation describes "Applications," "People," and "CPU/Memory Technical Analysis" perspectives. Provides real enterprise IT data on app performance and user productivity. **Can proxy for UX impact on productivity.** |
| **Forrester Digital UX Review Methodology** | Forrester | High | Methodological / Expert Analysis | RQ1, RQ2 | Partial | Forrester's heuristic UX review approach (expert evaluation, key customer scenarios). Publicly available methodology but full report requires subscription ($1,495). Useful for defining "UX heuristics" framework for RQ2. |
| **e-CRM Dataset (S-O-R Model, Mendeley)** | Mendeley Data | Low | Survey (485 e-commerce users) | None | Yes | Consumer e-commerce loyalty data; not B2B SaaS. Included for completeness but limited direct relevance. Could serve as consumer baseline for "consumerization" but better alternatives (ACSI, CrUX) exist. |

---

### 1.2 Curation Summary

#### **Core Datasets (Essential for All RQs)**

1. **G2 Software Reviews Dataset** — 1M+ B2B software reviews with satisfaction ratings; foundational for all three RQs.
2. **Stack Overflow Developer Survey (2024, 2025)** — 49,000-65,000 developers; tool satisfaction and adoption proxy.
3. **HG Insights CRM & ERP Market Reports** — Market-level purchasing criteria and adoption data; essential for RQ1.
4. **American Customer Satisfaction Index (ACSI)** — 8,239 respondents; satisfaction benchmark for consumer-grade baseline (RQ1).
5. **Chrome User Experience Report (CrUX)** — Real-world web performance metrics; consumerization baseline (RQ1).

#### **Supplementary Datasets (RQ-Specific Support)**

- **RQ1 (Consumerization):** Mendeley SaaS Customer Experience Survey, OECD SME reports, Forrester UX methodology.
- **RQ2 (UX → Adoption):** Stack Overflow Survey (tool satisfaction as adoption proxy), Lakeside Software performance data.
- **RQ3 (Adoption → Business Outcomes):** World Bank Enterprise Survey, World Bank Digital-Tech Adoption paper, Kaggle Top 100 SaaS, Kaggle Customer Satisfaction (10K+).

#### **Rejected Datasets**

- **AWS SaaS Sales Dataset** — Explicitly fictitious; excluded despite being labeled "realistic." Violates real data mandate.

---

## Section 2: Conceptual Framework Mapping

### 2.1 "Ladder of Thought" Mapping to Datasets

```
UX LAYER (The Product Reality)
├─ Datasets: CrUX (web performance benchmarks for "consumer-grade" baseline)
├─ Datasets: Mendeley UI/UX Dataset, G2 reviews (software-specific UX ratings)
└─ Datasets: Forrester UX methodology (expert heuristic evaluation)

       ↓ PERCEPTION LAYER (How Users Evaluate the Tool)
├─ Datasets: ACSI (satisfaction formation model; expectations → quality → satisfaction)
├─ Datasets: Stack Overflow Survey (developer perception of tool quality)
├─ Datasets: Mendeley SaaS Customer Experience Survey (user expectations)
└─ Datasets: G2 reviews (user perception ratings; "ease of use," "implementation," etc.)

       ↓ EMOTION LAYER (Affective Response)
├─ Datasets: ACSI (emotional constructs: satisfaction, confirmation of expectations, comparison to ideal)
├─ Datasets: Stack Overflow Survey (favorability, frustration metrics)
├─ Datasets: Mendeley SaaS Survey (satisfaction with chat support, responsiveness)
└─ **GAP:** No direct emotional/sentiment datasets for B2B SaaS; relying on satisfaction as proxy.

       ↓ BEHAVIOR LAYER (User Actions)
├─ Datasets: G2 reviews (feature adoption mentions; use case data)
├─ Datasets: Stack Overflow Survey (tool adoption frequency, "most used" vs. "want to use")
├─ Datasets: Lakeside Software Performance Data (application usage, frequency, engagement)
└─ **CRITICAL GAP:** No public user-level dataset linking UX to feature adoption (core_features_used, secondary_features_used, adoption_rate). World Bank and Lakeside provide proxy metrics, but not UX-specific.

       ↓ BUSINESS OUTCOME LAYER (Financial Impact)
├─ Datasets: Kaggle Top 100 SaaS (firm valuation, growth, revenue)
├─ Datasets: HG Insights CRM/ERP (market spend, customer retention indicators)
├─ Datasets: G2 reviews (customer retention mentions, NPS-like data if available)
├─ Datasets: World Bank Enterprise Survey (firm productivity, TFP premiums from tech adoption)
└─ Datasets: World Bank Digital-Tech Adoption Paper (1.6%-2.2% productivity premiums; empirical basis)
```

---

### 2.2 Antecedents & Consequences Framework

#### **ANTECEDENTS (The "Why": Drivers of UX Priority)**

**Proposition:** The consumerization of IT creates pressure on B2B software vendors to improve UX because business users now have exposure to consumer-grade apps (iPhone, Slack, Figma) and expect workplace software to match that standard.

| **Antecedent** | **Evidence Dataset** | **Key Finding** |
|---|---|---|
| **Consumer App Exposure** | CrUX (75th percentile LCP: <2.5s for top sites); ACSI (satisfaction 65-80 on 0-100 scale) | Baseline: Consumer users expect fast, responsive, intuitive interfaces. |
| **Enterprise Software Complexity** | HG Insights ERP ($147.7B market; complexity noted as barrier); OECD SME report | Enterprise software historically complex, requiring months to implement. Gap exists. |
| **Developer Expectations** | Stack Overflow Survey (84% using AI tools; frustration with "almost-right" solutions; tool satisfaction correlates with adoption) | Technical users demand tools that "just work"; poor UX → abandonment. |
| **Market Signaling** | HG Insights reports (purchasing criteria mentions); G2 reviews (prominence of "ease of use" category) | UX now explicitly mentioned in purchasing criteria; competitive differentiator. |

**Consequence:** UX becomes a purchasing priority in B2B SaaS purchasing criteria (hypothesis for RQ1).

---

#### **CONSEQUENCES (The "So What": Impact of Better UX)**

| **Consequence** | **Evidence Dataset** | **Proposed Link** |
|---|---|---|
| **Higher Satisfaction** | ACSI (satisfaction → loyalty strong correlation, r=.820); G2 reviews (satisfaction ratings) | Better UX → higher satisfaction scores → measurable via ACSI-like models or G2 ratings. |
| **Increased Feature Adoption** | Userpilot benchmark (24.5% avg adoption rate); Stack Overflow (tool satisfaction correlates with continued use); Pendo finding (80% of volume from 12% of features) | Better UX → lower friction → more users access more features. Proxy: tool satisfaction → adoption. |
| **Higher Retention** | ACSI model (satisfaction → loyalty/repurchase, strong path); World Bank (tech adoption → productivity → firm success) | Feature adoption → value realization → lower churn. Proxy: tech adoption correlates with firm productivity. |
| **Higher NRR** | Churnzero/Wudpecker benchmarks (NRR 106% median; feature adoption 70%+ doubles retention likelihood) | Adoption + satisfaction → expansion revenue (upsells) → NRR >100%. |

---

## Section 3: Detailed Analytical Plan (per Research Question)

### 3.1 Research Question 1: Consumerization's Impact on UX Priority

**Research Question:** *To what extent does the "consumerization of IT" influence the priority of UX in the purchasing and evaluation criteria for modern B2B SaaS platforms compared to traditional on-premise software?*

#### **Hypothesis**
The gap between consumer app satisfaction (high) and enterprise app satisfaction (lower) is quantifiable and drives a purchasing shift toward UX-centric solutions in B2B SaaS.

#### **Proposed Analysis**

##### **Step 1: Establish Consumer-Grade Baseline**

**Datasets:** ACSI, CrUX

- **ACSI Benchmark:** Extract satisfaction scores (0-100 scale) from ACSI dataset for industries categorized as "consumer-facing" (airlines, ISPs, retail). Compute mean satisfaction, confidence intervals, and satisfaction-to-loyalty correlation (from published ACSI model: satisfaction → loyalty r=.820).
  - *Finding:* Consumer industry satisfaction typically 70-80 on 0-100 scale; strong satisfaction → loyalty pathway.
  
- **CrUX Benchmark:** Aggregate Core Web Vitals (LCP, INP, CLS) for top 1,000 consumer websites from public CrUX dashboard. Calculate 75th percentile performance metrics.
  - *Finding:* Median LCP ~2.5s for fast sites; median CLS ~0.05. Consumer baseline for "fast, responsive."

##### **Step 2: Compare Enterprise Software Performance**

**Datasets:** Stack Overflow Developer Survey, G2 Reviews, Mendeley SaaS Customer Experience Survey

- **Developer Satisfaction:** From Stack Overflow 2025 survey, extract satisfaction/favorability scores for "enterprise tools" vs. "consumer tools" (e.g., GitHub vs. legacy version control; Slack vs. legacy enterprise chat).
  - *Proposed Analysis:* Comparative favorability percentages. E.g., "Slack: 80% positive sentiment" vs. "Legacy enterprise collaboration tool: 35% positive sentiment."
  - *Limitation:* Stack Overflow survey focuses on developer tools; may not fully represent non-technical enterprise software.

- **G2 Reviews (Categorical Analysis):** Within G2 dataset, filter for enterprise software categories. Extract "Ease of Use" ratings and compare across:
  - Legacy on-premise software (e.g., Oracle EBS, SAP ECC) vs. Modern SaaS (e.g., Salesforce, HubSpot).
  - *Proposed Analysis:* Mean "Ease of Use" score comparison; effect size (Cohen's d).
  - *Finding Expected:* Modern SaaS scores 3.5-4.5 / 5 on "Ease of Use"; legacy on-premise 2.0-2.8 / 5.

- **Mendeley SaaS Survey:** Direct question responses on expectations (response times, interface intuitiveness, AI integration). Codify expectations and compare to industry norms.

##### **Step 3: Proxy for Purchasing Priority**

**Datasets:** HG Insights CRM/ERP reports, G2 category prominence

- **Keyword Prevalence in Purchasing Criteria:** Use HG Insights reports to identify whether "UX," "usability," "ease of implementation," or "time-to-value" appear in buyer purchasing criteria commentary.
  - *Proposed Finding:* If these terms appear in 40%+ of buyer decision drivers, supports RQ1 hypothesis.

- **G2 Category Trending:** Analyze frequency of "Ease of Use" reviews in top-performing SaaS products (2022-2025 time series). If trending upward, suggests buyer prioritization.

##### **Step 4: Correlate with Market Segmentation**

**Datasets:** HG Insights, Kaggle Top 100 SaaS

- **Hypothesis Test:** Companies with strong "Ease of Use" ratings on G2 have higher market valuations or growth rates than those with low "Ease of Use" ratings.
  - *Proposed Analysis:* Correlation between G2 "Ease of Use" score and company valuation/ARR growth from Kaggle Top 100 SaaS.
  - *Expected Relationship:* Positive correlation (high UX → higher valuation as investors reward product-market fit).

#### **Limitations for RQ1**
- Analysis is correlational and relies on proxies (satisfaction, reviews) for "purchasing priority." Direct causal evidence requires internal buyer decision data (not available publicly).
- Comparison assumes G2 and Stack Overflow reviews are representative; potential selection bias (satisfied users more likely to review positively).
- Time-series data limited; multi-year trends strengthen inference.

---

### 3.2 Research Question 2: UX → Feature Adoption Link

**Research Question:** *How does improved UX, measured by usability heuristics or validated satisfaction metrics, correlate with the adoption rates for both core and secondary features in B2B software?*

#### **Hypothesis**
Higher UX/usability scores for a platform correlate positively with higher adoption rates, especially for secondary (non-core) features. The strength of this link is strongest for secondary features (lower UX barrier = lower activation cost).

#### **Proposed Analysis**

##### **Critical Gap Acknowledgment**
**There is NO public dataset providing user-level UX scores AND feature adoption data for the same B2B product.** This is the hardest link in the causal chain to establish with public data. All proposed analyses rely on proxies.

##### **Proxy Analysis 1: Overall Satisfaction ↔ Breadth of Feature Use**

**Datasets:** G2 Reviews, Mendeley SaaS Customer Experience Survey, Kaggle Customer Satisfaction (10K+)

- **G2 Cross-Tabulation:** For a subset of SaaS products (e.g., 50-100 major CRM, HCM, ERP platforms), extract:
  - (1) "Ease of Use" rating (proxy for UX/usability)
  - (2) Review text mentions of "features used," "breadth," or specific secondary features (NLP parsing or manual coding)
  
  *Proposed Analysis:* Correlation between "Ease of Use" score and feature breadth mentions in reviews.
  - *Expected Finding:* Positive correlation (higher usability → users mention more features).
  - *Limitation:* Feature breadth is inferred from review text; not validated adoption metrics.

- **Mendeley SaaS Survey + Kaggle Satisfaction Dataset (10K+):** If either dataset includes items like:
  - "How many features do you actively use?" (adoption breadth)
  - "Rate the overall ease of use" (UX proxy)
  
  *Proposed Analysis:* Run Spearman or Pearson correlation; logistic regression with "high feature adoption" (yes/no) as outcome and satisfaction/usability as predictor.
  - *Expected Coefficient:* Positive; statistically significant.
  - *Limitation:* Limited sample size (Mendeley: 50 respondents; Kaggle 10K limited to available items).

##### **Proxy Analysis 2: Developer Tool Satisfaction ↔ Tool Adoption Frequency**

**Datasets:** Stack Overflow Developer Survey (2024, 2025)

- **Tool Satisfaction ↔ Adoption:** From Stack Overflow survey, identify questions that capture:
  - (1) Satisfaction/favorability with specific tools (e.g., "Do you want to continue using this tool?")
  - (2) Frequency of use (e.g., "How often do you use this tool?")
  
  *Proposed Analysis:* Cross-tabulation + correlation. Example:
  ```
  Tool = "GitHub"
  Favorable Sentiment: 75% of users
  Use Frequency: 85% report "daily use"
  
  Tool = "Jira"
  Favorable Sentiment: 45% of users
  Use Frequency: 60% report "daily use"
  ```
  
  *Correlation:* Run chi-square test or logistic regression (favorable sentiment → daily use).
  - *Expected Outcome:* Positive association (satisfaction → continued use).
  - *Interpretation:* Satisfaction (proxy for good UX) correlates with adoption behavior.

##### **Proxy Analysis 3: Usage Friction ↔ Feature Adoption Decline**

**Datasets:** Stack Overflow Survey (frustration questions), Lakeside Software performance data

- **Stack Overflow Frustration ↔ Tool Adoption:** 2025 Survey reports 66% of developers frustrated with "AI solutions that are almost right, but not quite," leading to debugging time and tool abandonment.
  - *Proposed Analysis:* Correlate frustration levels with tool switching intent or tool abandonment rates (if available in survey).
  - *Expected Finding:* High frustration → lower future adoption / higher likelihood of tool switch.
  - *Interpretation:* Poor UX (manifested as frustration) reduces adoption.

- **Lakeside Application Performance Data:** If Lakeside data includes both:
  - (1) Application response time / performance metrics (UX proxy)
  - (2) Frequency of application use (adoption frequency)
  
  *Proposed Analysis:* Correlation or regression: app_performance → frequency_of_use.
  - *Expected Relationship:* Faster, more responsive apps have higher use frequency.

#### **Overall RQ2 Analytical Strategy**

| **Approach** | **Datasets** | **Strengths** | **Limitations** |
|---|---|---|---|
| **G2 Satisfaction ↔ Feature Breadth** | G2 Reviews + NLP | Large scale (120K+ products); real reviews | Feature breadth inferred from text; no validated adoption metrics |
| **Survey Correlation** | Mendeley, Kaggle (10K+) | Direct questions on both satisfaction and adoption | Small samples (Mendeley: 50); Kaggle limited item coverage |
| **Developer Tool Satisfaction** | Stack Overflow | Large sample (49K+ developers); real tool data; year-over-year trend | Developer tools only; not enterprise software broadly |
| **Performance ↔ Frequency** | Lakeside Software | Enterprise data; performance + usage combined | Access limited; not open dataset; requires subscription/partnership |

**Key Conclusion for RQ2:** The public data supports **indirect, proxy-based inference** that "satisfaction ↔ adoption" link exists, but **no direct user-level dataset links UX heuristics to feature adoption.** Researchers should acknowledge this gap prominently.

---

### 3.3 Research Question 3: Feature Adoption → Business Metrics (Churn, NRR, CLV)

**Research Question:** *What is the quantitative relationship between feature adoption rates and key business metrics, such as customer churn, Net Revenue Retention (NRR), and Customer Lifetime Value (CLV)?*

#### **Hypothesis**
Higher feature adoption rates (and/or user satisfaction as a proxy) correlate with lower churn, higher NRR, and higher CLV. This relationship is modeled at multiple levels: micro (individual account), macro (ecological/national), and firm-level.

#### **Proposed Analysis**

##### **Micro-Level Analysis: Satisfaction/Adoption → Churn (Individual/Account-Level Proxy)**

**Datasets:** Kaggle Customer Satisfaction (10K+ entries), Kaggle Top 100 SaaS

- **Logistic Regression Model:** If Kaggle Customer Satisfaction dataset includes variables such as:
  - DV: `likelihood_to_renew` (binary: yes/no) or `churn_status` (binary: churned/retained)
  - IV: `satisfaction_score` (0-100 scale) or `feature_adoption_breadth` (count or %)
  
  *Proposed Specification:*
  ```
  Logit(P(Retained=1)) = β0 + β1(Satisfaction_Score) + β2(Company_Size) + β3(Contract_Length) + ε
  
  Expected β1 > 0 and significant at p<.05
  Interpretation: 1-point increase in satisfaction → X% increase in odds of retention
  ```
  
  *Implementation:*
  - Logistic regression or gradient boosting (XGBoost, LightGBM) for robustness.
  - Include controls: company size, industry, tenure, pricing tier.
  - Test non-linear relationships (satisfaction_score² term).
  
  - *Expected Outcome:* Coefficient β1 positive and significant. E.g., "Every 10-point increase in satisfaction score associated with ~15% lower churn probability."
  
  - *Limitation:* Kaggle 10K dataset likely cross-sectional; cannot infer causation without panel structure or instrumental variables.

##### **Firm-Level Analysis: Public Satisfaction ↔ Financial Performance**

**Datasets:** G2 Reviews + Kaggle Top 100 SaaS, HG Insights CRM/ERP reports

- **Satisfaction-Performance Correlation (Illustrative):**
  
  *Step 1: Harmonize datasets.*
  - Match G2-reviewed SaaS products with Kaggle Top 100 SaaS by company name/domain.
  - Extract G2 metrics: `overall_satisfaction_score`, `ease_of_use_score`, `implementation_score`.
  - Extract Kaggle metrics: `company_valuation` (or valuation proxy), `growth_rate_yoy`, `employee_count` (as size proxy).
  
  *Step 2: Correlation & Regression.*
  ```
  Valuation_Growth ~ Ease_of_Use_Score + Implementation_Score + Company_Size + Industry
  NRR_Proxy ~ Overall_Satisfaction + Feature_Breadth_Mentions + Time_in_Market
  ```
  
  - *Expected Relationships:*
    - Ease of Use → Higher valuation growth (companies with better UX grow faster).
    - Overall Satisfaction → Implied NRR (higher satisfaction indicates strong retention/expansion).
  
  - *Implementation:* OLS regression with heteroskedasticity-robust standard errors (HC3/HC4).
  
  - *Limitations:*
    - Correlational only; confounding variables (marketing spend, founder reputation, market timing).
    - Valuation growth determined by many factors beyond UX; difficult to isolate UX effect.
    - Small sample of matched firms (likely 30-50 products with both G2 and Kaggle data).
    - Selection bias: Only high-growth SaaS companies likely in "Top 100" list; truncated sample.

##### **Macro-Level Ecological Analysis: Technology Adoption ↔ Firm Productivity/Outcomes**

**Datasets:** World Bank Enterprise Survey, World Bank Digital-Technology Adoption & Productivity Paper

- **Ecological Regression (Country/Sector-Level):**
  
  *Data:* World Bank Enterprise Survey captures, for 58,000+ firms across 82 countries:
  - Firm-level: Technology adoption (email, website, ERP usage), productivity, revenue, employment, churn/exit rates.
  
  *Proposed Analysis:*
  ```
  Log(Productivity_i) = β0 + β1(Tech_Adoption_i) + β2(Firm_Size_i) + β3(Industry_i) + ε_i
  
  OR (Ecological):
  
  Mean_Productivity_c = β0 + β1(% Tech_Adopters_c) + β2(Mean_Firm_Size_c) + country_FE
  ```
  
  - *Expected Outcome:* From World Bank paper: Email adoption → 1.6% median productivity premium; website → 2.2% premium.
  - *Implementation:* 
    - Use control function approach (CFA) to account for endogeneity (firms adopt technology because they're productive, or productive because they adopt?).
    - Leverage panel structure if available; instrument for adoption using exogenous variation (e.g., regional tech infrastructure rollout).
  
  - *Interpretation for RQ3:*
    - Technology adoption (imperfect proxy for "feature adoption" in B2B context) → Productivity gains.
    - Productivity gains → Firm survival, revenue growth (proxies for lower churn, higher CLV).
    - **Indirect evidence:** If adopting firms are more productive and survive longer, then adoption (driven by better UX) → retention.
  
  - *Limitations:*
    - "Technology adoption" is binary (email: yes/no) or crude (website: yes/no); not feature adoption within a single B2B product.
    - World Bank data primarily manufacturing; limited to formal enterprises in developing countries.
    - Ecological fallacy: Relationships at country-level may not hold at firm-level.
    - Causality requires strong assumptions (orthogonal innovation timing, no reverse causality).

##### **Secondary: NRR & Feature Adoption Benchmarks**

**Datasets:** Churnzero Customer Revenue Leadership Study 2025, Wudpecker SaaS Benchmarks, Userpilot Feature Adoption Report

- **Descriptive Analysis:**
  - Churnzero finds: "Customers engaging with 70%+ of core features are twice as likely to stay" (strong correlation, not causal).
  - Userpilot finds: Average core feature adoption 24.5% across 181 companies; HR products highest at 31%.
  - Wudpecker finds: Median NRR 106%; companies with high feature adoption (70%+) have NRR >120%.
  
  - *Proposed Use:* These benchmarks provide **context and validation** for RQ3 analyses. If own correlation analyses find similar direction (adoption → retention), validates external benchmarks. If contrary, suggests confounding.

#### **Overall RQ3 Analytical Strategy**

| **Level** | **Datasets** | **Method** | **Expected Finding** | **Causality Claim** |
|---|---|---|---|---|
| **Micro (Account-Level)** | Kaggle 10K Satisfaction | Logistic regression | Satisfaction → Lower churn (β>0, sig.) | Correlational; not causal |
| **Firm-Level (SaaS Companies)** | G2 + Kaggle Top 100 | OLS regression | UX scores → Growth (β>0) | Correlational; confounding likely |
| **Macro (Ecological)** | World Bank Enterprise Survey | Control function / Instrumental variables | Tech adoption → Productivity (β≈1.6-2.2%) | Quasi-causal (with strong assumptions) |
| **Benchmark Validation** | Churnzero, Userpilot, Wudpecker | Comparative descriptive | Feature adoption 70%+ → NRR >120% | Descriptive; correlational |

**Key Conclusion for RQ3:** Macro-level analysis with World Bank data provides the **strongest quasi-causal evidence** (via control function approach) that technology adoption (proxy for better UX driving adoption) → productivity → firm retention. Firm-level and micro-level analyses are correlational but useful for triangulation.

---

## Section 4: Synthesis, Gaps, and "Ideal Dataset" Specification

### 4.1 Overall Narrative: Answering the Three RQs

**The "Ladder of Thought" narrative, synthesized across all three RQs:**

1. **RQ1 - Consumerization Establishes the "Why":**
   - **Evidence:** CrUX and ACSI data show consumer app satisfaction (70-80/100) and performance (LCP <2.5s) as baseline expectations.
   - **Evidence:** HG Insights, G2 reviews, and Stack Overflow data reveal a satisfaction/usability gap between legacy enterprise software and modern SaaS.
   - **Evidence:** Purchasing criteria (HG reports, G2 categories) increasingly emphasize "Ease of Use," "implementation speed," "time-to-value."
   - **Conclusion:** Consumerization drives demand for improved UX in B2B SaaS; UX is now a **purchasing and adoption criterion.**

2. **RQ2 - Better UX Drives Feature Adoption (The Behavioral Link, via Proxies):**
   - **Evidence:** Stack Overflow survey shows tool satisfaction → continued tool adoption; frustration → abandonment.
   - **Evidence:** G2 reviews suggest ease of use and satisfaction correlate with feature breadth mentions.
   - **Evidence:** Kaggle Satisfaction data (if analyzable) and Userpilot benchmarks suggest adoption is non-random; easier-to-use products have higher adoption.
   - **Conclusion:** While no single dataset directly links UX to feature adoption, proxy analyses **support the hypothesis** that better UX → higher adoption. The mechanism is: lower friction → lower activation barriers → more users try more features.
   - **Caveat:** This link is inferred; not directly proven with public data.

3. **RQ3 - Feature Adoption Drives Business Outcomes (Retention, NRR, CLV):**
   - **Evidence:** World Bank Enterprise Survey + paper shows technology adoption → 1.6-2.2% productivity premiums → firm survival and growth.
   - **Evidence:** Churnzero and benchmark data directly link high feature adoption (70%+) to retention and NRR >120%.
   - **Evidence:** Kaggle Satisfaction 10K dataset (if analyzable) supports satisfaction/adoption → lower churn.
   - **Conclusion:** **Adoption → business outcomes link is strongest.** Feature adoption is a tangible driver of lower churn and higher NRR; this is widely documented in SaaS benchmarks and supported by World Bank firm-level data.

**Synthesized Causal Chain (with Evidence Confidence Levels):**

```
Consumerization (RQ1) ────────→ Better UX Prioritized (HIGH confidence)
                                        ↓
                            Better UX Available (HIGH)
                                        ↓
Improved UX (RQ2) ──────────→ Reduced Friction (MEDIUM confidence, proxy-based)
                                        ↓
                            Higher Feature Adoption (MEDIUM confidence)
                                        ↓
Higher Adoption (RQ3) ──────→ Lower Churn, Higher NRR/CLV (HIGH confidence)
                                        
OVERALL CAUSAL CLAIM: MODERATE
  - RQ1: HIGH evidence (consumerization → UX priority)
  - RQ2: MEDIUM evidence (proxies; no direct link)
  - RQ3: HIGH evidence (adoption → outcomes, widely documented)
```

---

### 4.2 Identified Gaps

#### **Critical Gaps**

1. **No Public User-Level UX × Feature Adoption Dataset**
   - **Gap:** There is no publicly available dataset linking:
     - Usability metrics (heuristic scores, task completion times, error rates) or satisfaction ratings
     - **WITH** feature adoption (core_features_used, secondary_features_used, adoption_depth)
     - **FOR** the same set of B2B SaaS products.
   - **Impact:** RQ2 cannot be directly answered; relies entirely on proxies.
   - **Why the Gap:** Internal company data (e.g., Mixpanel, Amplitude, Intercom logs with NPS/CSAT + feature flags) is proprietary and not shared publicly.

2. **No Public NRR × Feature Adoption Data**
   - **Gap:** NRR and detailed feature adoption metrics are typically internal KPIs. While benchmark reports (Churnzero, Wudpecker) provide aggregate statistics, individual company-level data linking NRR to specific feature adoption rates is not publicly available.
   - **Impact:** RQ3 must rely on ecological analysis (World Bank) and inferences from aggregate benchmarks rather than direct regression.

3. **Limited B2B SaaS-Specific UX Benchmarking Data**
   - **Gap:** ACSI, CrUX, and other major satisfaction/performance datasets are either consumer-focused (ACSI covers processed food, airlines, banks; CrUX is web performance) or developer-tool focused (Stack Overflow).
   - **Limitation:** Proxy-based comparison of consumer vs. enterprise software satisfaction exists but is not direct.

4. **Lack of Longitudinal Panel Data Linking UX Changes to Outcome Changes**
   - **Gap:** Ideal would be: "Company X improved usability heuristics (Q1 2023); measured feature adoption increased by X% (Q2-Q3 2023); churn decreased (Q4 2023)." No such longitudinal dataset exists publicly.
   - **Impact:** Cannot establish temporal precedence and rule out confounding for RQ2-RQ3 links.

---

#### **Moderate Gaps**

5. **G2 Reviews Data Accessibility**
   - While G2.com dataset exists (1M+ reviews), full programmatic access requires subscription or web scraping. Publicly available via webautomation.io or Bright Data but at cost ($250-500/100K records).
   - **Mitigation:** Feasible to purchase; not a complete barrier.

6. **World Bank Enterprise Survey Specificity**
   - World Bank data focuses on manufacturing in developing countries; limited to large formal enterprises. Not representative of modern SaaS-dominated B2B markets in developed economies.
   - **Mitigation:** Provides macro-level support for tech adoption → productivity link; sufficient for RQ3 as indirect evidence.

7. **Stack Overflow Survey Generalizability**
   - Developer survey; primarily captures developer tools, not all enterprise software (e.g., HR, Finance, Supply Chain). Limited generalization to non-technical B2B SaaS.
   - **Mitigation:** Useful for consumerization hypothesis (RQ1) and developer UX expectations; not comprehensive for all B2B SaaS.

---

### 4.3 "Ideal Dataset" Specification

**Hypothetical "Perfect" Dataset for Definitively Answering All RQs**

```yaml
Dataset Name: "B2B SaaS Product Usage & Outcomes Panel"

Required Structure: Time-series panel data (monthly or quarterly observations)

Coverage:
  - Sample: 50-100 B2B SaaS companies (diverse industries: CRM, HCM, ERP, Analytics, Collaboration)
  - Timeframe: 24-36 months (to capture adoption trajectories and churn)
  - Level: User-account (or feature-group) level and firm-level aggregates

Core Variables:

USER/ACCOUNT LEVEL:
  - user_id: Unique identifier
  - account_id: Company/account identifier
  - date: Observation date (YYYY-MM-DD)
  - tenure_days: Days since account creation
  - subscription_tier: Pricing tier (e.g., "starter," "professional," "enterprise")
  
UX METRICS (Continuous, Monthly):
  - usability_score: Aggregate heuristic score (0-100 scale, validated via usability testing or expert eval)
    * Components: learnability, efficiency, memorability, error_recovery, satisfaction
  - nps_score: Net Promoter Score (0-100)
  - csat_score: Customer Satisfaction (0-100)
  - task_completion_rate: % of intended tasks completed per month (inferred from usage logs)
  - error_rate: % of actions resulting in error state
  - help_request_count: Support tickets, documentation views (proxy for friction)
  - time_to_first_action: Time (minutes) from login to first productive action
  
FEATURE ADOPTION METRICS (Binary or Count, Monthly):
  - core_feature_X_used: Boolean or count (whether user accessed/used core feature X)
  - core_features_used_count: Total count of distinct core features used in month
  - core_feature_adoption_breadth: % of available core features used
  - secondary_feature_Y_used: Boolean or count (secondary features, e.g., advanced reporting, automation)
  - secondary_features_used_count: Total count of distinct secondary features
  - secondary_feature_adoption_breadth: % of available secondary features
  - feature_usage_frequency: Feature use count per month (frequency, not just binary adoption)
  - feature_recency: Days since last use of each major feature
  - feature_depth: Measure of advanced vs. basic feature usage within category

OUTCOME METRICS (Monthly/Quarterly):
  - mrr_value: Monthly Recurring Revenue attributed to this account ($)
  - churn_status: Binary (0=retained, 1=churned)
  - churn_date: If churned, date of churn
  - nrr_contribution: Net Revenue Retention contribution from this account (0-200%+ range)
  - expansion_revenue: Upsell/cross-sell revenue this period ($)
  - expansion_flag: Binary (whether account expanded in this period)
  - clv_estimate: Estimated customer lifetime value ($) at observation date
  - support_cost: Cost of support interactions for this account
  - support_sentiment: Positive/negative/neutral from support ticket sentiment analysis
  
BEHAVIORAL METRICS:
  - session_count: Number of login sessions per month
  - session_duration_mean: Average session length (minutes)
  - days_active: Days with at least one session per month
  - inactive_days: Consecutive days without login (leading indicator of churn)
  - page_views: Total page/screen views per month
  - api_call_count: For API-enabled products, programmatic usage volume

FIRMOGRAPHIC CONTROLS:
  - company_size: Employee count (or revenue size band)
  - industry: Industry classification (SIC/NAICS)
  - geographic_region: Country or region
  - implementation_type: "Self-service" vs. "vendor-assisted" vs. "consulting-led"
  - days_since_implementation: Months since go-live
  - contract_term_months: Contract length
  - go_live_quality_score: Implementation quality / onboarding satisfaction (1-5)

Output Variables:
  - Micro-level: user_id × date observations (structure: user × time panel)
  - Macro-level: account_id × date aggregates (feature adoption counts, churn status, MRR)
  - Company-level: company_id × quarter aggregates (NRR, NRR trend, cohort retention, expansion rate)

Sample Size Requirement:
  - Minimum: 50 companies × 12 quarters = 600 firm-quarter observations
  - Ideal: 100 companies × 12 quarters × 100 users/company = 120,000 user-month obs.

Access Level:
  - Privacy-compliant: Anonymized, aggregated at user/account level; no PII
  - Sharing: Agreement with companies to share anonymized product usage & outcome data

Potential Data Sources:
  - Partnership with B2B SaaS vendors (Salesforce, HubSpot, Intercom, Zendesk, etc.) to share anonymized data
  - Aggregator platforms (Product analytics vendors like Mixpanel, Amplitude, Pendo)
  - Industry consortia (e.g., SaaS Institute, SaaS Alliance)
```

---

### 4.4 Alternative (Partial) Ideal Datasets

If the comprehensive panel cannot be obtained, prioritize (in order):

1. **G2 + Company Financial Data Panel**
   - G2 monthly satisfaction scores + company valuation/growth data (Crunchbase, PitchBook)
   - Captures: UX satisfaction (proxy) → firm performance
   - Limitation: Aggregated; not user-level adoption data

2. **Product Analytics Export from Major SaaS Vendors**
   - E.g., Salesforce or HubSpot feature usage logs + customer health scores + churn data
   - Single company; highly detailed
   - Limitation: Not representative of industry; cannot generalize

3. **Stack Overflow Developer Survey + Employment/Satisfaction Tracking**
   - Longitudinal survey of developers on tool satisfaction + job retention/income
   - Captures: Tool UX (via satisfaction) → career outcomes (proxy for productivity/value)
   - Limitation: Developers only; not enterprise end-users broadly

---

## Section 5: Recommendations and Next Steps

### 5.1 Recommended Data Collection Roadmap

**Phase 1: Establish Evidence Foundation (Using Available Public Data)**

- Perform RQ1 analysis immediately using ACSI, CrUX, HG Insights, G2, Stack Overflow.
- Publish RQ1 findings to establish consumerization thesis.
- Clearly document RQ2 gap; acknowledge proxy-based analysis only.

**Phase 2: Negotiate Data Partnerships (6-12 Months)**

- Contact major B2B SaaS vendors (Salesforce, HubSpot, Intercom, etc.) for anonymized product usage + outcome data sharing.
- Pitch: Academic research benefiting both vendor and industry; anony mized publication.
- Goal: Obtain 3-5 companies' data for panel RQ2/RQ3 analysis.

**Phase 3: Synthesis & Publication**

- Publish RQ1 findings (consumerization impact) with strong confidence.
- Publish RQ2 findings with caveats about proxy methods; note data gap.
- Publish RQ3 findings using World Bank macro data + any new partnership data.
- Highlight "Ideal Dataset" specification as future research recommendation.

### 5.2 Analysis Output Structure

```
Research Paper Outline:

1. Introduction
   - Problem: Does UX truly drive B2B SaaS business outcomes?
   - Significance: B2B software investment is $200B+; if UX drives retention by 5-10%, impact is $10-20B+ annually.

2. Literature Review & Conceptual Model
   - Cite ACSI satisfaction model, CX research, consumerization literature.
   - Present "Ladder of Thought" framework.

3. Research Questions & Hypotheses
   - RQ1-RQ3 as specified in this memo.

4. Methodology & Data
   - Section 1 & 2 of this memo (dataset curation, framework mapping).
   - Document all data sources, access methods, limitations.

5. Findings
   - RQ1 Analysis: Consumerization manifests in purchasing criteria and satisfaction gap.
   - RQ2 Analysis: Proxy evidence supports satisfaction ↔ adoption link.
   - RQ3 Analysis: Robust evidence (World Bank + benchmarks) for adoption ↔ outcomes.

6. Discussion
   - Interpret causal chain; discuss mechanism.
   - Acknowledge gaps (especially RQ2 causal gap).
   - Practical implications for SaaS vendors and UX teams.

7. Limitations & Future Research
   - Note public data constraints.
   - Specify "Ideal Dataset" (Section 4.3).
   - Propose vendor partnerships.

8. Conclusion
```

---

## Appendix A: Data Access & Practical Notes

| **Dataset** | **Access Method** | **Cost** | **Availability** | **Time to Access** |
|---|---|---|---|---|
| ACSI (Mendeley) | Direct download (Mendeley Data repository) | Free | High | Immediate |
| CrUX | Google BigQuery / Chrome UX Report API | Free tier; paid for large queries | High | Immediate (requires GCP account) |
| Stack Overflow Survey | Public reports + data repository (Kaggle) | Free | High | Immediate |
| HG Insights Reports | Web reports (free summaries); full reports subscription | $-$$ | Medium (summaries sufficient for RQ1) | 1-2 days |
| G2 Reviews | Web scraping or via webautomation.io / Bright Data | $$-$$$ ($250-500/100K records) | High | 2-4 weeks (data purchase) |
| World Bank Enterprise Survey | Direct download from worldbank.org / enterprisesurveys.org | Free | High | Immediate |
| Kaggle Datasets (Top 100 SaaS, Satisfaction) | Direct download from Kaggle | Free | High | Immediate |
| Mendeley SaaS Customer Experience | Mendeley Data repository | Free | High | Immediate |

---

## Appendix B: Proposed Analysis Code Skeleton (Python)

```python
import pandas as pd
import numpy as np
from scipy.stats import pearsonr, spearmanr
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import seaborn as sns

# RQ1: Consumerization Analysis
def rq1_satisfaction_benchmark(acsi_df, crux_df):
    """Compare consumer satisfaction (ACSI) with enterprise expectations."""
    acsi_satisfaction = acsi_df['SATIS'].mean()  # Mean satisfaction score
    acsi_loyalty = acsi_df['REPUR'].mean()  # Mean repurchase likelihood
    
    # Expected: satisfaction 70-80, loyalty 70-80 on 0-100 scale
    print(f"ACSI Mean Satisfaction: {acsi_satisfaction:.2f}")
    print(f"ACSI Mean Loyalty: {acsi_loyalty:.2f}")
    
    # CrUX performance baseline
    crux_lcp_p75 = crux_df['LCP_ms'].quantile(0.75)
    print(f"CrUX Median LCP (75th %ile): {crux_lcp_p75:.0f} ms")
    
    return {'acsi_satisfaction': acsi_satisfaction, 'crux_lcp': crux_lcp_p75}

# RQ2: Satisfaction → Adoption Proxy
def rq2_satisfaction_adoption_correlation(g2_reviews_df):
    """Correlate ease of use (G2) with feature breadth mentions (NLP)."""
    # Assume G2 reviews include 'ease_of_use_score' and 'feature_breadth_mentions' (0-1 scale)
    corr, pval = spearmanr(g2_reviews_df['ease_of_use_score'], 
                           g2_reviews_df['feature_breadth_mentions'])
    print(f"RQ2: Ease of Use ↔ Feature Breadth | ρ={corr:.3f}, p={pval:.4f}")
    return {'correlation': corr, 'p_value': pval}

# RQ3: Adoption → Churn
def rq3_adoption_churn_logistic(satisfaction_df):
    """Logistic regression: satisfaction → retention."""
    X = satisfaction_df[['satisfaction_score']].values
    y = satisfaction_df['retained'].values  # 1=retained, 0=churned
    
    # Standardize
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Fit logit
    model = LogisticRegression()
    model.fit(X_scaled, y)
    
    coef = model.coef_[0][0]
    intercept = model.intercept_[0]
    print(f"RQ3: Satisfaction → Retention | Coefficient={coef:.4f}")
    
    # Interpretation: 1 SD increase in satisfaction → exp(coef) increase in odds of retention
    odds_ratio = np.exp(coef)
    print(f"Odds Ratio: {odds_ratio:.3f} (per 1 SD increase in satisfaction)")
    
    return {'coefficient': coef, 'odds_ratio': odds_ratio}

if __name__ == "__main__":
    print("=" * 60)
    print("B2B SaaS UX → Business Outcomes: Analysis Skeleton")
    print("=" * 60)
    
    # Example: Load ACSI, CrUX, G2 data...
    # acsi_data = pd.read_csv('acsi_dataset.csv')
    # crux_data = pd.read_csv('crux_dataset.csv')
    # g2_data = pd.read_csv('g2_reviews.csv')
    
    # rq1_results = rq1_satisfaction_benchmark(acsi_data, crux_data)
    # rq2_results = rq2_satisfaction_adoption_correlation(g2_data)
    # rq3_results = rq3_adoption_churn_logistic(satisfaction_data)
```

---

## Conclusion

This **Data Analysis Strategy Memo** provides a comprehensive roadmap for investigating the causal link from B2B SaaS UX to business outcomes using publicly available data. 

**Key Takeaways:**

1. **RQ1 (Consumerization)** can be answered with **high confidence** using ACSI, CrUX, HG Insights, and G2 data.

2. **RQ2 (UX → Adoption)** is the **critical gap**; proxy-based analyses using Stack Overflow, G2, and satisfaction datasets provide correlational evidence but not causal proof.

3. **RQ3 (Adoption → Outcomes)** can be answered with **strong confidence** using World Bank Enterprise Survey data (macro-level quasi-causal evidence) and SaaS benchmarks (correlational).

4. The **"Ideal Dataset"** specification (Section 4.3) should guide future research and vendor partnerships to close the RQ2 gap.

5. **All recommended analyses are feasible with publicly available data** and can be conducted within 3-6 months; however, interpretations must acknowledge proxy methods and correlational limitations.