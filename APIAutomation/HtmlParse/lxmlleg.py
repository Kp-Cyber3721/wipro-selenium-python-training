import requests
from lxml import html
url = "https://news.ycombinator.com"
response = requests.get(url)
data = html.fromstring(response.content)
# Find the <title> tag
title = data.find(".//title")
print(title.text)
#links
links =data.xpath("//a/@href")
print(links)
#links + URLs
links=data.xpath("//a")
for link in links:
    print(link.text)
    print(link.get("href"))

#extract the data  using class name
titlelines = data.xpath("//span[@class = 'titleline']")

print(titlelines)







