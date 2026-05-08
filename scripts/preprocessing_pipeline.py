"""
Preprocessing pipeline for the ECOTEC_Online Student Risk Dataset.

This script validates the public anonymized dataset, performs minimal cleaning,
and writes a processed CSV suitable for benchmark experiments.

Example:
    python scripts/preprocessing_pipeline.py \
        --input data/ecotec_online_student_risk.csv \
        --output derived_data/ecotec_online_student_risk_processed.csv
"""

from __future__ import annotations

import argparse

import pandas as pd

import sys
from pathlib import Path

CURRENT_DIR = Path(__file__).resolve().parent
sys.path.append(str(CURRENT_DIR))

from utils import load_dataset, validate_dataset, basic_cleaning


def main() -> None:
    parser = argparse.ArgumentParser(description="Preprocess ECOTEC_Online dataset.")
    parser.add_argument(
        "--input",
        type=str,
        default="data/ecotec_online_student_risk.csv",
        help="Path to the anonymized input CSV file.",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="derived_data/ecotec_online_student_risk_processed.csv",
        help="Path to save the processed CSV file.",
    )
    args = parser.parse_args()

    df = load_dataset(args.input)
    validate_dataset(df)

    processed = basic_cleaning(df)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    processed.to_csv(output_path, index=False)

    summary = pd.DataFrame(
        {
            "metric": [
                "input_rows",
                "input_columns",
                "processed_rows",
                "processed_columns",
                "duplicates_removed",
                "missing_target_rows_removed",
            ],
            "value": [
                df.shape[0],
                df.shape[1],
                processed.shape[0],
                processed.shape[1],
                df.shape[0] - df.drop_duplicates().shape[0],
                df[TARGET_COLUMN].isna().sum() if "TARGET_RISK" in df.columns else 0,
            ],
        }
    )

    summary_path = output_path.parent / "preprocessing_summary.csv"
    summary.to_csv(summary_path, index=False)

    print(f"Processed dataset saved to: {output_path}")
    print(f"Preprocessing summary saved to: {summary_path}")


if __name__ == "__main__":
    TARGET_COLUMN = "TARGET_RISK"
    main()
