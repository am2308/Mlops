import json
import boto3

# Initialize SageMaker runtime client
sagemaker_runtime = boto3.client('sagemaker-runtime')

def lambda_handler(event, context):
    # Extract input data from the API Gateway request
    input_data = event['body']
    
    # Invoke the SageMaker endpoint
    response = sagemaker_runtime.invoke_endpoint(
        EndpointName='housepricing',  # Replace with your endpoint name
        ContentType='text/csv',
        Body=input_data
    )
    
    # Parse the response
    result = response['Body'].read().decode('utf-8')
    
    # Return the prediction
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }