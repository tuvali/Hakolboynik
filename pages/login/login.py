from flask import Flask, render_template, url_for, session, request, redirect, Blueprint
from utilities.db.DB_users import dbUsers

# login blueprint definition
login = Blueprint('login', __name__, static_folder='static', static_url_path='/login', template_folder='templates')


# Routes
@login.route('/Login')
def page():
    return render_template('login.html')

@login.route('/Login_user', methods=['GET', 'POST'])
def login_func():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if dbUsers.check_user_exist(email, password):
            session['type']= dbUsers.check_user_type(email)
            session['user'] = email
            return render_template('homepage.html', message='ברוך הבא לאתר שלנו!')
        else:
            session['user'] = ''
            return render_template('login.html', message1='אחד או יותר מהפרטים שגויים, נסה שנית!')
    return render_template('login.html')




