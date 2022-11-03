import bs4

with open("source/index2.html", "r") as html_file:
    content = html_file.read()

# # Print All HTML
soup = bs4.BeautifulSoup(content, 'lxml')
# print(soup.prettify())

# # Print Specific Value of HTML Element
# heading2_tags = soup.find("h2")
# print(heading2_tags)
# print(heading2_tags.text)

# # # Print Multiple Values of HTML Element
# tags = soup.find_all("h5")
# print(tags)

# for _tags in tags:
#     print(_tags.text)

# # Print URL and URL text
# tags = soup.find("a")
# print(tags.text)
# print(tags.get("href"))

# # # Print Other Tags
# tags = soup.find("span")
# print(tags.text)

# tags = soup.find("strong")
# print(tags.text)
