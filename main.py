import sys
import math
import _sha256 as hash

from datetime import datetime
from product import Product
from product import select_product
from user import User
from user import Admin
from transaction import Purchase
from transaction import Invoice

import credential as crt
from database import *

# TODO
#  1. Change column's character limit
#  2. User (user.py) --> let admin view information
#  3. Transaction history (transaction.py, or something like that)
#  4. Store (store.py) --> add user, keep track of everything
#  5. Admin: have access to products, users, transaction.
#  Make the files for the classes first


# Open connection

db = Database(crt.host, crt.db_name, crt.user, crt.password)
result = db.query(""" SELECT * FROM "User" """)


def create_user(user_info, username):
    user_id = user_info[0]
    first_name = user_info[1].rstrip() if type(user_info[1]) is str else None
    last_name = user_info[2].rstrip() if type(user_info[2]) is str else None
    email = user_info[3].rstrip() if type(user_info[3]) is str else None
    age = user_info[4]
    address = user_info[5].rstrip() if type(user_info[5]) is str else None

    admin_info = get_admin(user_id)

    if len(admin_info) > 0:
        admin = Admin(int(admin_info[0][0]), user_id, username, first_name, last_name, email, age, address)
        return admin

    user = User(user_id, username, first_name, last_name, email, age, address)
    return user


def get_admin(user_id):
    query = """SELECT admin_id FROM "Admin" WHERE user_id = """ + user_id + ";"
    result = db.query(query)
    return result


def login(username, password):
    # password need hashing
    query = """
        SELECT * FROM "User" WHERE user_id = (SELECT user_id 
        FROM "Login" WHERE username = \'""" \
        + str(username) + """\' AND password = \'""" \
        + str(password) + """\');"""

    result = db.query(query)

    if not result:  # if it is not empty
        return None
    else:
        user = result[0]
        return user


new_user = login("user1", "password1")
username = "user1"

# Create user testing
# print(create_user(new_user, username))

# Product update testing
apple = Product(1, 2, 3, 4, 5, 6, 7)
# apple.update(db, "1", 2, 3, "4", 5, "6")

print(select_product(db, 1, "ben", 32.1, 10, "phone", 2022, "apple")[0])


purchase = Purchase(apple, 10)
invoice = Invoice(new_user, datetime.now())
invoice.add_purchase(purchase)

print(invoice.transactions[0].quantity)