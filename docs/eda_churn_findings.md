# Customer Churn – EDA Findings

_Date generated: 2025-12-29 18:39_  

## 1. Dataset Overview
- Source: training dataset for churn prediction.
- Target column: `Churn` (1 = churned, 0 = retained).
- Number of rows / columns: 440832 rows, 12 columns.

## 2. Key Univariate Insights
- Age, Tenure, Usage Frequency, Total Spend, Payment Delay, Support Calls, Last Interaction show reasonable ranges and no extreme outliers.
- Some numerical features are skewed (e.g., Support Calls, Payment Delay, Total Spend), which may benefit from transformation.

## 3. Key Bivariate Insights (Churn vs Features)
- **Contract Type:** Monthly contract customers churn significantly more than annual or quarterly customers.
- **Age:** Customers aged above ~45 are more likely to churn than younger customers.
- **Support Calls:** Higher number of support calls is associated with higher churn, suggesting dissatisfaction.
- **Payment Delay:** Customers delaying payment (e.g., > 15 days) churn more, possibly due to perceived high cost or low value.
- **Last Interaction:** Customers with no interaction for ~20+ days have higher churn risk, indicating disengagement.
- **Total Spend:** Lower–medium spenders churn more than very high spenders (loyal / power users).

## 4. Data Quality Notes
- Missing values: (summarize how you handled them – dropped / imputed).
- Duplicates: (state if any were found and removed).
- Categorical encodings: Gender, Subscription Type, Contract Length, etc., are clean and ready for encoding.

## 5. Implications for Modeling
- Strong candidate predictors: Contract Length, Support Calls, Payment Delay, Last Interaction, Usage Frequency, Age.
- Consider:
  - Encoding categorical variables (one‑hot or target encoding).
  - Scaling or transforming skewed numeric features for linear models.
  - Handling class imbalance if churn rate is low (e.g., SMOTE or class weights).

## 6. Link to Full HTML Profile
- Auto‑generated profile: `reports/churn_training_profile.html`

