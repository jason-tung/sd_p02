import os, csv, time, sqlite3, json
from urllib.request import Request, urlopen

from flask import Flask, render_template, request,session,url_for,redirect,flash

import util

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("login.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
