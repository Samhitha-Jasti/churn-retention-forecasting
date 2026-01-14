# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.18.1
#   kernelspec:
#     display_name: churn_env (3.11.0)
#     language: python
#     name: python3
# ---

# %%
import pandas as pd
data=pd.read_csv(r'C:\Users\asjas\OneDrive\Documents\Docker projects\churn-retention-forecasting\data\raw\customer_churn_dataset-training-master.csv')
data

# %%
data.dropna(how='all', inplace=True)
data

# %%
print(data.duplicated().sum())

# %%
data.drop('CustomerID', axis=1, inplace=True)

# %% [markdown]
# Feature encoding (creating new columns) - skipping for now

# %% [markdown]
# One-hot encoding all the categorical columns

# %% [markdown]
# test

# %%
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# 1. Define categorical columns
categorical_cols = ['Gender', 'Subscription Type', 'Contract Length']

# 2. Fit encoder on these columns
encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')

one_hot_encoded = encoder.fit_transform(data[categorical_cols])

# 3. Turn encoded array into DataFrame
one_hot_df = pd.DataFrame(
    one_hot_encoded,
    columns=encoder.get_feature_names_out(categorical_cols),
    index=data.index   # keep same index so concat is safe
)

# 4. Drop original categorical columns and concat encoded ones
data_encoded = pd.concat(
    [data.drop(categorical_cols, axis=1), one_hot_df],
    axis=1
)
data_encoded

# %%
# Select only numerical columns (excluding the target 'Churn' if it's there)
numerical_cols = ['Age', 'Tenure', 'Usage Frequency', 'Support Calls', 
                  'Payment Delay', 'Total Spend', 'Last Interaction']

# Calculate skewness
skew_values = data[numerical_cols].skew().sort_values(ascending=False)

print("Skewness Coefficients:")
print(skew_values)

# %% [markdown]
# How to Interpret the Numbers:
#
# -0.5 to 0.5: Symmetric (Normal enough). Action: No transformation needed. MinMax Scaling is fine.
#
# -1 to -0.5 OR 0.5 to 1: Moderately Skewed. Action: Consider Log Transform, but often robust enough to ignore.
#
# < -1 OR > 1: Highly Skewed. Action: Must Fix (Log Transform or Box-Cox).

# %%
import seaborn as sns
sns.boxplot(x=data['Support Calls'])

# %% [markdown]
# All the columns do not appear to be skewed so ignoring any transformations for now 

# %%
from sklearn.preprocessing import MinMaxScaler
one_hot_cols = [col for col in data_encoded.columns if col not in numerical_cols and col != 'Churn']

# Target column
target_col = 'Churn'
scaler = MinMaxScaler()

# Scale and convert back to DataFrame to preserve column names
data_encoded[numerical_cols] = scaler.fit_transform(data_encoded[numerical_cols])
final_data = data_encoded.copy()
final_data

# %%
print("✓ Final Data Shape:", final_data.shape)
print("\nColumn Names:")
print(final_data.columns.tolist())

print("\nData Types:")
print(final_data.dtypes)

print("\nFirst 5 rows:")
print(final_data.head())

print("\nNumerical columns (should be 0-1):")
print(final_data[numerical_cols].describe())

# %%
final_data.to_csv(r'C:\Users\asjas\OneDrive\Documents\Docker projects\churn-retention-forecasting\data\processed\final_data_processed.csv', index=False)

print("✓ Saved to: data/processed/final_data_processed.csv")
