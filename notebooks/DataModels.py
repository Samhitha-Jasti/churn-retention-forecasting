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
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
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

# %%
models = {}
# Model 1: Logistic Regression
print("Training Logistic Regression...")
lr = LogisticRegression(max_iter=1000, random_state=42)
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_val)
models['Logistic Regression'] = {
    'model': lr,
    'accuracy': accuracy_score(y_val, y_pred_lr),
    'precision': precision_score(y_val, y_pred_lr),
    'recall': recall_score(y_val, y_pred_lr),
    'f1': f1_score(y_val, y_pred_lr)
}

# Model 2: Random Forest
print("Training Random Forest...")
rf = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_val)
models['Random Forest'] = {
    'model': rf,
    'accuracy': accuracy_score(y_val, y_pred_rf),
    'precision': precision_score(y_val, y_pred_rf),
    'recall': recall_score(y_val, y_pred_rf),
    'f1': f1_score(y_val, y_pred_rf)
}

# Model 3: XGBoost
print("Training XGBoost...")
xgb = XGBClassifier(random_state=42, n_jobs=-1)
xgb.fit(X_train, y_train)
y_pred_xgb = xgb.predict(X_val)
models['XGBoost'] = {
    'model': xgb,
    'accuracy': accuracy_score(y_val, y_pred_xgb),
    'precision': precision_score(y_val, y_pred_xgb),
    'recall': recall_score(y_val, y_pred_xgb),
    'f1': f1_score(y_val, y_pred_xgb)
}

# %%
#Compare all models
comparison = pd.DataFrame(models).T
print("\n" + "="*60)
print("MODEL COMPARISON (on Validation Set)")
print("="*60)
print(comparison)

# Find best model
best_model_name = comparison['f1'].idxmax()
best_model = models[best_model_name]['model']

print(f"\n✅ BEST MODEL: {best_model_name}")
print(f"   F1-Score: {models[best_model_name]['f1']:.4f}")
