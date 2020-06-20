import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.AMD                      # 'dbsparta'라는 이름의 db를 만듭니다.

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://namu.wiki/w/2002%EB%85%84',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
movies = soup.select('#app > div > div:nth-child(2) > article > div:nth-child(5) > div:nth-child(2) > div > div > div:nth-child(108) > ul > li')
#app > div > div:nth-child(2) > article > div:nth-child(5) > div:nth-child(2) > div > div > div:nth-child(116) > ul > li:nth-child(1) > div
#app > div > div:nth-child(2) > article > div:nth-child(5) > div:nth-child(2) > div > div > div:nth-child(116) > ul > li:nth-child(2) > div

# movies (tr들) 의 반복문을 돌리기
for movie in movies:
    # movie 안에 a 가 있으면,
    a_tag = movie.select_one('div')
    if a_tag is not None:
        title = a_tag.text    
        year = 2001                        # a 태그 사이의 텍스트를 가져오기
        doc = {
          
            'name' : title,
            'Year' : year,
        }
        db.drama.insert_one(doc)