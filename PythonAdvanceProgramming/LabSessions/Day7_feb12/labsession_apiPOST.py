import requests
try:
    url = "https://videogamedb.uk:443/api/v2/videogame"
    payload = {
  "category": "Platform",
  "name": "Mario",
  "rating": "Mature",
  "releaseDate": "2012-05-04",
  "reviewScore": 85
}
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers, timeout=10)
    print("Response Status:", response.status_code)
    if response.status_code == 201 or response.status_code == 200:
        print("Data created successfully")
        data = response.json()
        print("Response JSON:", data)
    else:
        print(f"Error: Received status code {response.status_code}")
        print("Response:", response.text)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
