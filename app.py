# app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello from Zappa we are running live on the internet! For Real!</h1>'

if __name__ == '__main__':
    app.run()
