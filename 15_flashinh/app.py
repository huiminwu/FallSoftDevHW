#Hui Min Wu and Jack Lu, Team Teenage Mutant Jinja Turtles
#SoftDev1 pd7
#K15 -- Oh yes, perhaps I do...
#2018-10-02

from flask import Flask, render_template, request, url_for, redirect, session, flash
import os

app = Flask(__name__)
app.secret_key = os.urandom(32) #generate a private key and assing to built in secret key
usr = "hui"
pwd = "min"
@app.route("/")
def display():
    if usr in session:
        return render_template('welcome.html',
                               text = "Welcome!")
    return render_template('login.html')

@app.route("/auth", methods=["POST"])
def authorizer():
    user = request.form['username']
    passwd = request.form['password']
    if(user == usr and passwd == pwd): #if credentials are right
        session[usr] = pwd
        flash("Correct credentials")
        return render_template('welcome.html',
                               text = "Welcome!")
    flash("Wrong credentials!")
    return render_template('login.html')

@app.route("/logout", methods=["POST"])
def logout():
    session.pop("hui") #remove data from session
    return redirect(url_for("display"))

if __name__ == "__main__":
    app.debug = True
    app.run()
