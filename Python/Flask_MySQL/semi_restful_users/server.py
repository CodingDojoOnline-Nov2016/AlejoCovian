from flask import Flask, request, redirect, render_template, session
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'semirestfulusers')
app.secret_key = "098f0dsa098fsAKLFjdslakfjdskjl"

queries = {
	'select': "SELECT * FROM users",
	'show': "SELECT * FROM users WHERE id = :id"
}

@app.route('/')
def index():
	query = queries['select']
	users = mysql.query_db(query)
	return render_template('index.html', users=users)

@app.route('/show<id>')
def show(id):
	query = queries['show']
	data = {
		'id':id
	}
	users = mysql.query_db(query,data)
	return render_template('show.html', users=users)

@app.route('/edit<id>')
def edit(id):
	query = queries['show']
	data = {
		'id':id
	}
	users = mysql.query_db(query,data)
	return render_template('edit.html', users=session['user'])

app.run(debug=True)