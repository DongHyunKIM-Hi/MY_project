from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

client = MongoClient('mongodb://hyundong_k:940dfg@13.125.220.235', 27017)
db = client.AMD
# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
for generation in range(2000,2020): #2015년 부터 2019년까지 노래 순위 출력
    url='https://www.genie.co.kr/chart/musicHistory?year='+str(generation) 
    #반복문을 사용하여 2015년부터 2019년까지 반복하여 url을 바꿔서 실행
    data = requests.get(url,headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')
   
    musics = soup.select('#body-content > div.songlist-box > div.music-list-wrap > table > tbody > tr')
  #body-content > div.songlist-box > div.music-list-wrap > table > tbody > tr:nth-child(1) > td:nth-child(3) > a > img
#body-content > div.songlist-box > div.music-list-wrap > table > tbody > tr:nth-child(1) > td:nth-child(3) > a > img
#body-content > div.songlist-box > div.music-list-wrap > table > tbody > tr:nth-child(2) > td:nth-child(3) > a > img
    for music in musics:
   
        title = soup.select_one('#body-content > div.chart-date > div.date > h3')# 연도출력
        rank_tag = music.select_one('td.number')
        img_url = music.select_one('td:nth-child(3) > a > img')
        img = img_url.get('src')
        if int(rank_tag.text)>10:
            break
        name_tag = music.select_one('td.info > a.title.ellipsis')
        if name_tag.find('span'): #title테그 제거
            name_tag.find('span').extract()
            if name_tag.find('span'):#19금 테그 제거
                name_tag.find('span').extract()
        singer_tag = music.select_one(' td.info > a.artist.ellipsis')
        rank = rank_tag.text.strip()
        name=name_tag.text.strip()
        singer= singer_tag.text.strip()
        doc={
            'Year': title.text,
            'rank': rank,
            'name': name,
            'singer' : singer,
            'img_url' : img
        }
        db.music.insert_one(doc)