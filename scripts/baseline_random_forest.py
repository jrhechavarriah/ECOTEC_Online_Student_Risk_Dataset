"""
Random Forest benchmark for the ECOTEC_Online Student Risk Dataset.

This script provides a simple reproducible baseline for educational data mining
and student risk prediction.

Example:
    python scripts/baseline_random_forest.py \
        --input data/ecotec_online_student_risk.csv \
        --output-dir results/random_forest
"""

from __future__ import annotations

import argparse

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

import sys
from pathlib import Path

CURRENT_DIR = Path(__file__).resolve().parent
sys.path.append(str(CURRENT_DIR))

from utils import (
    load_dataset,
    validate_dataset,
    basic_cleaning,
    prepare_features,
    split_dataset,
    compute_binary_classification_metrics,
    save_metrics,
    save_classification_report,
    save_confusion_matrix,
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Random Forest benchmark.")
    parser.add_argument(
        "--input",
        type=str,
        default="data/ecotec_online_student_risk.csv",
        help="Path to the finalized anonymized public CSV file.",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="results/random_forest",
        help="Directory to save benchmark outputs.",
    )
    parser.add_argument("--seed", type=int, default=42, help="Random seed.")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    df = load_dataset(args.input)
    validate_dataset(df)
    df = basic_cleaning(df)

    X, y = prepare_features(df)

    categorical_features = X.select_dtypes(include=["object", "category"]).columns.tolist()
    numeric_features = X.select_dtypes(exclude=["object", "category"]).columns.tolist()

    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", Pipeline(steps=[
                ("imputer", SimpleImputer(strategy="most_frequent")),
                ("encoder", OneHotEncoder(handle_unknown="ignore")),
            ]), categorical_features),
            ("num", Pipeline(steps=[
                ("imputer", SimpleImputer(strategy="median")),
            ]), numeric_features),
        ]
    )

    model = Pipeline(
        steps=[
            ("preprocess", preprocessor),
            ("classifier", RandomForestClassifier(
                n_estimators=300,
                random_state=args.seed,
                class_weight="balanced",
                n_jobs=-1,
            )),
        ]
    )

    X_train, X_test, y_train, y_test = split_dataset(X, y, random_state=args.seed)

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    metrics = compute_binary_classification_metrics(y_test, y_pred, y_prob)
    metrics["model"] = "RandomForestClassifier"
    metrics["n_train"] = len(y_train)
    metrics["n_test"] = len(y_test)

    save_metrics(metrics, output_dir / "metrics.csv")
    save_classification_report(y_test, y_pred, output_dir / "classification_report.txt")
    save_confusion_matrix(y_test, y_pred, output_dir / "confusion_matrix.csv")

    print("Random Forest benchmark completed.")
    print(metrics)


if __name__ == "__main__":
    main()
