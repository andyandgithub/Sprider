import requests
from bs4 import BeautifulSoup
import time,os
from urllib.request import urlretrieve

from lxml.html.clean import unicode

if "photo" not in os.listdir():
    os.makedirs("photo")
img_list=[]
for num in range(1,81):

    url="http://www.mmonly.cc/ktmh/dmmn/list_29_%d.html" %num
    headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
            }
    imgs_url=requests.get(url,headers=headers,stream=True)
    imgs_url.encoding=imgs_url.apparent_encoding
    # imgs_url.encoding="utf-8"
    # print(imgs_url.apparent_encoding)
    html=imgs_url.text
    # print(html)
    soup=BeautifulSoup(html,"lxml")
    # print(soup.prettify())
    img_div=soup.find_all(class_="ABox")
    # print(type(img_div),len(img_div))
    # print(img_div)
    # img_div[1] = unicode(img_div[1], 'utf-8')
    # a=BeautifulSoup(img_div[1])
    # print(a.prettify())
    # print(img_div[1].encode("utf-8"))

    for each in img_div:
        # print(type(each))

        # print(s)
        img_list.append((each.img.get("alt"),each.a.img.get("src")))
        #下载图片名称
        # print(each.img.get("alt"))
# print(img_list)
print(len(img_list),"采集完成")
# print(type(img_div),type(img_div),type(img_div[0].a),type(img_div[0].a.get("href")))
print("开始下载图片")
for each in img_list:
    # print(type(each[0]))
    filename=str(each[0])+time.ctime()[-7:-5]+".jpg"#文件名称上加上time的变化因为所爬取的图片会右重名的
    print("正在下载",filename)
    urlretrieve(url=each[1], filename='photo/' + filename)
    time.sleep(0.5)

