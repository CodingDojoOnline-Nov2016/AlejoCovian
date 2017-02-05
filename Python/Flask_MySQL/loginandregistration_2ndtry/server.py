from flask import Flask, redirect, request, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)
import re
email_regex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app.secret_key = "f42jkfldsnakfl2jfsd;alfjhjkfAAAfjk"
mysql = MySQLConnector(app, 'loginandregister')
queries = {
	'register' : "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())",
	'pick' : "SELECT * FROM users WHERE email = :email LIMIT 1"
}

@app.route('/')
def index():
	if 'id' not in session:
		return render_template('index.html')
	elif 'id' in session:
		return redirect('/welcome')

@app.route('/register', methods = ['POST'])
def register():
	email = request.form['email']
	password = request.form['password']
	first_name = request.form['first_name']
	last_name = request.form['last_name']
	confirm_password = request.form['confirm_password']
	if len(first_name) < 1:
		flash("You need to input a first name to register.")
	if len(last_name) < 1:
		flash("You need to input a last name to register.")
	if len(email) < 1:
		flash("How can you register with us if you didn't even put in an email?")
	if not email_regex.match(email):
		flash("Invalid Email Address.")
	if len(password) < 1:
		flash("How do you expect to have a secure account without a long password?")
	elif password != confirm_password:
		flash("Passwords don't match. Darnit.")
	else:
		query = queries['register']
		pw_hash = bcrypt.generate_password_hash(password)
		data = {
			'first_name': first_name,
			'last_name' : last_name,
			'email': email,
			'password': pw_hash
		}
		mysql.query_db(query, data)
		login_query = queries['pick']
		login_data = {
			'email':email
		}
		user = mysql.query_db(login_query, login_data)
		session['id']= user[0]['first_name']
		return redirect('/welcome')

	return redirect('/')

@app.route('/login', methods = ['POST'])
def login():
	if len(request.form['email']) < 1:
		flash('invalid email.')
		return redirect('/')
	if len(request.form['password']) < 1:
		flash('invalid password')
		return redirect('/')
	email = request.form['email']
	password = request.form['password']
	query = queries['pick']
	data = {
		'email': email,
	}
	user = mysql.query_db(query, data)
	if bcrypt.check_password_hash(user[0]['password'], password):
		session['id'] = user[0]['first_name']
		return redirect('/welcome')
	else:
		flash("Whoops! Incorrect login.")
		return redirect('/')

@app.route('/welcome')
def welcome():
		return render_template('welcome.html')

@app.route('/logout')
def logout():
	session.pop('id')
	return redirect('/')


if __name__ == "__main__":
	app.run(debug=True)



