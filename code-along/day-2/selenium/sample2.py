import bs4
import random

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
# sleep(random.randint(12, 18))

target_page = "https://www.rappler.com/topic/covid-19/"
driver.get(target_page)
driver.maximize_window()

page_source = ----------------
soup = bs4.BeautifulSoup(page_source, '----------------------')

data = soup.select('--------------------')
for _data in data:
    link_info = _data.select('h2 > a')
    if len(link_info) > 0:
        print('URL', link_info[0]['href'])
        print('Title', link_info[0].text.strip())

        time_info = _data.find('time')
        print('Time', time_info.text.strip())

