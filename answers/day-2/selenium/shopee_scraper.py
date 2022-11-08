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
            ## Scroll to Show Results
            total_height = int(self.driver.execute_script("return document.body.scrollHeight"))
            for i in range(1, total_height, 5):
                self.driver.execute_script("window.scrollTo(0, {});".format(i))

            ### tag search
            title_tag = self.driver.find_elements_by_class_name("_2rQP1z")
            if len(title_tag) > 0:
                result['title'] = title_tag[0].text

            price_tag = self.driver.find_elements_by_class_name("_2Shl1j")
            if len(price_tag) > 0:
                result['price'] = price_tag[0].text.encode("utf-8")

            description_tag = self.driver.find_elements_by_class_name("_2jrvqA")
            if len(description_tag) > 0:
                result['description'] = description_tag[0].text

            ratings_tag = self.driver.find_elements_by_class_name("_3y5XOB")
            if len(ratings_tag) > 1:
                result['total_ratings'] = ratings_tag[0].text
                result['total_sold'] = ratings_tag[1].text

            overall_ratings_tag = self.driver.find_elements_by_class_name("_14izon")
            if len(overall_ratings_tag) > 0:
                result['overall_stars'] = overall_ratings_tag[0].text

            rating_tags = self.driver.find_elements_by_class_name("product-rating-overview__filter")
            if len(rating_tags) > 0:
                result['five_star_ratings'] = rating_tags[1].text
                result['four_star_ratings'] = rating_tags[2].text
                result['three_star_ratings'] = rating_tags[3].text
                result['two_star_ratings'] = rating_tags[4].text
                result['one_star_ratings'] = rating_tags[5].text

            follower_tag = self.driver.find_elements_by_class_name("_1i6OkT")
            if len(follower_tag) > 0:
                result['followers'] = follower_tag[0].text

        except:
            pass


        return result


        
           

    

        

        