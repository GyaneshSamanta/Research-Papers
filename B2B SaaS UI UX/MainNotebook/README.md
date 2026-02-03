# 📘 B2B SaaS UI/UX Research: Comprehensive Notebook Documentation

This repository contains a suite of three Jupyter Notebooks (`Rq1.ipynb`, `Rq2.ipynb`, `Rq3.ipynb`) designed to rigorously investigate the impact of User Experience (UX) on B2B software adoption, retention, and revenue.

This documentation is intended to serve as a complete guide for researchers and stakeholders, explaining **exactly** what data was used, **how** it was analyzed, and **why** specific statistical methods were chosen.

---

## 📂 Data Inventory & Locations

The analysis relies on specific datasets located in the `working datasets` and `Datasets` directories.

| Dataset Filename                     | Location               | Description                                                                                                                    | Used In      |
| :----------------------------------- | :--------------------- | :----------------------------------------------------------------------------------------------------------------------------- | :----------- |
| **`UI UX Dataset.csv`**              | `../Datasets/`         | Primary survey data containing **SUS (System Usability Scale)** scores, user roles, and product categories (B2B vs. Consumer). | **RQ1**      |
| **`b2b-saas-usage-retention.csv`**   | `../working datasets/` | Supplemental log data used to verify industry categorization and analyze basic retention patterns.                             | **RQ1**      |
| **`Dataset_UI_Manual_Group.csv`**    | `../working datasets/` | Experimental time-tracking data for users performing tasks with **manual interventions** (high friction).                      | **RQ2**      |
| **`Dataset_UI_No_Manual_Group.csv`** | `../working datasets/` | Experimental time-tracking data for users performing the same tasks with **automated workflows** (low friction).               | **RQ2**      |
| **`feature_adoption_medium.csv`**    | `../working datasets/` | Feature-level data linking "Friction Scores" (complexity) to "Adoption Rates" and user retention status.                       | **RQ2, RQ3** |
| **`SaaS Sales.csv`**                 | `../working datasets/` | Financial performance data segmented by Region (AMER, EMEA, APJ), used to link UX behaviors to revenue.                        | **RQ3**      |

---

## 🔬 Detailed Notebook Walkthroughs

### 1️⃣ RQ1: The "Experience Gap"

**File:** `Rq1.ipynb`
**Core Question:** _Is the "Consumerization of IT" real? Do B2B applications authentically lag behind Consumer apps in usability?_

#### **Methodology & Approach**

1.  **Data Segregation**: The `UI UX Dataset.csv` was split into two cohorts: "Enterprise/B2B" and "Consumer/B2C" based on the `Category` column.
2.  **Normality Testing**: Before comparing means, we checked if the UX scores followed a normal (Bell curve) distribution. They did _not_, which dictated our choice of statistical tests.
3.  **Statistical Comparison**: We compared the central tendency of UX scores between the two groups.
4.  **Classification Model**: We trained a Logistic Regression model to see if a computer could distinguish a B2B app from a Consumer app _solely_ by looking at its usability score.

#### **Statistical Tests Explained**

- **Mann-Whitney U Test**:
  - _What it is_: A non-parametric test that compares two independent groups to see if they come from the same population.
  - _Why we used it_: We could not use a standard T-Test because our UX data was **not normally distributed** (it was skewed). The Mann-Whitney test acts on _ranks_ rather than raw values, making it robust against outliers and non-normal data.
  - _Result_: `p < 0.001` (Extremely significant difference).

#### **Key Inferences & Insights**

- **The 22.5 Point Gap**: Consumer apps averaged an SUS score of ~85 (World Class), while B2B apps averaged ~62.5 (Below Average). This confirms a massive, quantifiable quality gap.
- **Predictability**: The "UX Gap" is so distinct that our Logistic Regression model could predict the software category with **89% accuracy (ROC-AUC)** just by knowing the UX score.
- **Conclusion**: B2B software is not just "styled differently"; it is objectively harder to use, falling into the "Promoter" vs. "Detractor" divide.

---

### 2️⃣ RQ2: The Mechanics of Friction

**File:** `Rq2.ipynb`
**Core Question:** _How strictly does "Usability Friction" (manual steps, clicks, time) dictate whether a user will adopt a feature?_

#### **Methodology & Approach**

1.  **A/B Testing**: We analyzed two groups of users performing identical objectives.
    - **Group A (Manual)**: Had to perform manual data entry/steps.
    - **Group B (No-Manual)**: Used a streamlined/automated version.
