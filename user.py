
class User:
    def __init__(self, user_id, username, first_name, last_name, email, age=None, address=None):
        self._user_id = user_id
        self._username = username
        self.first_name = first_name
        self.last_name = last_name
        self._email = email
        self._address = address
        self.age = age

    def __str__(self):
        return "User " + str(self.username) + ": id " + str(self.user_id) + ", name " + \
               self.first_name + " " + self.last_name + ", email " + self.email

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, new_id):
        self._user_id = new_id

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, new_username):
        self._username = new_username


user = User(1, "guy", "dude", "guy", "dude@guy.com")
user.user_id = 5
user.username = 1000
print(user.username)



