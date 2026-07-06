import os
import joblib
import numpy as np

# -------------------------------
# Load Model
# -------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_DIR, "crop_model.pkl"))
scaler = joblib.load(os.path.join(BASE_DIR, "scaler.pkl"))
label_encoder = joblib.load(os.path.join(BASE_DIR, "label_encoder.pkl"))

# -------------------------------
# Crop Prediction Function
# -------------------------------

def predict_crop(
    nitrogen,
    phosphorus,
    potassium,
    temperature,
    humidity,
    ph,
    rainfall
):
    """
    Predict the most suitable crop based on
    soil and environmental parameters.
    """

    input_data = np.array([[
        nitrogen,
        phosphorus,
        potassium,
        temperature,
        humidity,
        ph,
        rainfall
    ]])

    # Scale the input
    input_scaled = scaler.transform(input_data)

    # Predict using the trained model
    prediction = model.predict(input_scaled)

    # Convert numeric prediction back to crop name
    crop = label_encoder.inverse_transform(prediction)

    return crop[0]


# -------------------------------
# Testing
# -------------------------------

if __name__ == "__main__":

    crop = predict_crop(
        nitrogen=90,
        phosphorus=42,
        potassium=43,
        temperature=20.8,
        humidity=82,
        ph=6.5,
        rainfall=202
    )

    print("Recommended Crop:", crop)