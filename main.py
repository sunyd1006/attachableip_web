from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/register.html')
def register():
    return render_template('register.html')

@app.route('/controlHomeTemp.html')
def controlHomeTemp():
    return render_template('controlHomeTemp.html')

@app.route('/control')
@app.route('/control.html')
@app.route('/upload.html')
def control():
    return render_template('upload.html')

@app.route('/myproduct.html')
def myproduct():
    return render_template('myproduct.html')

@app.route('/txtStore.html')
def txtStore():
    return render_template('txtStore.html')

@app.route('/txtDetail.html')
def txtDetail():
    return render_template('txtDetail.html')

@app.route('/query.html')
def query():
    return render_template('query.html')

@app.route('/505.html')
def abcd505():
    return render_template('505.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
