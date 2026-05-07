import logging
import requests
import os
import time
import json
from datetime import datetime

logger = logging.getLogger(__name__)

def extract(url, max_tries=3, dir='data'):
    '''
    This will call an api. If there's a server side issue it will retry for the specified number of times.
    The data will be saved in the specified directory

    Args:
        url (str): URL to call
        max_tries (int): Number of times to retry if there's a server side error.
        dir (str): Directory to save data to.
    '''
    # variables
    url = url
    response = requests.get(url)
    data = response.json()
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    count = 0

    while count <= max_tries:

        if 200 <= response.status_code < 300:

            os.makedirs(dir, exist_ok=True)
            filename = f'{dir}/{timestamp}.json'
            with open(filename, 'w') as file:
                json.dump(data, file)
                
            logger.info(f'File {filename} was successfully created.')
            return True
            break

        elif response.status_code >= 500:
            # RETRY after 10 seconds for these status codes
            time.sleep(10)
            count+=1
            logger.info(f'Attempt #{count} to call {url}')

        else:
            logger.info(f'Error: {response.status_code}')
            return False
            break
