import os
import tempfile
import json
from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Define una lista inicial de miembros de la familia
initial_family_members = [
    {
        "id": 1,
        "first_name": "John",
        "last_name": "Jackson",
        "age": 33,
        "lucky_numbers": [7, 13, 22]
    },
    {
        "id": 2,
        "first_name": "Jane",
        "last_name": "Jackson",
        "age": 35,
        "lucky_numbers": [10, 14, 3]
    },
    {
        "id": 3,
        "first_name": "Jimmy",
        "last_name": "Jackson",
        "age": 5,
        "lucky_numbers": [1]
    }
]

# Define una lista que contendrá a los miembros de la familia
family_members = initial_family_members.copy()

# Implementa las rutas y funciones
@app.route('/members', methods=['GET'])
def get_members():
    return jsonify(family_members)

@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    for member in family_members:
        if member["id"] == member_id:
            return jsonify(member), 200
    return jsonify({"error": "Member not found"}), 404

@app.route('/member', methods=['POST'])
def add_member():
    data = request.json
    if "id" not in data:
        # Genera un nuevo ID aleatorio si no se proporcionó
        data["id"] = random.randint(10000000, 99999999)
    family_members.append(data)
    return jsonify(data), 200

@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    for member in family_members:
        if member["id"] == member_id:
            family_members.remove(member)
            return jsonify({"done": True}), 200
    return jsonify({"error": "Member not found"}), 404

if __name__ == '__main__':
    app.run()
