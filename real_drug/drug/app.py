from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient         
client = MongoClient('localhost', 27017)  
db = client.drug                   

#_______________________________________________________________________________________________________________________________________________________________
#click.py 부분
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

# HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

# API 역할을 하는 부분
@app.route('/test', methods=['POST'])
def test_post():
   title_receive = request.form['title_give']
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 POST!'})

# API 역할을 하는 부분
@app.route('/test', methods=['GET'])
def test_get():
   # #_______________________________________________________________________________________________________________________________________________________________
   # #click.py 부분
   # base_url = 'https://terms.naver.com/search.nhn?query='
   # plus_url = '게보린'
   # # plus_url = input('약품 이름을 입력하세요! :')
   # url = base_url + quote_plus(plus_url)

   # # # 네이버 백과사전을 열어서 약품 검색
   # driver = webdriver.Chrome('/Users/Chaser/Desktop/Sparta2🛠/Projects/drug/chromedriver')
   # driver.get(url)

   # ##검색 결과에서 해당 의약품을 한번 더 클릭
   # ## 추후에는 결과에서 나온 이름이 비슷한 의약품을 모두 정렬하고 선택할수 있게 해야함
   # html = driver.page_source
   # soup = BeautifulSoup(html, "html.parser")

   # ##soup.select('.info_area') 안에 info_area로 설정하는것이 어려웠움
   # ##이상한것이 섞여나오니 약품설명 밑에 "더보기"를 클릭하게 해서 제한해야함
   # ##약품 이름을 클릭하면 하이퍼링크가 클릭되서 해당화면으로 넘어가야함
   # info_area = soup.select('.info_area')
   # for i in info_area:
   #    # print(i.select_one('.title')?.text)

   # ##비슷한 이름의 약품별로 이름과 하이퍼링크 따오기
   #    base_href = 'https://terms.naver.com/'
   #    plus_href = i.a.attrs['href']
   #    href = base_href + plus_href
   #    raw1 = requests.get(href, headers={'User-Agent': 'Mozilla/5.0'})
   #    html2 = BeautifulSoup(raw1.text, "html.parser")

   #_______________________________________________________________________________________________________________________________________________________________
   #crawl.py 부분
   # headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
   # data = requests.get('https://terms.naver.com/entry.nhn?docId=2136613&cid=51000&categoryId=51000',headers=headers)
   # soup = BeautifulSoup(data.text, 'html.parser')

   #이름/ #content > div.section_wrap > div.headword_title > h2/ name2 결과값 = 게보린
   # name = soup.select_one ('#content > div.section_wrap > div.headword_title > h2')
   # name2 = name.text.replace('\h', ''), 

   # #성분/ #size_ct > p:nth-child(8)/ 결과값: <p class="txt">아세트아미노펜 300mg, 이소프로필안티피린 150mg, 카페인무수물 50mg</p>
   # ingrt = soup.select_one ('#size_ct > p:nth-child(8)')
   # #이미지/ 결과값: https://dbscthumb-phinf.pstatic.net/3323_000_18/20200419235410005_9M2AIXW4V.jpg/A11A1270A006002.jpg?type=m250&wm=N
   # img_url = soup.select_one ('#innerImage0')['data-src']

   # #효능효과/ #size_ct > p:nth-child(14)/ 결과값: <p class="txt">[허가사항변경(2013년 재평가 추가), 2015.06.09]<br/><br/>(정제)<br/>다음 질환의 진통 및 해열시 단기치료:<br/>- 두통, 치통, 발치(이를 뽑음)후 동통(통증), 인후(목구멍)통, 귀의 통증, 관절통, 신경통, 요(허리)통, 근육통, 견통(어깨통증), 타박통, 골절통, 염좌통(삔 통증), 월경통(생리통), 외상(상처)통의 진통<br/>- 오한(춥고 떨리는 증상), 발열시의 해열</p>
   # effect = soup.select_one ('#size_ct > p:nth-child(14)')

   # #용법/ #size_ct > p:nth-child(16)/ 결과값: <p class="txt">[허가사항변경(2013년 재평가 추가), 2015.06.09]<br/><br/>(정제)<br/>성인 1회 1정 1일 3회까지 공복(빈속)시를 피하여 복용한다.<br/>복용간격은 4시간 이상으로 한다.<br/>이 약은 원칙적으로 단기 복용한다.<br/>15세 미만의 소아는 이 약을 복용하지 않는다.</p>
   # intrc = soup.select_one ('#size_ct > p:nth-child(16)')

   #주의사항/ #size_ct > p:nth-child(18)/ 결과값: 생략, 작동O
   caution = soup.select_one ('#size_ct > p:nth-child(18)')









if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)