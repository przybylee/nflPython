from __future__ import annotations

import pandas as pd


def prepare_week_feature_frame(scores_df):
    """Prepare a numeric week feature baseline from scores data."""
    training = scores_df.dropna(subset=["home_score", "away_score"])
    training = training.assign(week_numeric=pd.to_numeric(training["week"], errors="coerce")).dropna(subset=["week_numeric"])
    if training.empty:
        raise ValueError("scores_df must include at least one row with numeric week and score values")

    return training, training[["week_numeric"]]
