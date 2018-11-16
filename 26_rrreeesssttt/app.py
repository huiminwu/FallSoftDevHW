'''
Hui Min Wu
SoftDev1 pd08
K26 -- Getting More REST
2018-11-15
'''
from flask import Flask, render_template
from yelpapi import YelpAPI


import json, urllib

app = Flask(__name__)

@app.route("/")
def home():
    # CLIMATE DATA API
    url1 ="http://climatedataapi.worldbank.org/climateweb/rest/v1/country/mavg/tas/2020/2039/BRA"
    request1 = urllib.request.urlopen(url1)
    response1 = request1.read()
    d1 = json.loads(response1)[0]
    print("---------------")
    print("CLIMATE RESPONSE")
    print(d1)

    # BORED API
    url2 = "http://www.boredapi.com/api/activity/"
    request2 = urllib.request.urlopen(url2)
    response2 = request2.read()
    d2 = json.loads(response2)
    print("---------------")
    print("BORED RESPONSE")
    print(d2)

    # YELP API
    yelp_api=YelpAPI("VUAGZaRKOeQggrzZ66K2o3hOYtqzi9UuL47M-hQkS3Hi5nMvyLRi3YTgGRbZXwrCHGMoybysDwBuInTsdkILZmtANvtd-6AGVx5cpQhqsnq-7Ls0dBW_eDChmgHuW3Yx")
    response3 = yelp_api.phone_search_query(phone = '+13474258511')
    print("---------------")
    print("YELP RESPONSE")
    print(response3)

    return render_template("web.html",
                           scenario = d1['scenario'],
                           model = d1['gcm'],
                           monthVals = d1['monthVals'],
                           start = d1['fromYear'],
                           end = d1['toYear'],
                           activity = d2['activity'],
                           accessibility = d2['accessibility'],
                           type = d2['type'],
                           participants = d2['participants'],
                           price = d2['price'],
                           name = response3['businesses'][0]['name'],
                           rating = response3['businesses'][0]['rating'],
                           price_rate = response3['businesses'][0]['price'],
                           phone = response3['businesses'][0]['phone'],
                           img = response3['businesses'][0]['image_url']
                           )

if __name__ == "__main__":
    app.debug = True
    app.run()
