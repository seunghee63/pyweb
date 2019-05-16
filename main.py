from flask import Flask, render_template, request, jsonify
import pymongo

mongo_url = 'mongodb+srv://song:yeji9140@cluster0-v0lp5.mongodb.net/test?retryWrites=true'
client = pymongo.MongoClient(mongo_url)
db = pymongo.database.Database(client,'Cluster0')
books = pymongo.collection.Collection(db,'Books')

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(host='0.0.0.0',port = 5000)


