class User(object):

    allusers = []

    def __init__(self, email=None, password=None, confirm_password=None):
        if email and password:
            self.email = email
            self.password = password
            self.confirm_password = confirm_password
        else:
            self.email = None
            self.password = None
            self.confirm_password = None

    '''Create user'''
    def register_user(self, email, password, confirm_password):
        user = User(email, password, confirm_password)
        self.allusers.append(user)

    def validate_email(self, email):
        for users in self.allusers:
            if users.email == email:
                return "email in use"
            return 'Invalid credentials'

    '''Retrieve user credentials'''
    def login(self, email, password):  # no arguments defined so that they can be picked from the 'input'
        for users in self.allusers:
            if users.email == email and users.password == password:
                return "Log in successful"  # you can also redirect to another url

    '''Edit user credentials'''
    def edit_details(self, email=None, password=None):
        if email:
            new_email = input("enter your new name: ")
            for users in self.allusers:
                if users.email == email:
                    users.email = new_email

        if email and password:
            new_password = input("enter your new password: ")
            new_email = input("enter your new name: ")
        for users in self.allusers:
            if users.email == email and users.password == password:
                users.email = new_email
                users.password = new_password

    def print_details(self):
        for users in self.allusers:
            print(users.email)
            print(users.password)

    '''Delete user credentials'''
    def delete(self):
        email = input("enter email: ")
        for users in self.allusers:
            if users.email == email:
                self.allusers.remove(users)

    def users(self):
        for users in self.allusers:
            print(users)
