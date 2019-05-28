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
            if not users.userCreate(request.form.to_dict(flat='true')):
                #중복 회원가입
                return render_template('welcome.html', info='중복된 아이디입니다.')
            else:
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
        if users.userAuthentication(request.form.to_dict(flat='true')):
            session['userEmail'] = request.form['userEmail']
            return render_template('welcome.html', info=session['userEmail'])
        else:
            return render_template('welcome.html', info ="잘못된 아이디/비밀번호 입니다.")
        if not 'userEmail' in session:
            return render_template('welcome.html', info ="이미 로그인 하셨습니다. 로그아웃 후, 재 로그인이 가능합니다.")
        return redirect(url_for('userAPI.signin'))

@userAPI.route('/logout')
def logout():
    if 'userEmail' in session:
        session.pop('userEmail')
        return redirect(url_for('userAPI.signin'))
    return redirect(url_for('userAPI.signin'))
