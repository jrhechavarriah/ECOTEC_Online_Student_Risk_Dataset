# ECOTEC_Online Student Risk Dataset

## Overview

The **ECOTEC_Online Student Risk Dataset** contains anonymized institutional student-level records from online higher education programs at Universidad ECOTEC, Ecuador. The public release comprises **12,632 unique students and 18 variables** and is intended to support reproducible research in learning analytics, educational data mining, institutional analytics, responsible artificial intelligence, explainable AI, fairness-aware AI, class-imbalanced classification, and educational decision-support research.

`TARGET_RISK` is a **binary contemporaneous administrative proxy derived during study-level data curation** from the restricted source variables `STUDENT_TYPE` and `GRADUATION_DATE`. It was **not a native variable** in the restricted institutional research extract and should not be interpreted as a prospectively observed dropout or retention outcome.

---

## Dataset Characteristics

| Attribute | Description |
|---|---|
| Institution | Universidad ECOTEC |
| Country | Ecuador |
| Educational modality | Online higher education |
| Observation unit | One unique student |
| Records | 12,632 |
| Variables | 18 |
| Target | `TARGET_RISK` |
| Missing cells | 0 |
| Duplicate rows | 0 |
| Unique `PUBLIC_RECORD_ID` | 12,632 |
| License | CC BY 4.0 |
| Version | 1.0.4 |
| Version DOI | 10.5281/zenodo.22015963 |
| Concept DOI | [10.5281/zenodo.20091001](https://doi.org/10.5281/zenodo.20091001) |

Canonical public CSV SHA-256:

```text
8466b02d028be1fb11c39a320517d0d388580436b5278f949d60e05ee06899ac
```

A release-specific SHA256SUMS.txt manifest provides SHA-256 checksums for the archived repository resources, supporting file-level integrity verification of this release.

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

### Financial and Payment-Related
- `PAYMENT_PLAN`
- `PAYMENT_DEFERRAL_TYPE`
- `SCHOLARSHIP_NAME`

### Target
- `TARGET_RISK`

---

## TARGET_RISK Definition and Scope

`TARGET_RISK` was derived during **study-level data curation** from two restricted administrative source variables that are not included among the public predictors:

- `TARGET_RISK = 0` when `STUDENT_TYPE = "Alumni"` **or** a valid `GRADUATION_DATE` was recorded.
- `TARGET_RISK = 1` when the student was not recorded as Alumni **and** no valid `GRADUATION_DATE` was recorded.

No grade threshold, academic-performance cutoff, predictive model, weighted score, or institutional risk index was used to define the target. Both `STUDENT_TYPE` and `GRADUATION_DATE` were excluded from the public dataset after target derivation.

Final class distribution:

| Class | Operational meaning | Records | Percentage |
|---|---|---:|---:|
| 0 | Alumni status and/or valid graduation date recorded | 691 | 5.47% |
| 1 | Not recorded as Alumni and no valid graduation date recorded | 11,941 | 94.53% |
| **Total** | — | **12,632** | **100.00%** |

Because the target and released predictors originate from the same institutional snapshot, the dataset does not establish a predictor-before-outcome temporal sequence. The benchmark analyses should therefore be interpreted as **cross-sectional computational reproducibility baselines**, not as evidence of prospective dropout prediction or operational early-warning performance.

---

## Financial and Payment-Related Variables

The public dataset includes three non-monetary financial and payment-related institutional variables:

- `PAYMENT_PLAN`: categorical institutional payment-plan descriptor (`No`, `Yes`).
- `PAYMENT_DEFERRAL_TYPE`: numeric duration of the institutionally recorded payment deferral, expressed in **months**. The public variable corresponds to the institutional source field `TIPO_DIFIRIMIENTO`. A value of `0` indicates **no payment deferral**; positive values indicate the corresponding number of months. The values are quantitative durations, not nominal category codes or monetary amounts.
- `SCHOLARSHIP_NAME`: categorical scholarship or discount descriptor. Monetary scholarship amounts are not included.

The complete public categories for `PAYMENT_PLAN` and `SCHOLARSHIP_NAME`, together with the observed `PAYMENT_DEFERRAL_TYPE` month values and their frequencies, are documented in `metadata/variable_dictionary.xlsx` and `metadata/codebook.pdf`.

These variables should be interpreted as institutional administrative descriptors rather than as direct measures of individual socioeconomic status.

---

## Data Provenance, Institutional Preparation, and Privacy

Universidad ECOTEC performed institutional preparation and anonymization **before delivering the research dataset to the authors**. The research team received an institutionally anonymized research dataset and did not access the pre-anonymization institutional source data.

The earliest auditable research cohort available to the authors contains **12,632 records and 42 variables**, corresponding to 12,632 unique students. The restricted research extract available to the study team did not contain student names, national identification numbers, email addresses, or telephone numbers.

During preparation of the public research release, documented and verifiable public-release treatments included replacement of the institutional student-record identifier with the release-specific `PUBLIC_RECORD_ID`, exclusion of restricted variables not included in the public schema, generalization of detailed geography to `REGION`, generalization of country-specific nationality to `Ecuadorian` and `International`, and derivation of `TARGET_RISK` during study-level data curation.

The public `REGION` variable contains Ecuador's four natural regions:

- `Coastal Region` — 11,063 records
- `Highlands Region` — 1,338 records
- `Amazon Region` — 190 records
- `Insular Region` — 41 records

`NATIONALITY_COUNTRY` contains:

- `Ecuadorian` — 12,542 records
- `International` — 90 records

The public `DISABILITY` variable is a binary status indicator; higher-granularity disability information is not included in the public release.

The publicly released analytical scripts operate exclusively on the finalized 18-variable public dataset and do not perform or reconstruct the upstream institutional anonymization process.

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
|-- SHA256SUMS.txt
|-- LICENSE
|-- .gitignore
`-- .gitattributes
```

---

## Reproducibility

The finalized anonymized public CSV is the canonical input for the released analytical workflows. No separate processed-data copy is required.

### Environment

`requirements.txt` specifies the principal compatible runtime dependencies. `requirements-lock.txt` records the principal package versions captured in the final benchmark validation environment, and `environment_versions.txt` documents the associated Python and platform information.

### Documented execution sequence

From the repository root, the public-data-derived outputs can be regenerated in the following order:

```bash
python scripts/generate_dataset_figures.py
python scripts/baseline_logistic_regression.py
python scripts/baseline_random_forest.py
```

The default arguments use:

```text
data/ecotec_online_student_risk.csv
```

and write outputs to:

```text
figures/
results/logistic_regression/
results/random_forest/
```

This documented three-command workflow is the reproducibility entry sequence for the archived release.

### Final benchmark results

| Metric | Logistic Regression | Random Forest |
|---|---:|---:|
| Accuracy | 0.940633 | 0.979683 |
| F1 (Class 1) | 0.967677 | 0.989271 |
| ROC-AUC | 0.988559 | 0.984338 |
| Balanced Accuracy | 0.945843 | 0.889115 |
| Macro-F1 | 0.802094 | 0.899102 |

Model-specific metrics, classification reports, and confusion matrices are available under `results/`.

The benchmarks are **computational reproducibility baselines**. They have not undergone prospective or temporal validation, probability-calibration assessment, threshold optimization for institutional objectives, external validation, impact assessment, or deployment testing.

---

## Intended Use

Appropriate uses include:

- learning analytics and educational data mining;
- institutional and subgroup-level exploratory analyses;
- benchmarking of machine-learning methods;
- methodological research on class imbalance;
- fairness-aware and explainable AI research;
- reproducible educational AI workflows;
- educational decision-support research.

---

## Out-of-Scope Uses

The dataset is not intended for:

- automated high-stakes decisions affecting individual students;
- identification or re-identification of individuals;
- medical or psychological diagnosis;
- commercial surveillance;
- operational deployment without independent temporal/external validation and appropriate governance.

---

## Limitations

- The dataset originates from a single higher education institution in Ecuador.
- It represents a cross-sectional student-level institutional snapshot with one record per unique student.
- It does not provide repeated observations or a documented longitudinal linkage key across releases.
- `CURRICULUM_YEAR` represents the curriculum-plan year and should not be interpreted as the student's observation year or academic cohort.
- `TARGET_RISK` is a contemporaneous administrative proxy and does not establish a predictor-before-outcome temporal sequence.
- The target distribution is strongly imbalanced.
- Indirect proxy associations with completion status may remain, and temporal leakage cannot be excluded for prospective use.
- Benchmark results should not be interpreted as evidence of prospective deployment validity.
- The public release is intended to reduce disclosure risk; it does not claim zero re-identification risk.

---

## FAIR-Oriented Data Management and Open Science

The repository supports FAIR-oriented reuse through:

- **Findability:** versioned Zenodo archiving, persistent DOI assignment, and standardized citation metadata through `CITATION.cff`;
- **Accessibility:** public access through Zenodo and the synchronized GitHub repository under CC BY 4.0;
- **Interoperability:** a widely supported CSV representation together with structured variable-level metadata and an accompanying codebook documenting the released schema, meanings, coding conventions, and units;
- **Reusability:** variable-level metadata and provenance documentation, repository documentation, validation and descriptive-analysis scripts, reproducible benchmark scripts and outputs, computational-environment specifications, licensing, and versioned archiving.

Computational integrity is additionally supported through the release-specific `SHA256SUMS.txt` manifest, generated after the final release files and DOI metadata have been fixed.

GitHub repository: https://github.com/jrhechavarriah/ECOTEC_Online_Student_Risk_Dataset

Zenodo version 1.0.4 DOI: 10.5281/zenodo.22015963

Concept DOI for all versions: https://doi.org/10.5281/zenodo.20091001

---

## Citation

If you use **version 1.0.4**, please cite:

> Hechavarria-Hernandez, J. R., Navarro-Espinosa, J. A., Blanc-Pihuave, G., & Ascencio-Jordan, E. (2026). *ECOTEC_Online Student Risk Dataset* (Version 1.0.4) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.22015963

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
