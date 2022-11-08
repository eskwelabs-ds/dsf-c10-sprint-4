import argparse
import getpass
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from time import sleep

from webdriver_manager.chrome import ChromeDriverManager

class Password:

    DEFAULT = 'Prompt if not specified'

    def __init__(self, value):
        if value == self.DEFAULT:
            value = getpass.getpass('Password: ')
        self.value = value

    def __str__(self):
        return self.value


def login(given_username, given_password):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://rapidapi.com/auth?referral=/hub")
    sleep(5)
    driver.implicitly_wait(30)
    login_btn = driver.find_element(By.CLASS_NAME, "login-form-button")

    email = driver.find_element_by_id('login-form_email')
    password = driver.find_element_by_id('login-form_password')

    email.send_keys(given_username)
    password.send_keys(str(given_password))
    login_btn.click()

    sleep(10)

    print(driver.current_url)
    print(driver.page_source.encode("utf-8"))

    driver.quit()

    return driver.page_source.encode("utf-8")


if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--username', )
    parser.add_argument('--password', type=Password,  default=Password.DEFAULT)
    args=parser.parse_args()

    html_files=login(args.username, args.password)