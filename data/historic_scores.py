from __future__ import annotations

from collections.abc import Iterable

import nfl_data_py as nfl
import pandas as pd

SCORE_COLUMNS = ["game_id", "season", "week", "gameday", "home_team", "away_team", "home_score", "away_score"]


def load_historic_scores(seasons: Iterable[int]) -> pd.DataFrame:
    """Load historical NFL schedules and scores for the requested seasons.

    Returns a DataFrame with game metadata and final score columns.
    """
    requested_seasons = sorted({int(season) for season in seasons})
    if not requested_seasons:
        raise ValueError("seasons must include at least one year")

    schedules = nfl.import_schedules(requested_seasons)
    missing_columns = [column for column in SCORE_COLUMNS if column not in schedules.columns]
    if missing_columns:
        raise ValueError(f"nfl_data_py response missing expected columns: {missing_columns}")

    schedules = schedules.dropna(subset=["home_score", "away_score"])
    if schedules.empty:
        raise ValueError("No completed games with final scores were found for the requested seasons")

    return schedules[SCORE_COLUMNS]
