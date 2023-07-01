from typing import List
from api.domain.base.base import BaseEntity
from api.domain.task.task_entity import Task


class AddTodoListDto(BaseEntity):
    def __init__(self, name: str, typeTask: str, userId: str) -> None:
        super().__init__()
        self.name = name
        self.typeTask = typeTask
        self.userId = userId