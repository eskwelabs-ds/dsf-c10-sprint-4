import bs4
from lxml import etree

with open("source/index3.html", "r") as html_file:
    content = html_file.read()

soup = bs4.BeautifulSoup(content, 'lxml')
dom = etree.HTML(str(soup))

print(dom.xpath('//div[@id="sample-1"]//p')[0].text)

data = dom.xpath('//div[@class="w3-container"]//div//p')
for _data in data:
    print(_data.text)
