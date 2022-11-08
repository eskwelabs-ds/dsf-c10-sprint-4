import random

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from time import sleep

from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument("--headless")
# options.add_argument("--start-maximized")
# options.add_argument("--disable-notifications")
# options.add_argument("--incognito")

driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
# sleep(random.randint(12, 18))
target_page = "https://www.rappler.com/topic/covid-19/"
driver.get(target_page)


### Browser Details
# print(driver.title)
# print(driver.current_url)
print(driver.page_source)

driver.quit()