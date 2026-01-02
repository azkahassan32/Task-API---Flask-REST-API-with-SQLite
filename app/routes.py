"""
Blueprint → Modular way to organize routes.

request → Access request data (POST/PUT JSON).

jsonify → Convert Python dict/list → JSON response.
"""
# REST Endpoints

from flask import Blueprint, request, jsonify
from app.models import (
    get_all_tasks, get_task,
    create_task, update_task, delete_task
)

api = Blueprint("api", __name__)

@api.route("/tasks", methods=["GET"])       # @api.route → Flask decorator to define URL.
def read_tasks():
    tasks = get_all_tasks()
    return jsonify([dict(task) for task in tasks])

@api.route("/tasks/<int:task_id>", methods=["GET"])
def read_task(task_id):
    task = get_task(task_id)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(dict(task))

@api.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()       #request.get_json() → Reads JSON body sent by client.
    create_task(data["title"])
    return jsonify({"message": "Task created"}), 201

@api.route("/tasks/<int:task_id>", methods=["PUT"])
def edit_task(task_id):
    data = request.get_json()
    update_task(task_id, data["completed"])
    return jsonify({"message": "Task updated"})

@api.route("/tasks/<int:task_id>", methods=["DELETE"])
def remove_task(task_id):
    delete_task(task_id)
    return jsonify({"message": "Task deleted"})
