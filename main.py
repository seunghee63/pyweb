from flask import Flask, render_template, request, jsonify, session, json, redirect, url_for
import pymongo
from datetime import timedelta

mongo_url = 'mongodb+srv://song:yeji9140@cluster0-v0lp5.mongodb.net/test?retryWrites=true'
client = pymongo.MongoClient(mongo_url)
db = pymongo.database.Database(client, 'Cluster0')
books = pymongo.collection.Collection(db, 'Books')
users = pymongo.collection.Collection(db, 'Users')

app = Flask(__name__)
app.secret_key = "111"

# with open("mongoDB,json") as Json:
#    user_doc = json.loads(Json.read())

@app.route('/register')
def register():
    if not 'userEmail' in session:
        return render_template('signin.html')

    return render_template('register.html')

# 요청은 request.form에 다 담김!
@app.route('/books', methods=['GET', 'POST'])
def showbooks():
    if request.method == 'POST':
        if not 'userEmail' in session :
            return render_template('signin.html')
        books.insert_one(request.form.to_dict(flat='true'))
    if not 'userEmail' in session:
        return render_template('signin.html')
    return render_template('books.html', result=books.find({}))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        if not 'userEmail' in session:
            return render_template('signup.html')
        return render_template('welcome.html', info="로그인이 된 상황입니다. 로그아웃 후, 회원가입이 가능합니다.")
    elif request.method == 'POST':
        if not 'userEmail' in session:
            users.insert_one(request.form.to_dict(flat='true'))
            session['userEmail'] = request.form['userEmail']
            return render_template('welcome.html', info=session['userEmail'])
        return render_template('welcome.html', info='이미 로그인이 되었습니다:)')


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'GET':
        if not 'userEmail' in session:
            return render_template('signin.html')
        return render_template('welcome.html', info = "이미 로그인 하셨습니다. 로그아웃 후, 재 로그인이 가능합니다..")
    elif request.method == 'POST':
        if users.find_one(request.form.to_dict(flat='true'))is not None:
            session['userEmail'] = request.form['userEmail']
            return render_template('welcome.html', info=session['userEmail'])
        if not 'userEmail' in session:
            return render_template('welcome.html', info ="이미 로그인 하셨습니다. 로그아웃 후, 재 로그인이 가능합니다.")
        return redirect(url_for('signin'))


@app.route('/logout')
def logout():
    if 'userEmail' in session:
        session.pop('userEmail')
        return redirect(url_for('signin'))
    return redirect(url_for('signin'))


@app.before_request
def make_session_permanent():
    session.parmanent = True
    app.permannent_session_lifetime = timedelta(minutes=60)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
