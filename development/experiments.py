# Experiments

from data.historic_scores import load_historic_scores
from models.logistic_regression import build_logistic_regression_model
from models.features import prepare_week_feature_frame

scores = load_historic_scores([2021, 2022, 2023])
model = build_logistic_regression_model(scores)

print(model)

prepare_week_feature_frame(scores)
