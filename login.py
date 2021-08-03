
def login(username, password, database):
    query = """
        SELECT * FROM "User" WHERE user_id = (SELECT user_id 
        FROM "Login" WHERE username = \'""" \
        + str(username) + """\' AND password = \'""" \
        + str(password) + """\');"""
    result = database.query(query)
    if not result:  # if it is not empty
        return None
    else:
        user = result[0]
        return user




