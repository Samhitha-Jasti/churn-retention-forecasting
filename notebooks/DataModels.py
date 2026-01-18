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

# %%
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

data_path = r'C:\Users\asjas\OneDrive\Documents\Docker projects\churn-retention-forecasting\data\processed\final_data_processed.csv'
train_data=pd.read_csv(data_path)
print(f"Training data shape: {train_data.shape}")

X = train_data.drop('Churn', axis=1)
y = train_data['Churn']

X_train, X_val, y_train, y_val = train_test_split(
    X, y,
    test_size=0.3,          
    random_state=42,
    stratify=y            
)

print(f"Train set: {X_train.shape[0]} rows")
print(f"Validation set: {X_val.shape[0]} rows")


model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train, y_train)

y_pred_val = model.predict(X_val)
val_accuracy = accuracy_score(y_val, y_pred_val)

print(f"\nValidation Accuracy: {val_accuracy:.4f}")
print(f"Validation Precision: {precision_score(y_val, y_pred_val):.4f}")
print(f"Validation Recall: {recall_score(y_val, y_pred_val):.4f}")
