import requests
import re
import time
from bs4 import BeautifulSoup
import json
import random

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3080.5 Safari/537.36'
}
baseUrl = "http://www.zdiao.com/"
survey_url = "http://www.zdiao.com/vtest.asp?kindid=0&page="
cookie = "UM_distinctid=15fcaba496276a-026e072a7f98d4-18117450-100200-15fcaba49636f9; CNZZDATA1000375697=1990878225-1510932141-http%253A%252F%252Fwww.zdiao.com%252F%7C1513262604; ASPSESSIONIDSSQQDRQQ=OLJCIMDBNHHGNMLMHFAAOHPD; landcode=42F226A7%2D703D%2D4712%2D9785%2D8E47655F87CC; Hm_lvt_7ddacf66134d1ba13d31392486ada51e=1510932357,1510972767,1513250826,1513272887; Hm_lpvt_7ddacf66134d1ba13d31392486ada51e=1513272933"
cookies = {

}
for item in cookie.split(";"):
    result = item.split("=", 1)
    key = result[0]
    value = result[1]
    cookies[key] = value

listUrl = "http://www.zdiao.com/pk.asp?page="

#获得pk的url
def get_pk_urls(page):
    urls = []
    session = requests.session()
    result = session.get(listUrl + str(page), cookies=cookies, headers=headers )
    result.encoding = result.apparent_encoding
    soup = BeautifulSoup(result.text, "html.parser")
    tags = soup.find_all("a", href=re.compile(r'pkid'))
    for item in tags:
        urls.append(baseUrl + item['href'])
    return urls

#进行pk
def beingPk(url):
    session = requests.session()
    result = session.get(url, cookies=cookies, headers=headers )
    result.encoding = result.apparent_encoding
    time.sleep(random.randint(3,5))
    soup = BeautifulSoup(result.text, "html.parser")
    pkid = url.split("=")[1]
    excuteUrl = "http://www.zdiao.com/pk_join.asp?pkid="+ str(pkid) +"&point=value" + str(random.randint(1,3))
    r = session.get(excuteUrl, cookies=cookies, headers=headers )
    print(excuteUrl)
    print(r.status_code)

def excute_method():
    for item in range(261, 360):
        urls = get_pk_urls(item)
        for url in urls:
            try:
                beingPk(url)
            except Exception as e:
                continue
excute_method()