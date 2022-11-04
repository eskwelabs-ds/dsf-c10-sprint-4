import bs4
import pandas as pd
from lxml import etree

with open("source/index4.html", "r") as html_file:
    content = html_file.read()

soup = bs4.BeautifulSoup(content, 'lxml')
dom = etree.HTML(str(soup))

data = dom.xpath("//table[@class='w3-table']//tr")
data_list = list()

for id, _tags in enumerate(data):
    tds = _tags.findall("td")
    if len(tds) > 0:
        data_list.append({
            'First Name': tds[0].text,
            'Last Name': tds[1].text,
            'Points':tds[2].text
        })

print(pd.DataFrame(data_list))
