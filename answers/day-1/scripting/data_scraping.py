class DataScraping:

    def __init__(self):
        self.filename = 'test.csv'

    def get_twitter(self):
        return self.filename

    def get_reddit(self, username):
        return username

if __name__ == '__main__':
    data_scraping = DataScraping()
    twitter_data = data_scraping.get_twitter()
    print(twitter_data)

    reddit_data = data_scraping.get_reddit('test_username')
    print(reddit_data)