class Task:
    def __init__(self, id, title, description, completed=False):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed
        }

    def getTitle(self):
        return self.title

    def getDescription(self):
        return self.description

    def getCompleted(self):
        return self.completed
    
    def setTitle(self, title):
        self.title = title

    def setDescription(self, description):
        self.description = description

    def setCompleted(self, completed):
        self.completed = completed
