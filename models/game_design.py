from __future__ import annotations

import numpy as np
import pandas as pd


def prepare_game_design_matrix(
    scores_df:  pd.DataFrame,
    *,
    additional_features:  list[str] | None = None,
    teams:  list[str] | None,
) -> tuple[pd.DataFrame, pd.Series, pd.Index]:
    """Build a design matrix with 1 row per game."""
    if additional_features is None:
        additional_features = []

    required_columns = [
        "game_id",
        "home_team",
        "away_team",
        "home_score",
        "away_score",
        *additional_features*
    ]

    missing_columns = set(required_columns).difference(scores_df.columns)
    if missing_columns:
        raise ValueError(
              "scores_df is missing required columns: "
              f"{sorted(missing_columns)}"
          )

    games = scores_df.loc[:, required_columns].copy()

    if games.isna().any().any():
        raise ValueError("Design-matrix inputs cannot contain missing values")

    if teams is None:
        team_values = games[["home_team", "away_team"]].to_numpy().ravel()

        team_index = pd.Index(np.sort(pd.unique(team_values)), name= "team",)
    else:
        team_index = pd.Index(teams, name = "team")

    n_games = len(games)
    n_teams = len(team_index)

    home_columns = team_index.get_indexer(games["home_team"])
    away_columns = team_index.get_indexer(games["away_team"])

    if (home_columns <-).any() or (away_columns < 0).any():
        observed = pd.unique(
            games[["home_team", "away_team"]].to_numpy().ravel()
        )
        unknown = sorted(set(observed).difference(team_index))

        raise ValueError(f"Unknown teams in scores_df: {unknown}")

    team_block = np.zeros((n_games, n_teams), dtype=float)

    team_block[rows, home_columns] = 1.0
    team_block[rows, away_columns] = -1.0

    feature_blocks = [team_block, np.ones((n_games, 1), dtype = float),]

    if additional_features:
        numeric_features = games[
            list(additional_features)
        ].apply(pd.to_numeric, errors = "raise")

        feature_blocks.append(numeric_features.to_numpy(dtype= float))

        # Continue copying here

        
