
from flask import render_template, flash, redirect, url_for,request,Flask
# from app import app
from app.forms import LoginForm
from app.api import getMessage

app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Daksh Patel'}
    return render_template('index.html', title='Home', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)    

@app.route('/projects')
def projects():
    user = {'username': 'Daksh Patel'}
    return render_template('projects.html', title='Projects', user=user)  


@app.route('/chat')
def chat():
    return render_template('chat.html')          

@app.route('/experiences')
def experiences():
    user = {'username': 'Daksh Patel'}
    return render_template('experiences.html', title='Experience', user=user)      


@app.route('/base')
def base():
    user = {'username': 'Daksh Patel'}
    return render_template('base.html', title='base', user=user)     


@app.route("/get")
def get():    
    return getMessage(request.args.get('msg'))     
