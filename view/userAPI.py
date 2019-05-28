from flask import Blueprint,request, render_template, session, redirect, url_for
from .db import mongo_connection, usersDAO

db_connection = mongo_connection.ConnectDB().db
users = usersDAO.User(db_connection)

userAPI = Blueprint('userAPI',__name__, template_folder='templates')

@userAPI.route('/signup', methods=['GET', 'POST'])
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
                    
@userAPI.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'GET':
        if not 'userEmail' in session:
            return render_template('signin.html')
        return render_template('welcome.html', info = "이미 로그인 하셨습니다. 로그아웃 후, 재 로그인이 가능합니다.")
    elif request.method == 'POST':
        if users.find_one(request.form.to_dict(flat='true'))is not None:
            session['userEmail'] = request.form['userEmail']
            return render_template('welcome.html', info=session['userEmail'])
        if not 'userEmail' in session:
            return render_template('welcome.html', info ="이미 로그인 하셨습니다. 로그아웃 후, 재 로그인이 가능합니다.")
        return redirect(url_for('signin'))

@userAPI.route('/logout')
def logout():
    if 'userEmail' in session:
        session.pop('userEmail')
        return redirect(url_for('signin'))
    return redirect(url_for('signin'))
