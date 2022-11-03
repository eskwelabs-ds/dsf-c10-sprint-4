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

        except:
            pass

        return result