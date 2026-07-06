from flask import Flask, render_template, request
from model.predict import predict_crop

app = Flask(__name__)


# -------------------------------
# Home Page
# -------------------------------
@app.route('/')
def home():
    return render_template('index.html')


# -------------------------------
# Crop Recommendation Page
# -------------------------------
@app.route('/recommendation')
def recommendation():
    return render_template('recommendation.html')


# -------------------------------
# Crop Suitability Page
# -------------------------------
@app.route('/suitability')
def suitability():
    return render_template('suitability.html')


# -------------------------------
# Research Dashboard
# -------------------------------
@app.route('/research')
def research():
    return render_template('research.html')


# -------------------------------
# About Page
# -------------------------------
@app.route('/about')
def about():
    return render_template('about.html')


# -------------------------------
# Contact Page
# -------------------------------
@app.route('/contact')
def contact():
    return render_template('contact.html')


# -------------------------------
# Crop Prediction
# -------------------------------
@app.route('/predict', methods=['POST'])
def predict():

    try:
        nitrogen = float(request.form['nitrogen'])
        phosphorus = float(request.form['phosphorus'])
        potassium = float(request.form['potassium'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])

        crop = predict_crop(
            nitrogen,
            phosphorus,
            potassium,
            temperature,
            humidity,
            ph,
            rainfall
        )

        return render_template(
            'result.html',
            crop=crop
        )

    except Exception as e:
        return render_template(
            'result.html',
            crop="Prediction Failed",
            error=str(e)
        )


# -------------------------------
# Crop Suitability Check
# -------------------------------
@app.route('/check_suitability', methods=['POST'])
def check_suitability():

    try:
        selected_crop = request.form['crop']

        nitrogen = float(request.form['nitrogen'])
        phosphorus = float(request.form['phosphorus'])
        potassium = float(request.form['potassium'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])

        recommended_crop = predict_crop(
            nitrogen,
            phosphorus,
            potassium,
            temperature,
            humidity,
            ph,
            rainfall
        )

        if selected_crop.lower() == recommended_crop.lower():
            suitability = "Suitable ✅"
        else:
            suitability = "Not Suitable ❌"

        return render_template(
            'result.html',
            crop=recommended_crop,
            selected_crop=selected_crop,
            suitability=suitability
        )

    except Exception as e:
        return render_template(
            'result.html',
            crop="Error",
            error=str(e)
        )


# -------------------------------
# Run Flask App
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)