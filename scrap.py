import urllib.request
from sqlalchemy import create_engine, engine
from bs4 import BeautifulSoup
import socket

def connection():
    return create_engine('postgresql://takanori:@localhost/test')
engine = connection()

print(engine)

def insert(id, name, tel):
    engine.execute("insert into team(year, name, position) values ('{}', '{}', '{}')".format(id, name, tel))
    return

def getTest(tel):
    return engine.execute("select * from team where year='{}'".format(tel))

headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

url = 'http://sebango.web.fc2.com/sebangou15/n-fighters-sebangou15.html'

def main():

    try:
        req = urllib.request.Request(url , headers=headers)
        soup = BeautifulSoup(urllib.request.urlopen(req).read())
        tr = soup.find('table').findAll('tr')
        print(tr)
        print(len(tr))
        for i in range(1,len(tr)-1):
            el = tr[i].findAll('td')
            year = str(el[0])[4:len(str(el[0]))-5]
            name = str(el[1])[4:len(str(el[1]))-5]
            position = str(el[2])[4:len(str(el[2]))-5]
            if len(name) >= 10 or len(name) > 10:
                continue
            if name == "　":
                ttt = '誰もつけていません'
                insert(year, ttt, '---')
            else:
                # print('{}, {}, {}'.format(year,name, position))
                insert(year,name, position)

    except urllib.error.HTTPError as err:
            print(err.code)
    except urllib.error.URLError as err:
            print(err.reason)
    except socket.error as err:
            print("timeout")
        
    a: engine.result.ResultProxy = getTest(2002)

    print(a)

if __name__=="__main__":
    main()