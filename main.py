# libraries
import requests
import json
import time
import os
import logging 
from datetime import datetime

# variables
url = f"https://api.tfl.gov.uk/BikePoint/"
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
response = requests.get(url)
data = response.json()

count = 0
max_tries = 3

while count <= max_tries:

    if 200 <= response.status_code < 200:

        dir = 'data'
        os.makedirs(dir, exist_ok=True)
        filename = f"{dir}/bikepoints_{timestamp}.json"
        with open(filename, "w") as file:
            json.dump(data, file)
            
        print(f"File {filename} was successfully created. Woohoo 🥳")
        break

    elif response >= 500:
        # RETRY after 10 seconds for these status codes
        time.sleep(10)
        count+=1
        print(f"Attempt #{count} to call {url}")

    else:
        print(f"Error: {response.status_code} {response.get("message","no message found")}")
        break
