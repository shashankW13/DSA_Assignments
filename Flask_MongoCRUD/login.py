from flask import Flask, session, redirect, render_template, url_for, request
from pymongo import MongoClient
import bcrypt

app = Flask(__name__)

client = MongoClient()
db = client.Userdb
users = db.user_info


@app.route("/")
def index():
    if 'username' in session:
        return 'You are logged in as ' + session['username'] + render_template('profile.html')

    else:
        return render_template('Home.html')


@app.route("/contractor", methods=['GET', 'POST'])
def contractor():
    return render_template('Contractor_login.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    return render_template('register.html')


@app.route("/contract", methods=['GET', 'POST'])
def contract():
    return render_template('Create_contractor.html')


@app.route("/contractor/login", methods=['POST'])
def contractor_login():
    login_user = users.find_one({'name': request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password']) == \
                login_user['password']:
            session['username'] = request.form['username']
            return redirect(url_for('index'))
    return 'Invalid username/password combination'


@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect(url_for('index'))


@app.route("/contractor_save", methods=['POST', 'GET'])
def contractor_save():
    if request.method == 'POST':
        existing_user = users.find_one({'name': request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert_one({'name': request.form['username'],
                              'password': hashpass,
                              'role': "Contractor",
                              'email': request.form['email']})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        return 'Username already exists!'

    return render_template('register.html')


@app.route("/negotiator_save", methods=['POST', 'GET'])
def negotiator_save():
    if request.method == 'POST':
        existing_user = users.find_one({'name': request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert_one({'name': request.form['username'],
                              'password': hashpass,
                              'role': "Negotiator",
                              'email': request.form['email']})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        return 'Username already exists!'

    return render_template('register.html')


if __name__ == '__main__':
    app.secret_key = 'secret'
    app.run(port=5000, debug=True)
