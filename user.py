
class User:
    def __init__(self, user_id, username, first_name, last_name, email, age=None, address=None):
        self.user_id = user_id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.address = address

    def __str__(self):
        return "User " + str(self.username) + ": id " + str(self.user_id) + ", name " + \
               self.first_name + " " + self.last_name + ", email " + self.email





