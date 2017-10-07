'''
Shaina Peters, Helen Ye
SoftDev1 pd7
HW07 -- Do I know you?
2017-10-06
'''

# Import all necessities
from flask import Flask, render_template, request, session, redirect, url_for
import os
app = Flask(__name__) # create instance of class

# Declare our username/password combo
username = "cooldude123"
password = "Super secret password"

# Define a secret key
app.secret_key = os.urandom(32)

# Initially loading the webpage, load the welcome page
# if they're logged in
@app.route("/", methods=["GET"])
@app.route("/login", methods=["GET"])
def login():
    errors = ""
    print request.args
    if 'err' in request.args:
        errors = request.args['err']
    if session.get("uname") == username:
        return render_template('welcome.html',
                               username = username)
    else:
        return render_template('login.html',
                               errors = errors)

@app.route("/auth", methods=["POST"])
def authentification():
    # Get user-inputted username and password
    userIn = request.form["username"]
    passIn = request.form["password"]
    # Authenticate user
    if userIn == username and passIn == password:
        session["uname"] = userIn
        return render_template("welcome.html",
                               username = username)
    elif userIn != username:
        return redirect(url_for("login", err = "Incorrect username"))
    else:
        return redirect(url_for("login", err = "Incorrect password"))

# Log out the user by resetting the session
@app.route("/logout")
def logout():
    session["uname"] = ""
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.debug = True
    app.run()
