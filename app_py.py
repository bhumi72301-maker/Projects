from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load model, scaler, and label encoder
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))
le = pickle.load(open('le.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get values from form
        values = [float(request.form.get(feat)) for feat in
                  ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]

        # Scale input
        values_scaled = scaler.transform([values])

        # Predict
        prediction_encoded = model.predict(values_scaled)[0]
        prediction_label = le.inverse_transform([prediction_encoded])[0]

        return render_template('index.html', prediction_text=f'Recommended Crop: {prediction_label}')

    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')


if __name__ == '__main__':
    app.run(debug=True)
