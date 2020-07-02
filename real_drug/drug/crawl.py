#click.py에 병합해야함
#click에서 사용자가 찾는 약을 선택하면 그 페이지로 이동하는것 이후의 코드임
#목표: 크롤링 
# #크롤링 할 객체: 이름, 사진('#innerImage0'), 효능효과, 용법, 주의사항 (정보량 방대하니 주의사항이라는 하이퍼링크를 클릭하면 다른페이지로 이동시키기)
#예제 페이지: 게보린 = https://terms.naver.com/entry.nhn?docId=2136613&cid=51000&categoryId=51000

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://terms.naver.com/entry.nhn?docId=2136613&cid=51000&categoryId=51000',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

#이름/ #content > div.section_wrap > div.headword_title > h2/ name2 결과값 = 게보린
name = soup.select_one ('#content > div.section_wrap > div.headword_title > h2')
name2 = name.text.replace('\h', ''), 

#성분/ #size_ct > p:nth-child(8)/ 결과값: <p class="txt">아세트아미노펜 300mg, 이소프로필안티피린 150mg, 카페인무수물 50mg</p>
ingrt = soup.select_one ('#size_ct > p:nth-child(8)')
#이미지/ 결과값: https://dbscthumb-phinf.pstatic.net/3323_000_18/20200419235410005_9M2AIXW4V.jpg/A11A1270A006002.jpg?type=m250&wm=N
img_url = soup.select_one ('#innerImage0')['data-src']

#효능효과/ #size_ct > p:nth-child(14)/ 결과값: <p class="txt">[허가사항변경(2013년 재평가 추가), 2015.06.09]<br/><br/>(정제)<br/>다음 질환의 진통 및 해열시 단기치료:<br/>- 두통, 치통, 발치(이를 뽑음)후 동통(통증), 인후(목구멍)통, 귀의 통증, 관절통, 신경통, 요(허리)통, 근육통, 견통(어깨통증), 타박통, 골절통, 염좌통(삔 통증), 월경통(생리통), 외상(상처)통의 진통<br/>- 오한(춥고 떨리는 증상), 발열시의 해열</p>
effect = soup.select_one ('#size_ct > p:nth-child(14)')

#용법/ #size_ct > p:nth-child(16)/ 결과값: <p class="txt">[허가사항변경(2013년 재평가 추가), 2015.06.09]<br/><br/>(정제)<br/>성인 1회 1정 1일 3회까지 공복(빈속)시를 피하여 복용한다.<br/>복용간격은 4시간 이상으로 한다.<br/>이 약은 원칙적으로 단기 복용한다.<br/>15세 미만의 소아는 이 약을 복용하지 않는다.</p>
intrc = soup.select_one ('#size_ct > p:nth-child(16)')

#주의사항/ #size_ct > p:nth-child(18)/ 결과값: 생략, 작동O
caution = soup.select_one ('#size_ct > p:nth-child(18)')






