import bs4

with open("source/index3.html", "r") as html_file:
    content = html_file.read()

soup = bs4.BeautifulSoup(content, 'lxml')

tags = soup.select()
print(tags)
for _tags in tags:
    print(_tags.text)

print('-----------------------------------------')


tags = soup.select()
print(tags)
for _tags in tags:
    print(_tags.text)