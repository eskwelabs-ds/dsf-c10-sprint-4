import bs4
import pandas as pd

with open("source/index4.html", "r") as html_file:
    content = html_file.read()

soup = bs4.BeautifulSoup(content, 'lxml')
data_list = list()

tags = soup
for id, _tags in enumerate(tags):
    print(id, _tags.text)

print(pd.DataFrame(data_list))