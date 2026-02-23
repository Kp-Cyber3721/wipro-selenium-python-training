#Section 1: Basic Level
#1. Write a Python script to send a GET request to https://jsonplaceholder.typicode.com/users and print only name and email.
import requests
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
users = response.json()
for user in users:
    print(f"Name: {user['name']}, Email: {user['email']}")


#2. Send a GET request with query parameter userId=2 and print number of posts returned.
import requests
url = "https://jsonplaceholder.typicode.com/posts"
params = {"userId": 2}
response = requests.get(url, params=params)
posts = response.json()
print("Number of posts:", len(posts))


#3. Write a POST request to create a new resource and verify status code 201.
import requests
url = "https://jsonplaceholder.typicode.com/posts"
payload = {
    "title": "API Testing",
    "body": "Learning POST request",
    "userId": 1
}
response = requests.post(url, json=payload)
print("Status Code:", response.status_code)
if response.status_code == 201:
    print("Resource created successfully!")


#4. Explain the difference between data= and json= in requests.post().


#5. Write code to check if response status code is not 200 and raise an exception.
import requests
response = requests.get("https://jsonplaceholder.typicode.com/users")
if response.status_code != 200:
    raise Exception(f"Request Failed! Status Code: {response.status_code}")
print("Request Successful")



#Section 2: Intermediate Level
#6. Fetch all users and print usernames in uppercase.
import requests
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
for user in response.json():
    print(user["username"].upper())


#7. Implement timeout handling (2 seconds) and catch Timeout exception
import requests
from requests.exceptions import Timeout
try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users",
        timeout=2
    )
    print("Request Successful")
except Timeout:
    print("Request timed out after 2 seconds!")


#8. Use Session object to send multiple requests and demonstrate cookie persistence.
import requests

session = requests.Session()
# First request
response1 = session.get("https://httpbin.org/cookies/set/sessionid/12345")
# Second request
response2 = session.get("https://httpbin.org/cookies")
print("Cookies persisted:", response2.json())


#9. Upload a file using requests and print server response.




#10. Fetch posts and save response JSON into a file named posts.json.
import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

posts = response.json()

with open("posts.json", "w") as file:
    json.dump(posts, file, indent=4)

print("Posts saved to posts.json")

