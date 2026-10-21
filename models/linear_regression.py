from __future__ import annotations

import pandas as pd
from sklearn.linear_model import LinearRegression
from .game_design import prepare_game_design_matrix


def build_linear_regression_model(scores_df: pd.DataFrame) -> LinearRegression:
    """Train a simple linear model to predict home score margin."""
    design_matrix, response, team_index = prepare_game_design_matrix(scores_df)
   
    # Starter baseline: use week as a minimal example feature.
    target = response["home_score"] - response["away_score"]

    model = LinearRegression()
    model.fit(design_matrix, target)
    return model
