import requests
from bs4 import BeautifulSoup

url_1 = "http://www.practicepython.org/assets/primenumbers.txt"
url_2 = "http://www.practicepython.org/assets/happynumbers.txt"

r_1 = requests.get(url_1)
r_2 = requests.get(url_2)

html_1 = r_1.text
html_2 = r_2.text

with open("primeslist.txt", "w") as open_file:
    open_file.write(html_1)

with open("happieslist.txt", "w") as open_file:
    open_file.write(html_2)