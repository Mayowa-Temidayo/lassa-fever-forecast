# Lassa Fever Forecast — Data Dictionary

> This document describes every dataset and every variable used throughout the project.

---

# Purpose

The data dictionary serves as the authoritative reference for:

- Raw datasets
- Processed datasets
- Engineered features
- Prediction inputs
- Model outputs

Every new dataset or feature introduced into the project **must** be documented here.

---

# Dataset Inventory

| Dataset | Source | Status |
|----------|--------|--------|
| Lassa Epidemiology | NCDC / Kaggle | ✅ |
| Weather | NASA POWER | Planned |
| Population | GRID3 | Planned |
| Geography | GRID3 | Planned |

---

# Raw Dataset Columns

## Lassa Epidemiology

| Column | Type | Description | Status |
|---------|------|-------------|--------|
| *(To be completed after data profiling)* | | | |

---

# Weather Dataset

| Column | Type | Description | Status |
|---------|------|-------------|--------|
| *(To be completed after integration)* | | | |

---

# Population Dataset

| Column | Type | Description | Status |
|---------|------|-------------|--------|
| *(To be completed after integration)* | | | |

---

# Geography Dataset

| Column | Type | Description | Status |
|---------|------|-------------|--------|
| *(To be completed after integration)* | | | |

---

# Engineered Features

This section will document every feature created during Feature Engineering.

Example:

| Feature | Source | Description |
|----------|--------|-------------|
| cases_lag_1 | Epidemiology | Previous week's confirmed cases |
| rainfall_rolling_4w | Weather | Four-week rolling rainfall average |

---

# Prediction Target

This section will define the forecasting target once finalized.

Example:

| Target | Horizon |
|---------|----------|
| Confirmed Cases | 1–12 Weeks |