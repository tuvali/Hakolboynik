from interact_with_DB import interact_db
import re


class dbOrders:

    def get_orders(self):
        query1 = 'select * from orders;'
        orders = interact_db(query=query1, query_type='fetch')
        return orders

    def insert_order(self, payer_email, order_Cost):
        query = "INSERT INTO orders (payer_email, order_Cost) VALUES ('%s' ,'%s');" % (
            payer_email, order_Cost)
        interact_db(query=query, query_type='commit')
        query1 = "SELECT id FROM orders WHERE payer_email='%s'" % payer_email
        order_number = max(interact_db(query=query1, query_type='fetch'))
        order_number_str = str(order_number)
        return re.findall(r"\d+", order_number_str)


dbOrders = dbOrders()
