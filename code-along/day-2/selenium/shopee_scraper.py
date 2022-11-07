import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

from time import sleep
from webdriver_manager.chrome import ChromeDriverManager


class ShopeeScraper:

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def get_details(self, url):
        result = {
            'title': '',
            'description': '',
            'overall_stars': '',
            'total_ratings': '',
            'total_sold': '',
            'five_star_ratings': '',
            'four_star_ratings': '',
            'three_star_ratings': '',
            'two_star_ratings': '',
            'one_star_ratings': '',
            'followers': '',
        }

        try:
            self.driver.get(url)

            total_height = int(self.driver.execute_script("return document.body.scrollHeight"))
            for i in range(1, total_height, 5):
                self.driver.execute_script("window.scrollTo(0, {});".format(i))

            title_tag = self.driver.find_element(By.CLASS_NAME, '_2rQP1z')
            if len(title_tag) > 0:
                result['title'] = title_tag[0].text

            description_tag = self.driver.find_element(By.CLASS_NAME, '_2jrvqA')
            if len(description_tag) > 0:
                result['title'] = description_tag[0].text

            print(result)

            
        except:
            pass

        return result