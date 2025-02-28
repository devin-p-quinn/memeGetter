import requests
from bs4 import BeautifulSoup
import urllib.request

url = "https://www.reddit.com/r/DogPics/"

response = requests.get(url)

if response.status_code != 200:
    print(f"Status: {response.status_code} — Try rerunning the code\n")
else:
    print(f"Status: {response.status_code}\n")

soup = BeautifulSoup(response.content, "html.parser")

images = soup.find_all("img", attrs = {"alt": "Post image"})

number = 0

for image in images:
	image_src = image["src"]
	print(image_src)
	urllib.request.urlretrieve(image_src, str(f"Pic{number}"))
	number += 1