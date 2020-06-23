from pymongo import MongoClient
from bs4 import BeautifulSoup
import requests
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)


client = MongoClient('localhost', 27017)
db = client.AMD
# URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://namu.wiki/w/2011%EB%85%84#s-5.1', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
#app > div > div:nth-child(2) > article > div:nth-child(5) > div:nth-child(2) > div > div > div:nth-child(92) > ul > li:nth-child(1) > div > a
soup = BeautifulSoup(data.text, 'html.parser')#app > div > div:nth-child(2) > article > div:nth-child(5) > div:nth-child(2) > div > div > div:nth-child(98) > ul > li:nth-child(1) > div > a
# select를 이용해서, tr들을 불러오기
movies = soup.select('#app > div > div:nth-child(2) > article > div:nth-child(5) > div:nth-child(2) > div > div > div:nth-child(92) > ul>li ')
# movies (tr들) 의 반복문을 돌리기
def many_list():
    for movie in movies:
        print('실행')
        movies_2 = movie.select('ul>li')
    
        for movie_2 in movies_2:
            a_tag = movie_2.select_one('div>a')
            if a_tag is not None:
                title = a_tag.text
            
                year = 2001                                    # a 태그 사이의 텍스트를 가져오기
                doc = {
                    'Year': year,
                    'name': title,

                }
                db.movie.insert_one(doc)

def one_list():
    for movie in movies:
        # movie 안에 a 가 있으면,
        a_tag = movie.select_one('div>a')
        if a_tag is not None:
            title = a_tag.text    
            year = 2011            # a 태그 사이의 텍스트를 가져오기
            doc = {
            
                'name' : title,
                'Year' : year,
            }
            print(title)
            print(year)
            db.movie.insert_one(doc)
one_list()
#app > div > div:nth-child(2) > article > div:nth-child(5) > div:nth-child(2) > div > div > div:nth-child(114) > ul:nth-child(1) > li > ul > li:nth-child(1) > div > a
#app > div > div:nth-child(2) > article > div:nth-child(5) > div:nth-child(2) > div > div > div:nth-child(114) > ul:nth-child(1) > li > ul > li:nth-child(2) > div > a
#app > div > div:nth-child(2) > article > div:nth-child(5) > div:nth-child(2) > div > div > div:nth-child(114) > ul:nth-child(3) > li > ul > li:nth-child(1) > div > a