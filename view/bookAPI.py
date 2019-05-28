from flask import Blueprint,request, render_template, session, redirect, url_for
from .db import mongo_connection, booksDAO

db_connection = mongo_connection.ConnectDB().db
books = booksDAO.Book(db_connection)

bookAPI =  Blueprint('bookAPI',__name__, template_folder='templates')

@bookAPI.route('/register')
def register():
    if not 'userEmail' in session:
        return render_template('signin.html')
    return render_template('register.html')

@bookAPI.route('/books', methods=['GET', 'POST'])
def showbooks():
    if request.method == 'POST':
        if not 'userEmail' in session :
            return render_template('signin.html')
        books.BookCreate(request.form.to_dict(flat='true'))
    if not 'userEmail' in session:
        return render_template('signin.html')
    all_book=books.getAllbooks()
    return render_template('books.html', result=all_book)
