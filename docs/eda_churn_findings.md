# Customer Churn – EDA Findings

_Date generated: 2025-12-30_

## 1. Dataset Overview
- **Source:** Training dataset for churn prediction.
- **Target column:** `Churn` (1 = churned, 0 = retained).
- **Dimensions:** 440,832 rows, 12 columns.
- **Action Taken:** Dropped 1 row containing 12 missing values.

## 2. Key Univariate Insights
- **Outliers:** No extreme outliers found; all numerical values are within reasonable ranges.
- **Skewness:**
  - `Age`: Skewed towards younger customers (20–50 range). Big drop-off after age 50.
  - `Support Calls`: Skewed right. Most people call 0–3 times. A small group calls 8–10 times (high risk).
  - `Total Spend`: Skewed right. Lower-medium spenders are the majority.

## 3. Key Bivariate Insights (Relationships)
- **Primary Churn Drivers (Strong Signals):**
  - **Support Calls:** Strong positive correlation. More calls = High likelihood of Churn.
  - **Contract Length:** Strong correlation. Monthly contracts appear to be the biggest churn driver.
  - **Payment Delay:** Moderate correlation. Delays > 15 days increase churn risk significantly.
  - **Age:** Older customers (>45) seem slightly more prone to churn than younger ones.
  
- **Secondary Insights:**
  - **Gender:** No significant relationship with Churn. (White in heatmap).
  - **Total Spend:** High spenders churn *less* (Negative correlation).
  - **Last Interaction:** Moderate signal. Customers silent for >20 days are at risk.

- **Multicollinearity (Features related to each other):**
  - `Contract Length` has a slight relationship with `Payment Delay` (Monthly users might delay more).

## 4. Modeling Strategy (Next Steps)
- **Feature Selection:**
  - **Keep:** Contract Length, Support Calls, Payment Delay, Last Interaction, Age, Total Spend.
  - **Drop:** `CustomerID` (Unique ID, no predictive value). `Gender` (Low correlation).
  
- **Preprocessing Plan:**
  - **Categorical:** One-Hot Encode `Contract Length` and `Subscription Type`.
  - **Numerical:** Apply Log Transformation to `Total Spend` and `Support Calls` to fix skewness.
  - **Scaling:** Normalize `Age` and `Total Spend` to 0–1 range.

## 5. Link to Full HTML Profile
- Auto‑generated profile: `reports/churn_training_profile.html`
