from flask import Flask
from flask import render_template
import db

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/account")
def account():
    id = db.get_user_id("test@test")
    return "Hello / account" + str(id)

@app.route("/reader")
def reader():
    return "Hello / reader"

@app.route("/reader/<id>")
def read_id(id):
    return "Hello / read id=" + str(id)

## API
@app.route("/acc/create")
@app.route("/acc/login")
def create_acc():
    return "Hello / create acc"