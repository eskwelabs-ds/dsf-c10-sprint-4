import bs4
import pandas as pd
import requests

from lxml import etree

try:
    response = requests.request("GET", "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc")

    if response.status_code == 200:
        soup = bs4.BeautifulSoup(response.text, 'lxml')
        dom = etree.HTML(str(soup))

        data = dom.xpath("//div[@class='lister-item-content']")
        top_movies = list()
        
        for _data in data:
            rank = _data.find("h3//span").text[:-1]
            title = _data.find("h3//a").text
            url = _data.find("h3//a").get("href")
            genre = _data.find("p//span[@class='genre']").text
            runtime =  _data.find("p//span[@class='runtime']").text
            details = _data
            vote = _data.findall('p[@class="sort-num_votes-visible"]/span[@name="nv"]')[0].text
            gross = _data.findall('p[@class="sort-num_votes-visible"]/span[@name="nv"]')[1].text
            # rating = _data

            top_movies.append({
                'rank': rank,
                'title': title,
                'url': url,
                'genre': genre,
                'runtime': runtime,
                'vote': vote,
                'gross': gross,
                # 'rating': rating
            })

        print(pd.DataFrame(top_movies))

except Exception as e: 
    print(str(e))



