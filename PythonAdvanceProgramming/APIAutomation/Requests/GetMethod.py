import requests
from requests.auth import HTTPBasicAuth

try:
    url = "https://videogamedb.uk:443/api/v2/videogame"

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.get(
        url,
        auth=HTTPBasicAuth('username', 'password'),
        headers=headers,
        timeout=5
    )

    print(response)

    if response.status_code == 200:
        print("Status code is 200 OK")
        data = response.json()
        print(data)
    else:
        print(f"Error: Received status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
