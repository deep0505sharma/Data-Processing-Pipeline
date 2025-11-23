## Description

A simple modular ETL (Extract → Transform → Normalize → Outliers → Encode → Load) pipeline built with Python.

---

## 📁 Project Structure
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

## Installation-Guide

```bash
git clone https://github.com/deep0505sharma/Data-Processing-Pipeline.git
```
**Open VS Code terminal**
```bash
cd Data-Processing-Pipeline
#Install Dependancies
pip3 install numpy
pip3 install pandas
pip3 install scikit-learn
pip3 install tomllib
pip3 install click
pip3 install pathlib
pip3 install tqdm
#Install this project in editable model
pip3 install -e .
```
Run pipeline.ipynb file to get the processed file or feel free to use terminal to run commands built using cli
### Code Snippet
<img width="1229" height="636" alt="Image" src="https://github.com/user-attachments/assets/545b21ee-6e03-40e3-8874-9371b93aec0d" />

### CLI-Commands Use-case

-----------
| **Use Case**                                            | **Command**                                                                       |
| ------------------------------------------------------- | ----------------------------------------------------------------------------------|
| **Run full pipeline using settings.toml**               | `datapipeline run-all --config config/settings.toml`                              |
| **Run full pipeline without config**                    | `datapipeline run-all data/raw/input.csv data/processedoutput.csv`                |
| **Run only selected steps**                             | `datapipeline run --config config/settings.toml`                                  |
| **Override missing-method default in settings.toml**    | `datapipeline run --config config/settings.toml --missing-method mode`            |
| **Override steps in settings.toml**                     | `datapipeline run --config config/settings.toml --steps extract --steps trasnform`|
| **Override fill-value in settings.toml**                | `datapipeline run --config config/settings.toml --missing-method constant --fill-value 3`|
| **Override outliers-method in settings.toml**           | `datapipeline run --config config/settings.toml --outlier-method zscore --threshold 2.5`|
| **Override encode-method default in settings.toml**     | `datapipeline run --config config/settings.toml --encode-method target --target-column price`|
-----------

## 🤝 Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AddFeature`)
3. Commit your Changes (`git commit -m 'Add some new Feature'`)
4. Push to the Branch (`git push origin feature/AddFeature`)
5. Open a Pull Request

### Development Guidelines:
- Follow existing code style and conventions
- Write clear, concise commit messages
- Add comments for complex logic
- Test your changes thoroughly before submitting
- Update documentation if needed

## 🐛 Bug/Issue Reporting
Feel free to [open an issue](https://github.com/deep0505sharma/Data-Processing-Pipeline/issues) on GitHub if you find bugs.

When reporting bugs, please include:
- Steps to reproduce the issue
- Expected vs actual behavior
- Screenshots if applicable
- Browser/device information
- error messages

## ⭐ Feature Request
- Feel free to [open an issue](https://github.com/deep0505sharma/Data-Processing-Pipeline/issues) on GitHub to request new features or enhancements.  
- Connect with me on [LinkedIn](https://www.linkedin.com/in/deepak-sharma-40a8781b8/) to discuss ideas and suggestions. 

### Potential Future Enhancements:
- [ ] Adding new options or methodologies for null imputation
- [ ] Support for large datasets using pyspark
- [ ] Adding option to save output in other file formats (e.g., .parquet)
