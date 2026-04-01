from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd


def plot_season_trends(season_stats: pd.DataFrame) -> None:
    """Plot total points and average goals per match by season."""
    fig, axes = plt.subplots(2, 1, figsize=(14, 10))
    ax1, ax2 = axes

    ax1.plot(
        season_stats["Season"],
        season_stats["Total_points"],
        marker="o",
        linewidth=2,
        color="red",
        markersize=6,
        markerfacecolor="white",
        markeredgecolor="red",
        markeredgewidth=1.5,
    )
    ax1.set_title("Manchester United: Total Points per Season", fontsize=16, fontweight="bold", pad=20)
    ax1.set_xlabel("Season", fontsize=14, labelpad=10)
    ax1.set_ylabel("Total Points", fontsize=14, labelpad=10)
    ax1.grid(True, alpha=0.3, linestyle="--", linewidth=0.5)

    max_point = season_stats.loc[season_stats["Total_points"].idxmax()]
    min_point = season_stats.loc[season_stats["Total_points"].idxmin()]
    ax1.annotate(
        f"Max: {max_point['Total_points']} pts",
        xy=(max_point["Season"], max_point["Total_points"]),
        xytext=(10, 10),
        textcoords="offset points",
        arrowprops={"arrowstyle": "->", "color": "darkred"},
        fontsize=10,
        color="darkred",
    )
    ax1.annotate(
        f"Min: {min_point['Total_points']} pts",
        xy=(min_point["Season"], min_point["Total_points"]),
        xytext=(10, -15),
        textcoords="offset points",
        arrowprops={"arrowstyle": "->", "color": "darkgreen"},
        fontsize=10,
        color="darkgreen",
    )

    ax2.plot(
        season_stats["Season"],
        season_stats["Avg_Goals_Per_Match"],
        marker="s",
        linewidth=2,
        color="blue",
        markersize=6,
        markerfacecolor="white",
        markeredgecolor="blue",
        markeredgewidth=1.5,
    )
    ax2.set_title(
        "Manchester United: Average Goals per Match per Season",
        fontsize=16,
        fontweight="bold",
        pad=20,
    )
    ax2.set_xlabel("Season", fontsize=13, labelpad=10)
    ax2.set_ylabel("Average Goals", fontsize=13, labelpad=10)
    ax2.grid(True, alpha=0.3, linestyle="--", linewidth=0.5)

    avg_goals_mean = season_stats["Avg_Goals_Per_Match"].mean()
    ax2.axhline(y=avg_goals_mean, linewidth=1.5, color="gray", linestyle=":", alpha=0.7)
    ax2.text(
        len(season_stats["Season"]) - 1,
        avg_goals_mean + 0.02,
        f"Mean: {avg_goals_mean:.2f}",
        fontsize=10,
        color="gray",
        ha="right",
    )

    for axis in (ax1, ax2):
        labels = season_stats["Season"].tolist()
        positions = range(len(labels))
        axis.set_xticks(list(positions))
        reduced_labels = [label if i % 5 == 0 else "" for i, label in enumerate(labels)]
        axis.set_xticklabels(reduced_labels, rotation=45, ha="right", fontsize=10)

    fig.suptitle("Manchester United Performance Analysis by Season", fontsize=18, fontweight="bold", y=0.98)
    plt.subplots_adjust(hspace=0.5)
    plt.show()


def plot_home_away_win_rates(win_rates: pd.Series) -> None:
    """Plot bar chart for home vs away win rates."""
    ordered = win_rates.reindex(["Away", "Home"])

    plt.figure(figsize=(8, 5))
    bars = plt.bar(ordered.index, ordered.values, color=["#FF9999", "#CC0000"], width=0.5)
    plt.title("Manchester United Win Rate: Home vs Away", fontsize=14, fontweight="bold")
    plt.xlabel("Match Venue", fontsize=12)
    plt.ylabel("Win Rate (%)", fontsize=12)
    plt.ylim(0, 100)

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + (bar.get_width() / 2), yval + 2, f"{yval:.2f}%", ha="center", fontsize=11)

    plt.show()


def plot_win_rate_forecast(season_stats: pd.DataFrame, slope: float, intercept: float, next_year: int, predicted: float) -> None:
    """Plot historical win rates and linear forecast point."""
    x = season_stats["Start_Year"]
    y = season_stats["WinRate"].mul(100)

    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color="blue", label="Actual Win Rate per Season", alpha=0.6)

    regression_line = (slope * x) + intercept
    plt.plot(x, regression_line, color="red", linewidth=2, label="Linear Trend Line")

    plt.scatter(
        next_year,
        predicted,
        color="gold",
        s=150,
        edgecolors="black",
        label=f"Prediction ({next_year}: {predicted:.2f}%)",
        zorder=5,
    )

    plt.title("Manchester United Win Rate Trend and Prediction", fontsize=15, fontweight="bold")
    plt.xlabel("Starting Year of Season", fontsize=12)
    plt.ylabel("Win Rate (%)", fontsize=12)
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.show()
