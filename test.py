from bs4 import BeautifulSoup
import urllib.request

url = 'https://vnexpress.net/giao-duc'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

elements = soup.find('section', class_='section section_topstory section_topstory_folder').find_all('a')
for element in elements:
    title = element.get('title')
    ND = element.get('description')
    print('Title: {} - ND: {}'.format(title, ND))
    print()