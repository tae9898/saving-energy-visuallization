from flask import Flask, request
from flask import render_template
import sys


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("hello.html")

@app.route("/today")
def today():
    return render_template("today.html")

@app.route("/record")
def record():
    return render_template("record.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
    