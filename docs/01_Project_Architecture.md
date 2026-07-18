# Lassa Fever Forecast — Project Architecture

> This document describes the logical architecture of the Lassa Fever Forecast system.

---

# System Overview

```text
                External Data Sources
                         │
     ┌───────────────────┼───────────────────┐
     │                   │                   │
     ▼                   ▼                   ▼
 NCDC / Kaggle      NASA POWER          GRID3 Data
(Epidemiology)      (Weather)      (Population/Geography)
     │                   │                   │
     └───────────────────┴───────────────────┘
                         │
                         ▼
                Data Acquisition
                         │
                         ▼
                Data Validation
                         │
                         ▼
                 Data Versioning
                         │
                         ▼
              Feature Engineering
                         │
                         ▼
               Forecast Dataset
                         │
                         ▼
              Forecast Model Training
                         │
                         ▼
                Model Evaluation
                         │
                         ▼
                   Prediction API
                         │
                         ▼
               Dashboard / Monitoring
```

---

# Architecture Layers

## 1. Configuration

Responsible for:

- Project settings
- Environment variables
- Logging
- Paths
- Data source configuration

---

## 2. Data Layer

Responsible for:

- Dataset acquisition
- Dataset loading
- Dataset validation
- Metadata generation
- Data profiling

---

## 3. Feature Layer

Responsible for:

- Calendar features
- Lag features
- Rolling statistics
- Weather features
- Population features
- Geographic features

---

## 4. Model Layer

Responsible for:

- Prophet
- SARIMAX
- LightGBM
- XGBoost
- CatBoost

---

## 5. Evaluation Layer

Responsible for:

- Metrics
- Backtesting
- Model comparison

---

## 6. Deployment Layer

Responsible for:

- FastAPI
- Prediction endpoints
- Dashboard
- Monitoring

---

# Design Principles

- One responsibility per module.
- No duplicated logic.
- Prefer composition over inheritance.
- Every pipeline should be reproducible.
- Automation wherever practical.

---

# Architecture Status

**Status:** Frozen after Phase A.

Future development should add capabilities without changing the overall architecture.