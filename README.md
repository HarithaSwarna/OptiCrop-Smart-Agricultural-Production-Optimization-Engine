# 🌱 OptiCrop: Smart Agricultural Production Optimization Engine

## 📖 Project Overview

OptiCrop is a Machine Learning-based web application designed to recommend the most suitable crop based on soil nutrients and environmental conditions. The system helps farmers, agricultural researchers, and policymakers make informed decisions to improve agricultural productivity and promote sustainable farming practices.

The application analyzes key parameters such as Nitrogen (N), Phosphorus (P), Potassium (K), Temperature, Humidity, pH, and Rainfall to predict the best crop using trained Machine Learning models.

---

## 🎯 Objectives

- Recommend the most suitable crop based on soil and environmental conditions.
- Improve agricultural productivity using Machine Learning.
- Help farmers make data-driven farming decisions.
- Support agricultural research and policy planning.
- Promote sustainable agriculture through efficient resource utilization.

---

## 🚀 Features

- 🌾 Smart Crop Recommendation
- 🌱 Crop Suitability Analysis
- 📊 Agricultural Research Dashboard
- 📈 Machine Learning Model Comparison
- 📉 Data Visualization using Graphs
- 💻 Interactive Flask Web Application
- 📱 Responsive User Interface using Bootstrap

---

## 📌 Scenarios

### Scenario 1: Smart Crop Recommendation

Farmers enter:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- pH
- Rainfall

The system predicts the most suitable crop for maximum productivity.

---

### Scenario 2: Crop Suitability Assessment

Users can evaluate whether the current environmental conditions are suitable for a selected crop.

---

### Scenario 3: Agricultural Research

Researchers and policymakers can analyze crop-environment relationships through visualizations and model insights.

---

# 🛠️ Technologies Used

## Programming Language

- Python 3.13

## Machine Learning

- Scikit-learn
- Random Forest
- Decision Tree
- K-Nearest Neighbors (KNN)
- Logistic Regression

## Python Libraries

- Pandas
- NumPy
- Matplotlib
- Seaborn
- Joblib

## Web Framework

- Flask

## Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript

---

# 📂 Project Structure

```
OptiCrop/
│
├── app.py
├── requirements.txt
├── README.md
│
├── dataset/
│   └── Crop_recommendation.csv
│
├── model/
│   ├── train_model.py
│   ├── preprocess.py
│   ├── predict.py
│   ├── crop_model.pkl
│   ├── scaler.pkl
│   └── label_encoder.pkl
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   ├── js/
│   │   └── script.js
│   │
│   └── images/
│       ├── crop_distribution.png
│       ├── heatmap.png
│       ├── rainfall.png
│       ├── temperature.png
│       └── farm.png
│
├── templates/
│   ├── index.html
│   ├── recommendation.html
│   ├── suitability.html
│   ├── research.html
│   ├── result.html
│   ├── about.html
│   └── contact.html
│
└── utils/
    └── generate_graphs.py
```

---

# 📊 Machine Learning Workflow

1. Load Agricultural Dataset
2. Data Preprocessing
3. Feature Scaling
4. Label Encoding
5. Train Multiple Machine Learning Models
6. Compare Model Accuracy
7. Select Best Model
8. Save Trained Model
9. Deploy using Flask

---

# 🤖 Machine Learning Models Used

| Model | Purpose |
|--------|----------|
| Random Forest | Final Prediction Model |
| Decision Tree | Performance Comparison |
| Logistic Regression | Classification |
| K-Nearest Neighbors | Classification |

---

# 📈 Model Performance

| Algorithm | Accuracy |
|------------|----------|
| Random Forest | **99.55%** |
| Decision Tree | 97.95% |
| KNN | 97.95% |
| Logistic Regression | 97.27% |

Random Forest achieved the highest accuracy and was selected as the final prediction model.

---

# 📊 Input Parameters

The system accepts the following parameters:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- pH Value
- Rainfall

---

# 🌾 Output

The application predicts the most suitable crop for the given soil and environmental conditions.

Example:

Input:

N = 90
P = 42
K = 43
Temperature = 20.8
Humidity = 82
pH = 6.5
Rainfall = 202

Output:

Recommended Crop: Rice

---

# 🎯 Future Enhancements

- Weather API Integration
- Fertilizer Recommendation System
- Disease Detection using Deep Learning
- Crop Yield Prediction
- AI Chatbot for Farmers
- Multi-language Support
- Cloud Deployment
- Mobile Application

---

## 🌱 Conclusion

OptiCrop is an intelligent agricultural recommendation system that leverages Machine Learning to analyze soil and environmental parameters for accurate crop prediction. By combining data-driven insights with an interactive Flask web application, the project helps farmers optimize crop selection, improve productivity, and encourage sustainable agricultural practices while also supporting agricultural research and policy planning.
