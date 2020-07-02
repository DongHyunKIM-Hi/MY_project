from pymongo import MongoClient 
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)
client = MongoClient('mongodb://hyundong_k:940dfg@13.125.220.235',27017)
db = client.AMD  

# HTML을 주는 부분


@app.route('/')
def home():
    return render_template('index.html')

# API 역할을 하는 부분
@app.route('/list_movie', methods=['GET'])
def list_movie_get():
    want_year = request.args.get('want_year')
    movies_list = list(db.movie.find({'Year': int(want_year)}, {'_id': False}))
    return jsonify({'result':'success', 'movies':movies_list})

@app.route('/list_drama', methods=['GET'])
def list_drama_get():
    want_year = request.args.get('want_year')
    dramas_list = list(db.drama.find({'Year': int(want_year)}, {'_id': False}))
    return jsonify({'result':'success', 'dramas':dramas_list})

@app.route('/list_music', methods=['GET'])
def list_music_get():
    want_year = request.args.get('want_year')
    musics_list = list(db.music.find({'Year': str(want_year)+"년"}, {'_id': False}))
    return jsonify({'result':'success', 'musics':musics_list})

@app.route('/best_list', methods=['GET'])
def best_list_get():
    want_year = request.args.get('want_year')
    best_music = list(db.music.find({'Year': str(want_year)+"년"}, {'_id': False}).sort('like',-1))
    best_drama = list(db.drama.find({'Year': int(want_year)}, {'_id': False}).sort('like',-1))
    best_movie = list(db.movie.find({'Year': int(want_year)}, {'_id': False}).sort('like',-1))
    return jsonify({'result':'success', 'music':best_music, 'drama': best_drama, 'movie': best_movie})

@app.route('/music/like', methods=['POST'])
def music_like():
    name_receive = request.form['name_give']
    like = db.music.find_one({'name':name_receive})
    new_like = like['like']+1
    db.music.update_one({'name':name_receive},{'$set':{'like':new_like}})
    return jsonify({'result': 'success'})

@app.route('/drama/like', methods=['POST'])
def drama_like():
    name_receive = request.form['name_give']
    like = db.drama.find_one({'name':name_receive})
    new_like = like['like']+1
    db.drama.update_one({'name':name_receive},{'$set':{'like':new_like}})
    return jsonify({'result': 'success'})

@app.route('/movie/like', methods=['POST'])
def movie_like():
    name_receive = request.form['name_give']
    
    like = db.movie.find_one({'name':name_receive})
    
    new_like = like['like']+1
    db.movie.update_one({'name':name_receive},{'$set':{'like':new_like}})

    return jsonify({'result': 'success'})

@app.route('/make_keyword', methods=['GET'])
def keyword_get():
    want_year = request.args.get('want_year')
    keyword_list = db.keyWord.find_one({'Year': int(want_year)}, {'_id': False})
    return jsonify({'result':'success', 'keyword':keyword_list})

@app.route('/input_keyword', methods=['POST'])
def keyword_post():
    key_receive = request.form['key_give']
    print("확인1")
    year_receive = request.form['year_give']
    print("확인2")
    key = db.keyWord.find_one({'Year':int(year_receive)})
    print(key['keyword_list'])
    doc= str(key['keyword_list'])+","+str(key_receive)
    print(doc)
    db.keyWord.update_one({'Year':int(year_receive)},{'$set':{'keyword_list':doc}})

    return jsonify({'result': 'success'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
