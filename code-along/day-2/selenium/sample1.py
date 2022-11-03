import ---------------------------

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import --------------------------------------------
from webdriver_manager.chrome import -----------------------------

driver = webdriver.Chrome(-------------------------.install())

target_page = "https://www.rappler.com/topic/covid-19/"
driver.get(target_page)

driver.quit()