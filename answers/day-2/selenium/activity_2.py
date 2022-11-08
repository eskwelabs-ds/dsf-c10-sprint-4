
import pandas as pd
from shopee_scraper import ShopeeScraper


df = pd.read_csv('urls.csv')
shopee_scraper = ShopeeScraper()

for index, row in df.iterrows():
    result = shopee_scraper.get_details(row['urls'])