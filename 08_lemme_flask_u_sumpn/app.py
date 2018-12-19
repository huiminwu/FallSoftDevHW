# Hui Min Wu
# SoftDev pd8
# K8 -- Fill Yer Flask
# 2018-09-18

from flask import Flask
app = Flask(__name__)

@app.route("/") #assigning fxn to 1st route
def englishHello():
    return "Hello World"

@app.route("/spanish") #assigning fxn to 2nd route
def spanishHello():
    return "Hola Mundo"

@app.route("/norwegian") #assigning fxn to 3rd route
def norwegianHello():
    return "Hei Verden"

if __name__ == "__main__":
    app.debug = True 
    app.run()

