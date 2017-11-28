import requests
import schedule
import time
url="https://zhidao.baidu.com/msubmit/signin?random=0.3507959078709957&"
cookie="复制cookie替换"
headers={
'Accept':'application/json',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'zh-CN,zh;q=0.9',
'Connection':'keep-alive',
'Content-Length':'11',
'Content-Type':'application/x-www-form-urlencoded',
'Cookie':cookie,
'Host':'zhidao.baidu.com',
'Origin':'https://zhidao.baidu.com',
'Referer':'https://zhidao.baidu.com/mmisc/signinfo?uid=C1954D0D376337B302790226BF0B702F&step=2',
'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
'X-ik-ssl':'1',
# 'X-ik-token':'xxxxxxxxxxx',
'X-Requested-With':'XMLHttpRequest',
}
payload={"ssid":"","cifr":""}
def sign():
    requests.post(url,headers=headers,data=payload)
schedule.every().day.at("10:30").do(sign)
while 1:
    schedule.run_pending()
    time.sleep(1)
