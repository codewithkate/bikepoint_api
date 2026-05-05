# libraries
from dotenv import load_dotenv
import boto3
import os

# Load environment variables from a .env file
load_dotenv()

# Store access credentials
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
bucket = os.getenv("AWS_BUCKET_NAME")

# Create a boto3 client/resource
s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY
)

data = "data/bikepoints_2026-05-05_10-29-27.json"
filename = "bikepoints_2026-05-05_10-29-27.json"

s3_client.upload_file(data, bucket, filename)
