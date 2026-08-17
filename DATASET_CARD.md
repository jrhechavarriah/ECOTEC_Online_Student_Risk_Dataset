# DATASET CARD
# ECOTEC_Online Student Risk Dataset

---

## Dataset Overview

The **ECOTEC_Online Student Risk Dataset** contains anonymized institutional student-level records from online higher education programs at Universidad ECOTEC, Ecuador. It provides a real-world educational dataset for reproducible research in learning analytics, educational data mining, institutional analytics, explainable artificial intelligence, fairness-aware AI, and educational decision-support systems.

The public release contains **12,632 unique student records and 18 variables**. Each row corresponds to one unique student.

---

## Dataset Characteristics

| Attribute | Description |
|---|---|
| Institution | Universidad ECOTEC |
| Country | Ecuador |
| Educational modality | Online Higher Education |
| Dataset type | Institutional tabular dataset |
| Observation unit | One unique student |
| Records | 12,632 |
| Variables | 18 |
| Missing cells | 0 |
| Duplicate rows | 0 |
| Unique `PUBLIC_RECORD_ID` | 12,632 |
| Target variable | `TARGET_RISK` |
| File format | CSV |
| License | CC BY 4.0 |
| Version | 1.0.3 |
| Version DOI | [10.5281/zenodo.21982443](https://doi.org/10.5281/zenodo.21982443) |
| Concept DOI | [10.5281/zenodo.20091001](https://doi.org/10.5281/zenodo.20091001) |

Dataset SHA-256:

```text
8466b02d028be1fb11c39a320517d0d388580436b5278f949d60e05ee06899ac
```

---

## Variable Categories

### Identifier
- `PUBLIC_RECORD_ID`

### Demographic Variables
- `GENDER`
- `AGE`
- `MARITAL_STATUS`
- `ETHNICITY`
- `DISABILITY`

### Academic Variables
- `FACULTY`
- `DEGREE_PROGRAM`
- `CURRICULUM_YEAR`

### Institutional and Geographic Variables
- `INSTITUTION_TYPE`
- `NATIONALITY_COUNTRY`
- `REGION`

### Admission Variables
- `TRANSFER_STUDENT_FLAG`
- `ONLINE_ADMISSION_TYPE`

### Financial and Administrative Variables
- `PAYMENT_PLAN`
- `PAYMENT_DEFERRAL_TYPE`
- `SCHOLARSHIP_NAME`

### Target Variable
- `TARGET_RISK`

---

## TARGET_RISK Definition and Scope

`TARGET_RISK` is a binary contemporaneous administrative target derived during institutional data preparation from `STUDENT_TYPE` and `GRADUATION_DATE`.

- `TARGET_RISK = 0`: `STUDENT_TYPE` indicated Alumni or a valid `GRADUATION_DATE` was recorded.
- `TARGET_RISK = 1`: the student was not recorded as Alumni and no valid `GRADUATION_DATE` was available.

The restricted source variables used to construct the target are not included in the public predictor matrix. No grade threshold, statistical model, weighted score, or institutional risk index was used to define the target.

Because the target and public predictors correspond to the same institutional snapshot, `TARGET_RISK` should not be interpreted as a prospectively observed dropout or retention outcome.

### Class Distribution

| Class | Records | Percentage |
|---|---:|---:|
| 0 | 691 | 5.47% |
| 1 | 11,941 | 94.53% |
| **Total** | **12,632** | **100.00%** |

---

## Data Collection and Institutional Preparation

The public dataset was compiled from institutional academic management information associated with online higher education programs at Universidad ECOTEC, Ecuador.

Before public dissemination, the institutional data underwent controlled preparation, verification, harmonization, and anonymization in accordance with the approved institutional protocol. The finalized public dataset contains 18 variables, no duplicate rows, and no missing cells.

---

## Data Anonymization and Privacy

The resulting public dataset contains no direct personal identifiers and retains selected variables only at the levels of granularity considered appropriate for scientific dissemination.

Geographic information was reviewed and harmonized during institutional data preparation. The public `REGION` variable is standardized to Ecuador's four natural regions:

| REGION | Records |
|---|---:|
| Coastal Region | 11,063 |
| Highlands Region | 1,338 |
| Amazon Region | 190 |
| Insular Region | 41 |

Country-specific nationality categories were generalized as follows:

| NATIONALITY_COUNTRY | Records |
|---|---:|
| Ecuadorian | 12,542 |
| International | 90 |

This generalization reduces disclosure risk associated with sparsely represented nationality categories while preserving the analytical distinction between domestic and international students.

The public `DISABILITY` variable retains a binary status indicator; higher-granularity disability information is not part of the public release.

The publicly released scripts operate on this finalized anonymized dataset and are intended to support data validation, descriptive analysis, and reproducible benchmark analyses.

---

## Repository Structure

```text
ECOTEC_Online_Student_Risk_Dataset/
|
|-- data/
|   `-- ecotec_online_student_risk.csv
|
|-- metadata/
|   |-- variable_dictionary.xlsx
|   `-- codebook.pdf
|
|-- scripts/
|   |-- utils.py
|   |-- baseline_logistic_regression.py
|   |-- baseline_random_forest.py
|   |-- generate_dataset_figures.py
|   |-- requirements.txt
|   |-- requirements-lock.txt
|   `-- environment_versions.txt
|
|-- results/
|   |-- logistic_regression/
|   |   |-- metrics.csv
|   |   |-- classification_report.txt
|   |   `-- confusion_matrix.csv
|   |
|   `-- random_forest/
|       |-- metrics.csv
|       |-- classification_report.txt
|       `-- confusion_matrix.csv
|
|-- figures/
|   |-- class_distribution.png
|   |-- subgroup_distribution.png
|   `-- feature_categories.png
|
|-- README.md
|-- DATASET_CARD.md
|-- CITATION.cff
|-- LICENSE
|-- .gitignore
`-- .gitattributes
```

---

## Reproducibility Resources

The public repository provides:

- validation and shared utility functions;
- Logistic Regression and Random Forest benchmark scripts;
- descriptive figure-generation code;
- principal runtime dependency specifications;
- exact package versions captured in the final benchmark validation environment;
- model-specific metrics, classification reports, and confusion matrices.

The benchmark models use 16 predictors after excluding `PUBLIC_RECORD_ID` and `TARGET_RISK`.

### Final Benchmark Results

| Metric | Logistic Regression | Random Forest |
|---|---:|---:|
| Accuracy | 0.940633 | 0.979683 |
| F1 (Class 1) | 0.967677 | 0.989271 |
| ROC-AUC | 0.988559 | 0.984338 |
| Balanced Accuracy | 0.945843 | 0.889115 |
| Macro-F1 | 0.802094 | 0.899102 |

The benchmarks are reproducibility baselines and are not prospectively validated operational early-warning systems.

---

## Intended Use

The dataset may support:

- learning analytics;
- educational data mining;
- institutional analytics;
- methodological benchmarking;
- class-imbalance research;
- fairness-aware machine learning;
- explainable artificial intelligence;
- educational decision-support research;
- reproducible educational AI workflows.

---

## Out-of-Scope Uses

The dataset was not designed for:

- automated high-stakes decisions affecting individual students;
- identification or re-identification of individuals;
- medical or psychological diagnosis;
- commercial surveillance;
- operational deployment without independent temporal/external validation and appropriate governance.

---

## Limitations

- Data originate from a single higher education institution in Ecuador.
- The dataset represents online higher education programs.
- `TARGET_RISK` is contemporaneous and does not establish a predictor-before-outcome temporal sequence.
- The target distribution is strongly imbalanced.
- Selected quasi-identifying variables are retained only at documented levels of generalization.
- Country-specific nationality and detailed geographic information are not available in the public release.
- Benchmark performance should not be interpreted as evidence of prospective deployment validity.

---

## FAIR Principles

### Findable
The dataset is versioned and persistently identified through Zenodo and described using `CITATION.cff`.

### Accessible
The public release is openly available through GitHub and Zenodo under CC BY 4.0.

### Interoperable
The main dataset is distributed as CSV and accompanied by structured metadata.

### Reusable
The repository includes a variable dictionary, codebook, scripts, benchmark outputs, environment documentation, licensing, and version-specific citation metadata.

---

## Citation

If you use **version 1.0.3**, please cite:

> Hechavarria-Hernandez, J. R., Navarro-Espinosa, J. A., Blanc-Pihuave, G., & Ascencio-Jordan, E. (2026). *ECOTEC_Online Student Risk Dataset* (Version 1.0.3) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.21982443

GitHub repository: https://github.com/jrhechavarriah/ECOTEC_Online_Student_Risk_Dataset

Version-specific DOI: https://doi.org/10.5281/zenodo.21982443

Concept DOI for all versions: https://doi.org/10.5281/zenodo.20091001

---

## License

Creative Commons Attribution 4.0 International (CC BY 4.0).

---

## Contact Information

**Jesus Rafael Hechavarria-Hernandez**  
Universidad ECOTEC  
Samborondon, Ecuador  
Email: jhechavarria@ecotec.edu.ec  
ORCID: https://orcid.org/0000-0002-9013-8665
