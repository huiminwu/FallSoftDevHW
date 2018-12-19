#Hui Min Wu
#SoftDev1 pd7
#K13 -- Echo Echo Echo
#2018-09-27

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def template():
    return render_template('simple.html')

@app.route("/auth")
def author():
    req = request.method
    user = request.args['username']
    return render_template('result.html',
                        greetings = 'Hello, ',
                        username = user,
                        reqused = req)

if __name__ == "__main__":
    app.debug = True
    app.run()
