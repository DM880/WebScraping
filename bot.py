from bs4 import BeautifulSoup as BS
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

s=Service(ChromeDriverManager().install())

browser = webdriver.Chrome(service=s, options=chrome_options)

url =  input('Enter url: ')

browser.get(url)

soup = BS(browser.page_source,features="html.parser")

video = soup.find_all(['iframe','img','video'])

if video:

    video_url =[]

    for vid in video:
        video_url.append(vid['src' if 'src' else ''])

    print(video_url)