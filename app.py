from flask import Flask
import os
import uuid

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/add/<a>/<b>')
def add(a, b):
    return str(int(a)+int(b))

@app.route('/mult/<a>/<b>')
def mult(a, b):
    return str(int(a)*int(b))

@app.route('/uuid')
def uuid():
    return str(uuid.uuid4())

@app.route('/cowsay/<message>')
def uuid(message):
    return str(uuid.uuid4() + message)

if __name__ == '__main__':
    app.run(port = os.environ.get('PORT'))
