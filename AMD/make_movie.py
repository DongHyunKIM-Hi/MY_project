from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.AMD
# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
for generation in range(2000,2020): #2015년 부터 2019년까지 노래 순위 출력
    url='https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query='+str(generation)+ '%EB%85%84%20%EC%98%81%ED%99%94%20%EC%88%9C%EC%9C%84'
    #반복문을 사용하여 2015년부터 2019년까지 반복하여 url을 바꿔서 실행
    data = requests.get(url,headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')
   
    movies = soup.select('#main_pack > div.content_search.section._cs_movie_box_office > div > div.contents03_sub > div > div.movie_rank_wrap > div.movie_audience_ranking._main_panel > div:nth-child(1) > ul > li')
 
    for movie in movies:
   
        title = generation

        rank_tag = movie.select_one('div.movie_info > a > div > span > span')
        #div.movie_info > a > div > span > span
        img_url = movie.select_one('div.thumb > a > img')
        #div.thumb > a > img
        img = img_url.get('src')
        if int(rank_tag.text)>10:
            break
        name_tag = movie.select_one('strong')
        #div.movie_info > a > div > strong
        rank = rank_tag.text.strip()
        name = name_tag.text.strip()
        #main_pack > div.content_search.section._cs_movie_box_office > div > div.contents03_sub > div > div.movie_rank_wrap > div.movie_audience_ranking._main_panel > div:nth-child(1) > ul > li:nth-child(1) > div.movie_info > a > div > span
        #main_pack > div.content_search.section._cs_movie_box_office > div > div.contents03_sub > div > div.movie_rank_wrap > div.movie_audience_ranking._main_panel > div:nth-child(1) > ul > li:nth-child(1) > div.movie_info > a > div > span > span
        #main_pack > div.content_search.section._cs_movie_box_office > div > div.contents03_sub > div > div.movie_rank_wrap > div.movie_audience_ranking._main_panel > div:nth-child(1) > ul > li:nth-child(2) > div.movie_info > a > div > span > span
        doc={
            'Year': title,
            'rank': rank,
            'name': name,
            
            'img_url' : img
        }
        db.movie.insert_one(doc)