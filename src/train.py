import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.datasets import fetch_california_housing
import boto3
import joblib
import os

# Load dataset
housing = fetch_california_housing()
data = pd.DataFrame(housing.data, columns=housing.feature_names)
data['Price'] = housing.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(data.drop(columns=["Price"]), data["Price"], test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Save model to S3
model_dir = "/opt/ml/model"
os.makedirs(model_dir, exist_ok=True)
model_path = os.path.join(model_dir, "model.joblib")
joblib.dump(model, model_path)

# Upload to S3
s3 = boto3.client("s3")
s3.upload_file(model_path, "my-sagemaker-bucket", "california-housing/model.joblib")