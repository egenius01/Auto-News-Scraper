"""
Extracting User Bio of the username in the input, only activer users
"""
import requests
from bs4 import BeautifulSoup

username = input("Enter Username: ")
url = f"https://www.github.com/{str(username)}"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
for tag_content in soup.findAll(
    "article",
    attrs={"class": "markdown-body entry-content container-lg f5", "itemprop": "text"},
):
    print(tag_content.text)

else:
    print("NOT FOUND")
