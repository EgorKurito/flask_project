from flask import Flask, render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Egor' }
    posts = [
        {
            'author': { 'nickname': 'Dima' },
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': { 'nickname': 'Susan' },
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",
                            title = 'Home',
                            user = user,
                            posts = posts)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Loginrequested for openID="' + form.openid.data + '", remember_me' +str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',
                            title = 'Sign In',
                            form = form)