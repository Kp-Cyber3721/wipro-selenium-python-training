from bs4 import BeautifulSoup

html_doc = """
<html>
  <head><title>Test Page</title></head>
  <body>
    <h1>Welcome</h1>
    <p>This is a paragraph.</p>
    <a href="https://example.com">Click Here</a>
  </body>
</html>
"""

# Parse HTML
soup = BeautifulSoup(html_doc, "html.parser")

# Extract title
print("Title:", soup.title.text)

# Extract h1
print("H1:", soup.h1.text)

# Extract paragraph
print("Paragraph:", soup.p.text)

# Find first link
link = soup.find("a")
print("First Link:", link.get("href"))

# Prettify HTML
print("\nFormatted HTML:\n")
print(soup.prettify())

# Difference demo: find_all()
print("\nUsing find_all():")
for tag in soup.find_all("p"):
    print(tag.text)











