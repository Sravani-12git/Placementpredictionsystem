import pandas as pd
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib


# ============================================================
# 1. PATHS
# ============================================================

PROJECT_DIR = Path(
    r"C:\Users\konak\PycharmProjects\Placementpredictionsystem"
)

DATASET_PATH = PROJECT_DIR / "data" / "placement_data (1).csv"

MODEL_PATH = PROJECT_DIR / "models" / "gradient_boosting.pkl"


# ============================================================
# 2. LOAD DATASET
# ============================================================

print("=" * 60)
print("        GRADIENT BOOSTING - PLACEMENT PREDICTION")
print("=" * 60)

print("\nLoading dataset...")
print("Dataset path:")
print(DATASET_PATH)

if not DATASET_PATH.exists():
    print("\nERROR: Dataset not found!")
    print("Check this path:")
    print(DATASET_PATH)
    exit()

df = pd.read_csv(DATASET_PATH)

print("\nDataset loaded successfully!")
print("Shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())


# ============================================================
# 3. DISPLAY DATA
# ============================================================

print("\nFirst 5 rows:")
print(df.head())


# ============================================================
# 4. REMOVE UNNECESSARY COLUMNS
# ============================================================

# Remove common ID columns if present
columns_to_drop = []

for col in df.columns:
    if col.lower() in ["id", "student_id", "sl_no", "sl.no", "serial_no"]:
        columns_to_drop.append(col)

if columns_to_drop:
    df = df.drop(columns=columns_to_drop)

print("\nAfter removing unnecessary columns:")
print(df.shape)


# ============================================================
# 5. FIND TARGET COLUMN
# ============================================================

possible_targets = [
    "placed",
    "placement",
    "status",
    "placement_status"
]

target_column = None

for col in df.columns:
    if col.lower() in possible_targets:
        target_column = col
        break

if target_column is None:
    print("\nERROR: Target column not found!")
    print("Available columns:")
    print(df.columns.tolist())
    exit()

print("\nTarget column:", target_column)


# ============================================================
# 6. PREPROCESS TARGET
# ============================================================

y = df[target_column]

# Convert text target to 0/1 if required
if y.dtype == "object":

    y = y.astype(str).str.strip().str.lower()

    mapping = {
        "placed": 1,
        "yes": 1,
        "y": 1,
        "true": 1,
        "1": 1,

        "not placed": 0,
        "not_placed": 0,
        "no": 0,
        "n": 0,
        "false": 0,
        "0": 0
    }

    y = y.map(mapping)

    if y.isnull().any():
        print("\nERROR: Unknown target values found.")
        print(df[target_column].unique())
        exit()


# ============================================================
# 7. FEATURES
# ============================================================

X = df.drop(columns=[target_column])


# Convert categorical columns to numerical
X = pd.get_dummies(X, drop_first=True)


# Handle missing values
X = X.fillna(X.median(numeric_only=True))

X = X.fillna(0)


print("\nNumber of features:", X.shape[1])


# ============================================================
# 8. TRAIN TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))


# ============================================================
# 9. GRADIENT BOOSTING MODEL
# ============================================================

print("\nTraining Gradient Boosting model...")

model = GradientBoostingClassifier(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
    random_state=42
)

model.fit(X_train, y_train)

print("Model training completed!")


# ============================================================
# 10. PREDICTION
# ============================================================

y_pred = model.predict(X_test)


# ============================================================
# 11. EVALUATION
# ============================================================

accuracy = accuracy_score(y_test, y_pred)

print("\n" + "=" * 60)
print("MODEL RESULTS")
print("=" * 60)

print("\nAccuracy:")
print(f"{accuracy * 100:.2f}%")

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# ============================================================
# 12. FEATURE IMPORTANCE
# ============================================================

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nTop Important Features:")
print(importance.head(10))


# ============================================================
# 13. SAVE MODEL
# ============================================================

MODEL_PATH.parent.mkdir(
    parents=True,
    exist_ok=True
)

joblib.dump(
    {
        "model": model,
        "features": X.columns.tolist()
    },
    MODEL_PATH
)

print("\nModel saved successfully!")
print("Model path:")
print(MODEL_PATH)

print("\n" + "=" * 60)
print("        GRADIENT BOOSTING COMPLETED")
print("=" * 60)