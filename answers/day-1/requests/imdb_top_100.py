import bs4
import pandas as pd
import requests

from lxml import etree

try:
    response = requests.request("GET", "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc")

    if response.status_code == 200:
        soup = bs4.BeautifulSoup(response.text, 'lxml')
        dom = etree.HTML(str(soup))

        data = dom.xpath('//div[@class="lister-item-content"]')
        top_movies = list()
        

        for _data in data:
            rank = _data.find("h3//span").text[:-1]
            title = _data.find("h3//a").text
            url = _data.find("h3//a").get('href')
            genre = _data.find("p//span[@class='genre']").text.strip()
            runtime = _data.find("p//span[@class='runtime']").text.strip()
            details = _data.findall("p//span[@name='nv']")
            vote = details[0].get('data-value')
            gross = details[1].get('data-value')
            rating = _data.find("div//div//strong").text

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



