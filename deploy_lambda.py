import boto3
import os

lambda_client = boto3.client('lambda')
s3_bucket = os.environ['S3_BUCKET']
s3_key = os.environ['S3_KEY']
lambda_function_name = os.environ['LAMBDA_FUNCTION_NAME']

def update_lambda_function():
    response = lambda_client.update_function_code(
        FunctionName=lambda_function_name,
        S3Bucket=s3_bucket,
        S3Key=s3_key,
    )
    print('Lambda function updated:', response)

if __name__ == "__main__":
    update_lambda_function()
