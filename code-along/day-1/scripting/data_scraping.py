class DataScraping:

    def __init__(self):
        self.filename='test.csv'
    
    def get_twitter_data(self):
        return self.filename


if __name__ == '__main__':
    data_scraping = DataScraping()
    results = data_scraping.get_twitter_data()
    print(results)