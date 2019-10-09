#spot.py

from app import mongo

class Spot:
    '''Spot model for init and abstraction purposes'''
    def __init__(self, load):
        self.thumbnail = load['thumbnail']
        self.company = load['company']
        self.price = load['price']
        self.techs = load['techs']
        self.user = load['user_id']

    def __repr__(self):
        return f'Spot object from company: {self.company}'
