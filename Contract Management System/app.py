from flask import Flask, render_template
from flask import jsonify, request
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash

app = Flask(__name__)

app.secret_key = "secretkey"

app.config['MONGO_URI'] = "mongodb://localhost:27017/Users"

mongo = PyMongo(app)


# @app.route("/")
# def hello():
#   return render_template("index2.html")

@app.route("/")
def contractor_login():
    # return render_template("Contractor_login.html")
    return render_template("index2.html")
    # return render_template("Homepage.html")


@app.route("/save", methods=['POST'])
def save():
    return render_template("Create_contractor.html")


@app.route("/add", methods=['POST'])
def add_user():
    # _json = request.json
    # _name = _json['name']
    # _email = _json['email']
    # _password = _json['pwd']

    _name = request.form['username']
    # _email = request.form['email']
    _password = request.form['pwd']

    if _name and _password and request.method == 'POST':
        _hashed_password = generate_password_hash(_password)

        id = mongo.db.users.insert_one({'name': _name, 'password': _hashed_password})

        resp = jsonify("User added successfully")

        resp.status_code = 200

        # return resp
        # return "User Successfully Logined."
        return render_template("Contractor_contents.html")

    else:
        return not_found()


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found' + request.url
    }

    resp = jsonify(message)

    resp.status_code = 404

    return resp


if __name__ == "__main__":
    app.run(debug=True, port=8888)
