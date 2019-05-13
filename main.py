from flask import Flask, render_template, request, jsonify
import pymongo

mongo_url = 'mongodb+srv://song:yeji9140@cluster0-v0lp5.mongodb.net/test?retryWrites=true'
client = pymongo.MongoClient(mongo_url)
db = pymongo.database.Database(client,'Cluster0')

app = Flask(__name__)

@app.route('/register')
def score():
    return render_template('register.html')  

#요청은 request.form에 다 담김!
@app.route('/books', methods=['GET','POST'])
def result():
    if request.method == 'GET': #입력값 없이 바로 주소쳐서 넘어갔을 경우
        return "It's GET"
    
    return render_template('books.html')  

if __name__ == '__main__':
    app.run(host='0.0.0.0',port = 5000)


