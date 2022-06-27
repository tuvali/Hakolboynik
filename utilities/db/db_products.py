from interact_with_DB import interact_db


class dbProduct:

    def get_products(self):
        query1 = 'select * from products;'
        products = interact_db(query=query1, query_type='fetch')
        return products

    def change_inventory(self, id, quantity):
        query = "UPDATE products set quantity='%s' WHERE id='%s';" %(quantity, id)
        interact_db(query=query, query_type='commit')
        query1 = "UPDATE shoppingcart set inventory_quantity='%s' WHERE product_ID='%s';" % (quantity, id)
        interact_db(query=query1, query_type='commit')
        return True


dbProduct = dbProduct()
