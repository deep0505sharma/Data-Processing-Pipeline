## 🎯 Description
A simple modular ETL (Extract → Transform → Normalize → Outliers → Encode → Load) pipeline built with Python.
Process the data (.csv format) to be used for model development purposes using a single user-command as well as using python notebook (pipeline.ipynb). users just need to define the configurations of various steps included in this data processing pipeline (e.g., null-values handling, outliers removal, normaliztion, etc.) in the settings.toml file present in config folder of this repo/directory. 

### 🚀 Features
1. ***Extract***: Read the datafile (input.csv) stored in location data/raw/ folder of this repo and store it in a dataframe.
2. ***Transform***: Performs the null-values handling in the dataset if present using one of the below-provided methods-
- [ ] Dropping the rows where null values are present ("Drop")
- [ ] Imputing the null values in the column with the mean of the corresponding column ("mean")
- [ ] Imputing the null values with mode of the corresponding column ("mode")
- [ ] Imputing the null values with median of the corresponding column ("median")
- [ ] Imputing the null values with a constant value ("constant"). User also need to provide the **fill value** they want to use to impute all the null values if using this method.
- [ ] Imputing the null values with backward fill and forward fill ('ffill') and ('bfill')
3. ***Normalization***: Rescale the data columns to ensure all featues lie in same/fixed range using one the three methods-
- [ ] ("Minmax") Rescales data to a fixed range, usually 0 to 1.
- [ ] ("Zscore") Standard Scaling, rescales data so it has mean = 0 and std deviation = 1.
- [ ] ("Robust") Median–IQR Scaling, scale data while ignoring outliers.
4. ***Outliers Removal***: Removes the outliers present in data using one of the two methods-
- [ ] ("iqr") This method is based on the spread of the middle 50% of the data, Works well for skewed (non-normal) data.
- [ ] ("Zscore") measures how far each value is from the mean in units of standard deviation.Based on the 68–95–99.7 rule of the normal distribution -> 99.7% of data lies within ±3 standard deviations. User also need to proovide the threshold they want to use if using this method in settings.toml config file.
5. ***Categorical Encoding***: converts non-numeric categorical data into numeric form so machine-learning models can understand it.
- [ ] ("One-hot") Creates a new binary column for each category (1 = present, 0 = not present).
- [ ] ("label") Assigns each category a unique integer value (A=0, B=1, C=2…).
- [ ] ("target") Replaces each category with the mean target value (e.g., average label for that category). User also need to specify the target column in this case in settings.toml file
6. ***Load***: Save your processeed file in the desired location.
7. ***Porfiling***: Process of analyzing a program to measure its performance, such as execution time and memory usage, to identify bottlenecks.
8. ***Logging***: records events, messages, and the program’s internal state during execution to help with debugging, monitoring, and auditing. 

## 🛠️ Dependancies
![GitHub tag](https://img.shields.io/github/tag/pandao/editor.md.svg)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![License](https://img.shields.io/github/license/pandao/editor.md.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Python Version](https://img.shields.io/badge/python-3.14.0-blue.svg)
![TOML](https://img.shields.io/badge/config-TOML-blue?logo=toml&logoColor=white)
![tqdm](https://img.shields.io/badge/tqdm-FFC107.svg?style=for-the-badge&logo=tqdm&logoColor=black)
![Click](https://img.shields.io/badge/Click-000000.svg?style=for-the-badge&logo=python&logoColor=white)

***Python***: High-level, interpreted programming language known for its simplicity, readability, and versatility across web development, data science, automation, and AI.

***TOML***: Minimal configuration file format that’s convenient to read and parse and primarily used for configuration, separating code from settings for flexibility.

***Visual Studio Code***: Primary code editor used for development.

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

## ⇢ Data processing pipeline-> Flow Diagram
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

## 📜 Installation-Guide

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
Upload your file in data/raw folder of this directory and mention the filepath in confid/settings.toml file and other desried configuration of the data processing and then run pipeline.ipynb file to get the processed file in the output path mention by user in config/settings.toml file or feel free to use terminal to run commands built using cli. 
### Code Snippet
<img width="1020" height="600" alt="Image" src="https://github.com/user-attachments/assets/545b21ee-6e03-40e3-8874-9371b93aec0d" />

Apart from this, I have also provided CLI support to the project and you can run the pipeline as per your desried method for processing using the single command and can also override the values set in settings.toml file. Some of the commands are provided below with their use-cases:-
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
| **Override normalize-method default in settings.toml**  | `datapipeline run --config config/settings.toml --normalize-method robust`        |
-----------

## 🤝 Contributing

Open-source thrives because of contributors like you. Whether it's a bug fix, feature, or suggestion, your contribution is **highly valued**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AddFeature`)
3. Commit your Changes (`git commit -m 'Add some new Feature'`)
4. Push to the Branch (`git push origin feature/AddFeature`)
5. Open a Pull Request

### 📑 Development Guidelines:
- Follow existing code style and conventions
- Write clear, concise commit messages
- Add comments for complex logic
- Test your changes thoroughly before submitting
- Update documentation if needed

### 🐛 Bug/Issue Reporting
Feel free to [open an issue](https://github.com/deep0505sharma/Data-Processing-Pipeline/issues) on GitHub if you find bugs.

When reporting bugs, please include:
- Steps to reproduce the issue
- Expected vs actual behavior
- Images if applicable
- Browser/device information
- error messages

### ⭐ Feature Request
- Feel free to [open an issue](https://github.com/deep0505sharma/Data-Processing-Pipeline/issues) on GitHub to request new features or enhancements.  
- Connect with me on [LinkedIn](https://www.linkedin.com/in/deepak-sharma-40a8781b8/) to discuss ideas and suggestions. 

## 🔮 Potential Future Enhancements:
- [ ] Adding new options or methodologies for null imputation
- [ ] Support for large datasets using pyspark
- [ ] Adding option to save output in other file formats (e.g., .parquet)

## ✍🏻 Author
**Deepak Sharma**
- GitHub: [@deep0505sharma](https://github.com/deep0505sharma)
- LinkedIn: [Love to connect with you](https://www.linkedin.com/in/deepak-sharma-40a8781b8/)
- Email: [Contact me](mailto:ds8407205@gmail.com)

---------
  ```javascript
  if youLiked : 
      ⭐ Star_Repository
  # Thank You! 🙏
  ```
-----------
