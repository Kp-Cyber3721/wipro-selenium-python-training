import requests

try:
    url = "https://videogamedb.uk:443/api/v2/videogame/1"

    response = requests.delete(url, timeout=10)

    print("Status Code:", response.status_code)

    if response.status_code == 200 or response.status_code == 204:
        print("Record deleted successfully")

    elif response.status_code == 404:
        print("Record not found")

    else:
        print(f"Unexpected status code: {response.status_code}")
        print(response.text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
