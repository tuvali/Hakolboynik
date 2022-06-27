from flask import Blueprint, render_template, request, redirect

from utilities.db.db_products import dbProduct
from utilities.db.db_kit import dbKit
from utilities.db.db_shoppingcart import dbShoppingcart


# catalog blueprint definition
catalog = Blueprint('catalog', __name__, static_folder='static', static_url_path='/catalog',
                    template_folder='templates')


# Routes
@catalog.route('/catalog')
def index():
    products = dbProduct.get_products()
    kit = dbKit.get_products_kit()
    return render_template('catalog.html', products=products, kit=kit)


@catalog.route('/change_inventory', methods=['POST'])
def change():
    id = request.form['id']
    quantity = request.form['quantity']
    if dbProduct.change_inventory(id, quantity):
        dbShoppingcart.check_quantity()
        return redirect('/catalog')


@catalog.route('/change_inventory_kit', methods=['POST'])
def change_kit():
    id = request.form['id']
    quantity = request.form['quantity']
    if dbKit.change_inventory_kit(id, quantity):
        dbShoppingcart.check_quantity()
        return redirect('/catalog')
