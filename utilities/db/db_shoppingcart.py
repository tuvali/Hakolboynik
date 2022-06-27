from interact_with_DB import interact_db


class dbShoppingcart:

    def get_products_in_cart(self, user_email):
        query = "select * from shoppingcart WHERE user_email='%s';" % user_email
        chosen_products = interact_db(query=query, query_type='fetch')
        return chosen_products

    def update_quantity(self, productID, quantity, action, user_email):
        if action == "add":
            query = "UPDATE shoppingcart set quantity='%s'+1 WHERE product_ID='%s' AND user_email='%s' ;" % (
                quantity, productID, user_email)
            query1 = "UPDATE shoppingcart set total_price=quantity*price WHERE product_ID='%s' AND user_email='%s' ;" % (
                productID, user_email)
        if action == "reduce":
            query = "UPDATE shoppingcart set quantity='%s'-1 WHERE product_ID='%s' AND user_email='%s' ;" % (
                quantity, productID, user_email)
            query1 = "UPDATE shoppingcart set total_price=quantity*price WHERE product_ID='%s' AND user_email='%s' ;" % (
                productID, user_email)
        interact_db(query=query, query_type='commit')
        interact_db(query=query1, query_type='commit')
        items = dbShoppingcart.get_products_in_cart(user_email)
        total_amount = 0
        for item in items:
            total_amount = total_amount + item.total_price
        return total_amount

    def defult_total_amount(self, user_email):
        items = dbShoppingcart.get_products_in_cart(user_email)
        defult_total_amount = 0
        for item in items:
            defult_total_amount = defult_total_amount + item.total_price
        return defult_total_amount

    def check_exist_item(self, productID, price, name, image, user_email, quantity):
        check_exist = "SELECT product_ID FROM shoppingcart WHERE product_ID='%s' AND user_email='%s' ;" % (
            productID, user_email)
        existing = interact_db(query=check_exist, query_type='fetch')
        print(len(existing))
        if len(existing) == 0:
            query = "INSERT INTO shoppingcart (product_ID, price, product_Name, image, user_email, inventory_quantity) VALUES ('%s' ,'%s' ,'%s','%s','%s','%s');" % (
                productID, price, name, image, user_email, quantity)
            interact_db(query=query, query_type='commit')
            return True
        else:
            return False


    def remove_item(self, productID, user_email):
        query = "DELETE FROM shoppingcart WHERE product_ID='%s' AND user_email='%s' ;" % (productID, user_email)
        interact_db(query=query, query_type='commit')
        return True

    def delete_items(self, user_email):
        query = "DELETE FROM shoppingcart WHERE user_email='%s' ;" % user_email
        interact_db(query=query, query_type='commit')
        return True

    def check_quantity(self):
        query = "UPDATE shoppingcart set quantity='0' WHERE inventory_quantity<quantity ;"
        interact_db(query=query, query_type='commit')
        query1 = "UPDATE shoppingcart set total_price=quantity*price ;"
        interact_db(query=query1, query_type='commit')
        return True


dbShoppingcart = dbShoppingcart()
