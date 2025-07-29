from flask import Blueprint, request, jsonify
from controllers.task import TaskController

task_routes = Blueprint('task_routes', __name__)

@task_routes.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    task, message, status_code = TaskController.create_task(data)
    if not task:
        return jsonify(message), status_code
    return jsonify({"message": message, "task": task.to_dict()}), status_code

@task_routes.route('/tasks', methods=['GET'])
def get_tasks():
    tasks, message, status_code = TaskController.get_all_tasks()
    return jsonify({
        "tasks": [task.to_dict() for task in tasks],
        "total": message["total_tasks"]
    }), status_code

@task_routes.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task, message, status_code = TaskController.get_task(task_id)
    if message:
        return jsonify(message), status_code
    return jsonify(task.to_dict()), status_code

@task_routes.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()
    task, message, status_code = TaskController.update_task(task_id, data)
    if not task:
        return jsonify(message), status_code
    return jsonify({"message": message, "task": task.to_dict()}), status_code

@task_routes.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task, message, status_code = TaskController.delete_task(task_id)
    if not task:
        return jsonify(message), status_code
    return jsonify(message), status_code