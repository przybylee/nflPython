# nflPython

`nflPython` is a starter repository for building NFL game winner prediction workflows in Python.

## What this skeleton includes

- A `data/` module with a helper that uses [`nfl_data_py`](https://pypi.org/project/nfl-data-py/) to load historical NFL scores.
- A `models/` directory with simple regression model helpers for winner prediction experiments.

## Project layout

```text
nflPython/
├── data/
│   ├── __init__.py
│   └── historic_scores.py
├── models/
│   ├── __init__.py
│   ├── features.py
│   ├── linear_regression.py
│   └── logistic_regression.py
|── pyproject.toml
|__ uv.lock
```

## Quick start

This is a [`uv`](https://docs.astral.sh/uv/getting-started/installation/) project.  Folow the link to install, then sycrhronize the project environment with 

```bash
uv sync
```

That creates a local `.venv` volder and installs the dependencies recorded in `uv.lock`.  You do not need to activate the virtual environment when using `uv.run`.  

Start a Python session inside the project environment:

```bash
uv run python
```

Example usage (run from the repository root):

```python
from data.historic_scores import load_historic_scores
from models.logistic_regression import build_logistic_regression_model

scores = load_historic_scores([2021, 2022, 2023])
model = build_logistic_regression_model(scores)
```

Other coammands can be run in the same environment by prefixing them with `uv run`, for example:

```bash
uv run pytest
```

## Next steps

- Add feature engineering (rest days, travel, injuries, Elo, etc.).
- Add train/test splits by season or week.
- Add tests for data loading and model behavior.
