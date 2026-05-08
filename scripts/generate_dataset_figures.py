"""
Generate descriptive figures for the ECOTEC_Online Student Risk Dataset.

The figures are descriptive and intended for dataset documentation only.

Example:
    python scripts/generate_dataset_figures.py \
        --input data/ecotec_online_student_risk.csv \
        --output-dir figures
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

import sys
from pathlib import Path

CURRENT_DIR = Path(__file__).resolve().parent
sys.path.append(str(CURRENT_DIR))

from utils import load_dataset, validate_dataset, basic_cleaning


FEATURE_CATEGORIES = {
    "Demographic": ["GENDER", "AGE", "MARITAL_STATUS", "ETHNICITY", "DISABILITY"],
    "Academic": ["FACULTY", "DEGREE_PROGRAM", "CURRICULUM_YEAR"],
    "Institutional": ["INSTITUTION_TYPE", "NATIONALITY_COUNTRY", "REGION"],
    "Admission": ["TRANSFER_STUDENT_FLAG", "ONLINE_ADMISSION_TYPE"],
    "Financial": ["PAYMENT_PLAN", "PAYMENT_DEFERRAL_TYPE", "SCHOLARSHIP_NAME"],
    "Target": ["TARGET_RISK"],
}


def save_bar_chart(series: pd.Series, title: str, xlabel: str, ylabel: str, output_path: Path) -> None:
    fig, ax = plt.subplots(figsize=(8, 5))
    series.plot(kind="bar", ax=ax)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.tight_layout()
    fig.savefig(output_path, dpi=300)
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate dataset descriptive figures.")
    parser.add_argument(
        "--input",
        type=str,
        default="data/ecotec_online_student_risk.csv",
        help="Path to anonymized input CSV file.",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="figures",
        help="Directory to save figures.",
    )
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    df = load_dataset(args.input)
    validate_dataset(df)
    df = basic_cleaning(df)

    # Target class distribution
    target_counts = df["TARGET_RISK"].value_counts().sort_index()
    save_bar_chart(
        target_counts,
        "TARGET_RISK class distribution",
        "TARGET_RISK",
        "Number of records",
        output_dir / "class_distribution.png",
    )

    # Gender subgroup distribution
    if "GENDER" in df.columns:
        gender_counts = df["GENDER"].value_counts()
        save_bar_chart(
            gender_counts,
            "GENDER subgroup distribution",
            "GENDER",
            "Number of records",
            output_dir / "subgroup_distribution.png",
        )

    # Feature category distribution
    category_counts = pd.Series({category: len(cols) for category, cols in FEATURE_CATEGORIES.items()})
    save_bar_chart(
        category_counts,
        "Feature category distribution",
        "Feature category",
        "Number of variables",
        output_dir / "feature_categories.png",
    )

    # Missing values by variable
    missing_counts = df.isna().sum()
    missing_counts = missing_counts[missing_counts > 0].sort_values(ascending=False)
    if not missing_counts.empty:
        save_bar_chart(
            missing_counts,
            "Missing values by variable",
            "Variable",
            "Missing values",
            output_dir / "missing_values.png",
        )

    print(f"Figures saved to: {output_dir}")


if __name__ == "__main__":
    main()
