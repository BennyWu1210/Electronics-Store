import sys
import datetime
import math
import credential as crt
from database import *

# Open connection yayyyyy
db = Database(crt.host, crt.db_name, crt.user, crt.password)
result = db.query(""" SELECT * FROM "User" """)
print(result)


