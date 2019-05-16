from flask import Flask, render_template, request, jsonify, session, json, redirect, url_for
import pymongo

mongo_url = 'mongodb+srv://song:yeji9140@cluster0-v0lp5.mongodb.net/test?retryWrites=true'
client = pymongo.MongoClient(mongo_url)
db = pymongo.database.Database(client,'Cluster0')
books = pymongo.collection.Collection(db,'Books')
Users = pymongo.collection.Collection(db,'Users')


app = Flask(__name__)
app.secret_key = "111"

#with open("mongoDB,json") as Json:
#    user_doc = json.loads(Json.read())


@app.route('/register')
def score():
    return render_template('register.html')  

#요청은 request.form에 다 담김!
@app.route('/books', methods=['GET','POST'])
def result():
    if request.method == 'POST': 
        books.insert_one(request.form.to_dict(flat='true'))
      
    #return books.watch()
    return render_template('books.html',result = books.find({})) 

@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    elif request.method == 'POST':
        Users.insert_one(request.form.to_dict(flat='true'))
        session['userEmail'] = request.form['userEmail']
	return render_template('welcome.html',info = session['userEmail'])

@app.route('/signin', methods=['GET''POST'])
def signin():
    if request.method == 'GET':
        return render_template('signin.html')
    elif request.method == 'POST':
        if Users.find_one(request.form.to_dict(flat='true')) is not None:
	    session['userEmail'] = request.form['userEmail']
            return render_template('welcome.html', info = session['userEmail'])
	return redirect(url_for('signin'))


if __name__ == '__main__':
    app.run(host='0.0.0.0',port = 5000)


