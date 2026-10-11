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
└── requirements.txt
```

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows (PowerShell), use:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Example usage:

```python
from data.historic_scores import load_historic_scores
from models.logistic_regression import build_logistic_regression_model

scores = load_historic_scores([2021, 2022, 2023])
model = build_logistic_regression_model(scores)
```

## Next steps

- Add feature engineering (rest days, travel, injuries, Elo, etc.).
- Add train/test splits by season or week.
- Add tests for data loading and model behavior.
