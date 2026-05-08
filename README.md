# ECOTEC_Online Student Risk Dataset

## Overview

The ECOTEC_Online Student Risk Dataset contains anonymized institutional records collected from online higher education programs at Universidad ECOTEC (Ecuador). The repository was organized to support reproducible research in learning analytics, educational data mining, student retention modeling, institutional analytics, and responsible artificial intelligence applications in higher education environments.

The repository integrates demographic, academic, financial, admission, and institutional variables associated with student risk analytics under real-world educational conditions.

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
| Target Variable | TARGET_RISK |
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

## Included Resources

### Data Resources
- Curated anonymized public dataset
- Processed reproducibility dataset
- Preprocessing summary artifacts

### Metadata Resources
- Variable dictionary
- Codebook
- Preprocessing documentation

### Benchmark Resources
- Random Forest baseline pipeline
- Logistic Regression baseline pipeline
- Classification metrics
- Classification reports

### Visualization Resources
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

## Data Anonymization

Personally identifiable information was removed prior to public dissemination. The anonymization workflow excluded:
- Names
- Identification numbers
- Email addresses
- Telephone numbers
- Direct institutional identifiers

Additional transformations and categorical aggregations were applied to reduce re-identification risk while preserving analytical utility.

---

## Reproducibility

The repository includes preprocessing scripts, benchmark machine learning pipelines, metadata documentation, reproducibility artifacts, and FAIR/Open Science resources intended to facilitate transparent educational AI workflows.

### Included reproducibility components
- Preprocessing pipeline
- Random Forest benchmark pipeline
- Logistic Regression benchmark pipeline
- Variable dictionary
- Metadata documentation
- Benchmark outputs
- Figure generation scripts
- Requirements file

---

## Potential Reuse

The dataset may support research and benchmarking in:
- Learning analytics
- Educational data mining
- Student retention modeling
- Institutional analytics
- Responsible artificial intelligence
- Fairness-aware machine learning
- Explainable artificial intelligence
- Educational decision-support systems
- Reproducible educational AI research

---

## FAIR Data Principles

The repository was organized according to FAIR data principles:

- Findable
- Accessible
- Interoperable
- Reusable

---

## License

This dataset is distributed under the Creative Commons Attribution 4.0 International (CC BY 4.0) license.

---

## Citation

If you use this dataset, please cite:

Hechavarria-Hernandez, J.R., Navarro-Espinosa, J.A., Blanc-Pihuave, G., Ascencio-Jordán, E. (2026). ECOTEC_Online Student Risk Dataset. Zenodo. DOI pending.

---

## Repository Citation File

Citation metadata compatible with GitHub and Zenodo is available in:

```text
CITATION.cff
```

---

## Contact Information

Corresponding author:

Jesus Rafael Hechavarria-Hernandez  
Universidad ECOTEC  
Samborondón, Ecuador  
Email: jhechavarria@ecotec.edu.ec
