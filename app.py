from flask import Flask
import os
import uuid

app = Flask(__name__)

def cowsay(message: str) -> str:
    """Run cowsay with the given message."""
    try:
        result = subprocess.run(
            ["cowsay", message],
            capture_output=True,
            text=True,
            shell=False
        )
        return result.stdout
    except subprocess.SubprocessError as e:
        return f"Error running cowsay: {e}"


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
    return str(cowsay(message))

if __name__ == '__main__':
    app.run(port = os.environ.get('PORT'))
