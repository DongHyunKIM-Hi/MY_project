from pymongo import MongoClient
from bs4 import BeautifulSoup
import requests
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)
count = 0

client = MongoClient('localhost', 27017)
db = client.AMD
count=0
make_list = list(db.movie.find())
for a in make_list:
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    url='https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EC%98%81%ED%99%94+'+a['name']
    #반복문을 사용하여 2015년부터 2019년까지 반복하여 url을 바꿔서 실행
    data = requests.get(url,headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')
   
    movies = soup.select_one('#_au_movie_info > div.info_main > div > a > img')
    img_url=movies.get('src')
    count=count+1
    print(count)
    print(img_url)
    db.movie.update_one({'name':a['name']},{'$set':{'img_url':img_url}})