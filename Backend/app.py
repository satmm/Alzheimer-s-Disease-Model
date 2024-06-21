from flask import Flask, request, jsonify
from flask_cors import CORS
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.optimizers import Adam
import numpy as np
import os

# Load the model without the optimizer
model = load_model('alzheimers_model.keras', compile=False)

# Compile the model with a new optimizer
model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])

# Class labels
class_labels = {0: 'Mild Dementia', 1: 'Moderate Dementia', 2: 'Non Dementia', 3: 'Very Mild Dementia'}

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Add this line to enable CORS

# Ensure the uploads directory exists
if not os.path.exists('uploads'):
    os.makedirs('uploads')

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if file:
        # Save the file
        filepath = os.path.join('uploads', file.filename)
        file.save(filepath)

        # Preprocess the image
        img = load_img(filepath, target_size=(224, 224, 3))
        img = img_to_array(img)
        img = img / 255.0
        img = np.expand_dims(img, axis=0)

        # Predict the class
        predictions = model.predict(img)
        predicted_class = np.argmax(predictions, axis=1)[0]
        probability = round(np.max(predictions) * 100, 2)

        result = {
            'prediction': class_labels[predicted_class],
            'probability': probability
        }

        return jsonify(result)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.optimizers import Adam
from flask_cors import CORS
import numpy as np
import os

# Load the model without the optimizer
model = load_model('alzheimers_model.keras', compile=False)

# Compile the model with a new optimizer
model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])

# Class labels
class_labels = {0: 'Mild Dementia', 1: 'Moderate Dementia', 2: 'Non Dementia', 3: 'Very Mild Dementia'}

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Ensure the uploads directory exists
if not os.path.exists('uploads'):
    os.makedirs('uploads')

# Define the home route
@app.route('/')
def home():
    return "Flask backend is running"

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if file:
        # Save the file
        filepath = os.path.join('uploads', file.filename)
        file.save(filepath)

        # Preprocess the image
        img = load_img(filepath, target_size=(224, 224))
        img = img_to_array(img)
        img = img / 255.0
        img = np.expand_dims(img, axis=0)

        # Predict the class
        predictions = model.predict(img)
        predicted_class = np.argmax(predictions, axis=1)[0]
        probability = round(np.max(predictions) * 100, 2)

        result = {
            'prediction': class_labels[predicted_class],
            'probability': probability
        }

        return jsonify(result)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
