from flask import Blueprint, render_template,request

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('base.html')

@main.route('/talk')
def talk():
    username = request.cookies.get('username')
    return render_template('talk.html', username=username)
