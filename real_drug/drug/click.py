##목표:사용자가 찾는 약을 선택하면 그 페이지로 이동하기
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote_plus
from bs4 import BeautifulSoup


base_url = 'https://terms.naver.com/search.nhn?query='
plus_url = input('약품 이름을 입력하세요! :')
url = base_url + quote_plus(plus_url)

# # 네이버 백과사전을 열어서 약품 검색
driver = webdriver.Chrome('/Users/Chaser/Desktop/Sparta2🛠/Projects/drug/chromedriver')
driver.get(url)

##검색 결과에서 해당 의약품을 한번 더 클릭
## 추후에는 결과에서 나온 이름이 비슷한 의약품을 모두 정렬하고 선택할수 있게 해야함
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

##soup.select('.info_area') 안에 info_area로 설정하는것이 어려웠움
##이상한것이 섞여나오니 약품설명 밑에 "더보기"를 클릭하게 해서 제한해야함
##약품 이름을 클릭하면 하이퍼링크가 클릭되서 해당화면으로 넘어가야함
info_area = soup.select('.info_area')
for i in info_area:
    # print(i.select_one('.title')?.text)

##비슷한 이름의 약품별로 이름과 하이퍼링크 따오기
    base_href = 'https://terms.naver.com/'
    plus_href = i.a.attrs['href']
    href = base_href + plus_href
    raw1 = requests.get(href, headers={'User-Agent': 'Mozilla/5.0'})
    html2 = BeautifulSoup(raw1.text, "html.parser")


