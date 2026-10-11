from __future__ import annotations


def build_logistic_regression_model(scores_df):
    """Train a simple logistic model to predict home-team wins."""
    from sklearn.linear_model import LogisticRegression

    training = scores_df.dropna(subset=["home_score", "away_score"])
    # Starter baseline: use week as a minimal example feature.
    features = training[["week"]]
    target = (training["home_score"] > training["away_score"]).astype(int)

    model = LogisticRegression(max_iter=1000)
    model.fit(features, target)
    return model
