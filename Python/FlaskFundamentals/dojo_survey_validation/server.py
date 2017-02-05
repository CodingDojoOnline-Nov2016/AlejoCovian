from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key='very secret'

@app.route('/')
def index():
	return render_template('first.html')
@app.route('/create', methods = ['POST'])
def create():
	data = request.form
	error = False
	if len(request.form['description']) ==0:
		error = True
		session['description_len']= "must be greater than 0"
	if len(request.form['name'])==0:
		error = True
		session['name_len']="must be greater than 0"
	if len(request.form['description']) > 221:
		error = True
		session['description_len'] = "must be less than 120"
	if error:
		return redirect('/')
	session.pop('name_len')
	session.pop('description_len')
	return render_template('result.html', data=data)

if __name__ == "__main__":
	app.run(debug=True)