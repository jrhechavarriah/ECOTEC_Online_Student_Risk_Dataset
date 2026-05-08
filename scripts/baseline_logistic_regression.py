"""
Logistic Regression benchmark for the ECOTEC_Online Student Risk Dataset.

This script provides a simple linear baseline for educational data mining
and student risk prediction.

Example:
    python scripts/baseline_logistic_regression.py \
        --input derived_data/ecotec_online_student_risk_processed.csv \
        --output-dir results/logistic_regression
"""

from __future__ import annotations

import argparse

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

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
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Logistic Regression benchmark.")
    parser.add_argument(
        "--input",
        type=str,
        default="derived_data/ecotec_online_student_risk_processed.csv",
        help="Path to processed CSV file.",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="results/logistic_regression",
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
                ("scaler", StandardScaler()),
            ]), numeric_features),
        ]
    )

    model = Pipeline(
        steps=[
            ("preprocess", preprocessor),
            ("classifier", LogisticRegression(
                max_iter=1000,
                random_state=args.seed,
                class_weight="balanced",
            )),
        ]
    )

    X_train, X_test, y_train, y_test = split_dataset(X, y, random_state=args.seed)

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    metrics = compute_binary_classification_metrics(y_test, y_pred, y_prob)
    metrics["model"] = "LogisticRegression"
    metrics["n_train"] = len(y_train)
    metrics["n_test"] = len(y_test)

    save_metrics(metrics, output_dir / "metrics.csv")
    save_classification_report(y_test, y_pred, output_dir / "classification_report.txt")

    print("Logistic Regression benchmark completed.")
    print(metrics)


if __name__ == "__main__":
    main()
