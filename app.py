from flask import Flask, request, jsonify
import mlflow.pyfunc
import pandas as pd
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load the MLflow model
# Set MLflow tracking URI
mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI"))
MODEL_PATH = 'runs:/2c83bc91ac874492a60025ddd11d8df3/model'
try:
    logger.info("Loading model from MLflow...")
    model = mlflow.pyfunc.load_model(MODEL_PATH)
    logger.info("Model loaded successfully.")
except Exception as e:
    logger.error(f"Error loading model: {e}")
    raise
#model = mlflow.pyfunc.load_model(MODEL_PATH)

# Initialize Flask app
app = Flask(__name__)

@app.route('/test', methods=['GET'])
def test():
    logger.info("Entered /test endpoint")
    return jsonify({'message': 'Flask app is working!'})
    
# Define prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    logger.info("Entered /predict endpoint")  # Add this line
    try:
        # Log the incoming request
        logger.info("Received a POST request at /predict")
        input_data = request.json
        logger.info(f"Input data: {input_data}")

        # Convert input data to DataFrame
        input_df = pd.DataFrame(input_data)
        logger.info(f"Input DataFrame:\n{input_df}")

        # Make predictions
        predictions = model.predict(input_df)
        logger.info(f"Predictions: {predictions}")

        # Return predictions as JSON
        return jsonify({'predictions': predictions.tolist()})
    except Exception as e:
        logger.error(f"Error during prediction: {e}")
        return jsonify({'error': str(e)}), 500

# Health check endpoint
@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5008)