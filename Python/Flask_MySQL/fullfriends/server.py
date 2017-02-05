##THIS IS UNFINISHED.

from flask import Flask, redirect, request, render_template, flash, session
from mysqlconnection import MySQLConnector
app = Flask(__name__)
import re
import md5
mysql = MySQLConnector(app, 'friendsdb')

queries = {
	'index' : "SELECT * FROM friends",
	'create' : "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (:first_name, :last_name, :occupation, NOW(), NOW())",
	'select' : "SELECT * FROM friends WHERE id = :id",
	'delete' : "DELETE FROM friends WHERE id = :id",
	'update' : "UPDATE friends WHERE id = :id"
}

@app.route('/')
def index():
	query = queries['index']
	friends = mysql.query_db(query)
	return render_template('index.html', friends=friends)

@app.route('/friends', methods=['POST'])
def create():
	query = queries['create']
	data = {
		'first_name' : request.form['first_name'],
		'last_name' : request.form['last_name'],
		'occupation': request.form['occupation']
		}
	mysql.query_db(query, data)
	return redirect('/')

@app.route('/friends/<id>', methods=['GET'])
def select(id):
	query = queries['select']
	data = {'id' :id}
	friend = mysql.query_db(query, data)
	return render_template('friend.html', friend=friend[0])

@app.route('/goback', methods=['GET'])
def goback():
	return redirect('/')

@app.route('/friends/<id>/delete', methods=['POST'])
def delete(id):
	query = queries['delete']
	data = {'id' :id}
	mysql.query_db(query, data)
	return redirect('/')

@app.route('/friends/<id>/edit', methods=['POST'])
def edit():
	pass

app.run(debug=True)



