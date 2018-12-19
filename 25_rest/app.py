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
    url ="https://api.fda.gov/food/enforcement.json?search=city:%22Westborough%22&limit=1"
    request = urllib.request.urlopen(url)
    response = request.read()
    d = json.loads(response)
    print("---------------")
    print("RESPONSE")
    print(d)
    return render_template("web.html",
                           product = d['results'][0]['product_description'],
                           quantity = d['results'][0]['product_quantity'],
                           reason = d['results'][0]['reason_for_recall'],
                           distr = d['results'][0]['distribution_pattern']
                           )

if __name__ == "__main__":
    app.debug = True
    app.run()
