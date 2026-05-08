"""
Utility functions for the ECOTEC_Online Student Risk Dataset.

These functions provide reusable loading, validation, feature preparation,
train-test splitting, metric computation, and output helpers for benchmark
experiments.
"""

from __future__ import annotations

from pathlib import Path
from typing import Dict, Tuple

import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score, classification_report
from sklearn.model_selection import train_test_split


TARGET_COLUMN = "TARGET_RISK"
ID_COLUMNS = ["PUBLIC_RECORD_ID"]

REQUIRED_COLUMNS = [
    "PUBLIC_RECORD_ID",
    "FACULTY",
    "DEGREE_PROGRAM",
    "CURRICULUM_YEAR",
    "GENDER",
    "AGE",
    "MARITAL_STATUS",
    "ETHNICITY",
    "DISABILITY",
    "INSTITUTION_TYPE",
    "NATIONALITY_COUNTRY",
    "TRANSFER_STUDENT_FLAG",
    "PAYMENT_PLAN",
    "ONLINE_ADMISSION_TYPE",
    "PAYMENT_DEFERRAL_TYPE",
    "SCHOLARSHIP_NAME",
    "TARGET_RISK",
    "REGION",
]


def load_dataset(path: str | Path) -> pd.DataFrame:
    """Load the dataset from a CSV file."""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Dataset file not found: {path}")

    df = pd.read_csv(path)
    return df


def validate_dataset(df: pd.DataFrame) -> None:
    """Validate that the expected columns exist in the dataset."""
    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        raise ValueError(f"The dataset is missing required columns: {missing}")

    if TARGET_COLUMN not in df.columns:
        raise ValueError(f"Target column '{TARGET_COLUMN}' not found.")

    unique_targets = sorted(df[TARGET_COLUMN].dropna().unique().tolist())
    if not set(unique_targets).issubset({0, 1}):
        raise ValueError(
            f"Target column '{TARGET_COLUMN}' must be binary with values 0 and 1. "
            f"Found: {unique_targets}"
        )


def basic_cleaning(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply minimal reproducible cleaning.

    The dataset is expected to be already anonymized. This function removes
    duplicate records, standardizes column names, and keeps only rows with
    non-missing target values.
    """
    df = df.copy()
    df.columns = [str(col).strip().upper() for col in df.columns]
    df = df.drop_duplicates()
    df = df.dropna(subset=[TARGET_COLUMN])
    df[TARGET_COLUMN] = df[TARGET_COLUMN].astype(int)
    return df


def prepare_features(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.Series]:
    """Separate features and target."""
    feature_drop = [TARGET_COLUMN] + [col for col in ID_COLUMNS if col in df.columns]
    X = df.drop(columns=feature_drop)
    y = df[TARGET_COLUMN].astype(int)
    return X, y


def split_dataset(
    X: pd.DataFrame,
    y: pd.Series,
    test_size: float = 0.30,
    random_state: int = 42,
):
    """Create a stratified train-test split."""
    return train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=y,
    )


def compute_binary_classification_metrics(y_true, y_pred, y_prob) -> Dict[str, float]:
    """Compute standard binary classification benchmark metrics."""
    metrics = {
        "accuracy": accuracy_score(y_true, y_pred),
        "f1_score": f1_score(y_true, y_pred),
        "roc_auc": roc_auc_score(y_true, y_prob),
    }
    return metrics


def save_metrics(metrics: Dict[str, float], output_path: str | Path) -> None:
    """Save metrics dictionary as a CSV file."""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame([metrics]).to_csv(output_path, index=False)


def save_classification_report(y_true, y_pred, output_path: str | Path) -> None:
    """Save the classification report as a text file."""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    report = classification_report(y_true, y_pred)
    output_path.write_text(report, encoding="utf-8")
