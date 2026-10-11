from __future__ import annotations

from collections.abc import Iterable


def load_historic_scores(seasons: Iterable[int]):
    """Load historical NFL schedules and scores for the requested seasons."""
    requested_seasons = sorted({int(season) for season in seasons})
    if not requested_seasons:
        raise ValueError("seasons must include at least one year")

    import nfl_data_py as nfl

    schedules = nfl.import_schedules(requested_seasons)
    schedules = schedules.dropna(subset=["home_score", "away_score"])
    columns = ["game_id", "season", "week", "gameday", "home_team", "away_team", "home_score", "away_score"]
    return schedules[columns]
