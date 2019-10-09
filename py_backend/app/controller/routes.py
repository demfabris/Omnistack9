#routes.py

from flask import Flask, jsonify, request, Blueprint, current_app
from app.controller.sessions import store
import os

routes = Blueprint('routes', __name__)

@routes.route('/sessions', methods=['POST'])
def sessions():
    response = store(request.json)
    return jsonify(response)

@routes.route('/spots', methods=['POST'])
def spots():
    result = request.form
    file = request.files["file"]
    file.save(os.path.join(current_app.config["UPLOAD_FOLDER"], file.filename))
    response = {"thumbnail": file.filename}.update(result)
    return jsonify(response)
