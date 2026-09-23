# ============================================================
# AGGLOMERATIVE CLUSTERING
# ============================================================

import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram, linkage


# ============================================================
# 1. CREATE MODEL
# ============================================================

def create_model(k):

    model = AgglomerativeClustering(
        n_clusters=k,
        linkage="ward"
    )

    return model


# ============================================================
# 2. TRAIN MODEL
# ============================================================

def train_model(model, X):

    model.fit(X)

    print("\nAgglomerative Clustering Result:")
    print("Model trained successfully.")

    return model


# ============================================================
# 3. EVALUATE MODEL
# ============================================================

def evaluate_model(model, X):

    labels = model.labels_

    score = silhouette_score(X, labels)

    print("\nSilhouette Score:", round(score, 4))

    return score


# ============================================================
# 4. DISPLAY CLUSTERS
# ============================================================

def plot_clusters(X, model):

    labels = model.labels_

    plt.figure(figsize=(8, 6))

    plt.scatter(
        X[:, 0],
        X[:, 1],
        c=labels,
        s=50
    )

    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")

    plt.title("Agglomerative Clustering")

    plt.grid(True)

    plt.show()


# ============================================================
# 5. DISPLAY DENDROGRAM
# ============================================================

def plot_dendrogram(X):

    linked = linkage(
        X,
        method="ward"
    )

    plt.figure(figsize=(10, 6))

    dendrogram(linked)

    plt.title("Hierarchical Clustering Dendrogram")

    plt.xlabel("Data Points")

    plt.ylabel("Distance")

    plt.grid(True)

    plt.show()


# ============================================================
# 6. MAIN PROGRAM
# ============================================================

if __name__ == "__main__":

    # --------------------------------------------------------
    # Create sample dataset
    # --------------------------------------------------------

    X = np.array([
        [1.0, 2.0],
        [1.2, 2.2],
        [0.8, 1.8],
        [1.1, 2.1],
        [1.3, 2.3],

        [5.0, 6.0],
        [5.2, 6.2],
        [4.8, 5.8],
        [5.1, 6.1],
        [5.3, 6.3],

        [9.0, 1.0],
        [9.2, 1.2],
        [8.8, 0.8],
        [9.1, 1.1],
        [9.3, 1.3]
    ])


    print("=" * 55)
    print("AGGLOMERATIVE CLUSTERING")
    print("=" * 55)

    print("\nDataset shape:", X.shape)


    # --------------------------------------------------------
    # Standardize data
    # --------------------------------------------------------

    scaler = StandardScaler()

    X = scaler.fit_transform(X)

    print("Data scaling completed.")


    # --------------------------------------------------------
    # Number of clusters
    # --------------------------------------------------------

    k = 3


    # --------------------------------------------------------
    # Create model
    # --------------------------------------------------------

    model = create_model(k)


    # --------------------------------------------------------
    # Train model
    # --------------------------------------------------------

    model = train_model(model, X)


    # --------------------------------------------------------
    # Display cluster labels
    # --------------------------------------------------------

    print("\nCluster Labels:")

    print(model.labels_)


    # --------------------------------------------------------
    # Evaluate model
    # --------------------------------------------------------

    evaluate_model(model, X)


    # --------------------------------------------------------
    # Plot clusters
    # --------------------------------------------------------

    plot_clusters(X, model)


    # --------------------------------------------------------
    # Plot dendrogram
    # --------------------------------------------------------

    plot_dendrogram(X)