# Churn & Retention Forecasting Project

A machine learning project to predict customer churn and identify retention strategies using Amazon reviews dataset.

## Business Problem

**Objective**: An e‑commerce marketplace like Amazon wants to reduce customer churn and increase repeat purchases in categories such as Electronics and Beauty.

**Users**: 
- Active shoppers (recent reviews/purchases)
- At‑risk shoppers (activity dropping over time)
- High‑value shoppers (many purchases, high spend / high ratings)

**KPIs**: Precision@K, Recall@K, MAP, CTR uplift, Retention rate

**Problem statement**: Given a user’s past interactions (ratings, review text, categories, recency/frequency), predict their churn risk and recommend products or offers that maximize the chance they stay active.

### Prerequisites
- Docker Desktop installed
- VS Code installed
- Git installed

### Setup

1. **Clone repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/churn-retention-forecasting.git
   cd churn-retention-forecasting
   ```

2. **Reopen in Dev Container (VS Code)**
   - Install "Dev Containers" extension.
   - Ctrl+Shift+P → "Reopen in Container"
   - Wait for container to build (~5-10 minutes first time)

3. **Start Jupyter**
   ```bash
   make notebook
   ```

4. **Open notebooks**
   - http://localhost:8888 (Jupyter)
   - Start with `notebooks/01_eda.ipynb`

## 📁 Project Structure

```
churn-retention-forecasting/
├── .devcontainer/          # VS Code Docker config
├── src/
│   ├── data/               # Data loading & preprocessing
│   ├── features/           # Feature engineering
│   ├── models/             # Model implementations
│   ├── evaluation/         # Metrics & SHAP
│   ├── app/                # Streamlit UI
│   └── utils/              # Helper functions
├── notebooks/              # Jupyter notebooks for exploration
├── data/                   # Raw, processed, splits
├── models/                 # Trained model files
├── tests/                  # Unit tests
├── Makefile                # Common commands
├── docker-compose.yml      # Multi-container setup
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

## 🔧 Available Commands

```bash
make help              # Show all commands
make notebook          # Start Jupyter Lab
make streamlit         # Start Streamlit app
make test              # Run unit tests
make clean             # Clean cache files
```

## 👨‍💻 Author

Anjani Samhitha Jasti

## 📝 License

MIT License - feel free to use and modify
