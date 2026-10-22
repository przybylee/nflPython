from __future__ import annotations
from sklearn.linear_model import LinearRegression
from .game_design import prepare_game_design_matrix

import numpy as np
import pandas as pd

def build_linear_regression_model(scores_df: pd.DataFrame) -> LinearRegression:
    """Train a simple linear model to predict home score margin."""
    design_matrix, response, team_index = prepare_game_design_matrix(scores_df)

    target = response["home_score"] - response["away_score"]

    # Attach a row to sum team effects to impose league average at 0
    team_columns = [f"team_{team}" for team in team_index]

    constraint_name = "team_avg0"
    constraint_row = pd.DataFrame(
        0.0, 
        index = [constraint_name], 
        columns = design_matrix.columns,
        )

    constraint_row.loc[constraint_name, team_columns,] = 1.0

    constraint_target = pd.Series(
        [0.0], 
        index = [constraint_name], 
        name = target.name,
        )

    constrained_design = pd.concat([design_matrix, constraint_row],)

    constrained_target = pd.concat([target, constraint_target],)

   
    model = LinearRegression(fit_intercept=False)
    model.fit(constrained_design, constrained_target)
    
    # Calculate residuals, std dev
    # follow sklearn conventions and use underscore for estimates
    fitted = pd.Series(
      model.predict(design_matrix), 
      index = target.index,
      name="predicted_margin"
      )
    model.residuals_ = target - fitted

    model.sse_ = float(np.sum(model.residuals_**2))
    model.deg_freedom_ = len(constrained_target) - model.rank_
    model.sd_ = np.sqrt(model.sse_/model.deg_freedom_)       
    
    return model
