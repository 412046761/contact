# -*- codeing = utf-8 -*-
# @Time     :2021/4/25
# @Author   :ly
# @File     :__init__.py.py
# @Spftware :PyCharm

from bs4 import BeautifulSoup # 网页解析
import re # 正则
import urllib.request,urllib.error # 订制URL
import xlwt # excel 操作
import os # 文件操作
import sqlite3 # 数据库

# 电影详情
findlink = re.compile(r'<a href="(.*?)">',re.S)  # 创建正则表达式对象
# 电影名称
findmovieName = re.compile(r'<span class="title">(.*?)</span>')
# 电影海报
findSrc = re.compile(r'class="" src="(.*?)" width="100"/>')
# 内容简介
findinq = re.compile(r'<span class="inq">(.*?)</span>')
# 评分
findage = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')
# 多少人评价
findManNumbers = re.compile(r'<span>(.*?)</span>')




def main():
    baseUrl = "https://movie.douban.com/top250?start="
    savePath = ".\\豆瓣电影Top250.xls"
    dbPath = "movietest.db"
    # 1. 爬取网站
    datalist = getData(baseUrl)
    # 2. 解析数据
    datas = analyticalData(datalist)
    # 3. 保存数据
    # save(datas,savePath) Excle
    savedb(datas,dbPath) #db

# 保存到数据库
def savedb(datas, dbPath):
    # 初始化表
    init_db(dbPath)
    conn = sqlite3.connect(dbPath)
    c = conn.cursor()

    for data in datas:
        for index in range(len(data)):
            data[index] = data[index].replace('"',"'")
            data[index] = '"'+data[index]+'"'
        sql = '''
            insert into movie250(
            name,link,inq,score,ManNumbers,image         
            ) values (%s)'''%",".join(data)
        print(sql)
        c.execute(sql)

    conn.commit()
    c.close()

# 初始化数据库表
def init_db(dbPath):
    # 是否已经初始化
    if (os.path.exists(dbPath)):
        return

    sql = '''
        create table movie250
        (
        id integer  primary key autoincrement,
        name varchar,
        link text,
        inq text,
        score number ,
        mannumbers number ,
        image text
        )
    '''
    conn = sqlite3.connect(dbPath)
    c = conn.cursor()
    c.execute(sql)
    conn.commit()
    conn.close()

# 2. 解析数据
def analyticalData(datalist):
    rslist = []
    for html in datalist:
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_="item"):
            data = []
            item = str(item)
            # 电影名
            name = re.findall(findmovieName, item)[0]
            data.append(name)
            # 链接
            link = re.findall(findlink,item)[0]
            data.append(link)
            # 简介
            inq = re.findall(findinq, item)
            if len(inq) != 0:
                data.append(str(inq))
            else:
                data.append(' ')
            # 评分
            score = re.findall(findage, item)[0]
            data.append(score)
            # 评分人数
            ManNumbers = re.findall(findManNumbers, item)[0]
            data.append(ManNumbers)
            # 电影海报 图片
            src = re.findall(findSrc, item)[0]
            # 下载海报到jpg文件夹
            jpgUrl = './jpg/' + name
            if(not os.path.exists(jpgUrl)):
                os.mkdir(jpgUrl)

            jpgNames = str(src).split('/')
            jpgName  = jpgUrl + '/' + jpgNames[len(jpgNames)-1]
            # 开始下载图片
            #urllib.request.urlretrieve(src,jpgName)

            data.append(src)
            rslist.append(data)
    return rslist

# 1.爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0,10):            # 10次
        url = baseurl + str(i*25)   # 每页25条
        html = askURL(url)          # 获取网页源码
        datalist.append(html)
    return datalist

# 得到指定一个URL的网页内容
def askURL(url):
    # 组装头部信息
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
    }
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
        return html
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

# 3.保存数据
def save(datas,savePath):
    book = xlwt.Workbook(encoding="utf-8")   # 创建workbook对象
    sheet = book.add_sheet('sheet1')         # 创建工作表
    sheet.write(0, 0, '电影名称')
    sheet.write(0, 1, '电影详情')
    sheet.write(0, 2, '内容简介')
    sheet.write(0, 3, '电影评分')
    sheet.write(0, 4, '评分人数')
    sheet.write(0, 5, '电影海报')
    for data in datas:
        h = datas.index(data)+1
        for l in range(0, len(data)):
            sheet.write(h, l, data[l])  # 写入数据，（行，列，内容）

    book.save(savePath)                 # 保存
    print("完成……")

if __name__=="__main__":
   main()
   print('OK!')