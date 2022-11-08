import bs4
import pandas as pd
from lxml import etree

with open("source/index4.html", "r") as html_file:
    content = html_file.read()

soup = bs4.BeautifulSoup(content, 'lxml')
dom = etree.HTML(str(soup))

data = dom.xpath('//table[@class="w3-table"]//tr')
data_list = list()
for _data in data:
    td_values = _data.findall("td")

    if len(td_values) > 0:
        data_list.append({
            'First Name': td_values[0].text,
            'Last Name': td_values[1].text,
            'Points': td_values[2].text
        })

print(pd.DataFrame(data_list))
