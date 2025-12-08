# 📊 Data Documentation

## Dataset Overview

- **File**: `customer_churn_dataset-training-master.csv`
- **Records**: 440,832 customers
- **Columns**: 12 features + 1 target
- **Format**: CSV
- **Churn Rate**: 57% (imbalanced dataset)

## Column Definitions

### ID Column
- **CustomerID**: Unique identifier (drop for modeling)

### Numeric Features (8)
| Feature | Range | Meaning | Processing |
|---------|-------|---------|-----------|
| Age | 18-65 | Customer age | Drop missing, Scale |
| Tenure | 1-60 mo | Months with company | Create: IsNewCustomer |
| Usage Frequency | 1-30/mo | Times used per month | Create: UsageSegment |
| Support Calls | 0-10 | Help tickets filed | Create: IsHighSupport |
| Payment Delay | 0-30 days | Days late on payment | Create: IsLatePayment |
| Total Spend | $100-$1K | Total $ spent | Create: SpendPerMonth |
| Last Interaction | 1-30 days | Da
