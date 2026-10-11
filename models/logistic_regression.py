from __future__ import annotations

from sklearn.linear_model import LogisticRegression
from .features import prepare_week_feature_frame


def build_logistic_regression_model(scores_df):
    """Train a simple logistic model to predict home-team wins."""
    training, features = prepare_week_feature_frame(scores_df)
    # Starter baseline: use week as a minimal example feature.
    target = (training["home_score"] > training["away_score"]).astype(int)

    model = LogisticRegression(max_iter=1000)
    model.fit(features, target)
    return model
