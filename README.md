# CSV Preprocessing Engine

A modular, config-driven preprocessing engine for CSV datasets, designed for reproducible and scalable machine learning pipelines.

---

## 🚀 Overview

This project provides a **lightweight preprocessing framework** for tabular data stored in CSV files.  
Instead of writing ad-hoc pandas scripts, you define a **configuration-driven pipeline** that transforms raw CSV data into **ML-ready datasets**.

The engine follows clear responsibilities and explicit transformation steps, inspired by production-grade ML pipelines.

---

## ✨ Key Features

- 📄 CSV in → CSV out (no API or frontend required)
- ⚙️ Fully **config-driven** preprocessing
- 🧩 Modular architecture (Loader, Cleaner, Encoder, Scaler)
- 🔁 Reproducible transformations (`fit` / `transform`)
- 🧪 Easy to test and extend
- 🧠 Designed for ML and data science workflows

---

## 🧱 Architecture

The engine is composed of independent modules, each with a **single responsibility**:

```text
engine/
├── loaders.py     # Load CSV files (encoding, separator, path)
├── cleaners.py    # Handle missing or invalid data
├── encoders.py    # Encode categorical features
├── scalers.py     # Scale numerical features
├── pipeline.py    # Orchestrates the preprocessing flow
```
Each component respects the following principles:

No hidden decisions

No dataset-specific logic

Behavior is defined only by configuration

🔄 Processing Flow
CSV
 ↓
Loader      → reads raw data
 ↓
Cleaner     → handles missing values
 ↓
Encoder     → encodes categorical columns
 ↓
Scaler      → scales numerical features
 ↓
Processed CSV (ML-ready)


⚙️ Configuration Example
config = {
    "loader": {
        "path": "data/raw.csv",
        "separator": ",",
        "encoding": "utf-8"
    },
    "cleaner": {
        "strategy": "fill",
        "method": "mean",
        "columns": ["age", "salary"]
    },
    "encoder": {
        "type": "onehot",
        "columns": ["city", "gender"]
    },
    "scaler": {
        "type": "standard",
        "columns": ["age", "salary"]
    }
}


🧪 Example Usage
from pipeline import Pipeline

pipeline = Pipeline(config)
df_processed = pipeline.run()
