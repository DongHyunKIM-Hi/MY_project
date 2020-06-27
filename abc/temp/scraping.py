
import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('mongodb://locoalhost',27017)
db = client.dbsparta

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
url = 'https://www.google.com/search?hl=ko&tbm=lcl&sxsrf=ALeKk01RgyxAv7u_dMTi22bIqSCo3QllCA%3A1592829212950&ei=HKXwXtDDOcOB-QbFwoLwDg&q=연남동맛집'
data = requests.get(url,headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기

title_list = soup.select('#rl_ist0 > div.rl_tile-group > div.rlfl__tls.rl_tls > div > div > div.uMdZh.rl-qs-crs-t.mnr-c > div > a > div')
# title = soup.select_one('#rl_ist0 > div.rl_tile-group > div.rlfl__tls.rl_tls > div:nth-child(1) > div > div.uMdZh.rl-qs-crs-t.mnr-c > div > a > div > div.dbg0pd > div') 
# title2 = soup.select_one('#rl_ist0 > div.rl_tile-group > div.rlfl__tls.rl_tls > div:nth-child(2) > div > div.uMdZh.rl-qs-crs-t.mnr-c > div > a > div > div.dbg0pd > div')
# title3 = soup.select_one('#rl_ist0 > div.rl_tile-group > div.rlfl__tls.rl_tls > div:nth-child(3) > div > div.uMdZh.rl-qs-crs-t.mnr-c > div > a > div > div.dbg0pd > div')
# title4 = soup.select_one('#rl_ist0 > div.rl_tile-group > div.rlfl__tls.rl_tls > div:nth-child(4) > div > div.uMdZh.rl-qs-crs-t.mnr-c > div > a > div > div.dbg0pd > div')
# title5 = soup.select_one('#rl_ist0 > div.rl_tile-group > div.rlfl__tls.rl_tls > div:nth-child(3) > div > div.uMdZh.rl-qs-crs-t.mnr-c > div > a > div > div.dbg0pd > div')
# title6 = soup.select_one('#rl_ist0 > div.rl_tile-group > div.rlfl__tls.rl_tls > div:nth-child(7) > div > div.uMdZh.rl-qs-crs-t.mnr-c > div > a > div > div.dbg0pd > div')
# title7 = soup.select_one('#rl_ist0 > div.rl_tile-group > div.rlfl__tls.rl_tls > div:nth-child(8) > div > div.uMdZh.rl-qs-crs-t.mnr-c > div > a > div > div.dbg0pd > div')
# title8 = soup.select_one('#rl_ist0 > div.rl_tile-group > div.rlfl__tls.rl_tls > div:nth-child(9) > div > div.uMdZh.rl-qs-crs-t.mnr-c > div > a > div > div.dbg0pd > div')
# title9 = soup.select_one('#rl_ist0 > div.rl_tile-group > div.rlfl__tls.rl_tls > div:nth-child(10) > div > div.uMdZh.rl-qs-crs-t.mnr-c > div > a > div > div.dbg0pd > div')
# title10 = soup.select_one('#rl_ist0 > div.rl_tile-group > div.rlfl__tls.rl_tls > div:nth-child(11) > div > div.uMdZh.rl-qs-crs-t.mnr-c > div > a > div > div.dbg0pd > div')
# title11 = soup.select_one('#rl_ist0 > div.rl_tile-group > div.rlfl__tls.rl_tls > div:nth-child(12) > div > div.uMdZh.rl-qs-crs-t.mnr-c > div > a > div > div.dbg0pd > div')
# title12 = soup.select_one('#rl_ist0 > div.rl_tile-group > div.rlfl__tls.rl_tls > div:nth-child(13) > div > div.uMdZh.rl-qs-crs-t.mnr-c > div > a > div > div.dbg0pd > div')
# title13 = soup.select_one('#rl_ist0 > div.rl_tile-group > div.rlfl__tls.rl_tls > div:nth-child(14) > div > div.uMdZh.rl-qs-crs-t.mnr-c > div > a > div > div.dbg0pd > div')
# title14 = soup.select_one('#rl_ist0 > div.rl_tile-group > div.rlfl__tls.rl_tls > div:nth-child(15) > div > div.uMdZh.rl-qs-crs-t.mnr-c > div > a > div > div.dbg0pd > div')
# title15 = soup.select_one('#rl_ist0 > div.rl_tile-group > div.rlfl__tls.rl_tls > div:nth-child(16) > div > div.uMdZh.rl-qs-crs-t.mnr-c > div > a > div > div.dbg0pd > div')
# title16 = soup.select_one('#rl_ist0 > div.rl_tile-group > div.rlfl__tls.rl_tls > div:nth-child(17) > div > div.uMdZh.rl-qs-crs-t.mnr-c > div > a > div > div.dbg0pd > div')
# title17 = soup.select_one('#rl_ist0 > div.rl_tile-group > div.rlfl__tls.rl_tls > div:nth-child(18) > div > div.uMdZh.rl-qs-crs-t.mnr-c > div > a > div > div.dbg0pd > div')

# print(title_list)
for box in title_list:
    title = box.select_one('div.dbg0pd > div')
    #print(title.text)
    cate_box = box.select_one('span > div:nth-child(1)')
    cate = cate_box.text.replace(' · ₩₩', '').split(' · ')[1]
    print(cate)
   
    doc = {'title':title.text, 'cate' : cate}
    print("==========================")
    print(doc)
    db.taste.insert_one(doc) 

# print(title.text,title2.text,title3.text,title4.text,title5.text,title6.text,title7.text,title8.text,title9.text,title10.text,title11.text,title12.text,title13.text,title14.text,title15.text,title16.text,title17.text)

#,title8.text,title9.text
#title10.text,title11.text,title12.text,title13.text,title14.text,title15.text,title16.text,title17.text




