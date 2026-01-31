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
├── Cleaner/
│   ├── cleaner.py              # Base cleaner interface
│   ├── cleaner_static.py       # Stateless cleaning utilities
│   └── cleanerFactory.py       # Cleaner factory
│
├── Encoder/
│   ├── encoder.py              # Base encoder interface
│   └── encoderFactory.py       # Encoder factory
│
├── Loader/
│   ├── csv_loader.py           # CSV loader implementation
│   └── loaderFactory.py        # Loader factory
│
├── Scaler/
│   ├── scaler.py               # Base scaler interface
│   └── scalerFactory.py        # Scaler factory
│
├── pipeline.py                 # Pipeline orchestration
├── test.py                     # Local tests / experiments
```
Each component respects the following principles:

No hidden decisions

No dataset-specific logic

Behavior is defined only by configuration

🔄 Processing Flow
```text
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
```

⚙️ Configuration Example
```text
config = {
    "loader": {
        "path": "data/raw.csv",
        "separator": ",",
        "encoding": "utf-8"
    },
    "cleaner": {
        "type": "mean",
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
```

🧪 Example Usage
```text
from pipeline import Pipeline

pipeline = Pipeline(config)
df_processed = pipeline.run()
```
