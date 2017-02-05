from flask import Flask, redirect, render_template, request, session, flash
import re
email_regex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = 'f3nq2k2l_rf92q0'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/result', methods = ['POST'])
def result():

	if len(request.form['first_name']) < 1:
		flash('First name cannot be blank.')
	if len(request.form['last_name']) < 1:
		flash('Last name cannot be blank.')
	if len(request.form['email']) < 1:
		flash('Email cannot be blank.')
	if len(request.form['password']) < 1:
		flash('Password cannot be blank.')
	if len(request.form['password']) < 8:
		flash('Password must have at least 8 characters.')

	elif request.form['password'] != request.form['confirm_password']:
		flash('Password confirmation does not match.')
	if request.form['first_name'].isalpha() == False:
		flash('Name cannot have numbers in it.')
	if request.form['last_name'].isalpha() == False:
		flash('Name cannot have numbers in it.')
	if not email_regex.match(request.form['email']):
		flash("Invalid email address.")
		
	else:
		flash('Thanks for submitting your information.')
	return redirect('/')

app.run(debug=True)