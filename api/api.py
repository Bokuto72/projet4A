from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import pandas as pd
import numpy as np
import random


app = Flask(__name__)
api = Api(app)

@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "username": "Thibault"           
    }

    extra = request.args.get("extra")
    if extra:
         user_data["extra"] = extra

    return jsonify(user_data), 200

@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()

    return jsonify(data), 201

if __name__ == '__main__':
     app.run(host='0.0.0.0')
     #app.run(debug=True)