import requests
from bs4 import BeautifulSoup

URL =  input('Enter url: ')
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
html = soup.find_all("div")

print(html.prettify())