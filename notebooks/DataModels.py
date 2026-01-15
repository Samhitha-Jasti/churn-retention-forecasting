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
print("Hello, this is DataModels notebook")

# %%
import pandas as pd
import os

# Load the processed data
data_path = r'C:\Users\asjas\OneDrive\Documents\Docker projects\churn-retention-forecasting\data\processed\final_data_processed.csv'

final_data = pd.read_csv(data_path)
final_data
