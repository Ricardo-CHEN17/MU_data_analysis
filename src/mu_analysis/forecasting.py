from __future__ import annotations

import numpy as np
import pandas as pd


def forecast_next_season_win_rate(season_stats: pd.DataFrame) -> dict[str, float]:
    """Fit a linear trend on win rate and forecast the next season."""
    x = season_stats["Start_Year"].to_numpy()
    y = season_stats["WinRate"].mul(100).to_numpy()

    slope, intercept = np.polyfit(x, y, 1)
    next_year = int(x.max() + 1)
    predicted = float((slope * next_year) + intercept)

    return {
        "slope": float(slope),
        "intercept": float(intercept),
        "next_year": float(next_year),
        "predicted_win_rate": predicted,
    }