2.  **Time-on-Task Analysis**: We measured the exact time (in seconds) it took for users to complete the workflow.
3.  **Adoption Correlation**: We mapped the "Friction Score" of various features against their actual utilization rates in the product.

#### **Statistical Tests Explained**

- **Independent Samples T-Test**:
  - _What it is_: Compares the means of two independent groups to determine if there is statistical evidence that the associated population means are significantly different.
  - _Why we used it_: To prove that the difference in task completion time between the "Manual" and "No Manual" groups was not due to random chance.
- **Linear Regression**:
  - _What it is_: Models the relationship between two variables by fitting a linear equation.
  - _Why we used it_: To quantify the "tax" of friction—specifically, to calculate exactly how much adoption drops for every unit increase in friction/time.

#### **Key Inferences & Insights**

- **The 40% Friction Tax**: Users in the "Manual" group took **~40% longer** to complete tasks.
- **Direct Negative Correlation**: There is a strong linear relationship ($R^2$ value) showing that as Time-on-Task increases, Adoption Rate decreases.
- **The "Usage Wall"**: Features with friction scores above a certain threshold saw adoption drop to near zero. Users do not "power through" bad UX; they abandon the feature entirely.

---

### 3️⃣ RQ3: The Business Payoff

**File:** `Rq3.ipynb`
**Core Question:** _Does better UX actually make money? Can we link these "soft" metrics to Churn and Revenue?_

#### **Methodology & Approach**

1.  **Cohort Analysis**: We split the user base into "Adopters" (high engagement with core features) and "Non-Adopters."
2.  **Survival Analysis**: We tracked these two groups over a 50-day period to see how long they remained active customers.
3.  **Revenue Mapping**: We bridged the gap between User IDs and Regional Sales data (AMER, EMEA, APJ) to see if regions with better UX scores generated more revenue.

#### **Statistical Tests Explained**

- **Kaplan-Meier Estimator**:
  - _What it is_: A statistic used to estimate the "survival function" from lifetime data. It shows the probability of a customer "surviving" (not churning) over time.
  - _Why we used it_: It handles "censored data" (customers who are still alive at the end of the observation period) correctly, which allows for an accurate view of retention curves.
- **Cox Proportional Hazards Model**:
  - _What it is_: A regression model that investigates the association between the survival time of subjects and one or more predictor variables.
  - _Why we used it_: To get a **Hazard Ratio (HR)**. This tells us the _magnitude_ of the benefit.
  - _Result_: HR = 0.77. This means being an "Adopter" reduces the _instantaneous risk of churn_ by **23%**.

#### **Key Inferences & Insights**

- **UX is a Retention Shield**: Adopters had significantly flatter survival curves (higher retention) than Non-Adopters. A 23% reduction in churn risk is financially massive for a SaaS business.
- **Regional Revenue Link**: We found that regions (like EMEA) with higher aggregate Feature Adoption scores also posted the highest Total Sales ($1M+).
- **The Value Chain**: Confirmed the causal chain: **Better UX → Lower Effort → Higher Adoption → Lower Churn → Higher Lifetime Value (CLV).**

---

## 📚 Glossary of Terms & Abbreviations

- **SUS (System Usability Scale)**: A standardized 10-question survey used since 1986 to assess the usability of a system.
  - _Scores 0-50_: F (Unacceptable)
  - _Scores 51-70_: D/C (Marginal)
  - _Scores 71-85_: B/A (Good to Excellent)
  - _Scores >85_: A+ (World Class - e.g., iPhone, Google Search)
- **TTV (Time to Value)**: The latency between a user signing up and achieving their first "Aha!" moment or successful outcome.
- **HR (Hazard Ratio)**: In survival analysis, the ratio of the hazard rates corresponding to the conditions described by two levels of an explanatory variable. An HR of 0.77 means the treatment group is 23% less likely to experience the event (churn) at any given time.
- **p-value**: A measure of the probability that an observed difference could have occurred just by random chance. A p-value < 0.05 is the standard threshold for "statistically significant."
- **KDE (Kernel Density Estimation)**: Only used in RQ1. Think of it as a smooth, continuous histogram. It allows us to visualize the "shape" of the data distribution (e.g., seeing two distinct "humps" for B2B vs. Consumer scores).
- **ROC-AUC**: A performance measurement for classification problems. A score of 1.0 represents a perfect model; 0.5 represents a random guess. Our score of 0.89 indicates high predictive power.
