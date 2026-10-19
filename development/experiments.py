# Experiments

from data.historic_scores import load_historic_scores
from models.logistic_regression import build_logistic_regression_model
from models.features import prepare_week_feature_frame
from models.game_design import prepare_game_design_matrix

scores_df = load_historic_scores([2025])
# Need to add home field site
scores_df.head

## Making the game design list
design = prepare_game_design_matrix(scores_df)


model = build_logistic_regression_model(scores)

print(model)

prepare_week_feature_frame(scores)
