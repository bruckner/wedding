from flask import Flask
from flask import render_template

app = Flask(__name__, static_folder='media')

app.debug = True

@app.route("/")
def splash():
    return render_template("splash.html") 

@app.route("/welcome")
def welcome():
    default = '/work-in-progress'
    menuitems = [
        {'title': 'OUR STORY', 'target': '/romance'},
        {'title': 'OUR PROPOSAL', 'target': '/proposal'},
        {'title': 'SHEDULE of EVENTS', 'target': '/schedule'},
        {'title': 'ACCOMODATIONS', 'target': '/hotel'},
        {'title': 'TRAVEL', 'target': '/travel'},
        {'title': 'REGISTRY', 'target': 
            '/work-in-progress'},
    ]
    return render_template("welcome.html", menuitems=menuitems)

@app.route("/details/<what>")
def details(what):
    return render_template("%s-details.html" % what)

@app.route("/schedule")
def events():
    return render_template("events.html")

@app.route("/travel")
def travel():
    return render_template("travel.html")

@app.route("/hotel")
def hotel():
    return render_template("hotel.html")

@app.route("/romance")
def romance():
    return render_template("romance.html")

@app.route("/proposal")
def proposal():
    return render_template("proposal.html")

@app.route("/work-in-progress")
def wip():
    return render_template("construction.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0")

