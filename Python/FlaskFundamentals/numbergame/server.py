from flask import Flask, render_template, session, redirect, request
import random
app = Flask(__name__)
app.secret_key = "fdsajkr3jFA3"

@app.route('/')
def index():
	if 'number' not in session:
		session['number'] = 0
	else:
		session['number']=random.randrange(0,101)
	return render_template('index.html')

@app.route('/guessing', methods = ['POST'])
def toguess():
	session['output'] = ''
	session['guess'] = int(request.form['guess'])
	if 'guess' not in session:
		session['output'] += 'Hmmm ... try again'
	elif session['guess'] == session['number']:
		session['output'] += 'Hah. you win'
	elif session['guess'] < session['number']:
		session['output'] += 'Wrong! too low'
	elif session['guess'] > session['number']:
		session['output'] += 'Wrong! too high'
	else:
		session['output'] += "Hmmm ... try again"
	return render_template('index.html')

@app.route('/reset', methods = ['GET'])
def cancel():
	session['guess'] = 0
	if 'output' in session:
		session.pop('output')
	return redirect('/')
	
app.run(debug=True)
