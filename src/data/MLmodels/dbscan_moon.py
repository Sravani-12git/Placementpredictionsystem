# ============================================================
# DBSCAN CLUSTERING - MOON DATASET
# ============================================================

import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_moons
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN


# ============================================================
# 1. CREATE MOON DATASET
# ============================================================

def create_dataset():
    X, y = make_moons(
        n_samples=300,
        noise=0.08,
        random_state=42
    )

    return X, y


# ============================================================
# 2. PREPROCESS / SCALE DATA
# ============================================================

def preprocess_data(X):
    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    return X_scaled


# ============================================================
# 3. APPLY DBSCAN
# ============================================================

def apply_dbscan(X):
    model = DBSCAN(
        eps=0.3,
        min_samples=5
    )

    model.fit(X)

    return model


# ============================================================
# 4. DISPLAY MODEL INFORMATION
# ============================================================

def display_model(X, model):

    labels = model.labels_

    # Number of clusters
    unique_labels = set(labels)

    # Remove noise label (-1)
    n_clusters = len(unique_labels - {-1})

    # Number of noise points
    n_noise = list(labels).count(-1)

    print("=" * 50)
    print("DBSCAN CLUSTERING RESULTS")
    print("=" * 50)

    print("Total data points :", len(X))
    print("Number of clusters:", n_clusters)
    print("Noise points      :", n_noise)

    print("\nCluster labels:")
    print(labels)

    print("=" * 50)


# ============================================================
# 5. PLOT ORIGINAL DATA
# ============================================================

def plot_original_data(X):

    plt.figure(figsize=(8, 6))

    plt.scatter(
        X[:, 0],
        X[:, 1],
        s=50
    )

    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.title("Original Moon Dataset")

    plt.grid(True)

    plt.show()


# ============================================================
# 6. PLOT DBSCAN CLUSTERS
# ============================================================

def plot_clusters(X, model):

    # Get cluster labels
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

    plt.title("DBSCAN Clustering")

    plt.grid(True)

    plt.show()


# ============================================================
# 7. MAIN PROGRAM
# ============================================================

if __name__ == "__main__":

    # --------------------------------------------------------
    # Step 1: Create dataset
    # --------------------------------------------------------

    X, y = create_dataset()

    print("\nDataset created successfully.")
    print("Dataset shape:", X.shape)


    # --------------------------------------------------------
    # Step 2: Show original dataset
    # --------------------------------------------------------

    plot_original_data(X)


    # --------------------------------------------------------
    # Step 3: Scale dataset
    # --------------------------------------------------------

    X_scaled = preprocess_data(X)

    print("\nData scaling completed.")


    # --------------------------------------------------------
    # Step 4: Apply DBSCAN
    # --------------------------------------------------------

    model = apply_dbscan(X_scaled)

    print("DBSCAN model trained successfully.")


    # --------------------------------------------------------
    # Step 5: Display results
    # --------------------------------------------------------

    display_model(X_scaled, model)


    # --------------------------------------------------------
    # Step 6: Plot clusters
    # --------------------------------------------------------

    plot_clusters(X_scaled, model)