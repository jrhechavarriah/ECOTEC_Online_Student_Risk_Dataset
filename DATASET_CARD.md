# DATASET CARD
# ECOTEC_Online Student Risk Dataset

---

## Dataset Overview

The **ECOTEC_Online Student Risk Dataset** contains anonymized institutional student-level records from online higher education programs at Universidad ECOTEC, Ecuador. It provides a real-world educational dataset for reproducible research in learning analytics, educational data mining, institutional analytics, explainable artificial intelligence, fairness-aware AI, class-imbalanced classification, and educational decision-support research.

The public release contains **12,632 unique student records and 18 variables**. Each row corresponds to one unique student.

---

## Dataset Characteristics

| Attribute | Description |
|---|---|
| Institution | Universidad ECOTEC |
| Country | Ecuador |
| Educational modality | Online higher education |
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
| Version | 1.0.4 |
| Version DOI | 10.5281/zenodo.22015963 |
| Concept DOI | [10.5281/zenodo.20091001](https://doi.org/10.5281/zenodo.20091001) |

Canonical public CSV SHA-256:

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

### Financial and Payment-Related Variables
- `PAYMENT_PLAN`
- `PAYMENT_DEFERRAL_TYPE`
- `SCHOLARSHIP_NAME`

### Target Variable
- `TARGET_RISK`

---

## TARGET_RISK Definition, Provenance, and Scope

`TARGET_RISK` is a binary contemporaneous administrative target derived during **study-level data curation** from the restricted source variables `STUDENT_TYPE` and `GRADUATION_DATE`. It was **not a native field** in the restricted institutional research extract.

- `TARGET_RISK = 0`: `STUDENT_TYPE = "Alumni"` or a valid `GRADUATION_DATE` was recorded.
- `TARGET_RISK = 1`: the student was not recorded as Alumni and no valid `GRADUATION_DATE` was recorded.

The restricted source variables used to construct the target are not included in the public predictor matrix. No grade threshold, academic-performance cutoff, statistical model, weighted score, or institutional risk index was used to define the target.

Because the target and public predictors originate from the same institutional snapshot, `TARGET_RISK` should not be interpreted as a prospectively observed dropout or retention outcome and does not establish a predictor-before-outcome temporal sequence.

### Class Distribution

| Class | Operational meaning | Records | Percentage |
|---|---|---:|---:|
| 0 | Alumni status and/or valid graduation date recorded | 691 | 5.47% |
| 1 | Not recorded as Alumni and no valid graduation date recorded | 11,941 | 94.53% |
| **Total** | — | **12,632** | **100.00%** |

---

## Financial and Payment-Related Variables

The public release contains three non-monetary financial and payment-related institutional variables:

- `PAYMENT_PLAN`: categorical institutional payment-plan descriptor with public categories `No` and `Yes`.
- `PAYMENT_DEFERRAL_TYPE`: numeric duration of the institutionally recorded payment deferral, expressed in **months**. It corresponds to the institutional source field `TIPO_DIFIRIMIENTO`. A value of `0` indicates no payment deferral; positive values indicate the corresponding number of months. The values are quantitative durations, not nominal category codes or monetary amounts.
- `SCHOLARSHIP_NAME`: categorical scholarship or discount descriptor; monetary scholarship amounts are not included.

The complete public categories and observed frequencies are documented in `metadata/variable_dictionary.xlsx` and `metadata/codebook.pdf`.

These variables are institutional administrative descriptors rather than direct measures of individual socioeconomic status.

---

## Data Provenance and Institutional Preparation

The public dataset originates from institutional academic management information associated with online higher education programs at Universidad ECOTEC, Ecuador.

Universidad ECOTEC performed institutional preparation and anonymization **before delivery of the research dataset to the authors**. The research team received an institutionally anonymized research dataset and did not access the pre-anonymization institutional source data.

The earliest auditable research cohort available to the study team contains **12,632 records and 42 variables**, corresponding to 12,632 unique students. The restricted research extract available to the authors did not contain student names, national identification numbers, email addresses, or telephone numbers.

Subsequent study-level data curation created `TARGET_RISK`, replaced the institutional student-record identifier with the release-specific `PUBLIC_RECORD_ID`, and produced the finalized 18-variable public schema without changing the 12,632-student cohort.

---

## Public-Release Generalization and Privacy

The public dataset contains no direct personal identifiers.

The public `REGION` variable contains Ecuador's four natural regions:

| REGION | Records |
|---|---:|
| Coastal Region | 11,063 |
| Highlands Region | 1,338 |
| Amazon Region | 190 |
| Insular Region | 41 |

`NATIONALITY_COUNTRY` contains:

| NATIONALITY_COUNTRY | Records |
|---|---:|
| Ecuadorian | 12,542 |
| International | 90 |

The public `DISABILITY` variable is a binary status indicator; higher-granularity disability information is not included in the public release.

`PUBLIC_RECORD_ID` is a release-specific public record identifier replacing the restricted institutional student-record code. No public crosswalk to the original institutional identifier is released, and the field should not be interpreted as a documented longitudinal person-level linkage key across academic periods, independent institutional extracts, or future releases.

The documented public-release treatments are intended to reduce disclosure risk while retaining analytical utility. The dataset does **not** claim zero re-identification risk or a formal k-anonymity, l-diversity, or differential-privacy guarantee.

The publicly released scripts operate exclusively on the finalized anonymized public dataset and do not perform or reconstruct the upstream institutional anonymization process.

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

## Reproducibility Resources

The public repository provides:

- validation and shared utility functions;
- Logistic Regression and Random Forest benchmark scripts;
- descriptive figure-generation code;
- principal runtime dependency specifications;
- package versions captured in the final benchmark validation environment;
- model-specific metrics, classification reports, and confusion matrices;
- a release-specific SHA-256 manifest for file-integrity verification.

The benchmark models use 16 predictors after excluding `PUBLIC_RECORD_ID` and `TARGET_RISK`.

### Documented execution sequence

From the repository root:

```bash
python scripts/generate_dataset_figures.py
python scripts/baseline_logistic_regression.py
python scripts/baseline_random_forest.py
```

The scripts use the finalized public CSV as the canonical input and write the corresponding descriptive figures and benchmark outputs to the documented repository folders. This documented three-command workflow is the reproducibility entry sequence for the archived release.

### Final Benchmark Results

| Metric | Logistic Regression | Random Forest |
|---|---:|---:|
| Accuracy | 0.940633 | 0.979683 |
| F1 (Class 1) | 0.967677 | 0.989271 |
| ROC-AUC | 0.988559 | 0.984338 |
| Balanced Accuracy | 0.945843 | 0.889115 |
| Macro-F1 | 0.802094 | 0.899102 |

The benchmarks are computational reproducibility baselines and are not prospectively validated operational early-warning systems.

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
- The dataset represents a cross-sectional student-level institutional snapshot with one record per unique student.
- The public release does not contain an observation-year variable or a documented predictor-before-outcome sequence.
- `CURRICULUM_YEAR` represents the curriculum-plan year and should not be interpreted as the student's observation year or academic cohort.
- `PUBLIC_RECORD_ID` should not be assumed to persist across future independent releases.
- `TARGET_RISK` is a contemporaneous administrative proxy, not a prospectively observed dropout or retention outcome.
- The target distribution is strongly imbalanced.
- Indirect proxy associations with completion status may remain, and temporal leakage cannot be excluded for prospective use.
- External transferability requires local variable harmonization, target-definition equivalence assessment, external validation, subgroup assessment, and, where appropriate, recalibration.
- The public release reduces but does not eliminate disclosure risk.

---

## FAIR-Oriented Data Management

### Findable
The dataset is versioned and persistently identified through Zenodo and described using standardized citation metadata in `CITATION.cff`.

### Accessible
The public release is openly available through GitHub and Zenodo under CC BY 4.0.

### Interoperable
The main dataset is distributed as a widely supported CSV representation and accompanied by structured variable-level metadata and a codebook documenting schema, variable meanings, coding conventions, and units of measurement. This supports syntactic and documentation-level interoperability.

### Reusable
The repository includes variable-level metadata and provenance documentation, a codebook, scripts, benchmark outputs, software-environment documentation, licensing, version-specific citation metadata, and a release-specific checksum manifest.

---

## Citation

If you use **version 1.0.4**, please cite:

> Hechavarria-Hernandez, J. R., Navarro-Espinosa, J. A., Blanc-Pihuave, G., & Ascencio-Jordan, E. (2026). *ECOTEC_Online Student Risk Dataset* (Version 1.0.4) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.22015963

GitHub repository: https://github.com/jrhechavarriah/ECOTEC_Online_Student_Risk_Dataset

Version-specific DOI: https://doi.org/10.5281/zenodo.22015963

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
