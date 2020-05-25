import requests
from bs4 import BeautifulSoup

url_1 = "http://www.practicepython.org/assets/nameslist.txt"
r_1 = requests.get(url_1)
html_1 = r_1.text

url_2 = "http://www.practicepython.org/assets/Training_01.txt"
r_2 = requests.get(url_2)
html_2 = r_2.text

with open("nameslist.txt", "w") as open_file:
    open_file.write(html_1)

with open("imageslist.txt", "w") as open_file:
    open_file.write(html_2)