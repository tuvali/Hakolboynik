from interact_with_DB import interact_db


class dbKit:

    def get_products_kit(self):
        query1 = 'select * from kit;'
        kit = interact_db(query=query1, query_type='fetch')
        return kit

    def change_inventory_kit(self, id, quantity):
        query1 = "UPDATE kit set quantity='%s' WHERE id='%s';" %(quantity, id)
        interact_db(query=query1, query_type='commit')
        query1 = "UPDATE shoppingcart set inventory_quantity='%s' WHERE product_ID='%s';" % (quantity, id)
        interact_db(query=query1, query_type='commit')
        return True

dbKit = dbKit()
