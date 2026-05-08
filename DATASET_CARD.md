# DATASET CARD
# ECOTEC_Online Student Risk Dataset

---

## Dataset Overview

The ECOTEC_Online Student Risk Dataset contains anonymized institutional records collected from online higher education programs at Universidad ECOTEC (Ecuador). The repository was organized to support reproducible research in learning analytics, educational data mining, institutional analytics, student retention modeling, and responsible artificial intelligence applications in higher education environments.

The dataset integrates demographic, academic, financial, admission, and institutional variables associated with student risk analytics under real-world educational conditions.

---

## Dataset Characteristics

| Attribute | Description |
|---|---|
| Institution | Universidad ECOTEC |
| Country | Ecuador |
| Educational Modality | Online Higher Education |
| Dataset Type | Institutional Tabular Dataset |
| Number of Records | 12,632 |
| File Format | CSV |
| Language | English variable labels |
| Repository Type | Open-science educational dataset |
| License | CC BY 4.0 |

---

## Repository Structure

```text
ECOTEC_Online_Student_Risk_Dataset/
│
├── data/
│   └── ecotec_online_student_risk.csv
│
├── derived_data/
│   ├── ecotec_online_student_risk_processed.csv
│   └── preprocessing_summary.csv
│
├── results/
│   ├── logistic_regression/
│   │   ├── metrics.csv
│   │   └── classification_report.txt
│   │
│   └── random_forest/
│       ├── metrics.csv
│       └── classification_report.txt
│
├── figures/
│   ├── class_distribution.png
│   ├── subgroup_distribution.png
│   └── feature_categories.png
│
├── metadata/
│   ├── variable_dictionary.xlsx
│   ├── codebook.pdf
│   └── preprocessing_description.pdf
│
├── scripts/
│   ├── utils.py
│   ├── preprocessing_pipeline.py
│   ├── generate_dataset_figures.py
│   ├── baseline_random_forest.py
│   ├── baseline_logistic_regression.py
│   └── requirements.txt
│
├── README.md
├── DATASET_CARD.md
├── LICENSE
├── CITATION.cff
└── .gitignore
```

---

## Included Data Resources

### Data Files
- Curated anonymized public dataset
- Processed reproducibility dataset
- Preprocessing summary artifacts

### Metadata Resources
- Variable dictionary
- Codebook
- Preprocessing description

### Reproducibility Resources
- Preprocessing pipeline
- Benchmark Random Forest pipeline
- Benchmark Logistic Regression pipeline
- Reproducibility artifacts and benchmark outputs
- Requirements file

### Benchmark Outputs
- Random Forest classification metrics
- Logistic Regression classification metrics
- Classification reports

### Figures
- TARGET_RISK class distribution
- Gender subgroup distribution
- Feature category distribution

---

## Variable Categories

### Demographic Variables
- AGE
- GENDER
- MARITAL_STATUS
- ETHNICITY
- DISABILITY

### Academic Variables
- FACULTY
- DEGREE_PROGRAM
- CURRICULUM_YEAR
- ENROLLMENT_STATUS

### Financial Variables
- PAYMENT_PLAN
- SCHOLARSHIP_NAME

### Admission Variables
- ONLINE_ADMISSION_TYPE

### Target Variable
- TARGET_RISK

---

## Intended Use

This dataset may support:
- Learning analytics research
- Educational data mining
- Student retention modeling
- Institutional analytics
- Benchmarking of machine learning models
- Fairness-aware AI research
- Explainable AI research
- Educational decision-support systems
- Reproducible educational AI workflows

---

## Out-of-Scope Uses

The dataset was not designed for:
- Individual student profiling
- Automated decision-making affecting students
- Psychological diagnosis
- Medical evaluation
- Identification of individual persons
- Commercial surveillance applications

---

## Data Collection Process

Institutional records were extracted from academic management systems associated with online higher education programs at Universidad ECOTEC, Ecuador. Data acquisition procedures included preprocessing, normalization, anonymization, and removal of personally identifiable information prior to public dissemination.

The repository integrates structured tabular data intended for reproducible analytical workflows.

---

## Data Anonymization and Privacy

Personally identifiable information was removed before public release. The anonymization workflow excluded:
- Names
- Identification numbers
- Email addresses
- Telephone numbers
- Direct institutional identifiers

Additional transformations and categorical aggregations were applied to reduce re-identification risk while preserving analytical utility.

---

## Ethical Considerations

The repository contains anonymized institutional records only. Publicly released files do not contain sensitive personal information or direct identifiers.

The dataset was organized under privacy-preserving procedures intended to protect student confidentiality and support open-science dissemination.

---

## Limitations

- Single institutional source
- Online higher education context only
- Class imbalance associated with real-world institutional distributions
- Variable availability dependent on institutional systems
- Some variables aggregated during anonymization procedures

---

## FAIR Principles

This repository was organized according to FAIR data principles:

### Findable
The dataset is publicly indexed through GitHub and Zenodo.

### Accessible
The repository is openly accessible under CC BY 4.0 licensing.

### Interoperable
Data files are distributed using interoperable CSV formats.

### Reusable
Metadata documentation and reproducibility resources are included to facilitate reuse.

---

## Reproducibility

The repository includes:
- Preprocessing scripts
- Benchmark Random Forest pipeline
- Benchmark Logistic Regression pipeline
- Variable dictionaries
- Metadata documentation
- Reproducibility artifacts
- Requirements file

These resources are intended to facilitate reproducible educational AI workflows.

---

## License

This dataset is distributed under the Creative Commons Attribution 4.0 International (CC BY 4.0) license.

---

## Citation

If you use this dataset, please cite:

Hechavarria-Hernandez, J.R., Navarro-Espinosa, J.A., Blanc-Pihuave, G., Ascencio-Jordán, E. (2026). ECOTEC_Online Student Risk Dataset. Zenodo. [DOI pending]

---

## Contact Information

Corresponding author:

Jesus Rafael Hechavarria-Hernandez  
Universidad ECOTEC  
Samborondón, Ecuador  
Email: jhechavarria@ecotec.edu.ec
