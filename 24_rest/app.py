from flask import Flask, render_template
import urllib
import json

@app.route("/")
def home():
    u = urllib.request.urlopen("https://api.nasa.gov/planetary/earth/imagery?lon=100.75&lat=1.5&date=2014-02-01&cloud_score=True&api_key=DEMO_KEY")
    response = u.read()


    return render_template("

if __name__ == "__main__":
    app.debug = True
    app.run()
