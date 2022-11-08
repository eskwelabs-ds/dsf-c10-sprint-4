import bs4

with open("source/index3.html", "r") as html_file:
    content = html_file.read()

soup = bs4.BeautifulSoup(content, 'lxml')


### Get All Tags
tags = soup.find_all('div', id='sample-1')
for _tags in tags:
    print(_tags.p.text)


### Get All Tags
tags = soup.find_all('div', class_='w3-card-4')
for _tags in tags:
    print(_tags.p.text)




