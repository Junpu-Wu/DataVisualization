import urllib.error
import requests
import ssl
import re
from bs4 import BeautifulSoup
from urllib import request
import xlwt

class SpiderTest:
    def __init__(self, baseUrl, itemInfs):
        self.baseUrl = baseUrl
        self.itemInfs = itemInfs
        self.dataList = []

    def gethtml(self,url):  # 网页请求
        head = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55"
        }
        html = ""
        context = ssl._create_unverified_context()
        try:
            # print(head)
            # print('2')
            response = requests.get(url, headers=head)
            # print('1')
            text = response.status_code
            print("status:{}".format(text))
            req = request.Request(url, headers=head)
            response2 = request.urlopen(req, context=context)
            html = response2.read().decode("utf-8")
        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                print(e.code)
            if hasattr(e, "reason"):
                print(e.reason)
        return html

    def parseData(self, item):
        data = []
        res = re.findall(eval(self.itemInfs["name"]), item)
        if len(res) != 0:
            data.append(res[0])
        else:
            data.append("")
        # data.append(res)
        # print(res)
        res = re.findall(eval(self.itemInfs["area"]), item)
        if len(res) != 0:
            res = res[0]
            res = re.split(r'\s+', res)
            res = res[1]
            res = re.search(r'\d+', res).group()
            data.append(res)
        else:
            data.append("")
        # print(res)
        res = re.findall(eval(self.itemInfs["floor"]), item)
        if len(res) != 0:
            res = re.split(r'\s+', res[0])
            res0 = res[1]
            res1 = res[2]
            res1 = re.search(r'((\d+))', res1)
            res1 = res1.group()
            data.append(res0)
            # data.append(res1)
        else:
            data.append("")
            data.append("")
        # data.append(res)
        # print(res)
        res = re.findall(eval(self.itemInfs["TotalFloor"]), item)
        if len(res) != 0:
            res = re.split(r'\s+', res[0])
            res0 = res[1]
            res1 = res[2]
            res1 = re.search(r'((\d+))', res1)
            res1 = res1.group()
            # data.append(res0)
            data.append(res1)
        else:
            data.append("")
            data.append("")

        res = re.findall(eval(self.itemInfs["decorate"]), item)
        if len(res) != 0:
            data.append(res[0])
        else:
            data.append("")
        res = re.findall(eval(self.itemInfs["nearSubway"]), item)
        if len(res) != 0:
            data.append(res[0])
        else:
            data.append("")
        res = re.findall(eval(self.itemInfs["rentFee"]), item)
        if len(res) != 0:
            data.append(res[0])
        else:
            data.append("")
        return data

    def getData(self):
        for i in range(1, 36):
            url = self.baseUrl + str(i) + "rt200600000001/#contentList"#我也不知道怎么回事，这样保持不动就可以跑起来，没有问题的话请不要修改它
            html = self.gethtml(url)
#            file = open('douban250.html', 'rb')
#            html = file.read()
#            print(html)
            bs = BeautifulSoup(html, "html.parser")
            for item in bs.find_all('div', class_='content__list--item'):
                data = self.parseData(str(item))
                self.dataList.append(data)
                # print("data:",data)


    def saveXls(self,fname):
        workbook = xlwt.Workbook(encoding="utf-8")
        worksheet = workbook.add_sheet('sheet1')
        keys = self.itemInfs.keys()
        for i,key in enumerate(keys):
            worksheet.write(0, i, key)
        for i, film in enumerate(self.dataList):
            for j, item in enumerate(film):
                worksheet.write(i+1, j, item)
        workbook.save(fname)

def main():
    itemInfs = {
        "name": '''re.compile(r'<a href="/zufang/jinrongcheng/" target=.*>(.*)</a>')''',
        "area": '''re.compile(r'</a>\\n<i>/</i>(.*?)<i>/</i>',re.S)''',
        "floor": '''re.compile(r'<span class="hide">.*<i>/</i>(.*?)</span>',re.S)''',
        "TotalFloor": '''re.compile(r'<span class="hide">.*<i>/</i>(.*?)</span>',re.S)''',
        "decorate": '''re.compile(r'<i class="content__item__tag--decoration">(.*)</i>')''',
        "nearSubway": '''re.compile(r'<i class="content__item__tag--is_subway_house">(.*)</i>')''',
        "rentFee": '''re. compile(r'<span class="content__list--item-price"><em>(.*)</em> 元/月</span>')'''
    }
    test = SpiderTest("https://cd.lianjia.com/zufang/jinrongcheng/pg", itemInfs)
    test.getData()
    # print(test.dataList)
    # print(test.dataList)
    test.saveXls("text.xls")
    return

main()