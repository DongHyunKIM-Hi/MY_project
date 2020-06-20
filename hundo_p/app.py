from flask import Flask, render_template
import os
import sys
import urllib.request
app = Flask(__name__)
#-*- coding: utf-8 -*-
client_id = "1KGupjON0Vd1Jd5X5k21"
client_secret = "rvqwP425Cm"
url = "https://openapi.naver.com/v1/datalab/search";
body = "{\"startDate\":\"2017-01-01\",\"endDate\":\"2017-04-30\",\"timeUnit\":\"month\",\"keywordGroups\":[{\"groupName\":\"한글\",\"keywords\":[\"한글\",\"korean\"]},{\"groupName\":\"영어\",\"keywords\":[\"영어\",\"english\"]}],\"device\":\"pc\",\"ages\":[\"1\",\"2\"],\"gender\":\"f\"}";

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
request.add_header("Content-Type","application/json")
response = urllib.request.urlopen(request, data=body.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)
## URL 별로 함수명이 같거나,
## route('/') 등의 주소가 같으면 안됩니다.
#main_pack > div.content_search.section._cs_movie_box_office > div > div.contents03_sub > div > div.movie_rank_wrap > div.movie_audience_ranking._main_panel > div:nth-child(1) > ul > li:nth-child(1)
#main_pack > div.content_search.section._cs_movie_box_office > div > div.contents03_sub > div > div.movie_rank_wrap > div.movie_audience_ranking._main_panel > div:nth-child(1) > ul > li:nth-child(2)
@app.route('/')
def home():
   return render_template('main_login.html')

@app.route('/create_account')
def register():
   return render_template('create_account.html')
if __name__ == '__main__':
   app.run('localhost', port=5000, debug=True)