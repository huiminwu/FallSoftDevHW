#Hui Min Wu and Jack Lu, Team Teenage Mutant Jinja Turtles
#SoftDev1 pd7
#K15 -- Oh yes, perhaps I do...
#2018-10-02

from flask import Flask, render_template, request, url_for, redirect, session
import os
app = Flask(__name__)
app.secret_key = os.urandom(32) #generate a private key and assing to built in secret key

user = {"hui" : "min"}

@app.route("/", methods=["POST", "GET"])
def display():
    if "hui" in session:
        return render_template('welcome.html',
                               text = "Welcome!")
    return redirect(url_for("display_login")) #if you're not logged in, you're redirected to the login page

@app.route("/login", methods=["POST", "GET"])
def display_login():
    return render_template('login.html')

@app.route("/auth", methods=["POST", "GET"])
def authorizer():
    user = request.args['username']
    passwd = request.args['password']
    if(user == "hui" and passwd == "min"): #if credentials are right
        session["hui"] = "min"
        return render_template('welcome.html',
                               text = "Welcome!")
    else: #if credentials arent right
        return render_template('error.html',
                               text = "Sorry, try again by going to root route")

@app.route("/logout")
def logout():
    session.pop("hui") #remove data from session
    return redirect(url_for("display_login"))

if __name__ == "__main__":
    app.debug = True
    app.run()
