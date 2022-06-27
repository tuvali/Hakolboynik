from flask import Flask, render_template, url_for, session, request, redirect, Blueprint
from utilities.db.DB_users import dbUsers

# signup blueprint definition
signup = Blueprint('signup', __name__, static_folder='static', static_url_path='/signup', template_folder='templates')


@signup.route('/signup')
def page():
    return render_template('signup.html')


# Routes
@signup.route('/insert_user', methods=['POST'])
def sign_up():
    Full_Name = request.form['Full_Name']
    email = request.form['email']
    address = request.form['address']
    phone = request.form['phone']
    password = request.form['password']
    if dbUsers.insert_user(Full_Name, email, address, phone, password):
        return render_template('Login.html',message='ברוך הבא לאתר שלנו! התחבר ותהנה ממה שיש לנו להציע!')
    else:
        return render_template('signup.html', message1='מצטערים אך נראה שיש לך משתמש, נסה להתחבר או להרשם עם מייל שונה')

    return render_template('signup.html')
