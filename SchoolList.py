from bs4 import BeautifulSoup
import requests
import time
import random
import os
from yzy_spider import  BaseRequestInfo


class SchoolList:

    def __init__(self, baseUrl, baseFile):
        self.baseUrl = baseUrl
        self.baseFile = baseFile

    def fileAdd(self, content, name):
        if not os.path.exists(self.baseFile):
            os.makedirs(self.baseFile)
        files = os.listdir(self.baseFile)
        if (str(name) + ".html") not in files:
            with open(self.baseFile + "\\" + str(name) + ".html", "w", encoding="utf-8") as f:
                f.write(content)
                print("save ok " + str(name))
                f.close()
    def fileIsExists(self, fileName):
        file = str(fileName) + ".html"
        if not os.path.exists(self.baseFile):
            os.makedirs(self.baseFile)
        files = os.listdir(self.baseFile)
        if file in files:
            return True
        return False

    def findAllSchoolPage(self, pageNum):
        for curPage in range(1, pageNum + 1):
            session = requests.session()
            if self.fileIsExists(curPage):
                continue
            try:
                curData = session.get(self.baseUrl + str(curPage), cookies=BaseRequestInfo.cookies, headers=BaseRequestInfo.headers)
                time.sleep(random.randint(3, 6))
                curData.encoding = curData.apparent_encoding
                if curData.status_code == 200:
                    curSoup = BeautifulSoup(curData.text, "html.parser")
                    self.fileAdd(curSoup.prettify(), curPage)
                    print(self.baseUrl + str(curPage))
            except Exception as e:
                continue

    def checkCurIsLogin(self, personalUrl):
        session = requests.session()
        personalInfo = session.get(personalUrl, cookies=BaseRequestInfo.cookies,headers=BaseRequestInfo.headers)
        personalInfo.encoding = personalInfo.apparent_encoding
        soup = BeautifulSoup(personalInfo.text, "html.parser")
        print(soup.prettify())
def main():
    sl = SchoolList("https://www.youzy.cn/college/search?page=", "F:\\Code\\PythonTest\\yzy_spider\\schoolList")
    sl.findAllSchoolPage(11)
main()
