from __future__ import annotations

import pandas as pd

RESULT_TO_POINTS = {"H": 3, "D": 1, "A": 0}


def _season_from_date(value: pd.Timestamp) -> str:
    year = value.year
    if value.month >= 8:
        return f"{year}/{str(year + 1)[2:]}"
    return f"{year - 1}/{str(year)[2:]}"


def add_points_and_season(team_matches: pd.DataFrame) -> pd.DataFrame:
    """Add points and season labels to team-level match records."""
    df = team_matches.copy()
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df["points"] = df["Team_Result"].map(RESULT_TO_POINTS)
    df["Season"] = df["Date"].apply(_season_from_date)
    return df


def build_season_stats(team_matches: pd.DataFrame) -> pd.DataFrame:
    """Aggregate season-level metrics."""
    season_stats = (
        team_matches.groupby("Season")
        .agg(
            Total_points=("points", "sum"),
            Total_Goals=("Team_Goals", "sum"),
            Matches=("Team_Goals", "count"),
            WinRate=("Win", "mean"),
        )
        .reset_index()
    )

    season_stats["Avg_Goals_Per_Match"] = season_stats["Total_Goals"] / season_stats["Matches"]

    season_stats["Start_Year"] = season_stats["Season"].str[:4].astype(int)
    season_stats = season_stats.sort_values("Start_Year").reset_index(drop=True)
    return season_stats


def compute_home_away_win_rates(team_matches: pd.DataFrame) -> pd.Series:
    """Return home and away win rates in percent."""
    return team_matches.groupby("Venue")["Win"].mean().mul(100).sort_index()
