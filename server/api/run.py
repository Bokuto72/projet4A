from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import pandas as pd
import numpy as np
import random


app = Flask(__name__)
api = Api(app)

users = [{
     "user_id": "1",
     "username": "Zidane"
}]

@app.route("/", methods=['GET'])
def index():
    data = {'message': 'Hello from Flask API!'}
    return jsonify(data)

@app.route("/get-user/<user_id>", methods=["GET"])
def get_user(user_id):
    user = [users for user in users if user['user_id'] == user_id]
    user_data = {
        "user": user[0],     
    }

    extra = request.args.get("extra")
    if extra:
         user_data["extra"] = extra

    return jsonify(user_data), 200

@app.route("/create-user", methods=["POST"])
def create_user():
    data = {"user_id": request.json('user_id'),
            "username": request.json('username')
            }

    users.append(data)
    return jsonify(data), 201

@app.route("/predict-move", methods=["POST"])
def predictMove(input):
    data = input.dict()
    existingData = data
    
    # Modele à créer dans ./model/ 
    # prediction = model.predict(existingData)
    prediction = [] # temp

    return {
        'predictedMove': prediction[0]
    }

if __name__ == '__main__':
     #app.run(host='0.0.0.0', port=5000)
     app.run(debug=True)
 