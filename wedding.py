from flask import Flask
from flask import render_template

app = Flask(__name__, static_folder='media')

app.debug = True

@app.route("/")
def splash():
    return render_template("splash.html") 

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

@app.route("/work-in-progress")
def wip():
    return render_template("construction.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0")

