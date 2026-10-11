from __future__ import annotations

import pandas as pd


def prepare_week_feature_frame(scores_df):
    """Prepare filtered training rows and baseline features from scores data.

    Callers should build targets from the returned training frame to keep row alignment.
    """
    training = scores_df.dropna(subset=["home_score", "away_score"])
    training = training.assign(week_numeric=pd.to_numeric(training["week"], errors="coerce"))
    training = training.dropna(subset=["week_numeric"])
    if training.empty:
        raise ValueError("scores_df must include at least one row with numeric week and score values")

    training = training.reset_index(drop=True)
    return training, training[["week_numeric"]]
