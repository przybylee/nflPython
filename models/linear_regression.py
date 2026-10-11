from __future__ import annotations

from sklearn.linear_model import LinearRegression


def build_linear_regression_model(scores_df):
    """Train a simple linear model to predict home score margin."""
    training = scores_df.dropna(subset=["home_score", "away_score"])
    # Starter baseline: use week as a minimal example feature.
    features = training[["week"]]
    target = training["home_score"] - training["away_score"]

    model = LinearRegression()
    model.fit(features, target)
    return model
