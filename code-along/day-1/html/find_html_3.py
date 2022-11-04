import bs4

with open("source/index3.html", "r") as html_file:
    content = html_file.read()

soup = bs4.BeautifulSoup(content, 'lxml')

# tags = soup.find_all("div", class_="w3-panel")
# for _tags in tags:
#     print(_tags.p.text)

# tags = soup.find_all("div", id="sample-1")
# print(tags[0].text)

tags = soup.find_all('div', class_='w3-panel w3-card-4 w3-yellow')
for _tags in tags:
    print(_tags.p.text)








