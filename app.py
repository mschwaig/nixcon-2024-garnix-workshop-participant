from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/add/{a}/{b}')
def add():
    return str(int(a)+int(b))

@app.route('/add/{a}/{b}')
def mult():
    return str(int(a)*int(b))

@app.route('/uuid')
def mult():
    return "02056b52-22c7-4688-946d-32ffa06eb808"

if __name__ == '__main__':
    app.run(port = os.environ.get('PORT'))
