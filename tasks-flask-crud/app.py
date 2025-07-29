from flask import Flask
from routes.tasks_routes import task_routes

app = Flask(__name__)
app.register_blueprint(task_routes)

if __name__ == "__main__":
    app.run(debug=True)