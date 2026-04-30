# libraries
import requests
import json
from datetime import datetime
import time

# variables
# url = f"https://api.tfl.gov.uk/BikePoint/"
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
# response = requests.get(url)
# data = response.json() 

# if response.status_code == 200:

#     for item in data:
#         id = item["id"]
#         id_response = requests.get(url+id)
#         id_data = response.json()
        
#         if id_response.status_code == 200:    
#             filename = f"./bikepoints/{id}_{timestamp}.json"
#             with open(filename, "w") as file:
#                 json.dump(id_data, file)
            
#             print(f"File {filename} was successfully created. Woohoo 🥳")
#         else:
#             try: 
#                 print(f"Error: {id_response.status_code} {id_data.get("message","no message found")}")
#             except: 
#                 print(id)
# else:
#     print(f"Error: {response.status_code} {data.get("message","no message found")}")

with open("BikePoints_all_2026-04-29_15-02-41.json", "r") as file:
    data = json.load(file)

failed_items = []

for item in data:
    try:
        id = item["id"]
        filename = f"./bikepoints_from_all/{id}_{timestamp}.json"
        
        with open(filename, "w") as file:
            json.dump(item, file)

        print(f"File {filename} was successfully created. Woohoo 🥳")
    except:
        failed_items.append(item)

print("Total Failed Items:", len(failed_items))
