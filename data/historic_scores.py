from __future__ import annotations

from collections.abc import Iterable

import nfl_data_py as nfl


def load_historic_scores(seasons: Iterable[int]):
    """Load historical NFL schedules and scores for the requested seasons."""
    requested_seasons = sorted({int(season) for season in seasons})
    if not requested_seasons:
        raise ValueError("seasons must include at least one year")

    columns = ["game_id", "season", "week", "gameday", "home_team", "away_team", "home_score", "away_score"]
    schedules = nfl.import_schedules(requested_seasons)
    missing_columns = [column for column in columns if column not in schedules.columns]
    if missing_columns:
        raise ValueError(f"nfl_data_py response missing expected columns: {missing_columns}")

    schedules = schedules.dropna(subset=["home_score", "away_score"])
    return schedules[columns]
