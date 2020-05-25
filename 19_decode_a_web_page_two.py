import requests
from bs4 import BeautifulSoup

url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
r = requests.get(url)
html = r.text

soup = BeautifulSoup(html, "html.parser")

for text in soup.findAll("p"):
    print(str(text.getText()))