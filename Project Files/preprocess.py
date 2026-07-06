import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
import joblib
import os


def load_dataset(path="../dataset/Crop_recommendation.csv"):
    """
    Load the crop recommendation dataset.
    """
    df = pd.read_csv(path)
    return df


def preprocess_data(df):
    """
    Preprocess the dataset:
    - Remove missing values
    - Encode crop labels
    - Scale features
    - Split into training and testing sets
    """

    # Remove missing values
    df = df.dropna()

    # Features
    X = df.drop("label", axis=1)

    # Target
    y = df["label"]

    # Encode crop labels
    encoder = LabelEncoder()
    y = encoder.fit_transform(y)

    # Save label encoder
    os.makedirs("model", exist_ok=True)
    joblib.dump(encoder, "model/label_encoder.pkl")

    # Feature Scaling
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Save scaler
    joblib.dump(scaler, "model/scaler.pkl")

    # Split Dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    return (
        X_train,
        X_test,
        y_train,
        y_test,
        scaler,
        encoder
    )


if __name__ == "__main__":

    df = load_dataset()

    X_train, X_test, y_train, y_test, scaler, encoder = preprocess_data(df)

    print("Dataset Loaded Successfully")

    print("Training Samples :", len(X_train))
    print("Testing Samples  :", len(X_test))