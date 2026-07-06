import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# Paths
# -------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATASET_PATH = os.path.join(
    BASE_DIR,
    "..",
    "dataset",
    "Crop_recommendation.csv"
)

IMAGE_DIR = os.path.join(
    BASE_DIR,
    "..",
    "static",
    "images"
)

os.makedirs(IMAGE_DIR, exist_ok=True)

# -------------------------------
# Load Dataset
# -------------------------------

print("Loading dataset...")
print(DATASET_PATH)

df = pd.read_csv(DATASET_PATH)

print("Dataset Loaded Successfully!")

# -------------------------------
# Crop Distribution
# -------------------------------

plt.figure(figsize=(10,6))
df["label"].value_counts().plot(kind="bar")
plt.title("Crop Distribution")
plt.tight_layout()
plt.savefig(os.path.join(IMAGE_DIR, "crop_distribution.png"))
plt.close()

# -------------------------------
# Correlation Heatmap
# -------------------------------

plt.figure(figsize=(8,6))
sns.heatmap(df.drop(columns=["label"]).corr(), cmap="YlGnBu")
plt.title("Feature Correlation")
plt.tight_layout()
plt.savefig(os.path.join(IMAGE_DIR, "heatmap.png"))
plt.close()

# -------------------------------
# Temperature Distribution
# -------------------------------

plt.figure(figsize=(8,5))
plt.hist(df["temperature"], bins=20)
plt.title("Temperature Distribution")
plt.xlabel("Temperature")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(os.path.join(IMAGE_DIR, "temperature.png"))
plt.close()

# -------------------------------
# Rainfall Distribution
# -------------------------------

plt.figure(figsize=(8,5))
plt.hist(df["rainfall"], bins=20)
plt.title("Rainfall Distribution")
plt.xlabel("Rainfall")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(os.path.join(IMAGE_DIR, "rainfall.png"))
plt.close()

print("\nGraphs Generated Successfully!")
print("Saved in:", IMAGE_DIR)