import random

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(ChromeDriverManager().install())

target_page = "https://www.rappler.com/topic/covid-19/"
driver.get(target_page)

print(driver.title)
print(driver.current_url)
print(driver.page_source)

driver.quit()