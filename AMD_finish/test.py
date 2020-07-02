#-*- coding: utf-8 -*- 
from pymongo import MongoClient
import requests
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)
client = MongoClient('localhost',27017)
db = client.drug                   

doc = {
       'name':'이름',
       'image':'https://search.pstatic.net/common/?src=http%3A%2F%2Fpost.phinf.naver.net%2FMjAxODA4MjdfMjQ1%2FMDAxNTM1MzIyMjU1MTMx.g7Lddk5Nru_GoXoth-BQwqzRKI_oYJFAXr7QgnWKHAcg.90vrFOjfqyuL3qww3dMxjQHvTjMFG5U19RLbDYFcWREg.JPEG%2FIGHXpUmOXEh_iRF1uKQcuIe8MFXE.jpg&type=b400',
       'desc': 'desc'
       # 'url':url_receive
    }
db.realdrug.insert_one(doc)