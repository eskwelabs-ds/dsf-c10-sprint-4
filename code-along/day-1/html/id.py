import bs4

with open("source/id.html", "r") as html_file:
    content = html_file.read()

# # Print All HTML
soup = bs4.BeautifulSoup(content, 'lxml')
print(soup.prettify())

p_id = soup
print(p_id)
print(p_id.text)