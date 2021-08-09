import sys
import datetime
import math
import login
from user import User

import credential as crt
from database import *

# TODO
#  1. Change column's character limit
#  2. Login to database (login.py)
#  3. Product class (product.py) --> update product, select product...
#  4. User (user.py) --> let admin view information
#  5. Transaction history (transaction.py, or something like that)
#  6. Store (store.py) --> add user, keep track of everything
#  Make the files for the classes first


# Open connection

db = Database(crt.host, crt.db_name, crt.user, crt.password)
result = db.query(""" SELECT * FROM "User" """)

new_user = login.login("user1", "password1", db)
username = "user1"


def create_user(user_info, username):
    user_id = user_info[0]
    first_name = user_info[1].rstrip() if type(user_info[1]) is str else None
    last_name = user_info[2].rstrip() if type(user_info[2]) is str else None
    email = user_info[3].rstrip() if type(user_info[3]) is str else None
    age = user_info[4]
    address = user_info[5].rstrip() if type(user_info[5]) is str else None

    user = User(user_id, username, first_name, last_name, email, age, address)
    return user


print(create_user(new_user, username))


