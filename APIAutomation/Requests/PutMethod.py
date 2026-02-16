import requests

try:
    url = "https://videogamedb.uk:443/api/v2/videogame/0"

    payload = {
        "id": 0,
        "name": "Updated Game",
        "releaseDate": "2020-10-10",
        "reviewScore": 8,
        "category": "Adventure",
        "rating": "PG"
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.put(url, json=payload, headers=headers, timeout=10)

    print("Status Code:", response.status_code)

    if response.status_code == 200:
        print("Record updated successfully")
        data = response.json()
        print(data)

    elif response.status_code == 404:
        print("Record not found")

    else:
        print(f"Unexpected status code: {response.status_code}")
        print(response.text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
