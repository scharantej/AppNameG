 
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/players')
def players():
    return render_template('players.html')

@app.route('/fixtures')
def fixtures():
    return render_template('fixtures.html')

@app.route('/results')
def results():
    return render_template('results.html')

@app.route('/news')
def news():
    return render_template('news.html')

if __name__ == '__main__':
    app.run()
