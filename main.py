from flask import Flask, render_template, redirect, url_for, request, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from back import *
import pandas as pd

app = Flask(__name__)
app.secret_key = "SPDKfNSkdkf"

@app.route("/")
def index():
    return redirect("/login")

@app.route('/login', methods=['GET', 'POST'])
def login():
    users = pd.read_html('https://docs.google.com/spreadsheets/d/1qJ3veQPbXTwN21M7Ovl9ITWzkk5zaSJAVoB1_5FxfLw/edit?usp=sharing')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if сравни_эту_хуету(username, password)["значение"] == "норм":
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', message = "хуйня")

    return render_template('login.html')


@app.route('/enter', methods=["GET"])
def dashboard():
    return render_template('dashboard.html')

if __name__ == "__main__":
    app.run()