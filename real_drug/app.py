from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost',27017)
db = client.drug

# HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

# API 역할을 하는 부분
@app.route('/search', methods=['GET'])
def drug_list():
   want_name = request.args.get('drug_name')
   drug=db.realdrug.find_one(({'name':want_name}),{'_id':False})
   print(drug['name'])
   return jsonify({'result':'success', 'search_result':drug})   
   
@app.route('/review/make', methods=['POST'])
def review_list():
   name_receive = request.form['drug_name']
   review_receive = request.form['drug_review']
   review = {
       'name': name_receive,
       'review': review_receive}
   drug_review=db.drugreview.insert_one(review)
   return jsonify({'result': 'success', 'msg': '리뷰가 성공적으로 작성되었습니다.'})

@app.route('/review/list', methods=['GET'])
def review_list_get():
    want_name = request.args.get('drug_name')
    reviews = list(db.drugreview.find({'name':want_name},{'_id':0}))
    return jsonify({'result': 'success', 'reviews': reviews})

if __name__ == '__main__':
    app.run('localhost', port=5000, debug=True)