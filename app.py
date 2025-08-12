from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def intro():
    return render_template('intro.html')

@app.route('/play')
def play():
    return "<h2>Game starting soon! (placeholder)</h2>"

@app.route('/credits')
def credits():
    return "<h2>Credits page (placeholder)</h2>"

if __name__ == '__main__':
    app.run(debug=True)
