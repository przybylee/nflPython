from __future__ import annotations

import pandas as pd
from sklearn.linear_model import LinearRegression


def build_linear_regression_model(scores_df):
    """Train a simple linear model to predict home score margin."""
    training = scores_df.dropna(subset=["home_score", "away_score"])
    training = training.assign(week_numeric=pd.to_numeric(training["week"], errors="coerce")).dropna(subset=["week_numeric"])
    if training.empty:
        raise ValueError("scores_df must include at least one row with numeric week and score values")

    # Starter baseline: use week as a minimal example feature.
    features = training[["week_numeric"]]
    target = training["home_score"] - training["away_score"]

    model = LinearRegression()
    model.fit(features, target)
    return model
