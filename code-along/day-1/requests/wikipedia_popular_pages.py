import bs4
import pandas as pd
import requests

from lxml import etree

try:
    response = requests.request("GET", "https://en.wikipedia.org/wiki/Wikipedia:Tambayan_Philippines/Popular_pages")

    if response.status_code == 200:
        soup = bs4.BeautifulSoup(response.text, "lxml")
        dom = etree.HTML(str(soup))
        popular_pages = []

        data = dom.xpath("//table//tr")

        for _data in data:
            td_values = _data.findall("td")
            if len(td_values) > 5:
                popular_pages.append({
                    'Rank': td_values[0].text,
                    'Page Title': td_values[1].find("a").text,
                    'Views': td_values[2].find("a").text,
                    'Daily Average': td_values[3].text,
                    'Assessment': td_values[4].find("a").text,
                    'Importance': td_values[5].find("a").text,
                })

        print(pd.DataFrame(popular_pages))

except Exception as e: 
    print(str(e))



