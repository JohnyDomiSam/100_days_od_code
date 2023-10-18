import requests
from datetime import datetime

# Create user
pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "asdfgsagfsagsadgfdsaasfd"
USER_NAME = "johnydomidam"
u_parameters = {"token": TOKEN,
                "username": USER_NAME,
                "agreeTermsOfService": "yes",
                "notMinor": "yes"
                }

# response = requests.post(url=pixela_endpoint, json=u_parameters)

# Create a graph definition
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {"id": "graph1",
                "name": "Cycling Graph",
                "unit": "Km",
                "type": "float",
                "color": "shibafu"}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

# Create a new pixel
today = datetime.now()
km_cycled = "8.5"
f_today = today.strftime("%Y%m%d")
pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/graph1"
pixel_config = {"date": f_today,
                "quantity": km_cycled
                }
# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)

# Change an existing pixel
put_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/graph1/{f_today}"
put_config = {"quantity": "8.8"}
# response = requests.put(url=put_endpoint, json=put_config, headers=headers)

# Delete the pixel
# response = requests.delete(url=pixel_endpoint, headers=headers)

