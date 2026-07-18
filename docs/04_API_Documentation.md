# Lassa Fever Forecast — API Documentation

> This document defines the public API of the Lassa Fever Forecast system.

---

# Purpose

The API exposes forecasting capabilities to external applications such as:

- Web Dashboard
- Mobile Applications
- Public Health Systems
- Third-party Integrations

---

# Planned Endpoints

## Health Check

GET `/health`

Returns the service status.

Example Response

```json
{
  "status": "healthy"
}
```

---

## Forecast

POST `/forecast`

Generate a disease forecast.

Example Request

```json
{
  "state": "Ondo",
  "forecast_horizon": 12
}
```

Example Response

```json
{
  "state": "Ondo",
  "forecast_horizon": 12,
  "predictions": []
}
```

---

## Model Information

GET `/models`

Returns the currently deployed forecasting model.

---

## Available Locations

GET `/locations`

Returns all supported states or regions.

---

## Metadata

GET `/metadata`

Returns dataset and model metadata.

---

# Authentication

Initial development:

- No authentication

Production:

- API Key or OAuth2

---

# Versioning

Current Version

v1

Future versions will follow semantic API versioning.