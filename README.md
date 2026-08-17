# ECOTEC_Online Student Risk Dataset

## Overview

The **ECOTEC_Online Student Risk Dataset** contains anonymized institutional student-level records from online higher education programs at Universidad ECOTEC, Ecuador. The public release comprises **12,632 unique students and 18 variables** and is intended to support reproducible research in learning analytics, educational data mining, institutional analytics, responsible artificial intelligence, explainable AI, fairness-aware AI, and educational decision-support systems.

`TARGET_RISK` is a **contemporaneous administrative proxy** derived during institutional data preparation from `STUDENT_TYPE` and `GRADUATION_DATE`. It should not be interpreted as a prospectively observed dropout or retention outcome.

---

## Dataset Characteristics

| Attribute | Description |
|---|---|
| Institution | Universidad ECOTEC |
| Country | Ecuador |
| Educational modality | Online Higher Education |
| Observation unit | One unique student |
| Records | 12,632 |
| Variables | 18 |
| Target | `TARGET_RISK` |
| Missing cells | 0 |
| Duplicate rows | 0 |
| License | CC BY 4.0 |
| Version | 1.0.3 |
| Version DOI | [10.5281/zenodo.21982443](https://doi.org/10.5281/zenodo.21982443) |
| Concept DOI | [10.5281/zenodo.20091001](https://doi.org/10.5281/zenodo.20091001) |

Dataset SHA-256:

```text
8466b02d028be1fb11c39a320517d0d388580436b5278f949d60e05ee06899ac
```

---

## Public Variables

### Identifier
- `PUBLIC_RECORD_ID`

### Demographic
- `GENDER`
- `AGE`
- `MARITAL_STATUS`
- `ETHNICITY`
- `DISABILITY`

### Academic
- `FACULTY`
- `DEGREE_PROGRAM`
- `CURRICULUM_YEAR`

### Institutional and Geographic
- `INSTITUTION_TYPE`
- `NATIONALITY_COUNTRY`
- `REGION`

### Admission
- `TRANSFER_STUDENT_FLAG`
- `ONLINE_ADMISSION_TYPE`

### Financial and Administrative
- `PAYMENT_PLAN`
- `PAYMENT_DEFERRAL_TYPE`
- `SCHOLARSHIP_NAME`

### Target
- `TARGET_RISK`

---

## TARGET_RISK

`TARGET_RISK` was derived during institutional data preparation using restricted administrative information that is not included among the public predictors:

- `TARGET_RISK = 0` when `STUDENT_TYPE` indicated Alumni **or** a valid `GRADUATION_DATE` was recorded.
- `TARGET_RISK = 1` when the student was not recorded as Alumni **and** no valid `GRADUATION_DATE` was available.

No grade threshold, predictive model, weighted score, or institutional risk index was used to define the target.

Final class distribution:

| Class | Records | Percentage |
|---|---:|---:|
| 0 | 691 | 5.47% |
| 1 | 11,941 | 94.53% |
| **Total** | **12,632** | **100.00%** |

---

## Data Preparation, Anonymization, and Privacy

Before public release, the institutional data underwent a controlled preparation and anonymization process in accordance with the approved institutional protocol. The resulting public dataset contains no direct personal identifiers and retains selected variables only at the levels of granularity considered appropriate for scientific dissemination.

Geographic information was reviewed and harmonized during institutional data preparation, and the public `REGION` variable was standardized to Ecuador's four natural regions:

- `Coastal Region` — 11,063 records
- `Highlands Region` — 1,338 records
- `Amazon Region` — 190 records
- `Insular Region` — 41 records

Country-specific nationality categories were generalized to:

- `Ecuadorian` — 12,542 records
- `International` — 90 records

This generalization reduces disclosure risk associated with sparsely represented nationality categories while preserving the analytical distinction between domestic and international students.

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

## Reproducibility

The released Python scripts support validation of the public dataset, generation of descriptive figures, and reproducible Logistic Regression and Random Forest benchmark analyses. The benchmark models use 16 predictors after excluding `PUBLIC_RECORD_ID` and `TARGET_RISK`.

`requirements.txt` specifies the principal runtime dependencies. `requirements-lock.txt` records the corresponding package versions captured in the final benchmark validation environment, and `environment_versions.txt` documents the associated computational environment.

The benchmark models are provided as **computational reproducibility baselines** and should not be interpreted as prospectively validated dropout-prediction models or operational early-warning systems.

### Final benchmark results

| Metric | Logistic Regression | Random Forest |
|---|---:|---:|
| Accuracy | 0.940633 | 0.979683 |
| F1 (Class 1) | 0.967677 | 0.989271 |
| ROC-AUC | 0.988559 | 0.984338 |
| Balanced Accuracy | 0.945843 | 0.889115 |
| Macro-F1 | 0.802094 | 0.899102 |

Model-specific classification reports and confusion matrices are available under `results/`.

---

## Intended Use

Appropriate uses include:

- learning analytics and educational data mining;
- institutional and subgroup-level exploratory analyses;
- benchmarking of machine-learning methods;
- methodological research on class imbalance;
- fairness-aware and explainable AI research;
- reproducible educational AI workflows.

The dataset is not intended for automated high-stakes decisions about individual students, identification of individuals, medical or psychological diagnosis, or operational deployment without independent validation and appropriate governance.

---

## FAIR and Open Science

The repository supports FAIR-oriented reuse through:

- persistent versioned archiving in Zenodo;
- standardized citation metadata through `CITATION.cff`;
- interoperable CSV data;
- structured metadata in `variable_dictionary.xlsx` and `codebook.pdf`;
- version-controlled source code and benchmark outputs;
- CC BY 4.0 licensing.

GitHub repository: https://github.com/jrhechavarriah/ECOTEC_Online_Student_Risk_Dataset

Zenodo version 1.0.3: https://doi.org/10.5281/zenodo.21982443

Concept DOI for all versions: https://doi.org/10.5281/zenodo.20091001

---

## Citation

If you use **version 1.0.3**, please cite:

> Hechavarria-Hernandez, J. R., Navarro-Espinosa, J. A., Blanc-Pihuave, G., & Ascencio-Jordan, E. (2026). *ECOTEC_Online Student Risk Dataset* (Version 1.0.3) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.21982443

---

## License

This dataset and repository materials are distributed under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license.

---

## Contact

**Jesus Rafael Hechavarria-Hernandez**  
Universidad ECOTEC  
Samborondon, Ecuador  
Email: jhechavarria@ecotec.edu.ec  
ORCID: https://orcid.org/0000-0002-9013-8665
