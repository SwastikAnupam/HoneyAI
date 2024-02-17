from flask import Flask, request
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import json

app = Flask(__name__)

# Placeholder for preprocessing incoming data
def preprocess_data(data):
    # Convert data to a format suitable for the NN
    # This is highly simplified; actual implementation will vary based on the data
    return np.array([np.zeros(10)])  # Example: returning a dummy array

# Create a simple LSTM model
def create_model():
    model = Sequential([
        LSTM(64, input_shape=(1, 10)),  # Adjust based on your input shape
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

# Global model variable
model = create_model()

# Example route to simulate vulnerable endpoint
@app.route('/vulnerable', methods=['POST'])
def vulnerable_endpoint():
    data = request.json
    preprocessed_data = preprocess_data(data)
    prediction = model.predict(preprocessed_data)
    
    # Assuming a binary classification: 0 for normal, 1 for anomalous
    if prediction[0][0] > 0.5:
        response = {"message": "Anomalous behavior detected."}
    else:
        response = {"message": "Normal behavior."}
    
    # Placeholder for online learning update mechanism
    # update_model(model, preprocessed_data, labels)  # labels to be defined
    
    return json.dumps(response)

# Function to update the model - assumes existence of labels which is complex in real-time scenarios
def update_model(model, data, labels):
    # This should be implemented with care to avoid data leakage and ensure model integrity
    pass

if __name__ == '__main__':
    app.run(debug=True, port=5000)
