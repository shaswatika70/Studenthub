# lets build simple flask app

from flask import Flask, render_template, request
import psycopg2, os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', message="StudentHub is LIVE on AWS!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)