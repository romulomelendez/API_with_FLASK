from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def helloWorld():
    return "<h1>Hello, World!</h1>"


@app.route('/<name>')
def hello(name):
    return f" Hello, {escape(name)}!"


