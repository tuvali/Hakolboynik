from flask import Blueprint, render_template

from utilities.db.db_products import dbProduct
# ItemList blueprint definition
ItemList = Blueprint('ItemList', __name__, static_folder='static', static_url_path='/ItemList', template_folder='templates')


@ItemList.route('/item list')
def item_func():  # put application's code here
    products = dbProduct.get_products()
    return render_template('ItemList.html', products=products)
