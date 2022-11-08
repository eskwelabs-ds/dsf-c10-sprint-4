from data_scraping import DataScraping
from data_cleaning import DataCleaning

if __name__ == '__main__':
    data_scraping = DataScraping()
    twitter_data = data_scraping.get_twitter()
    print(twitter_data)

    reddit_data = data_scraping.get_reddit('test_username')
    print(reddit_data)
    