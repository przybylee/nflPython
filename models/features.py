from __future__ import annotations

import pandas as pd


def prepare_week_feature_frame(scores_df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Prepare filtered training rows and baseline features from scores data.

    Returns:
        A tuple of (training, features) where both frames are row-aligned and
        `features` contains the single numeric `week_numeric` baseline feature.

    Callers should build targets from the returned training frame to keep row alignment.
    """
    required_columns = {"week", "home_score", "away_score"}
    missing_columns = required_columns.difference(scores_df.columns)
    if missing_columns:
        raise ValueError(f"scores_df is missing required columns: {sorted(missing_columns)}")

    training = scores_df.dropna(subset=["home_score", "away_score"])
    if training.empty:
        raise ValueError("scores_df must include at least one row with non-null home_score and away_score values")

    training = training.assign(week_numeric=pd.to_numeric(training["week"], errors="coerce"))
    training = training.dropna(subset=["week_numeric"])
    if training.empty:
        raise ValueError("scores_df must include at least one row with a numeric week value")

    training = training.reset_index(drop=True)
    return training, training[["week_numeric"]]
