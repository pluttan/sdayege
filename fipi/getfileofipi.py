import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import time
from fipi import passtojson

headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,/;q=0.8', 'Accept-Encoding': 'gzip, deflate, sdch', 'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4', 'Cache-Control': 'max-age=0', 'Connection': 'close', 'Host': 'www.propertyguru.com.sg',
           'Referer': 'propertyguru.com.sg/singapore-property-listing/', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36', 'Upgrade-Insecure-Requests': '1'}

with requests.Session() as s:
    # логинимся на сайте
    s.get("http://ege.fipi.ru/os11/xmodules/qprint/openlogin.php?proj=AC437B34557F88EA4115D2F374B0A07B").text
    # открываем тему
    s.get("http://ege.fipi.ru/os11/xmodules/qprint/qsearch.php?theme_guid=2ef483029541e311b90c001fc68344c9&proj_guid=AC437B34557F88EA4115D2F374B0A07B")
    # открываем главу темы
    site = "http://ege.fipi.ru/os11/xmodules/qprint/index.php?proj_guid=AC437B34557F88EA4115D2F374B0A07B&theme_guid=2ef483029541e311b90c001fc68344c9&md=qprint&groupno="
    for i in range(40,144):
        getsite = s.get(site+str(i)).text
        soup = BeautifulSoup(getsite, 'lxml')
        soup = str(soup)\
            .replace('bgcolor="#F0F0F0"', ' class="find"')\
            .replace('../../', 'http://ege.fipi.ru/os11/')\
            .replace('style="color:#D0D0D0"', ' class="nofind"')\
            .replace('\n', '')
        soup = BeautifulSoup(soup, 'lxml')
        quotes = list(map(str, soup.find_all('td', class_="find")))
        no = list(map(str, soup.find_all('span', class_="nofind")))
        for z in range(len(no)):
            no[z]=no[z]\
                .replace('<span class="nofind">', "")\
                .replace('</span>', "")
            passtojson(no[z], quotes[z])
        print(no,i)
        #time.sleep(10)
