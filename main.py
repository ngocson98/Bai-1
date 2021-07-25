# from newspaper import Article
import requests
from bs4 import BeautifulSoup
import csv

URL = "https://vnexpress.net/giao-duc"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

# =============================================================================


# =============================================================================

results1 = soup.find(class_="sub-news-top")
# print(results1.prettify())
elements1 = results1.find_all("ul", class_="list-sub-feature")
for element1 in elements1:
    # print(element1, end="\n"*2)

    title1 = element1.find("h3", class_="title-news")
    description1 = element1.find("p", class_="description")
    print('Title: {}'.format(title1))
    print('ND: {}'.format(description1))
    print()

# =============================================================================
# def not_description(description):
#    return None
# =============================================================================

results2 = soup.find(class_="section section_container section_five_news mt20")
# print(results2.prettify())
elements2 = results2.find_all("div", class_="inner-item-news-five width_common")
for element2 in elements2:
    # print(element2, end="\n"*2)

    title2 = element2.find("h3", class_="title-news")
    description2 = element2.find("p", class_="description")
    print('Title: {}'.format(title2))
    print('ND: {}'.format(description2))
    print()

# =============================================================================

results3 = soup.find(id="blockThuongVien0")
# print(results3.prettify())
elements3 = results3.find_all('article', class_="item-news item-news-common")
for element3 in elements3:
    # print(element3, end="\n"*2)
    title3 = element3.find("h3", class_="title-news")
    description3 = element3.find("p", class_="description")
    print('Title: {}'.format(title3))
    print('ND: {}'.format(description3))
    # print('Title: {}'.format(title3.text.strip()))
    # print('ND: {}'.format(description3.text.strip()))
    print()

# =============================================================================
results4 = soup.find(id="blockThuongVien1")
# print(results4.prettify())
elements4 = results4.find_all('article', class_="item-news item-news-common")
for element4 in elements4:
    # print(element4, end="\n"*2)
    title4 = element4.find("h3", class_="title-news")
    description4 = element4.find("p", class_="description")
    print('Title: {}'.format(title4.text.strip()))
    print('ND: {}'.format(description4.text.strip()))
    print()
# =============================================================================
'''
with open('data.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['title', 'description'])
    for element in elements:
        writer.writerow([element.get('title'), element.get('description')])
'''
