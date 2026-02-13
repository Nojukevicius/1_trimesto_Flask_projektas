from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", active = "home", title="Homepage")

@app.route("/gameplay")
def gameplay():
    return render_template("gameplay.html", active = "gameplay", title="Gameplay")

@app.route("/history")
def history():
        return render_template("history.html", active = "history", title="History")

@app.route("/about")
def about():
        return render_template("about.html", active = "about", title="About")

@app.route("/tips")
def tips():
        return render_template("tips.html", active = "tips", title="tips")

@app.route("/easteregg")
def easteregg():
        return render_template("easteregg.html", title="easteregg")

@app.route("/media")
def media():
        return render_template("media.html", active = "media", title="media")

@app.route("/initialD")
def easteregg2():
        return render_template("initialD.html", title="initialD")


if __name__ == "__main__":
    app.run(debug=True)