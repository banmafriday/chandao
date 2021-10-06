# coding:utf-8
import requests

# 禅道host地址
host = "zentao.lessoald.cn"

url = "http://zentao.lessoald.cn/zentao/user-login.html"

h = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate",
    "Referer": host + "/zentao/user-login.html",
    # "Cookie":  # 头部没登录前不用传cookie，因为这里cookie就是保持登录的
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
}

body1 = {"account": 'wushanzhang',
         "password": '60234286b7137ec45666d90573719de4953fbcee',
         "keepLogin[]": "on",
         "referer": host + "/zentao/my/"
         }

# s = requests.session()   不要写死session

r1 = requests.post(url, data=body1, headers=h)


print(r1.cookies)
print(r1)
print(r1.text)
