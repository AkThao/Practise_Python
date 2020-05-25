import requests
from bs4 import BeautifulSoup

url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
r = requests.get(url)
html = r.text

soup = BeautifulSoup(html, "html.parser")

article_text = []

for text in soup.findAll("p"):
    article_text.append(str(text.getText()))

with open("saved_article.txt", "w") as open_file:
    open_file.write("\n\n".join(article_text))