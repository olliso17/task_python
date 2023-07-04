

class InputCreateTodoListDto:
    def __init__(self, name: str, typeTask: str, userId: str):
        self.name = name
        self.typeTask = typeTask
        self.userId = userId


class OutputCreateTodoListDto:
    def __init__(self, id: str, createdAt: str, isActive: bool, name: str, typeTask: str, userId: str):
        self.id = id
        self.createdAt = createdAt
        self.isActive = isActive
        self.name = name
        self.typeTask = typeTask
        self.userId = userId
