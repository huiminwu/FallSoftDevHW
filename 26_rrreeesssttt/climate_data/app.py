'''
Hui Min Wu
SoftDev1 pd08
K25 -- Getting More REST
2018-11-14
'''

from flask import Flask, render_template
import json, urllib

app = Flask(__name__)

@app.route("/")
def home():
    url ="http://climatedataapi.worldbank.org/climateweb/rest/v1/country/mavg/tas/2020/2039/BRA"
    request = urllib.request.urlopen(url)
    response = request.read()
    d = json.loads(response)[0]
    print("---------------")
    print("RESPONSE")
    print(d)
    return render_template("web.html",
                           scenario = d['scenario'],
                           model = d['gcm'],
                           monthVals = d['monthVals'],
                           start = d['fromYear'],
                           end = d['toYear']
                           )

if __name__ == "__main__":
    app.debug = True
    app.run()
