###PROTOTYPE

from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import MySQLConnector
app = Flask(__name__)
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
import re
email_regex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
mysql = MySQLConnector(app, 'thewalldb')
app.secret_key = "PPPdsajkrlewaFLKdjsalfkjs"

queries = {
	'register': "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name,:last_name,:email,:password, NOW(), NOW())",
	'select': "SELECT * FROM users WHERE email = :email LIMIT 1",
	'indexusers': "SELECT * FROM users",
	'indexmessages': "SELECT * FROM users JOIN messages ON users.id = messages.user_id ORDER BY messages.id DESC",
	'indexcomments': "SELECT * FROM users JOIN comments ON users.id = comments.user_id LEFT JOIN messages ON comments.message_id = messages.id ORDER BY comments.id ASC",
	'insertmessage': "INSERT INTO messages (message, created_at, updated_at, user_id) VALUES (:message, NOW(), NOW(), :user_id)",
	'insertcomment': "INSERT INTO comments (comment, created_at, updated_at, message_id, user_id) VALUES(:comment, NOW(), NOW(), :message_id, :user_id)"
}

@app.route('/')
def index():
	if 'data' not in session:
		return render_template('login.html')
	else:
		return redirect('/welcome')

@app.route('/login', methods=['POST'])
def login():
	email = request.form['email']
	password = request.form['password']
	if len(email)<1:
		flash('You need to input an email in order to log in.')
		return redirect('/')
	if len(password)<1:
		flash('You need to input a password in order to log in.')
		return redirect('/')
	else:
		query = queries['select']
		data = {
			'email': email
		}
		user = mysql.query_db(query, data)
		if bcrypt.check_password_hash(user[0]['password'], password):
			session['data']=user[0]
			return redirect('/welcome')
		else:
			flash("Whoops! Account does not exist in the database.")
			return redirect('/')

@app.route('/register', methods=['POST'])
def register():
	first_name = request.form['first_name']
	last_name = request.form['last_name']
	email = request.form['email']
	password = request.form['password']
	confirm_password = request.form['confirm_password']
	if len(first_name)<1:
		flash("You need a first name.")
	if len(last_name)<1:
		flash("You need a last name.")
	if len(email)<1:
		flash("You need an email.")
	if len(password)<1:
		flash("You need a password.")
	if not email_regex.match(email):
		flash("Invalid Email Address. It must look something like this@example.etc")
	elif len(password)<8:
		flash("Your password must be at least eight characters in length.")
	elif password != confirm_password:
		flash("Passwords don't match.")
	else:
		regquery = queries['register']
		pw_hash = bcrypt.generate_password_hash(password)
		regdata = {
			'first_name': first_name,
			'last_name': last_name,
			'email': email,
			'password': pw_hash
		}
		mysql.query_db(regquery, regdata)

		query = queries['select']
		data = {
			'email': email
		}
		user = mysql.query_db(query, data)
		if bcrypt.check_password_hash(user[0]['password'], password):
			session['data']=user[0]
		return redirect('/welcome')

	return redirect('/')

@app.route('/welcome')
def welcome():
	query = queries['indexusers']
	users = mysql.query_db(query)
	messagequery = queries['indexmessages']
	messages = mysql.query_db(messagequery)
	commentquery = queries['indexcomments']
	comments = mysql.query_db(commentquery)
	return render_template('thewall.html', data=session['data'], users=users, messages=messages, comments=comments)

@app.route('/message', methods=['POST'])
def message():
	if len(request.form['message'])<1:
		return redirect('/welcome')
	else:
		query = queries['insertmessage']
		data = {
			'message' : request.form['message'],
			'user_id' : session['data']['id']
		}
		mysql.query_db(query,data)
		return redirect('/welcome')

@app.route('/comment/<message_id>', methods=['POST'])
def comment(message_id):
	if len(request.form['comment'])<1:
		return redirect('/welcome')
	else:
		query = queries['insertcomment']
		data = {
			'comment' : request.form['comment'],
			'message_id': message_id,
			'user_id' : session['data']['id']
		}
		mysql.query_db(query,data)
		print message_id
		return redirect('/welcome')

@app.route('/logout', methods=['POST'])
def logout():
	session.pop('data')
	return redirect('/')

app.run(debug=True)


