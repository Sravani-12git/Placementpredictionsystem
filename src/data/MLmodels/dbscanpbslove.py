import numpy as np
from sklearn.cluster import DBSCAN


# 1. CREATE DATA
def create_data():
    points = {
        'A': (2, 2),
        'B': (2, 3),
        'C': (3, 2),
        'D': (3, 3),
        'I': (4, 4),
        'E': (8, 8),
        'F': (8, 9),
        'G': (9, 8),
        'H': (25, 25)
    }

    names = list(points.keys())

    X = np.array([points[name] for name in names])

    return X, names


# 2. CREATE DBSCAN MODEL
def create_model(X, eps, min_samples):
    model = DBSCAN(
        eps=eps,
        min_samples=min_samples
    )

    model.fit(X)

    return model


# 3. DISPLAY MODEL
def display_model(model, names):

    core_indices = set(model.core_sample_indices_)

    for i, (name, label) in enumerate(
        zip(names, model.labels_)
    ):

        if i in core_indices:
            kind = "core"

        elif label == -1:
            kind = "noise"

        else:
            kind = "border"

        print(
            f"{name}: "
            f"Cluster = {label:>2}"
            f" -> {kind}"
        )


# 4. MAIN FUNCTION
def main():

    X, names = create_data()

    model = create_model(
        X,
        eps=1.5,
        min_samples=3
    )

    display_model(
        model,
        names
    )


# 5. PROGRAM START
if __name__ == "__main__":
    main()