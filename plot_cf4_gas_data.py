import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# New York Knicks colors used in your other plots
KNICKS_ORANGE = "#F58426"
KNICKS_BLUE = "#1f51ba"


def main() -> None:
    csv_path = Path("cf4_data.csv")
    if not csv_path.exists():
        csv_path = Path("cf4_gasData.csv")

    # Keep initial spaces in headers from WebPlotDigitizer export, then strip them.
    df = pd.read_csv(csv_path, skipinitialspace=True)
    df.columns = [c.strip() for c in df.columns]

    data_x = df["data x"]
    data_y = df["datay"]

    mc_x = df["MC x"]
    mc_y = df["MC Y"]
    mc_err_y_top = df["mcError y"]

    mc = pd.DataFrame({"x": mc_x, "y": mc_y, "y_top": mc_err_y_top}).dropna()

    # Last column is the error-bar top in y, so convert to a y-error magnitude.
    mc_yerr = (mc["y_top"] - mc["y"]).abs()

    fig, ax = plt.subplots(figsize=(8.5, 5.5))

    ax.plot(
        data_x,
        data_y,
        marker="o",
        markersize=5,
        linestyle="-",
        linewidth=1.8,
        color=KNICKS_BLUE,
        label="Data",
    )

    ax.errorbar(
        mc["x"],
        mc["y"],
        yerr=mc_yerr,
        fmt="s",
        markersize=5,
        capsize=4,
        elinewidth=1.5,
        linewidth=1.5,
        color=KNICKS_ORANGE,
        ecolor=KNICKS_ORANGE,
        label="MC",
    )

    ax.set_xlabel("Density")
    ax.set_ylabel("NPE")
    ax.set_title("CF4 Density vs NPE")
    ax.grid(alpha=0.25)
    ax.legend(frameon=False)
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
