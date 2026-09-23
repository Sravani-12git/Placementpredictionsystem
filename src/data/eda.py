# ============================================================
# EXPLORATORY DATA ANALYSIS (EDA)
# Placement Prediction System
# ============================================================

from pathlib import Path

from src.data.load_data import load_data

import matplotlib.pyplot as plt
import seaborn as sns


# ============================================================
# PATH CONFIGURATION
# ============================================================

# eda.py is inside:
# Placementpredictionsystem/src/data/eda.py
#
# parents[0] = data
# parents[1] = src
# parents[2] = Placementpredictionsystem

PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Folder where all EDA graphs will be stored
RESULTS_DIR = PROJECT_ROOT / "app" / "static" / "charts" / "results"

# Create the folder automatically if it doesn't exist
RESULTS_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================
# BASIC EDA
# ============================================================

def basic_eda(df):

    print("\n" + "=" * 60)
    print("BASIC EDA")
    print("=" * 60)

    # --------------------------------------------------------
    # First 5 rows
    # --------------------------------------------------------

    print("\nFirst 5 Rows")
    print(df.head())

    # --------------------------------------------------------
    # Last 5 rows
    # --------------------------------------------------------

    print("\nLast 5 Rows")
    print(df.tail())

    # --------------------------------------------------------
    # Rows 25 to 35
    # --------------------------------------------------------

    print("\nRows 25 to 35")
    print(df.iloc[25:35])

    # --------------------------------------------------------
    # Column names
    # --------------------------------------------------------

    print("\nColumn Names")
    print(df.columns)

    # --------------------------------------------------------
    # Data types
    # --------------------------------------------------------

    print("\nData Types")
    print(df.dtypes)

    # --------------------------------------------------------
    # Dataset information
    # --------------------------------------------------------

    print("\nDataset Information")
    df.info()

    # --------------------------------------------------------
    # Minimum values
    # --------------------------------------------------------

    print("\nMinimum Values")

    # Only numeric columns
    numeric_df = df.select_dtypes(include="number")

    print(numeric_df.min())

    # --------------------------------------------------------
    # Maximum values
    # --------------------------------------------------------

    print("\nMaximum Values")
    print(numeric_df.max())

    # --------------------------------------------------------
    # Duplicate rows
    # --------------------------------------------------------

    print("\nDuplicate Rows")
    print(df.duplicated().sum())

    # --------------------------------------------------------
    # Null values
    # --------------------------------------------------------

    print("\nNull Values")
    print(df.isnull().sum())

    # --------------------------------------------------------
    # Placement Status Bar Chart
    # --------------------------------------------------------

    count = df["PlacementStatus"].value_counts().sort_index()

    plt.figure(figsize=(6, 5))

    plt.bar(
        count.index.astype(str),
        count.values
    )

    plt.title("Placement Status")
    plt.xlabel("Placement Status")
    plt.ylabel("Count")

    plt.tight_layout()

    plt.savefig(
        RESULTS_DIR / "placement_status_barchart.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()
    plt.close()

    print("\nPlacement status graph saved successfully.")


# ============================================================
# UNIVARIATE ANALYSIS
# ============================================================

def univariate(df):

    print("\n" + "=" * 60)
    print("UNIVARIATE ANALYSIS")
    print("=" * 60)

    # --------------------------------------------------------
    # Histogram - CGPA
    # --------------------------------------------------------

    plt.figure(figsize=(6, 5))

    plt.hist(
        df["CGPA"].dropna(),
        bins=10
    )

    plt.title("Histogram of CGPA")
    plt.xlabel("CGPA")
    plt.ylabel("Frequency")

    plt.tight_layout()

    plt.savefig(
        RESULTS_DIR / "Histogram.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()
    plt.close()

    print("CGPA histogram saved successfully.")

    # --------------------------------------------------------
    # Pie Chart - Gender
    # --------------------------------------------------------

    gender_count = df["Gender"].value_counts()

    plt.figure(figsize=(6, 5))

    plt.pie(
        gender_count,
        labels=gender_count.index,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Gender Distribution")

    plt.tight_layout()

    plt.savefig(
        RESULTS_DIR / "Pie_Chart.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()
    plt.close()

    print("Gender pie chart saved successfully.")


# ============================================================
# BIVARIATE ANALYSIS
# ============================================================

def bivariate(df):

    print("\n" + "=" * 60)
    print("BIVARIATE ANALYSIS")
    print("=" * 60)

    # --------------------------------------------------------
    # Scatter Plot
    # CGPA vs Aptitude Test Score
    # --------------------------------------------------------

    scatter_data = df[
        ["CGPA", "AptitudeTestScore"]
    ].dropna()

    plt.figure(figsize=(6, 5))

    plt.scatter(
        scatter_data["CGPA"],
        scatter_data["AptitudeTestScore"]
    )

    plt.title("CGPA vs Aptitude Test Score")
    plt.xlabel("CGPA")
    plt.ylabel("Aptitude Test Score")

    plt.tight_layout()

    plt.savefig(
        RESULTS_DIR / "scatterplot.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()
    plt.close()

    print("Scatter plot saved successfully.")

    # --------------------------------------------------------
    # Box Plot
    # CGPA vs Placement Status
    # --------------------------------------------------------

    placed = df[
        df["PlacementStatus"] == 1
    ]["CGPA"].dropna()

    not_placed = df[
        df["PlacementStatus"] == 0
    ]["CGPA"].dropna()

    plt.figure(figsize=(6, 5))

    plt.boxplot(
        [placed, not_placed],
        tick_labels=[
            "Placed",
            "Not Placed"
        ]
    )

    plt.title("CGPA vs Placement Status")
    plt.xlabel("Placement Status")
    plt.ylabel("CGPA")

    plt.tight_layout()

    plt.savefig(
        RESULTS_DIR / "boxplot.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()
    plt.close()

    print("Box plot saved successfully.")


# ============================================================
# MULTIVARIATE ANALYSIS
# ============================================================

def multivariate(df):

    print("\n" + "=" * 60)
    print("MULTIVARIATE ANALYSIS")
    print("=" * 60)

    # --------------------------------------------------------
    # Selected Feature Correlation
    # --------------------------------------------------------

    data = df[
        [
            "CGPA",
            "AptitudeTestScore",
            "PlacementStatus"
        ]
    ]

    correlation = data.corr()

    plt.figure(figsize=(6, 5))

    sns.heatmap(
        correlation,
        annot=True,
        cmap="coolwarm",
        fmt=".2f"
    )

    plt.title("Correlation Matrix")

    plt.tight_layout()

    plt.savefig(
        RESULTS_DIR / "heatmap.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()
    plt.close()

    print("Selected correlation heatmap saved successfully.")

    # --------------------------------------------------------
    # Complete Numeric Correlation Matrix
    # --------------------------------------------------------

    correlation = df.corr(
        numeric_only=True
    )

    plt.figure(figsize=(12, 9))

    sns.heatmap(
        correlation,
        annot=True,
        cmap="coolwarm",
        fmt=".2f"
    )

    plt.title("Complete Correlation Matrix")

    plt.tight_layout()

    plt.savefig(
        RESULTS_DIR / "heatmap2.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()
    plt.close()

    print("Complete correlation heatmap saved successfully.")


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    print("\nLoading dataset...")

    df = load_data()

    print("Dataset loaded successfully.")

    print("\nDataset Shape:")
    print(df.shape)

    # --------------------------------------------------------
    # Run all EDA sections
    # --------------------------------------------------------

    basic_eda(df)

    univariate(df)

    bivariate(df)

    multivariate(df)

    print("\n" + "=" * 60)
    print("EDA COMPLETED SUCCESSFULLY")
    print("=" * 60)

    print("\nGraphs are saved in:")
    print(RESULTS_DIR)