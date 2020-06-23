#-*- coding: utf-8 -*- 
from pymongo import MongoClient
from bs4 import BeautifulSoup
import requests
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)


client = MongoClient('localhost', 27017)
db = client.AMD
doc="세월호 세월호 겨울왕국 let it go 명량 가오갤 인터스텔라 하지마 별그대 김수현 전지현 정도전 장보리 미생 밀회 피노키오 AOA 짧은치마 단발머리 눈코입 연결고리 마마무 방탄 상남자 걸스데이 엘사 울라프 엘사 울라프 월드컵 월드컵 월드컵 월드컵 으리 신토부으리 의리 의리 의리 의리 김보성 호갱 흑우 호갱님 호갱 "
db.keyWord.update_one({'Year':2014},{'$set':{'keyword_list':doc}})