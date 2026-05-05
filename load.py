# libraries
import os
import boto3
import logging
from datetime import datetime
from dotenv import load_dotenv
from pathlib import Path

# Configure logs
log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
log_filename = f"{log_dir}/load_{timestamp}.log"

logging.basicConfig(
    filename=log_filename,
    format='%(asctime)s - %(levelname)s - %(message)s',    # format as time, level, and message
    level=logging.INFO                                      # lowest level you want to capture with logs
)

logger = logging.getLogger()
logger.info('Logger initialized')

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

data_dir = Path('data')
files = list(data_dir.glob('*.json'))

for file in files:
    filename = os.path.basename(file)
    s3_client.upload_file(file, bucket, filename)
    logger.info(f"{file} uploaded to S3")
