from bs4 import BeautifulSoup
import urllib.request
import csv
import sqlite3

url = 'https://vnexpress.net/giao-duc'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

feed = soup.select(".title-news a")
list = soup.select('.title_news')
feeds = soup.select("p.description")

feed_title = [title.text for title in feed]
feed_title2 = [title.text for title in list]
feed_title.insert(1, feed_title2[0])
feed_title.insert(2, feed_title2[1])
feed_title.insert(3, feed_title2[2])

feed_link = [title["href"] for title in feed]
feeds_des = [description.text for description in feeds]
feeds_des.insert(4, "None")
feeds_des.insert(5, "None")
feeds_des.insert(6, "None")
feeds_des.insert(7, "None")

#for ND in soup.select("p.description"):
 #   print(ND.get_text())

'''
print(feed_title) 38
print(feeds_des)  64
print(feed_link)  35
print(feed_title[0])
'''
'''
print(len(feed_link))
def get_urls(pages=35):
    urls =[]
    for root_url in feed_link:
        urls.append(root_url)
        for res in range(1, pages, 1):
            urls.append((root_url+f"-p{res}"))
    print(len(urls))
    return urls

'''
print(len(feeds_des))

for i in range(len(feed_title)):
    print(feed_title[i])
    print(feeds_des[i])
    # print(feed_link[i])
    print('-'*15)

# SQL command to insert the data in the table
