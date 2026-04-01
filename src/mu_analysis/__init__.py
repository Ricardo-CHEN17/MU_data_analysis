"""Manchester United data analysis package."""

from .data_processing import load_matches, build_team_matches
from .analysis import (
    add_points_and_season,
    build_season_stats,
    compute_home_away_win_rates,
)
from .forecasting import forecast_next_season_win_rate
from .visualization import (
    plot_season_trends,
    plot_home_away_win_rates,
    plot_win_rate_forecast,
)

__all__ = [
    "load_matches",
    "build_team_matches",
    "add_points_and_season",
    "build_season_stats",
    "compute_home_away_win_rates",
    "forecast_next_season_win_rate",
    "plot_season_trends",
    "plot_home_away_win_rates",
    "plot_win_rate_forecast",
]
