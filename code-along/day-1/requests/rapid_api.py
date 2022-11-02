import argparse
import requests

class RapidAPI:

    def __init__(self):
        self.hacker_news_url = "https://community-hacker-news-v1.p.rapidapi.com/updates.json"

    def query_hacker_news(self, key, host):
        try:
            querystring = {"print":"pretty"}
            headers = {
                "X-RapidAPI-Key": key,
                "X-RapidAPI-Host": host
            }

            

            
        except Exception as e: 
            print(str(e))



if __name__ == '__main__':
    parser=argparse.ArgumentParser()