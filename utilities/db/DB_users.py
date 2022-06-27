from interact_with_DB import interact_db


class dbUsers:
    def insert_user(self, Full_name, email, address, phone, password):
        email_validation = "SELECT email FROM users WHERE email='%s';" % email
        user = interact_db(query=email_validation, query_type='fetch')
        if len(user) == 0:
            insert = "INSERT INTO users (Full_name, email, address, phone, password) VALUES ('%s','%s','%s','%s','%s');" % (
            Full_name, email, address, phone, password)
            interact_db(query=insert, query_type='commit')
            return True
        else:
            False

    def check_user_exist(self, email, password):
        email_validation = "SELECT email FROM users WHERE email='%s';" % email
        check = interact_db(query=email_validation, query_type='fetch')
        if len(check) == 0:
            return False
        else:
            password_validation = "SELECT password FROM users WHERE email='%s';" % email
            check = interact_db(query=password_validation, query_type='fetchone')
            if check[0] == password:
                return True
            else:
                return False

    def check_user_type(self, email):
        check_type = "SELECT type FROM users WHERE email='%s';" % email
        check = interact_db(query=check_type, query_type='fetchone')
        print(check)
        return check


dbUsers = dbUsers()
