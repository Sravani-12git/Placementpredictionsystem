import pandas as pd
import matplotlib.pyplot as plt

from pathlib import Path
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score, davies_bouldin_score


# ============================================================
# 1. PATHS
# ============================================================

PROJECT_DIR = Path(
    r"C:\Users\konak\PycharmProjects\Placementpredictionsystem"
)

# Actual dataset location
DATASET_PATH = Path(
    r"C:\Users\konak\PycharmProjects\Placementpredictionsystem\data\placement_data (1).csv"
)

# Output file
OUTPUT_PATH = (
    PROJECT_DIR
    / "data"
    / "placement_kmeans++_clustered.csv"
)


print("=" * 60)
print("       PLACEMENT STUDENT K-MEANS++")
print("=" * 60)


# ============================================================
# 2. LOAD DATASET
# ============================================================

print("\nLoading dataset...")
print("Dataset path:")
print(DATASET_PATH)


if not DATASET_PATH.exists():

    print("\nERROR: Dataset not found!")
    print("Check this path:")
    print(DATASET_PATH)
    exit()


try:

    df = pd.read_csv(DATASET_PATH)

except Exception as e:

    print("\nERROR while loading dataset:")
    print(e)
    exit()


print("\nDataset loaded successfully!")

print("Rows    :", df.shape[0])
print("Columns :", df.shape[1])


# ============================================================
# 3. DISPLAY COLUMNS
# ============================================================

print("\n" + "=" * 60)
print("ACTUAL COLUMNS")
print("=" * 60)


for column in df.columns:

    print(repr(column))


# ============================================================
# 4. SELECT FEATURES
# ============================================================

features = [
    "CGPA",
    "AttendencePercent",
    "Internships",
    "Project",
    "coding test score"
]


print("\n" + "=" * 60)
print("SELECTED FEATURES")
print("=" * 60)


for feature in features:

    print("-", feature)


# ============================================================
# 5. CHECK FEATURES
# ============================================================

missing_features = [
    feature
    for feature in features
    if feature not in df.columns
]


if missing_features:

    print("\nERROR: Missing features:")

    for feature in missing_features:

        print("-", feature)


    print("\nAvailable columns:")

    print(df.columns.tolist())

    exit()


# ============================================================
# 6. CREATE FEATURE DATA
# ============================================================

X = df[features].copy()


# ============================================================
# 7. CONVERT TO NUMERIC
# ============================================================

for feature in features:

    X[feature] = pd.to_numeric(
        X[feature],
        errors="coerce"
    )


# ============================================================
# 8. REMOVE MISSING VALUES
# ============================================================

before = len(X)

X = X.dropna()

after = len(X)


print("\nRows before cleaning :", before)
print("Rows after cleaning  :", after)
print("Rows removed         :", before - after)


if len(X) < 3:

    print("\nERROR: Not enough data.")
    exit()


# ============================================================
# 9. STANDARDIZATION
# ============================================================

print("\n" + "=" * 60)
print("STANDARDIZATION")
print("=" * 60)


scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)


print("Standardization completed!")


# ============================================================
# 10. K-MEANS++ MODEL
# ============================================================

print("\n" + "=" * 60)
print("K-MEANS++ CLUSTERING")
print("=" * 60)


# Use the K obtained from Elbow Method

K = 2


print("\nSelected K:", K)

print("Initialization: K-Means++")


kmeans = KMeans(
    n_clusters=K,
    init="k-means++",
    random_state=0,
    n_init=10
)


# ============================================================
# 11. TRAIN MODEL
# ============================================================

clusters = kmeans.fit_predict(
    X_scaled
)


print("\nK-Means++ model trained successfully!")


# ============================================================
# 12. CLUSTER ASSIGNMENTS
# ============================================================

X_result = X.copy()

X_result["Cluster"] = clusters


print("\n" + "=" * 60)
print("CLUSTER ASSIGNMENTS")
print("=" * 60)


print(
    X_result.head(10)
)


# ============================================================
# 13. CLUSTER DISTRIBUTION
# ============================================================

print("\n" + "=" * 60)
print("CLUSTER DISTRIBUTION")
print("=" * 60)


cluster_counts = (
    X_result["Cluster"]
    .value_counts()
    .sort_index()
)


for cluster, count in cluster_counts.items():

    print(
        "Cluster",
        cluster,
        ":",
        count,
        "students"
    )


# ============================================================
# 14. SILHOUETTE SCORE
# ============================================================

silhouette = silhouette_score(
    X_scaled,
    clusters
)


# ============================================================
# 15. DAVIES-BOULDIN SCORE
# ============================================================

davies_bouldin = davies_bouldin_score(
    X_scaled,
    clusters
)


print("\n" + "=" * 60)
print("MODEL EVALUATION")
print("=" * 60)


print("\nSilhouette Score:")

print(
    round(silhouette, 4)
)


print("\nDavies-Bouldin Score:")

print(
    round(davies_bouldin, 4)
)


# ============================================================
# 16. CLUSTER CENTERS
# ============================================================

print("\n" + "=" * 60)
print("CLUSTER CENTERS")
print("=" * 60)


centres = kmeans.cluster_centers_


centres_original = scaler.inverse_transform(
    centres
)


center_df = pd.DataFrame(
    centres_original,
    columns=features
)


center_df.index.name = "Cluster"


print(center_df)


# ============================================================
# 17. SAVE RESULT
# ============================================================

OUTPUT_PATH.parent.mkdir(
    parents=True,
    exist_ok=True
)


X_result.to_csv(
    OUTPUT_PATH,
    index=False
)


print("\n" + "=" * 60)
print("RESULT SAVED")
print("=" * 60)


print("\nSaved at:")

print(OUTPUT_PATH)


# ============================================================
# 18. GRAPH 1
# ============================================================

plt.figure(
    figsize=(8, 6)
)


plt.scatter(
    X["CGPA"],
    X["coding test score"],
    c=clusters,
    s=60
)


plt.xlabel(
    "CGPA"
)


plt.ylabel(
    "Coding Test Score"
)


plt.title(
    "K-Means++ Clustering\nCGPA vs Coding Test Score"
)


plt.grid(True)

plt.tight_layout()

plt.show()


# ============================================================
# 19. GRAPH 2
# ============================================================

plt.figure(
    figsize=(8, 6)
)


plt.scatter(
    X["AttendencePercent"],
    X["CGPA"],
    c=clusters,
    s=60
)


plt.xlabel(
    "Attendance Percentage"
)


plt.ylabel(
    "CGPA"
)


plt.title(
    "K-Means++ Clustering\nAttendance vs CGPA"
)


plt.grid(True)

plt.tight_layout()

plt.show()


# ============================================================
# 20. FINAL SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("FINAL SUMMARY")
print("=" * 60)


print("\nTotal Students       :", len(X_result))

print("Number of Clusters   :", K)

print("Method               : K-Means++")

print(
    "Silhouette Score     :",
    round(silhouette, 4)
)

print(
    "Davies-Bouldin Score:",
    round(davies_bouldin, 4)
)


print("\nCluster Distribution:")

print(cluster_counts)


print("\nK-Means++ clustering completed successfully!")

