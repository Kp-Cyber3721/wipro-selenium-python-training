import requests

try:
    data = {
        "category": "Platform",
        "name": "Mario",
        "rating": "Mature",
        "releaseDate": "2012-05-04",
        "reviewScore": 85
    }

    url = "https://videogamedb.uk:443/api/v2/videogame"

    response = requests.post(url, json=data)

    print("Raw Response:", response)

    # Validate status code for POST (should be 201 Created)
    if response.status_code == 201:
        print("Game created successfully")

        # Convert response to JSON
        response_data = response.json()

        print("\nResponse JSON:")
        print(response_data)

        print("\nText:")
        print(response.text)

        print("\nContent:")
        print(response.content)

        print("\nHeaders:")
        print(response.headers)

        print("\nURL:")
        print(response.url)

        print("\nHistory:")
        print(response.history)

        # Get specific header value
        content_type = response.headers.get("Content-Type")
        print("\nContent-Type:", content_type)

        # Capture ID for further requests (PUT/PATCH/DELETE)
        game_id = response_data.get("id")
        print("\nCreated Game ID:", game_id)

    else:
        print("Failed with status code:", response.status_code)
        print(response.text)

except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
