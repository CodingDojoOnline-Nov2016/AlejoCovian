from flask import Flask, redirect, request, render_template, session, flash
import re
email_regex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'urwifjnk3utrsoi'
mysql = MySQLConnector(app, 'loginandregister')
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

queries = {
	'index': "SELECT * FROM users",
	'register': "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())",
	'select': "SELECT * FROM users WHERE email = :email LIMIT 1",
	'by_email': "SELECT id, password FROM users WHERE email = :email"
} 

@app.route('/')
def index():
	if 'data' not in session:
		return render_template('index.html')
	else:
		return redirect('/welcome')


@app.route('/register', methods = ['POST'])
def register():
	first_name = request.form['first_name']
	last_name = request.form['last_name']
	email = request.form['email']
	password = request.form['password']
	if len(first_name) < 1:
		flash("You left the first name field empty.")
	elif len(last_name) < 1:
		flash("You left the last name field empty.")
	elif len(email) < 1:
		flash("You left the email field empty.")
	elif len(password) < 1:
		flash("You left the password field empty.")

	elif request.form['first_name'].isalpha() == False:
		flash('Name cannot have numbers in it.')
	elif request.form['last_name'].isalpha() == False:
		flash('Name cannot have numbers in it.')
	elif not email_regex.match(request.form['email']):
		flash("Invalid Email Address.")

	else:
		query = queries['register']
		pw_hash = bcrypt.generate_password_hash(password)
		data = {
			'first_name': first_name,
			'last_name': last_name,
			'email': email,
			'password': pw_hash
		}
		mysql.query_db(query, data)
		session['data'] = data
		return redirect('/welcome')
	return redirect('/')

@app.route('/login', methods = ['POST'])
def login():
	email = request.form['email']
	password = request.form['password']
	if len(email)<1:
		flash("No email added")
	if len(password)<1:
		flash("You forgot your password")
	else:
		query = queries['select']
		data = {
			'email':email
		}
		user = mysql.query_db(query, data)
		if bcrypt.check_password_hash(user[0]['password'], password):
			session['data'] = user[0]
			return redirect('/welcome')
	return redirect('/welcome')

@app.route('/welcome')
def welcome():
	return render_template('success.html', data = session['data'])

@app.route('/logout', methods = ['POST'])
def logout():
	session.pop('data')
	return redirect('/')

app.run(debug=True)


