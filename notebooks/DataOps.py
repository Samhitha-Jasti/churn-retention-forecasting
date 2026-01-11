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
