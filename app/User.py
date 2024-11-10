import uuid

class User:
    def __init__(self, username, email):
        self.user_id = uuid.uuid1()
        self.username = username
        self.email = email

    def setUsername(self, name):
        self.username = name
    def getUsername(self):
        return self.username
    
    def setEmail(self, email):
        self.email = email
    def getEmail(self):
        return self.email