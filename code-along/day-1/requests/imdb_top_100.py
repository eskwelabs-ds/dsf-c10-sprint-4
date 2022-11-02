import bs4
import pandas as pd
import requests

from lxml import etree

try:
    response = requests.request("GET", "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc")

    if response.status_code == 200:
        soup = bs4.BeautifulSoup(response.text, 'lxml')
        dom = etree.HTML(str(soup))

        data = dom.xpath('')
        top_movies = list()
        

        for _data in data:
            rank = _data
            title = _data
            url = _data
            genre = _data
            runtime = _data
            details = _data
            vote = details[0]
            gross = details[1]
            rating = _data

            top_movies.append({
                'rank': rank,
                'title': title,
                'url': url,
                'genre': genre,
                'runtime': runtime,
                'vote': vote,
                'gross': gross,
                'rating': rating
            })

        print(pd.DataFrame(top_movies))

except Exception as e: 
    print(str(e))



