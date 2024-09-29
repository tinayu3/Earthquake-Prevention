import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'}
url = "http://www.52safety.com/yjzrzh/index.jhtml"

html = requests.get(url)
soup = BeautifulSoup(html.text, 'lxml')
data = soup.select('body > div > div.main.container_1000 > div.main_left > div.index_list.list_news.index_list_bg > ul > li')
for item in data:
    result = {
            'title': item.get_text(),
    }
    print(result)