from flask import Flask, render_template, redirect, url_for, request, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import pandas

app = Flask(__name__)



@app.route('/login', methods=['GET', 'POST'])
def login():
    users = {}  # GOOGLE TABLE HERE #
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and check_password_hash(users[username], password):
            session['username'] = username
            flash('вечер в хату', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('сори че то не то', 'danger')

    return render_template('login.html')


@app.route('/enter')
def dashboard():
    users = {}  # GOOGLE TABLE HERE #
    username = request.form['username']
    if username not in users:
        return (redirect('https://docs.google.com/spreadsheets/d/1qJ3veQPbXTwN21M7Ovl9ITWzkk5zaSJAVoB1_5FxfLw/edit?usp=sharing'))
        # редиректим на гугл таблицу для реги
    return render_template('dashboard.html', username=username)