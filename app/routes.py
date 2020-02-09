from flask import render_template, flash, redirect, url_for, session, request
from flask_login import LoginManager, UserMixin, login_required, current_user, login_user
from app import app
from app.forms import LoginForm
from config import Config
from app.models import User
from werkzeug.urls import url_parse
import pyrebase





@app.route('/')
@app.route('/index')
def index():
    # Check if user is authenticated
    try:
        print(session['usr'])
    except:
        return redirect(url_for('login'))
    
    user = {'email': session['name']}
    
    return render_template('index.html', title='Home', user=user)





@app.route('/login', methods=['GET', 'POST'])
def login():
    # Check if user is authenticated
    try:
        print(session['usr'])
        return redirect(url_for('index'))
    except:
        pass

    form = LoginForm()

    if form.validate_on_submit():
        flash('Login requested for user {}, password={}, remember_me={}'.format(
            form.email.data, form.password.data, form.remember_me.data
        ))

        user = User.get(form.email.data, form.password.data)
        print(user)
        if user is None:
            return redirect(url_for('login'))

        else:
            # Set the user's session
            session['usr'] = user['idToken']
            session['name'] = user['displayName']
            session['email'] = user['email']
            return redirect(url_for('index'))

    return render_template('login.html', title='Sign in', form=form)


@app.route('/logout')
def logout():
    # Delete the session
    try:
        del session['usr']
    except:
        pass

    return redirect(url_for('index'))