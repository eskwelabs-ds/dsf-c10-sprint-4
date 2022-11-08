import bs4
import pandas as pd
import requests

from lxml import etree

try:
    response = requests.request("GET", "https://en.wikipedia.org/wiki/Wikipedia:Tambayan_Philippines/Popular_pages")

    if response.status_code == 200:
        soup = bs4.BeautifulSoup(response.text, 'lxml')
        dom = etree.HTML(str(soup))

        data = dom.xpath('//table//tbody//tr')
        popular_pages = []

        for _data in data:
            td_values = _data.findall("td")
            if len(td_values) > 0:
                popular_pages.append({
                    'Rank': td_values[0].text.replace("\n", ""),
                    'Page Title': td_values[1].find("a").text,
                    'Daily Average': td_values[3].text.replace("\n", ""),
                    'Assessment': td_values[4].find("a").text,
                    'Importance': td_values[5].find("a").text,
                })

except Exception as e: 
    print(str(e))

print(pd.DataFrame(popular_pages))

