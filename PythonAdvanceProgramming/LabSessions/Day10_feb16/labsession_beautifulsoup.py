from bs4 import BeautifulSoup
import requests

html = """
<html>
<head><title>My Page</title></head>
<body>
<h1>Welcome</h1>
<h2>Subheading</h2>
<p>Para 1</p>
<p>Para 2</p>
<a href="https://google.com">Google</a>
<a href="https://example.com">Example</a>
<b>Bold 1</b>
<b>Bold 2</b>
<table>
<tr><th>Name</th><th>Age</th></tr>
<tr><td>John</td><td>25</td></tr>
<tr><td>Anna</td><td>30</td></tr>
</table>
<img src="img1.png">
<img src="img2.png">
</body>
</html>
"""
soup = BeautifulSoup(html, "html.parser")

# 1 Title and H1
print("Title:", soup.title.text)
print("H1:", soup.h1.text)

# 2 Paragraphs
print("\nParagraphs:", [p.text for p in soup.find_all("p")])

# 3 Links + Count
links = soup.find_all("a")
print("\nLinks Count:", len(links))

# 4 Attributes
print("First Link Attr:", links[0].attrs)

# 5 First h2
print("H2:", soup.find("h2").text)

# 6 Bold Text
print("Bold:", [b.text for b in soup.find_all("b")])

# 7 href values
print("Hrefs:", [a["href"] for a in links])

# 8 All Text
print("\nAll Text:", soup.get_text())

# 9 Title from Website
url = "https://www.wikipedia.org"
res = requests.get(url, headers={"User-Agent": "Chrome/120.0.0.0"})
web = BeautifulSoup(res.text, "html.parser")
print("\nWebsite Title:", web.title.text if web.title else "No title")

# 10 All Headings
print("\nHeadings:", [h.text for h in soup.find_all(["h1","h2","h3"])])

# 11 Table Data
for row in soup.find_all("tr"):
    print([c.text for c in row.find_all(["td","th"])])

# 12 Images
print("\nImages:", [img["src"] for img in soup.find_all("img")])
