from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/play")
def play():
    return "<h1>Play Page Coming Soon!</h1>"

@app.route("/credits")
def credits():
    return "<h1>Credits Page Coming Soon!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
