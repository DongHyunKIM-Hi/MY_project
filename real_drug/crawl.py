import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
import re
from pymongo import MongoClient          
client = MongoClient('localhost',27017)
db = client.dbsparta     

# dnm = drug name/ dnb = drug number
#ranks.append 로 사용해서 시간을 정말 많이 허비함. append로 해보니 [ranks][ranks_add] 형태로 추가됨 -> extend를 이용 확장하는것으로 변경
ranks = [
    {'dnm':'게보린정', 'dnb':'2140308'}, {'dnm':'타메타정', 'dnb':'2134977'},{'dnm':'광동원탕', 'dnb':'2139155'},{'dnm':'이가탄에프', 'dnb':'2164251'},{'dnm':'아로나민골드', 'dnb':'2133933'},{'dnm':'노스카나겔', 'dnb':'2129266'},{'dnm':'게보린', 'dnb':'2136613'},{'dnm':'인사돌플러스', 'dnb':'2147474'},{'dnm':'베나치오에프액', 'dnb':'2131309'},{'dnm':'테라플루 나이트타임', 'dnb':'2150722'},
    {'dnm':'판피린큐액', 'dnb':'2147161'},{'dnm':'판콜에스내복액', 'dnb':'2134976'},{'dnm':'케토톱플라스타', 'dnb':'2133620'},{'dnm':'타이레놀', 'dnb':'2140308'},{'dnm':'광동경옥고', 'dnb':'2161921'},{'dnm':'탁센연질캡슐', 'dnb':'2132214'},{'dnm':'잇치페이스트', 'dnb':'2163218'} #10까지
]


ranks_problem = [
    {'dnm':'임팩타민프리미엄', 'dnb':'2126845'},{'dnm':'비맥스메타정', 'dnb':'5743347'},{'dnm':'엑세라민엑소정', 'dnb':'3340899'},
    {'dnm':'텐텐츄정', 'dnb':'2145609'},{'dnm':'벤포벨정', 'dnb':'3341068'},{'dnm':'머시론정', 'dnb':'머시론정'}, 
    {'dnm':'우루사', 'dnb':'2134422'},{'dnm':'아이록 점안액', 'dnb':'2698641'},{'dnm':'광동우황청심원현탁액', 'dnb':'2139152'},{'dnm':'광동우황청심원환(사향)', 'dnb':'2139170'},{'dnm':'둘코락스-에스', 'dnb':'2124747'},{'dnm':'후시딘연고10g', 'dnb':' 후시딘연고10g '},{'dnm':'겔포스엠현탁액', 'dnb':'2135848'},{'dnm':'비판텐연고', 'dnb':'2158633'},{'dnm':'마그비액티브정', 'dnb':'3651447'},{'dnm':'경방갈근탕액', 'dnb':'2148669'},{'dnm':'인사돌', 'dnb':'2132742'},{'dnm':'코앤쿨나잘스프레이', 'dnb':'2849962'},{'dnm':'아렉스 ', 'dnb':'2147656'},{'dnm':'오트리빈멘톨0.1%분무제', 'dnb':'2153258'},{'dnm':'광동우황청심원현탁액', 'dnb':'2139152'},{'dnm':'복합우루사연질캡슐', 'dnb':'2153236'},{'dnm':'이지엔6 이브연질캡슐', 'dnb':'2129211'},{'dnm':'챔프시럽', 'dnb':'2128565'}, #45까지
    {'dnm':'테라플루콜드&코프나이트', 'dnb':'2126711'},{'dnm':'테라플루데이타임건조시럽', 'dnb':'2150721'},{'dnm':'이지엔6프로연질캡슐', 'dnb':'2159189'},{'dnm':'아로나민실버프리미엄', 'dnb':'2698355'} #50까지
]


# ranks.extend(ranks_add)
ranks.extend(ranks_problem)


for rank in ranks_problem:
    base_url = 'https://terms.naver.com/entry.nhn?docId='
    plus_url = rank['dnb']
    url_after = '&cid=51000&categoryId=51000'
    url = base_url + plus_url + url_after
    print(url)
    


#크롤링 할것: 이름, (제조사), 사진, 효과, 성분, 복용법, 주의사항
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url,headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    d_name = soup.select_one('meta[property="og:title"]')['content']
    d_image = soup.select_one('meta[property="og:image"]')['content']
    og_desc = soup.select_one('meta[property="og:description"]')['content']
    desc_pre_div = og_desc.replace('[','<').replace(']','>')
    desc_div= [i for i in re.split('<[^<>]+>', desc_pre_div) if i !='']
    # wae = '[외형정보]' +  desc_div[0]
    # sung = '[성분정보]' + desc_div[1]
    # ju = '[저장방법]' + desc_div[2]
    # hyo = '[효능효과]' + desc_div[3]
    # yong = '[용법용량]' + desc_div[5]
    print(d_name)
    print(og_desc)


    # d_list = {'name':d_name, 'img_url':d_image, 'shape':wae, 'ingrt':sung, 'store':ju, 'effect':hyo, 'inst':yong, 'url':url}

    # db.drugs.insert_one(d_list)






    