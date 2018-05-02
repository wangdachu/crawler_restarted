#笑神本部，标签，字幕组，时间，视频链接
import requests
from bs4 import BeautifulSoup
import csv

websrc = requests.get('http://owaraiclub.com/post/').text
soup = BeautifulSoup(websrc,'lxml')
csv_file = open('xiaoshenbenbu.csv', 'w',encoding='utf-8')
# print(soup.prettify())
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headerline', 'date', 'aouthor','link'])

for article in soup.find_all('section',class_='article-list'):
    sours = article.a.text
    #print(sours)
    try:
        vidheader = article.find('div', class_='categories').a.text
    except Exception as e:
        vidheader = None
    print(vidheader)
    try:
        viddate = article.find('div', class_='date').text
    except Exception as e:
        viddate = None
    print(viddate)
    try:
        vidauthor = article.find('span', class_='author').text
    except Exception as e:
        vidauthor = None
    print(vidauthor)
    try:
        vidlink = article.find('div',class_='thumbnail hovereffect').a['href']
        vidlinkw = f'http://owaraiclub.com{vidlink}'
    except Exception as e:
        vidlinkw = None
    print(vidlinkw)
    csv_writer.writerow([vidheader, viddate, vidauthor,vidlinkw])

csv_file.close()



