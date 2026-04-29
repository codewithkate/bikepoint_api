# libraries
import requests
import json
from datetime import datetime

# variables
# id =  "BikePoints_888"
url = f"https://api.tfl.gov.uk/BikePoint/"
response = requests.get(url)
data = response.json()
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

if response.status_code == 200:
    filename = f"BikePoints_all_{timestamp}.json"
    with open(filename, "w") as file:
        json.dump(data, file)
    
    print(f"File {filename} was successfully created. Woohoo 🥳")

else:
    print(f"Error: {response.status_code} {data.get("message","no message found")}")
