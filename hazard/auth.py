from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
# I am aware that my class structures are not written cleanly. I didn't want to write helper. Please forgive me :(
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST', 'GET'])
def login_page():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if len(username) < 4:
            flash('username to short')
        elif len(password) < 8:
            flash('Password is not correct', category='error')
        else:
            user = User.query.filter_by(username=username).first()
            if user:
                if check_password_hash(user.password, password):
                    flash('Login is Successfully!', category='success')
                    login_user(user, remember=True)
                    return redirect(url_for('views.home'))
                else:
                    flash('Incorrect Password', category='error')
            else:
                flash('Email or password dont exist', category='error')
    return render_template('login.html', user=current_user)


@auth.route('/logout')
@login_required
def logout_page():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/register', methods=['POST', 'GET'])

def register_page():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        tel = request.form.get('tel')
        firstname = request.form.get('firstname')
        email = request.form.get('email')
        user = User.query.filter_by(username=username).first()

        if len(username) < 4:
            flash('username to short', category='error')

        elif len(password) < 8:
            flash('Password is not correct', category='error')
        elif user:
            flash('Email already exists', category='error')
        elif password != password2:
            flash('Password one and password two is not equal', category='error')
        elif len(firstname) < 4: 
            flash('firstname is to short', category='error')
        #The thing to do here is to use regex.
        #import re please
        else:
            new_user = User(username=username, email=email , firstname=firstname, password=generate_password_hash(password, method='sha256'), tel=tel)
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)



            flash('Account Created!', category='success')
            return redirect(url_for('views.index'))

    return render_template('register.html', user=current_user)

