from pymongo import MongoClient
client = MongoClient('mongodb://test:test@localhost',27017)
db = client.dbsparta

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
   return 'This is Home!'

if __name__ == '__main__':  
   app.run('0.0.0.0', port=5000, debug=True)