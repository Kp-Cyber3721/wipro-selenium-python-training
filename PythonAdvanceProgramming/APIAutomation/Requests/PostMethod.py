import requests

try:
    url = "https://videogamedb.uk:443/api/v2/videogame"

    payload = {
        "name": "Spider-Man",
        "releaseDate": "2018-09-07",
        "reviewScore": 9,
        "category": "Action",
        "rating": "PG-13"
    }

    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers, timeout=10)

    print("Response Status:", response.status_code)

    if response.status_code in [200, 201]:
        data = response.json()
        game_id = data["id"]

        print("Record created successfully")
        print("New Game ID:", game_id)

    else:
        print(f"Error: Received status code {response.status_code}")
        print(response.text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
