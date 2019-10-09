#user.py

from app import mongo

class User:
    '''User model for init and abstraction purposes'''
    def __init__(self, load):
        self.db = mongo.db.users
        self.email = load['email']

    def __repr__(self):
        return f'User object, email: {self.email}'
