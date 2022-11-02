import bs4
import pandas as pd
import requests

from lxml import etree

try:
    response = requests.request( "https://en.wikipedia.org/wiki/List_of_highest-grossing_Japanese_films")
    popular_pages = []

    if response == 200:
        soup = bs4.BeautifulSoup(response.text, 'lxml')
        dom = etree.HTML(str(soup))
        data = dom.xpath()

        for _data in data[:51]:
            td_values = _data
            if len(td_values) > 1:
                title = td_values[0]

                if title is None:
                    title = td_values[0]

                popular_pages.append({
                    'Title': title.text,
                    'Worldwide Gross': td_values[1].text.replace("\n", ""),
                    'Year': td_values[2].text.replace("\n", ""),
                })

    print(pd.DataFrame(popular_pages))

except Exception as e: 
    print(str(e))



