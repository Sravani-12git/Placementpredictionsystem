import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# ============================================================
# 1. PATHS
# ============================================================

PROJECT_DIR = Path(
    r"C:\Users\konak\PycharmProjects\Placementpredictionsystem"
)

# Dataset
DATASET_PATH = PROJECT_DIR / "data" / "placement_data (1).csv"

# Output CSV
OUTPUT_PATH = PROJECT_DIR / "data" / "placement_kmeans_clustered.csv"

# Output graphs
ELBOW_GRAPH_PATH = PROJECT_DIR / "data" / "kmeans_elbow_graph.png"
CLUSTER_GRAPH_PATH = PROJECT_DIR / "data" / "kmeans_cluster_graph.png"


# ============================================================
# 2. TITLE
# ============================================================

print("=" * 60)
print("        PLACEMENT STUDENT K-MEANS ELBOW METHOD")
print("=" * 60)


# ============================================================
# 3. LOAD DATASET
# ============================================================

if not DATASET_PATH.exists():
    print("\nERROR: Dataset not found!")
    print("Check this path:")
    print(DATASET_PATH)
    exit()

df = pd.read_csv(DATASET_PATH)

print("\nDataset loaded successfully!")
print("Rows    :", df.shape[0])
print("Columns :", df.shape[1])


# ============================================================
# 4. SELECT CORRECT FEATURES
# ============================================================

features = [
    "CGPA",
    "AttendancePercent",
    "Internships",
    "Projects",
    "CodingTestScore"
]

# Check features
missing_features = [
    feature for feature in features
    if feature not in df.columns
]

if missing_features:
    print("\nERROR: Missing features:")
    print(missing_features)
    print("\nAvailable columns:")
    print(df.columns.tolist())
    exit()


# ============================================================
# 5. PREPARE DATA
# ============================================================

X = df[features].copy()

# Convert everything to numeric
for feature in features:
    X[feature] = pd.to_numeric(
        X[feature],
        errors="coerce"
    )

# Remove missing values
valid_index = X.dropna().index

X = X.loc[valid_index]

# Keep original student records aligned
df_clean = df.loc[valid_index].copy()

if len(X) < 3:
    print("\nERROR: Not enough valid data.")
    exit()


# ============================================================
# 6. STANDARDIZATION
# ============================================================

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)


# ============================================================
# 7. ELBOW METHOD
# ============================================================

wcss = []

max_k = min(10, len(X) - 1)

for k in range(1, max_k + 1):

    kmeans = KMeans(
        n_clusters=k,
        init="k-means++",
        random_state=42,
        n_init=10
    )

    kmeans.fit(X_scaled)

    wcss.append(kmeans.inertia_)


# ============================================================
# 8. ELBOW GRAPH
# ============================================================

plt.figure(figsize=(10, 6))

plt.plot(
    range(1, max_k + 1),
    wcss,
    marker="o",
    linewidth=2
)

plt.title(
    "K-Means Elbow Method for Placement Students",
    fontsize=16
)

plt.xlabel(
    "Number of Clusters (K)",
    fontsize=12
)

plt.ylabel(
    "WCSS (Within-Cluster Sum of Squares)",
    fontsize=12
)

plt.xticks(range(1, max_k + 1))

plt.grid(True)

plt.tight_layout()

# Save graph
plt.savefig(
    ELBOW_GRAPH_PATH,
    dpi=300,
    bbox_inches="tight"
)

# SHOW GRAPH
plt.show()


# ============================================================
# 9. CHOOSE NUMBER OF CLUSTERS
# ============================================================

# You can change this value after looking at the elbow graph.
# 3 is a good starting point for placement students.

optimal_k = 3


# ============================================================
# 10. FINAL K-MEANS MODEL
# ============================================================

kmeans_final = KMeans(
    n_clusters=optimal_k,
    init="k-means++",
    random_state=42,
    n_init=10
)

cluster_labels = kmeans_final.fit_predict(X_scaled)


# ============================================================
# 11. ADD CLUSTER TO DATASET
# ============================================================

df_clean["Cluster"] = cluster_labels


# ============================================================
# 12. SAVE CLUSTERED DATA
# ============================================================

df_clean.to_csv(
    OUTPUT_PATH,
    index=False
)


# ============================================================
# 13. CLUSTER GRAPH
# ============================================================

plt.figure(figsize=(10, 7))

scatter = plt.scatter(
    df_clean["CGPA"],
    df_clean["CodingTestScore"],
    c=df_clean["Cluster"],
    cmap="viridis",
    s=15,
    alpha=0.7
)

# Cluster centers need to be converted
# back to original scale
centers_scaled = kmeans_final.cluster_centers_

centers_original = scaler.inverse_transform(
    centers_scaled
)

# CGPA is column 0
# CodingTestScore is column 4

plt.scatter(
    centers_original[:, 0],
    centers_original[:, 4],
    marker="X",
    s=250,
    edgecolors="black",
    linewidths=2,
    label="Cluster Centers"
)

plt.title(
    "K-Means Clustering of Placement Students",
    fontsize=16
)

plt.xlabel(
    "CGPA",
    fontsize=12
)

plt.ylabel(
    "Coding Test Score",
    fontsize=12
)

plt.grid(True)

plt.legend()

plt.tight_layout()

# Save graph
plt.savefig(
    CLUSTER_GRAPH_PATH,
    dpi=300,
    bbox_inches="tight"
)

# SHOW GRAPH
plt.show()


# ============================================================
# 14. FINAL MESSAGE
# ============================================================

print("\nK-Means clustering completed successfully!")

print("\nGraphs saved at:")

print(ELBOW_GRAPH_PATH)
print(CLUSTER_GRAPH_PATH)

print("\nClustered dataset saved at:")

print(OUTPUT_PATH)