from flask import Blueprint, render_template, session, request, redirect
from utilities.db.db_shoppingcart import dbShoppingcart

# card blueprint definition
card = Blueprint('card', __name__, static_folder='static', static_url_path='/card', template_folder='templates')


# Routes
@card.route('/card')
def index():
    user_email = session.get("user")
    total_amount = dbShoppingcart.defult_total_amount(user_email)
    return render_template('card.html',  total_amount = total_amount)
