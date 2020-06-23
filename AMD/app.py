from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)


client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.AMD  # 'dbsparta'라는 이름의 db를 만듭니다.

# HTML을 주는 부분


@app.route('/')
def home():
    return render_template('index.html')

# API 역할을 하는 부분
@app.route('/list_movie', methods=['GET'])
def list_movie_get():
    want_year = request.args.get('want_year')
    print(want_year)
    # movies_list = list(db.movie.find({'Year':str(want_year)}))
    movies_list = list(db.movie.find({'Year': int(want_year)}, {'_id': False}))
    return jsonify({'result':'success', 'movies':movies_list})

@app.route('/list_drama', methods=['GET'])
def list_drama_get():
    want_year = request.args.get('want_year')
    print(want_year)
    # movies_list = list(db.movie.find({'Year':str(want_year)}))
    dramas_list = list(db.drama.find({'Year': int(want_year)}, {'_id': False}))
    return jsonify({'result':'success', 'dramas':dramas_list})

@app.route('/list_music', methods=['GET'])
def list_music_get():
    want_year = request.args.get('want_year')
    print(want_year)
    # movies_list = list(db.movie.find({'Year':str(want_year)}))
    musics_list = list(db.music.find({'Year': str(want_year)+"년"}, {'_id': False}))
    return jsonify({'result':'success', 'musics':musics_list})


if __name__ == '__main__':
    app.run('localhost', port=5000, debug=True)
