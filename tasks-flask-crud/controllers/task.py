from models.task import Task

tasks = []
id_task_control = 1

class TaskController:
    @staticmethod
    def create_task(data):
        global id_task_control
        if not data or 'title' not in data or 'description' not in data:
            return None, {"error": "Title and description are required"}, 400
        
        new_task = Task(
            id=id_task_control, 
            title=data["title"], 
            description=data["description"]
        )
        tasks.append(new_task)
        id_task_control += 1
        return new_task, {"message": "Task created successfully"}, 201

    @staticmethod
    def get_all_tasks():
        return tasks, {"total_tasks": len(tasks)}, 200

    @staticmethod
    def get_task(task_id):
        task = next((t for t in tasks if t.id == task_id), None)
        if not task:
            return None, {"error": "Task not found"}, 404
        return task, None, 200

    @staticmethod
    def update_task(task_id, data):
        task = next((t for t in tasks if t.id == task_id), None)
        if not task:
            return None, {"error": "Task not found"}, 404
        
        if 'title' in data:
            task.title = data['title']
        if 'description' in data:
            task.description = data['description']
        if 'completed' in data:
            task.completed = data['completed']
        
        return task, {"message": "Task updated successfully"}, 200

    @staticmethod
    def delete_task(task_id):
        global tasks
        task = next((t for t in tasks if t.id == task_id), None)
        if not task:
            return None, {"error": "Task not found"}, 404
        
        tasks = [t for t in tasks if t.id != task_id]
        return task, {"message": "Task deleted successfully"}, 200