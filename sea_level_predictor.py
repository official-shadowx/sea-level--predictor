import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Import data
    df = pd.read_csv("epa-sea-level.csv")

    # Scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Line of best fit (all data)
    slope, intercept, _, _, _ = linregress(
        df['Year'], df['CSIRO Adjusted Sea Level']
    )

    years = pd.Series(range(1880, 2051))
    plt.plot(years, intercept + slope * years, 'r')

    # Line of best fit (from year 2000)
    df_recent = df[df['Year'] >= 2000]

    slope2, intercept2, _, _, _ = linregress(
        df_recent['Year'], df_recent['CSIRO Adjusted Sea Level']
    )

    years2 = pd.Series(range(2000, 2051))
    plt.plot(years2, intercept2 + slope2 * years2, 'g')

    # Labels
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save
    plt.savefig("sea_level_plot.png")

    return plt.gcf()