# Experiments

from data.historic_scores import load_historic_scores
from models.logistic_regression import build_logistic_regression_model
from models.linear_regression import build_linear_regression_model
from models.features import prepare_week_feature_frame
from models.game_design import prepare_game_design_matrix

import pandas as pd

scores_df = load_historic_scores([2026])
# Need to add home field site
scores_df.head

## Making the game design list
design_matrix, response, team_index = prepare_game_design_matrix(scores_df)

# Still fit using a week effect
model = build_logistic_regression_model(scores_df)
model.coef_

print(model)

model_linear = build_linear_regression_model(scores_df)

print(model_linear)
model_linear.coef_

# Names of all the features
model_linear.feature_names_in_

# rank
model_linear.rank_

# standard deviation
model_linear.sd_ 
model_linear.residuals_
model_linear.deg_freedom_ 

# Print a table of the estimates and their names
coefficient_table = (
    pd.DataFrame(
        {
            "feature": model_linear.feature_names_in_,
            "coefficient": model_linear.coef_,
        }
        )
        .sort_values(by="coefficient", ascending=False) 
        #.reset_index(drop = True)
    )

coefficient_table[coefficient_table["feature"].str.startswith("team_")]

coefficient_table["coefficient"].sum()
