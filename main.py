# libraries
import requests
import json
import time
import os
import logging 
from datetime import datetime

# logging
log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
log_filename = f"{log_dir}/log_{timestamp}.log"

logging.basicConfig(
    filename=log_filename,
    format='%(asctime)s - %(levelname)s - %(message)s',    # format as time, level, and message
    level=logging.DEBUG                                      # lowest level you want to capture with logs
)

logger = logging.getLogger()
logger.info('Logger initialized')

# variables
url = f"https://api.tfl.gov.uk/BikePoint/"
response = requests.get(url)
data = response.json()

count = 0
max_tries = 3

while count <= max_tries:

    if 200 <= response.status_code < 300:

        dir = 'data'
        os.makedirs(dir, exist_ok=True)
        filename = f"{dir}/bikepoints_{timestamp}.json"
        with open(filename, "w") as file:
            json.dump(data, file)
            
        logger.info(f"File {filename} was successfully created. Woohoo!")
        break

    elif response.status_code >= 500:
        # RETRY after 10 seconds for these status codes
        time.sleep(10)
        count+=1
        logger.info(f"Attempt #{count} to call {url}")

    else:
        logger.info(f"Error: {response.status_code} {data.get("message","no message found")}")
        break
