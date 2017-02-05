from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key="fklfamdsflkk3"

@app.route('/')
def index():
	if 'count' not in session:
		session['count'] = 0
	else:
		session['count']+=1
	return render_template('index.html')

@app.route('/add2')
def add2():
	session['count']+=1
	return redirect('/')

@app.route('/goback')
def goback():
	session['count']=0
	return redirect('/')

app.run(debug=True)