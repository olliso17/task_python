from typing import List

from api.domain.base.base import BaseEntity
from api.domain.task.task_entity import Task




class TodoList(BaseEntity):
    def __init__(self, name: str, typeTask: str, userId: str, tasks: List[Task]):
        super().__init__()
        self.__name = name
        self.__typeTask = typeTask
        self.__userId = userId
        self.__tasks = tasks

    @property
    def name(self):

        return self._get_String(self.__name, "Name")

    @property
    def typeTask(self):

        return self._get_String(self.__typeTask, "Type of Task")

    @property
    def userId(self):

        return self._get_String(self.__userId, "User id")

    @property
    def tasks(self):
        return self.__tasks
     
    @tasks.setter
    
    def tasks(self, task:Task):
        
        listTask = set(self.__tasks)
        
        if task in listTask:
            raise ValueError('Task already exists')
       
        self.__tasks.append(task)

    @tasks.setter
 
    def tasks(self, task:Task):
        
        listTask = set(self.__tasks)
        
        if len(self.__tasks) == 0:
            raise ValueError('Tasks not found')
    
        if task not in listTask:
            raise ValueError('Task not found')
        
        self.__tasks.remove(task)