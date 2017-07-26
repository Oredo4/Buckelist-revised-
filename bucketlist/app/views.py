# views.py

from flask import render_template, request, redirect, url_for
from app import app
from .models import User
from .bucketlist import Bucketlist

users = User()
bucket = Bucketlist()

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == "POST":
		email = request.form["username"]
		password = request.form["password1"]
		confirm_password = request.form["password2"]
		users.register_user(email, password, confirm_password)
		return redirect(url_for("signin"))
	return render_template("index.html")

@app.route('/signin', methods=['GET', 'POST'])
def signin():
	if request.method == "POST":
		email = request.form["username"]
		password = request.form["password1"]
		if users.login(email, password) == "Log in successful":
			return render_template("bucketlist.html")
	return render_template("signin.html")

@app.route('/bucketlist', methods=['GET', 'POST'])
def bucketlist():
	if request.method == "POST":
		name = request.form["bucketlist_name"]
		bucket.create_bucketlist(name)
		return redirect(url_for('bucketlist'))
	instance = bucket.view_bucketlist()
	return render_template("bucketlist.html", instance=instance)

@app.route('/additems', methods=['POST'])
def additems():
    return render_template("additems.html")
