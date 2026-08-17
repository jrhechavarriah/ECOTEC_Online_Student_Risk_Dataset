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

### Identifier
- PUBLIC_RECORD_ID

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

### Institutional and Geographic Variables
- INSTITUTION_TYPE
- NATIONALITY_COUNTRY
- REGION

### Admission Variables
- TRANSFER_STUDENT_FLAG
- ONLINE_ADMISSION_TYPE

### Financial and Administrative Variables
- PAYMENT_PLAN
- PAYMENT_DEFERRAL_TYPE
- SCHOLARSHIP_NAME

### Target Variable
- TARGET_RISK

**Operational definition.** `TARGET_RISK` is a binary contemporaneous
administrative target derived during restricted institutional curation from
`STUDENT_TYPE` and `GRADUATION_DATE`. Class 0 indicates that alumni status or
a valid graduation date was recorded; class 1 indicates that the student was
not recorded as alumni and no graduation date was available. The two
restricted source variables were excluded from the public predictor matrix
after target construction. The released label does not constitute a
prospectively observed dropout or retention outcome.

## Intended Use

This dataset may support:
- Learning analytics research
- Educational data mining
- Student retention modeling
- Institutional analytics
- Benchmarking of machine learning models
- Fairness-aware AI research
- Explainable AI research
- Methodological evaluation of educational classification and decision-support pipelines
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
- Prospective dropout prediction or early-warning deployment without a temporally ordered outcome and independent validation

---

## Data Collection Process

The public dataset contains 12,632 student-level records from online higher education programs at Universidad ECOTEC, Ecuador. Each public record corresponds to one unique student.

Before public dissemination, the institutional data underwent controlled preparation, verification, harmonization, and anonymization in accordance with the approved institutional protocol. The finalized public dataset contains 18 variables, no duplicate rows, and no missing cells.

`TARGET_RISK` is a binary contemporaneous administrative target derived during institutional data preparation from `STUDENT_TYPE` and `GRADUATION_DATE`. Class 0 indicates that alumni status or a valid graduation date was recorded, whereas Class 1 indicates that the student was not recorded as alumni and no valid graduation date was available. The variables used to construct the target are not included in the public predictor matrix.

## Data Anonymization and Privacy

Before public release, the institutional data underwent a controlled preparation and anonymization process in accordance with the approved institutional protocol. The resulting public dataset contains no direct personal identifiers and retains selected variables only at the levels of granularity considered appropriate for scientific dissemination.

Geographic information was reviewed and harmonized during institutional data preparation, and the public `REGION` variable was standardized to Ecuador's four natural regions: `Coastal Region`, `Highlands Region`, `Amazon Region`, and `Insular Region`.

Country-specific nationality categories were generalized to `Ecuadorian` and `International` to reduce disclosure risk associated with sparsely represented nationality categories while preserving the analytical distinction between domestic and international students.

The publicly released scripts operate on this finalized anonymized dataset and are intended to support data validation, descriptive analysis, and reproducible benchmark analyses.

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
- `TARGET_RISK` is a contemporaneous administrative status-derived label rather than a prospectively observed dropout or retention outcome
- Benchmark results should not be interpreted as validated early-warning performance or operational institutional decision support

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

The public repository is organized around the finalized anonymized dataset in `data/ecotec_online_student_risk.csv`.

The released Python scripts support validation of the public dataset, generation of descriptive figures, and reproducible Logistic Regression and Random Forest benchmark analyses. Model-specific outputs include overall performance metrics, class-specific classification reports, and confusion matrices.

`requirements.txt` specifies the principal runtime dependencies. `requirements-lock.txt` records the corresponding package versions captured in the final benchmark validation environment, while `environment_versions.txt` documents the associated computational environment.

The benchmark models are provided as computational reproducibility baselines and should not be interpreted as prospectively validated dropout prediction models or operational early-warning systems.

## License

This dataset is distributed under the Creative Commons Attribution 4.0 International (CC BY 4.0) license.

---

## Citation

If you use this dataset, please cite:

Hechavarria-Hernandez, J. R., Navarro-Espinosa, J. A., Blanc-Pihuave, G., & Ascencio-Jordan, E. (2026). ECOTEC_Online Student Risk Dataset (v1.0.2). Zenodo. https://doi.org/10.5281/zenodo.21243448

---

## Contact Information

Corresponding author:

Jesus Rafael Hechavarria-Hernandez  
Universidad ECOTEC  
Samborondón, Ecuador  
Email: jhechavarria@ecotec.edu.ec




