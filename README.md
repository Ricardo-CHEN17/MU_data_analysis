# MU Data Analysis

This project analyzes Manchester United's historical match performance in English league football and builds a simple win-rate forecast.

The core analysis is implemented in a Jupyter Notebook and covers:
- Data cleaning and filtering (focus period: 1986 onward)
- Season-level performance metrics (points, goals, win rate)
- Home vs away result interpretation
- Trend visualization with Matplotlib
- Linear trend-based prediction for the 2022/2023 season

## Project Files

- `PL_data.ipynb`: Main notebook with data processing, visual analysis, and forecasting logic.
- `main.py`: Script entry point that runs the full analysis pipeline.
- `src/mu_analysis/`: Reusable Python package for data processing, analysis, plotting, and forecasting.
- `england.csv`: Historical English football match dataset used as the data source.
- `MU_data_analysis.html`: Exported HTML version of the notebook for quick viewing.
- `README.md`: Project documentation.

## Project Structure

```text
MU_data_analysis/
├── england.csv
├── main.py
├── PL_data.ipynb
├── MU_data_analysis.html
├── README.md
└── src/
	└── mu_analysis/
		├── __init__.py
		├── data_processing.py
		├── analysis.py
		├── forecasting.py
		└── visualization.py
```

## Data Source

The dataset includes match-level records such as:
- `Date`, `Season`
- `home`, `visitor`
- `hgoal`, `vgoal`
- `result` (`H`, `D`, `A`)

The notebook derives Manchester United-specific features from these fields (for example, goals scored and result from the club's perspective in both home and away matches).

## Analysis Workflow

1. Load and parse `england.csv`.
2. Filter records to matches involving Manchester United from 1986 onward.
3. Convert match outcomes to points and aggregate by season.
4. Visualize total points and average goals per match across seasons.
5. Estimate a linear trend for historical win rate and project the next season.

## Requirements

Python 3.9+ is recommended.

Install dependencies:

```bash
pip install pandas numpy matplotlib jupyter
```

## How to Run

### Option 1: Run the modular Python script

```bash
python main.py
```

This command will:
- Load and clean raw match data.
- Build Manchester United match-level features.
- Generate season-level metrics and win-rate forecast.
- Render all visualizations.

### Option 2: Run the notebook

1. Open the project folder in VS Code or Jupyter.
2. Launch `PL_data.ipynb`.
3. Run all cells from top to bottom.
4. Review generated charts and the printed prediction output.

If you only want to view results without running code, open `MU_data_analysis.html` in a browser.

## Notes

- The forecast is a simple linear trend estimate and is intended for educational analysis.
- Results may vary if preprocessing logic or filtering windows are changed.