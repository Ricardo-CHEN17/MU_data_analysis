from __future__ import annotations

from pathlib import Path

import pandas as pd


def load_matches(csv_path: str | Path) -> pd.DataFrame:
    """Load raw match data and parse date columns."""
    df = pd.read_csv(csv_path, low_memory=False)
    df["date"] = pd.to_datetime(df["Date"], errors="coerce")
    return df


def _goals_for_team(row: pd.Series, team_name: str) -> int:
    return row["hgoal"] if row["home"] == team_name else row["vgoal"]


def _result_for_team(row: pd.Series, team_name: str) -> str:
    if row["home"] == team_name:
        return row["result"]
    return {"A": "H", "H": "A", "D": "D"}.get(row["result"], row["result"])


def build_team_matches(
    df: pd.DataFrame,
    team_name: str = "Manchester United",
    start_date: str = "1986-08-01",
) -> pd.DataFrame:
    """Filter matches for a team since start_date and derive team-centric columns."""
    filtered = df[df["date"] >= pd.to_datetime(start_date)].copy()

    team_home = filtered[filtered["home"] == team_name]
    team_away = filtered[filtered["visitor"] == team_name]
    team_matches = pd.concat([team_home, team_away], ignore_index=True).copy()

    team_matches["Team_Goals"] = team_matches.apply(_goals_for_team, axis=1, team_name=team_name)
    team_matches["Team_Result"] = team_matches.apply(_result_for_team, axis=1, team_name=team_name)
    team_matches["Venue"] = team_matches["home"].eq(team_name).map({True: "Home", False: "Away"})
    team_matches["Win"] = team_matches["Team_Result"].eq("H")

    return team_matches
