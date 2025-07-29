from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

tasks = []

id_task_controll = 1

@app.route("/tasks", methods=["POST"])
def create_task():
    global id_task_controll
    
    data = request.get_json()
    new_task = Task(
        id=id_task_controll, 
        title=data["title"], 
        description=data["description"]
    )
    tasks.append(new_task)
    id_task_controll += 1
    
    return jsonify({
        "message": "Nova tarefa criada com sucesso!",
    }), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]

    output = {
                "tasks": task_list,
                "total_tasks": len(task_list)
            }
    return jsonify(output)

@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = next((t for t in tasks if t.id == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    
    return jsonify({
        "task": {
            "id": task.id,
            "title": task.title,
            "description": task.description
        }
    })

if __name__ == "__main__":
    app.run(debug=True)