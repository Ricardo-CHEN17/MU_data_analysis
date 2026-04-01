from __future__ import annotations

from pathlib import Path

from src.mu_analysis.analysis import (
    add_points_and_season,
    build_season_stats,
    compute_home_away_win_rates,
)
from src.mu_analysis.data_processing import build_team_matches, load_matches
from src.mu_analysis.forecasting import forecast_next_season_win_rate
from src.mu_analysis.visualization import (
    plot_home_away_win_rates,
    plot_season_trends,
    plot_win_rate_forecast,
)


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    csv_path = base_dir / "england.csv"

    raw_df = load_matches(csv_path)
    man_utd_matches = build_team_matches(raw_df, team_name="Manchester United", start_date="1986-08-01")
    man_utd_matches = add_points_and_season(man_utd_matches)

    season_stats = build_season_stats(man_utd_matches)
    win_rates = compute_home_away_win_rates(man_utd_matches)
    forecast = forecast_next_season_win_rate(season_stats)

    print(f"Number of matches: {len(man_utd_matches)}")
    print("\nTop 3 seasons by total points:")
    for _, row in season_stats.nlargest(3, "Total_points").iterrows():
        print(f"  {row['Season']}: {row['Total_points']} points")

    print("\nTop 3 seasons by average goals per match:")
    for _, row in season_stats.nlargest(3, "Avg_Goals_Per_Match").iterrows():
        print(f"  {row['Season']}: {row['Avg_Goals_Per_Match']:.2f} goals per match")

    print("\nOverall statistics:")
    print(f"  Average points per season: {season_stats['Total_points'].mean():.1f}")
    print(f"  Average goals per match: {season_stats['Avg_Goals_Per_Match'].mean():.2f}")
    print(f"  Number of seasons analyzed: {len(season_stats)}")

    print("\nManchester United win rates:")
    print(win_rates.round(2).astype(str) + "%")

    slope = forecast["slope"]
    intercept = forecast["intercept"]
    next_year = int(forecast["next_year"])
    predicted = forecast["predicted_win_rate"]

    print(f"\nLinear Regression Equation: Win Rate = {slope:.2f} * Year + {intercept:.2f}")
    print(f"Predicted Win Rate for year {next_year}: {predicted:.2f}%")

    plot_season_trends(season_stats)
    plot_home_away_win_rates(win_rates)
    plot_win_rate_forecast(season_stats, slope=slope, intercept=intercept, next_year=next_year, predicted=predicted)


if __name__ == "__main__":
    main()
