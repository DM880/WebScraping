import requests
import urllib3
from bs4 import BeautifulSoup as BS

url =  input('Enter url: ')
data = urllib3.ulropen(url)

html = data.read()

soup = BS(html)
video = soup.find('video')
src = video['src']

print(video)