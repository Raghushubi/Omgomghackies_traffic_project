from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import io
import os
import traceback
import locale
import sys
from flask_cors import CORS

# Set locale to UTF-8
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

# Explicitly set environment variables
os.environ['PYTHONIOENCODING'] = 'utf-8'

# Load the trained model
model = load_model(r"traffic_sign_model.keras")

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Welcome to the Traffic Sign Prediction API. Use the `/predict` endpoint to get predictions."

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    try:
        # Read file content as bytes
        file_content = file.read()
        
        # Create image stream from bytes
        img_stream = io.BytesIO(file_content)
        
        # Load image
        img = image.load_img(img_stream, target_size=(64, 64))
        img_array = image.img_to_array(img) / 255.0  # Normalize the image
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

        # Suppress TensorFlow warnings and logs
        import os
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

        # Make prediction using a different method
        predictions = model.predict(img_array, verbose=0)
        predicted_class = np.argmax(predictions[0])

        # Map the prediction to class name
        class_names = ['stop', 'proceed', 'yield', 'extra']
        predicted_class_name = class_names[predicted_class]

        # Convert numpy float to Python float to avoid potential encoding issues
        confidence = float(predictions[0][predicted_class])

        return jsonify({
            "predicted_class": predicted_class_name,
            "confidence": confidence
        })
    except Exception as e:
        # Comprehensive error logging with safe string conversion
        error_details = {
            "error": str(e),
            "type": type(e).__name__,
            "traceback": str(traceback.format_exc())
        }
        app.logger.error(f"Prediction Error: {error_details}")
        
        return jsonify(error_details), 500

if __name__ == '__main__':
    app.run(debug=True)