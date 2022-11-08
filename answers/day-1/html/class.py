import bs4

with open("source/class.html", "r") as html_file:
    content = html_file.read()

# # Print All HTML
soup = bs4.BeautifulSoup(content, 'lxml')
print(soup.prettify())

p_class = soup.find_all('p', class_='center')

for _p_class in p_class:
    print(_p_class.text)