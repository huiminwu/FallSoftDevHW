from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def template():
	print(app)
	print(request)
	return render_template('simple.html')

@app.route("/auth")
def author():
	print(app)
	print(request)
	print(request.args)
	print(request.args['username'])
	print(request.headers)
	return "!!!"

if __name__ == "__main__":
	app.debug = True
	app.run()
