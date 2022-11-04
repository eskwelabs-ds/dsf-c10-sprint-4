import bs4
import pandas as pd

with open("source/index4.html", "r") as html_file:
    content = html_file.read()

soup = bs4.BeautifulSoup(content, 'lxml')
# print(soup.prettify())
data_list = list()

tags = soup.select("table.w3-table > tr")

for id, _tags in enumerate(tags):
    tds = _tags.find_all("td")
    if len(tds) > 0:
        data_list.append({
            'First Name': tds[0].text,
            'Last Name': tds[1].text,
            'Points':tds[2].text
        })

print(pd.DataFrame(data_list))