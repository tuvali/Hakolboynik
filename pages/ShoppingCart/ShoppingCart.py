from flask import Blueprint, render_template, session, request, redirect
from utilities.db.db_shoppingcart import dbShoppingcart
from utilities.db.db_products import dbProduct
from utilities.db.db_kit import dbKit
# ShoppingCart blueprint definition
ShoppingCart = Blueprint('ShoppingCart', __name__, static_folder='static', static_url_path='/ShoppingCart', template_folder='templates')


# Routes
@ShoppingCart.route('/ShoppingCart')
def ShoppingCart_func():
    user_email = session.get("user")
    chosen_products = dbShoppingcart.get_products_in_cart(user_email)
    dbShoppingcart.check_quantity()
    defult_total_amount = dbShoppingcart.defult_total_amount(user_email)
    return render_template('ShoppingCart.html', defult_total_amount=defult_total_amount, chosen_products=chosen_products)


@ShoppingCart.route('/add', methods=['POST'])
def add():
    quantity = request.form['quantity']
    productID = request.form['product_ID']
    price = request.form['price']
    user_email = session.get("user")
    add = "add"
    total_amount = dbShoppingcart.update_quantity(productID, quantity, add, user_email)
    chosen_products = dbShoppingcart.get_products_in_cart(user_email)
    return render_template('ShoppingCart.html', chosen_products=chosen_products, total_amount=total_amount)


@ShoppingCart.route('/reduce', methods=['POST'])
def reduce():
    quantity = request.form['quantity']
    productID = request.form['product_ID']
    price = request.form['price']
    user_email = session.get("user")
    reduce = "reduce"
    total_amount = dbShoppingcart.update_quantity(productID, quantity, reduce,user_email)
    chosen_products = dbShoppingcart.get_products_in_cart(user_email)
    return render_template('ShoppingCart.html', chosen_products=chosen_products, total_amount=total_amount)


@ShoppingCart.route('/addCart', methods=['POST'])
def add_to_cart():
    productID = request.form['id']
    price = request.form['price']
    name = request.form['name']
    image = request.form['product_image']
    quantity = request.form['quantity']
    user_email = session.get("user")
    if dbShoppingcart.check_exist_item(productID, price, name, image, user_email, quantity):
        products = dbProduct.get_products()
        return render_template('ItemList.html', products=products, message1="המוצר התווסף לסל בהצלחה!")

    else:
        products = dbProduct.get_products()
        return render_template('ItemList.html', products=products, message2="המוצר כבר נמצא בסל שלך, גש והזמן!")


@ShoppingCart.route('/addCartkit', methods=['POST'])
def add_to_cart_kit():
    productID = request.form['id']
    price = request.form['price']
    name = request.form['name']
    image = request.form['kit_image']
    quantity = request.form['quantity']
    user_email = session.get("user")
    if dbShoppingcart.check_exist_item(productID, price, name, image, user_email, quantity):
        kit = dbKit.get_products_kit()
        return render_template('kit.html', kit=kit, message1="המוצר התווסף לסל בהצלחה!")
    else:
        kit = dbKit.get_products_kit()
        return render_template('kit.html', kit=kit, message2="המוצר כבר נמצא בסל שלך, גש והזמן!")


@ShoppingCart.route('/remove_product', methods=['POST'])
def remove_product():
    productID = request.form['product_ID']
    user_email = session.get("user")
    if dbShoppingcart.remove_item(productID, user_email):
        return redirect('/ShoppingCart')

    return redirect('/ShoppingCart')
