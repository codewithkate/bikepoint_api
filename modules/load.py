import os
import boto3
import logging
from datetime import datetime
from dotenv import load_dotenv
from pathlib import Path

logger = logging.getLogger(__name__)

def upload_to_s3(aws_access_key_id, aws_secret_access_key, bucket, data_dir=Path('data')):
    """
    This will load any json files int eh data directory to a specified s3 bucket.

    Args:
        aws_access_key_id (str): The AWS access key ID attatched to an IAM User, with relevant permissions.
        aws_secret_access_key (str): The AWS secret access key attachted to an IAM User, with relevant permissions.
        bucket (str): The name of the S3 bucket.
        data_dir ('pathlib.WindowsPath'): Must be a complete filepath for the idrectory where the json files are located. Defaults to Path('data'). 

    Returns:
        None
    """    
    # Create a boto3 client/resource
    s3_client = boto3.client(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )

    # Upload file to the S3 bucket
    files = list(data_dir.glob('*.json'))

    processed = 0

    for file in files:
        filename = os.path.basename(file)
        try:
            s3_client.upload_file(file, bucket, filename)
            logger.info(f'{file} uploaded to S3')
            s3_client.head_object(Bucket=bucket, Key=filename) # only return metadata
            os.remove(file)
            logger.info(f'{file} deleted')
            processed+=1
        except Exception as e:
            logging.error(e)

    logging.info(f'{processed} files uploaded')