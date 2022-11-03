import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from time import sleep

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://rapidapi.com/auth?referral=/hub")
sleep(5)
driver.implicitly_wait(30)
login_btn = driver.find_element(By.CLASS_NAME, "----------------------------------")



email = driver.find_element_by_id('----------------')
password = driver.find_element_by_id('----------------------------')

email.send_keys('------------------------')
password.send_keys('-------------------------')
login_btn.click()

sleep(10)

print(driver.current_url)
print(driver.page_source.encode("utf-8"))


driver.quit()