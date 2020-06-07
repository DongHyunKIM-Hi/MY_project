from flask import Flask, render_template
app = Flask(__name__)

## URL 별로 함수명이 같거나,
## route('/') 등의 주소가 같으면 안됩니다.

@app.route('/')
def home():
   return render_template('main_login.html')

@app.route('/create_account')
def register():
   return render_template('create_account.html')
if __name__ == '__main__':
   app.run('localhost', port=5000, debug=True)