# Description

A simple modular ETL (Extract → Transform → Normalize → Outliers → Encode → Load) pipeline built with Python.

---

# 📁 Project Structure
```markdown
DATA_PROCESSING_PIPELINE/
├── config/
│   └── settings.toml                 # Pipeline configuration settings
│
├── data/
│   ├── processed/                    # Processed datasets
│   └── raw/                          # Raw input datasets
│
├── src/
│   └── my_pipeline/                  # Main Python package
│       ├── __init__.py               # Package initializer
│       ├── cli.py                    # Command-line interface
│       ├── encode.py                 # Encoding & feature engineering logic
│       ├── extract.py                # Data extraction functions
│       ├── load.py                   # Data loading utilities
│       ├── logger.py                 # Custom logging utilities
│       ├── normalize.py              # Normalization logic
│       ├── outliers.py               # Outlier detection and handling
│       ├── profiler.py               # Profiling & performance measurement
│       ├── progress.py               # Progress bar / tracking utilities
│       ├── transform.py              # Data transformation pipeline
│
├── tests/
│   └── test_pipeline.py              # Unit tests for the pipeline
│
├── .gitignore                        # Git ignore rules
├── LICENSE                           # License information
├── Pipeline.ipynb                    # Jupyter notebook for pipeline demo
├── pyproject.toml                    # Project metadata & dependencies
└── README.md                         # Project documentation
```

## Data processing pipeline-> Flow Diagram
                  ┌──────────────────────┐
                  │      RAW DATA        │
                  │     data/raw/        │
                  └──────────┬───────────┘
                             │
                             ▼
                ┌──────────────────────────┐
                │       extract.py         │
                │  - Load raw datasets     │
                └───────────┬──────────────┘
                             │
                             ▼
                ┌──────────────────────────┐
                │      transform.py        │
                │  - Apply transformations |
                │   (Null Imputation/Drop) |
                └────────────┬─────────────┘
                             │
                             ▼
                ┌──────────────────────────┐
                │     normalize.py         │
                │  - Scale / standardize   │
                │    numeric features      │
                └────────────┬─────────────┘
                             │
                             ▼
                ┌──────────────────────────┐
                │      outliers.py         │
                │  - Detect & remove       │
                │    outliers              │
                └────────────┬─────────────┘
                             │
                             ▼
                ┌──────────────────────────┐
                │       encode.py          │
                │  - Encode categorical    │
                │    variables             │
                └────────────┬─────────────┘
                             │
                             ▼
                ┌──────────────────────────┐
                │     processed/           │
                │  (Final clean dataset)   │
                └──────────────────────────┘
