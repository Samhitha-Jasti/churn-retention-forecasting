import pandas as pd
data=pd.read_csv(r'C:\Users\asjas\OneDrive\Documents\Docker projects\churn-retention-forecasting\data\raw\customer_churn_dataset-training-master.csv')
data

data.shape

data.head()

data.isnull().sum()

data[data.isnull().any(axis=1)]

'''
Problems Detected:
- Customer ID starts from 2 instead of 1
- ID is in format 'x.0' instead of 'x'
'''