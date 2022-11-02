import bs4
import pandas as pd
from lxml import etree

with open("source/index4.html", "r") as html_file:
    content = html_file.read()

soup = bs4.BeautifulSoup(content, 'lxml')
dom = etree.HTML(str(soup))

data = dom.xpath()
data_list = list()


print(pd.DataFrame(data_list))
