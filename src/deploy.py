import boto3
import time
from sagemaker import get_execution_role
from sagemaker.model import Model
from sagemaker.predictor import Predictor

# Load model from S3
model_data = "s3://my-sagemaker-bucket/california-housing/model.joblib"

# Create SageMaker model
role = get_execution_role()
model = Model(
    model_data=model_data,
    role=role,
    image_uri="123456789012.dkr.ecr.us-west-2.amazonaws.com/my-custom-image:latest",  # Replace with your custom image
    predictor_cls=Predictor
)

# Deploy model to endpoint
endpoint_name = "california-housing-endpoint"
model.deploy(
    initial_instance_count=1,
    instance_type="ml.m5.large",
    endpoint_name=endpoint_name
)

# Wait for endpoint to be in service
client = boto3.client("sagemaker")
waiter = client.get_waiter("endpoint_in_service")
waiter.wait(EndpointName=endpoint_name)

print(f"Endpoint {endpoint_name} is now in service.")