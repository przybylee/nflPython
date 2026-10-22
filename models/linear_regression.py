from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from .game_design import prepare_game_design_matrix


def build_linear_regression_model(scores_df: pd.DataFrame) -> LinearRegression:
    """Train a simple linear model to predict home score margin."""
    design_matrix, response, team_index = prepare_game_design_matrix(scores_df)
   
    # Starter baseline: use week as a minimal example feature.
    target = response["home_score"] - response["away_score"]

    model = LinearRegression(fit_intercept=False)
    model.fit(design_matrix, target)
    
    # Calculate residuals, std dev
    model.residuals = target - model.predict(design_matrix)
    model.rank = np.linalg.matrix_rank(design_matrix.to_numpy())
    sum_sq_error = np.sum(model.residuals**2)
    model.deg_freedom = len(model.residuals) - model.rank
    model.sd = np.sqrt(sum_sq_error/model.deg_freedom)       
    
    return model
