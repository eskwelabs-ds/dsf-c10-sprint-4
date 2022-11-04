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

            response= requests.get(self.hacker_news_url, headers=headers, params=querystring)
            print(response.text)
            print(response.status_code)

        except Exception as e: 
            print(str(e))


if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--key')
    parser.add_argument('--hosts')
    args=parser.parse_args()
    rapid_api = RapidAPI()
    result = rapid_api.query_hacker_news(args.key, args.hosts)
    print(result)
