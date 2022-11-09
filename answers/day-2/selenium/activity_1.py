
import pandas as pd
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from time import sleep

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://shopee.ph/Laptops-Computers-cat.11021121")

## Scroll to Show Results
total_height = int(driver.execute_script("return document.body.scrollHeight"))
available_links = []
for i in range(1, total_height, 5):
    driver.execute_script("window.scrollTo(0, {});".format(i))

items = driver.find_elements(By.XPATH, '//div[@class="row shopee-search-item-result__items"]//a')
for _items in items:
    available_links.append(_items.get_attribute('href'))


df = pd.DataFrame({'urls': available_links})
df.to_csv('urls.csv', index=False)