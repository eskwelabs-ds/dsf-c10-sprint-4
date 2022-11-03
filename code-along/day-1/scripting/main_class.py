from data_scraping import DataScraping
from data_cleaning import DataCleaning

if __name__ == '__main__':
    data_scraping = DataScraping()
    results = data_scraping.get_twitter_data()
    print(results)

    data_cleaning = DataCleaning()
    lower_data = data_cleaning.to_lowercase('Testing Message Main  ')
    print(lower_data)