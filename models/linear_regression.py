from __future__ import annotations

from sklearn.linear_model import LinearRegression
from .features import prepare_week_feature_frame


def build_linear_regression_model(scores_df):
    """Train a simple linear model to predict home score margin."""
    training, features = prepare_week_feature_frame(scores_df)
    # Starter baseline: use week as a minimal example feature.
    target = training["home_score"] - training["away_score"]

    model = LinearRegression()
    model.fit(features, target)
    return model
