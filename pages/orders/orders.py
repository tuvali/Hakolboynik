from flask import Blueprint, render_template

from utilities.db.db_orders import dbOrders

# orders blueprint definition
orders = Blueprint('orders', __name__, static_folder='static', static_url_path='/orders', template_folder='templates')


# Routes
@orders.route('/orders')
def index():
    orders = dbOrders.get_orders()
    return render_template('orders.html', orders=orders)
