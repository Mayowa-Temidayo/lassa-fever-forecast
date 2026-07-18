# Lassa Fever Forecast — Model Registry

> This document tracks every forecasting model implemented in the project.

---

# Purpose

The Model Registry provides a centralized record of:

- Implemented models
- Training status
- Hyperparameters
- Evaluation metrics
- Best-performing models
- Saved model artifacts

---

# Model Inventory

| Model | Type | Status | Notes |
|--------|------|--------|-------|
| Prophet | Time Series | Planned | Facebook Prophet baseline |
| SARIMAX | Statistical | Planned | Seasonal ARIMA with exogenous variables |
| LightGBM | Gradient Boosting | Planned | Tabular forecasting |
| XGBoost | Gradient Boosting | Planned | Tabular forecasting |
| CatBoost | Gradient Boosting | Planned | Handles categorical variables |
| LSTM | Deep Learning | Future | Sequence modeling |
| Temporal Fusion Transformer | Deep Learning | Future | Advanced forecasting |

---

# Evaluation Metrics

The following metrics will be recorded for each trained model:

- MAE
- RMSE
- MAPE
- SMAPE
- R² (where appropriate)

---

# Experiment Log

| Date | Model | Dataset | Result |
|------|-------|---------|--------|
| *(To be completed during model development)* | | | |

---

# Production Model

This section will identify the model selected for deployment.

| Model | Version | Date | Status |
|--------|---------|------|--------|
| *(Pending)* | | | |