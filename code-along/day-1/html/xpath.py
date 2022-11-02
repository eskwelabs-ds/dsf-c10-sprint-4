import bs4
from lxml import etree

with open("source/index3.html", "r") as html_file:
    content = html_file.read()

soup = bs4.BeautifulSoup(content, 'lxml')
dom = etree

## Get By ID
print(dom.xpath())

## Get By Class
data = dom.xpath()
for _data in data:
    print(_data.text)
