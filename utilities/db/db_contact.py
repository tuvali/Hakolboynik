from interact_with_DB import interact_db


class dbContact:

    def contact_func(self):  # put application's code here
        query = 'select * from contact;'
        contact = interact_db(query=query, query_type='fetch')
        return (contact)

    def insert_contact(self,first_Name,last_Name,email,message, complaint_Category):

        query = "INSERT INTO contact (first_Name, last_Name, email, message, complaint_Category) VALUES ('%s' ,'%s' ,'%s','%s','%s');" % (
            first_Name, last_Name, email, message, complaint_Category)
        interact_db(query=query, query_type='commit')
        return True

dbContact = dbContact()