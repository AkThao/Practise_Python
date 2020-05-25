import requests
from bs4 import BeautifulSoup

url = "https://www.nytimes.com"
r = requests.get(url)
html = r.text

soup = BeautifulSoup(html, "html.parser")

articles_1 = soup.findAll(["article", "h2"])
for article in articles_1:
    try:
        print(article.find("p").text)
    except:
        pass

articles_2 = soup.findAll("h2")
for article in articles_2:
    try:
        print(article.text)
    except:
        pass

"""for story_heading in soup.find_all(class_="story-heading"):
    if story_heading.a:
        print(story_heading.a.text.replace("\n", " ").strip())
    else:
        print(story_heading.contents[0].strip())""" # Doesn't work, class names have probably changed