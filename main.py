import os
from dotenv import load_dotenv
from pathlib import Path
from modules.log import setup_logging
from modules.extract import extract
from modules.load import upload_to_s3

# Start logging
logger = setup_logging()
logger.info('Logger initialized')

# Make API call
url = f"https://api.tfl.gov.uk/BikePoint/"

# Load environment variables from a .env file
load_dotenv()
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
bucket = os.getenv('AWS_BUCKET_NAME')

if extract(url, 3, 'data'):
    data_dir = Path('data')
    upload_to_s3(AWS_ACCESS_KEY, AWS_SECRET_KEY, bucket, data_dir)
else:
    logger.error('Extract failed. End of script.')