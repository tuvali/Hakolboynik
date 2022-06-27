from flask import Flask, render_template, url_for, session, request, redirect, Blueprint
from utilities.db.db_orders import dbOrders
from utilities.db.db_shoppingcart import dbShoppingcart

# order_recieved blueprint definition
order_recieved = Blueprint('order_recieved', __name__, static_folder='static', static_url_path='/order_recieved',
                           template_folder='templates')


# Routes
@order_recieved.route('/order_received')
def index():
    payer_email = session.get("user")
    order_Cost = dbShoppingcart.defult_total_amount(payer_email)
    order_id = dbOrders.insert_order(payer_email, order_Cost)
    if dbShoppingcart.delete_items(payer_email):
        return render_template('order_recieved.html', order_id=order_id)
