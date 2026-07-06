import os
import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

from preprocess import preprocess_data

# ======================================
# Get project paths
# ======================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATASET_PATH = os.path.join(
    BASE_DIR,
    "..",
    "dataset",
    "Crop_recommendation.csv"
)

MODEL_PATH = os.path.join(BASE_DIR, "crop_model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "scaler.pkl")
ENCODER_PATH = os.path.join(BASE_DIR, "label_encoder.pkl")

print("Loading dataset from:")
print(DATASET_PATH)

# ======================================
# Load Dataset
# ======================================

if not os.path.exists(DATASET_PATH):
    raise FileNotFoundError(
        f"\nDataset not found!\nExpected location:\n{DATASET_PATH}"
    )

df = pd.read_csv(DATASET_PATH)

print("Dataset Loaded Successfully!")
print("Total Records:", len(df))

# ======================================
# Preprocess Dataset
# ======================================

X_train, X_test, y_train, y_test, scaler, encoder = preprocess_data(df)

# ======================================
# Machine Learning Models
# ======================================

models = {
    "Random Forest": RandomForestClassifier(
        n_estimators=100,
        random_state=42
    ),

    "Decision Tree": DecisionTreeClassifier(
        random_state=42
    ),

    "Logistic Regression": LogisticRegression(
        max_iter=1000
    ),

    "KNN": KNeighborsClassifier(
        n_neighbors=5
    )
}

best_model = None
best_accuracy = 0
best_name = ""

print("\n======================================")
print("Model Accuracy")
print("======================================")

for name, model in models.items():

    model.fit(X_train, y_train)

    prediction = model.predict(X_test)

    accuracy = accuracy_score(y_test, prediction)

    print(f"{name:<22}: {accuracy*100:.2f}%")

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_model = model
        best_name = name

# ======================================
# Save Model
# ======================================

joblib.dump(best_model, MODEL_PATH)
joblib.dump(scaler, SCALER_PATH)
joblib.dump(encoder, ENCODER_PATH)

print("\n======================================")
print("Best Model :", best_name)
print("Accuracy   :", round(best_accuracy * 100, 2), "%")
print("======================================")
print("Model Saved Successfully!")
print("Location:", MODEL_PATH)
print("Scaler Saved Successfully!")
print("Encoder Saved Successfully!")