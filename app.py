from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def index():
    return render_template('home.html')

@app.route('/sayshello', methods = ["POST"])
def sayhello():
	name=request.form.get("name")
	name=name.capitalize()
	return render_template("sayhello.html", name=name)

@app.route('/post', methods=["POST", "GET"])
def post():
    return render_template('fakepost.html')

@app.route('/about', methods=["POST", "GET"])
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)