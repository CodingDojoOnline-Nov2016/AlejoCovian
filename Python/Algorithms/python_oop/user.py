class User(object):
    #__init__ method is called every time a new object is created.
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.logged = False
user1 = User("Anna Propas", "anna@anna.com")
print (user1.name)
print (user1.logged)
print (user1.email)
# print (new_user.name, new_user.email)
