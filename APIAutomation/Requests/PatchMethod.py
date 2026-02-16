import requests

try:
    base_url = "https://api.restful-api.dev/objects"

    create_payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2023,
            "price": 2500,
            "CPU model": "M2",
            "Hard disk size": "1 TB"
        }
    }

    headers = {"Content-Type": "application/json"}

    post_response = requests.post(base_url, json=create_payload, headers=headers)
    print("POST Status:", post_response.status_code)

    post_data = post_response.json()
    object_id = post_data["id"]

    print("Created ID:", object_id)

    patch_url = f"{base_url}/{object_id}"

    patch_payload = {
        "name": "Apple MacBook Pro 16 (Updated Name)"
    }

    patch_response = requests.patch(patch_url, json=patch_payload, headers=headers)
    print("PATCH Status:", patch_response.status_code)
    print("PATCH Response:", patch_response.json())

    get_response = requests.get(patch_url)
    print("GET Status:", get_response.status_code)
    print("Final Object:", get_response.json())

except requests.exceptions.RequestException as e:
    print("Error:", e)
