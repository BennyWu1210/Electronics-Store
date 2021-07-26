import sys
import datetime
import math
import credential as crt
from database import *

# TODO
#  1. Change column's character limit
#  2. Login to database (login.py)
#  3. Product class (product.py) --> update product, select product...
#  4. User (user.py) --> let admin view information
#  5. Transaction history (transaction.py, or something like that)
#  Make the files for the classes first


# Open connection yayyyyy
db = Database(crt.host, crt.db_name, crt.user, crt.password)
result = db.query(""" SELECT * FROM "User" """)
print(result)


