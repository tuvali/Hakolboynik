from flask import Blueprint, render_template ,session, request, redirect
from utilities.db.db_contact import dbContact
# orders blueprint definition
contact = Blueprint('contact', __name__, static_folder='static', static_url_path='/contact', template_folder='templates')


# Routes
@contact.route('/contact')
def contact_func():  # put application's code here
    contact = dbContact.contact_func()
    return render_template('contact.html', contact=contact)


@contact.route('/insert_contact', methods=['POST'])
def insert_contact():
    first_Name = request.form['first_Name']
    last_Name = request.form['last_Name']
    email = request.form['email']
    message = request.form['message']
    complaint_Category = request.form['complaint_Category']
    if dbContact.insert_contact(first_Name, last_Name,email,message, complaint_Category ):
         return  render_template('contact.html', message='תלונתך התקבלה בהצלחה!')
    return redirect('/contact')