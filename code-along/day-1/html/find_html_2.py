import bs4

with open("source/index2.html", "r") as html_file:
    content = html_file.read()

# # Print All HTML
soup = bs4.(content, '')
print(soup.prettify())

# # Print Specific Value of HTML Element
# heading2_tags = soup
# print(heading2_tags)
# print(heading2_tags.text)

# # Print Multiple Values of HTML Element
# tags = soup
# print(tags)

# for _tags in tags:
#     print(_tags.text)

# # Print URL and URL text
# tags = soup
# print(tags.text)
# print(tags)

# # Print Other Tags
# tags = soup
# print(tags.text)

# tags = soup
# print(tags.text)
