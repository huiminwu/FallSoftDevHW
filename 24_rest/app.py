'''
Hui Min Wu
SoftDev1 pd08
K24 -- A RESTful Journey Skyward
2018-11-13
'''

from flask import Flask, render_template
import json, urllib

app = Flask(__name__)

@app.route("/")
def home():
    url ="https://api.nasa.gov/planetary/earth/imagery/?lon=100.75&lat=1.5&date=2014-02-01&cloud_score=True&api_key=DnPxujKZGxW79axTpqLW9OKZfEdYIfhtwfPTZ2Ck"
    request = urllib.request.urlopen(url)
    response = request.read()
    d = json.loads(response)
    return render_template("web.html", img = d['url'])

if __name__ == "__main__":
    app.debug = True
    app.run()
