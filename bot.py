from bs4 import BeautifulSoup as BS
from selenium import webdriver
import validators

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd

# Set up Chrome

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

s = Service(ChromeDriverManager().install())

browser = webdriver.Chrome(service=s, options=chrome_options)

# Prompt user for url

url = input("Enter url: ")

# Check if url is valid

if not validators.url(url):
    while not validators.url(url):
        url = input("Enter valid url: ")

# Start scraping

browser.get(url)

soup = BS(browser.page_source, "html.parser")

video = soup.find_all(["iframe", "img", "video", "div"], {"src": True})

video_url = []

for vid in video:
    source = vid.attrs["src"]

    video_url.append(source)

# Use panda for dataframe and download

list_url = {'url':video_url}

datas = pd.DataFrame(list_url)

datas.to_csv('url_scraped.csv')

print(video_url)

browser.quit()