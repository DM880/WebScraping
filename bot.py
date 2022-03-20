import requests
import urllib.request
from bs4 import BeautifulSoup as BS

url =  input('Enter url: ')
data =  urllib.request.urlopen(url)

html = data.read()

soup = BS(html, features="html5lib")
video = soup.find_all('div')

print(video)