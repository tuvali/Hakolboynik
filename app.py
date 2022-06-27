from flask import Flask
app=Flask(__name__)

###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')

###### Pages
## Homepage
from pages.homepage.homepage import homepage
app.register_blueprint(homepage)

## orders
from pages.orders.orders import orders
app.register_blueprint(orders)

## Catalog
from pages.catalog.catalog import catalog
app.register_blueprint(catalog)

## Page error handlers
# from pages.page_error_handlers.page_error_handlers import page_error_handlers
# app.register_blueprint(page_error_handlers)


###### Components
## Main menu
from components.main_menu.main_menu import main_menu
app.register_blueprint(main_menu)

from components.footer.footer import footer
app.register_blueprint(footer)

from pages.contact.contact import contact
app.register_blueprint(contact)

from pages.policy.policy import policy
app.register_blueprint(policy)

from pages.signup.signup import signup
app.register_blueprint(signup)

from pages.ShoppingCart.ShoppingCart import ShoppingCart
app.register_blueprint(ShoppingCart)

from pages.order_recieved.order_recieved import order_recieved
app.register_blueprint(order_recieved)

from pages.login.login import login
app.register_blueprint(login)

from pages.kit.kit import kit
app.register_blueprint(kit)

from pages.ItemList.ItemList import ItemList
app.register_blueprint(ItemList)

from pages.card.card import card
app.register_blueprint(card)


if __name__ == '__main__':
    app.run(debug=True)
