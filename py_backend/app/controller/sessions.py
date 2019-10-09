#sessions.py
from flask import jsonify
from app.models.user import User

def store(load):
    '''Stores user email and returns its _id'''
    user = User(load)
    if not user.db.find_one(load):
        id = user.db.insert_one(load).inserted_id
        return {
            "_id": f'{id}',
            "email": f'{user.email}'
        }
    else:
        return [ load, {"error": "already exists"} ]
