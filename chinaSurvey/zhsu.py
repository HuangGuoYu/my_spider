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

#获取问题的url tag
def findQuestionUrl(tag):
    return tag.name == "a" and tag.parent.name == "td" and tag.has_attr("href")

#获取问题的url
def findQuestionItem(tag):
    return tag.name == "input" and tag.parent.previous_sibling['class'] == "style_hei_12_bold"

#答题连接
def get_list_of_surl(page):
    result = []
    session = requests.session()
    r = session.get(survey_url + str(page), cookies=cookies, headers=headers)
    r.encoding = r.apparent_encoding
    # print(r.text)
    soup = BeautifulSoup(r.text, "html.parser")
    for item in soup.find_all(findQuestionUrl):
        url =  baseUrl + item['href']
        result.append(url)
    return result

def questionOptions(tag):
    return tag.name == "input" and tag['value'] == "value1"
def answer_question(urls):
    session = requests.session()
    for item in urls:
        data = {}
        r = session.get(item,  cookies=cookies, headers=headers)
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text, "html.parser")
        time.sleep(random.randint(4,10))
        data["vtestid"] = item.split("=")[1]
        questions = soup.find_all(questionOptions)
        for ques in questions:
            data[ques['name']] = 'value' + str(random.randint(1,2))
        datas = json.dumps(data)
        print(datas)
        pr = session.post("http://www.zdiao.com/vtest_join.asp", data=data, cookies=cookies, headers=headers)
        pr.encoding = pr.encoding
        print(item)
        print(pr.status_code)
#测试是否登录
def is_login():
    session = requests.session()
    r = session.get("http://www.zdiao.com/u/member.asp", cookies=cookies, headers=headers)
    r.encoding = r.apparent_encoding
    print(r.text)



def main():
    for item in range(80, 300):
        print("******************" + str(item) + "*********************")
        urls = get_list_of_surl(item)
        print(urls)
        try:
            answer_question(urls)
        except Exception as e:
            continue
main()
# is_login()