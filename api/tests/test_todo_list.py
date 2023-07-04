from typing import List
import pytest
import uuid
from datetime import datetime
from api.domain.list.todo_list import TodoList


from api.domain.task.task_entity import Task
 

class TestTodoList:
    
    def test_list_name_string(self):
        date_s = (datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
        task = Task("","testando a entidade", True, uuid.uuid4().hex, date_s)
        todoList = TodoList("lista de compras","checkbox", uuid.uuid4().hex, [])
        todoList.tasks.append(task)
        assert todoList.name == "lista de compras"
    
    def test_list_name_empty(self):
        date_s = (datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
        task = Task("teste","testando a entidade", True, uuid.uuid4().hex, date_s)
        todoList = TodoList("","checkbox", uuid.uuid4().hex, [])
        todoList.tasks.append(task)
        with pytest.raises(ValueError, match=r"Name is required"):
            todoList.name
            
    def test_list_name_blank(self):
        date_s = (datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
        task = Task("teste","testando a entidade", True, uuid.uuid4().hex, date_s)
        todoList = TodoList("   ","checkbox", uuid.uuid4().hex, [])
        todoList.tasks.append(task)
        with pytest.raises(ValueError, match=r"Name is required"):
            todoList.name
    
    def test_list_type_empty(self):
        date_s = (datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
        task = Task("teste","testando a entidade", True, uuid.uuid4().hex, date_s)
        todoList = TodoList("lista compras","", uuid.uuid4().hex, [])
        todoList.tasks.append(task)
        with pytest.raises(ValueError, match=r"Type of Task is required"):
            todoList.typeTask
            
    def test_list_type_blank(self):
        date_s = (datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
        task = Task("teste","testando a entidade", True, uuid.uuid4().hex, date_s)
        todoList = TodoList("lista","   ", uuid.uuid4().hex, [])
        todoList.tasks.append(task)
        with pytest.raises(ValueError, match=r"Type of Task is required"):
            todoList.typeTask
    
    def test_list_uuid_empty(self):
        date_s = (datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
        task = Task("teste","testando a entidade", True, uuid.uuid4().hex, date_s)
        todoList = TodoList("lista de compras","checkbox", "", [])
        todoList.tasks.append(task)
        with pytest.raises(ValueError, match=r"User id is required"):
            todoList.userId
            
    def test_list_uuid_blank(self):
        date_s = (datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
        task = Task("teste","testando a entidade", True, uuid.uuid4().hex, date_s)
        todoList = TodoList("lista de compras","checkbox", "", [])
        todoList.tasks.append(task)
        with pytest.raises(ValueError, match=r"User id is required"):
            todoList.userId
      
    # def test_list_task_not_found(self):
    #     date_s = (datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
    #     task = Task("teste","testando a entidade", True, uuid.uuid4().hex, date_s)
    #     task1 = Task("teste3","testando a entidade", True, uuid.uuid4().hex, date_s)
    #     todoList = TodoList("lista de compras","checkbox", "", [])
    #     todoList.tasks.append(task)
    #     # todoList.tasks.append(task1)
    #     todoList.tasks.remove(task1)
    #     with pytest.raises(ValueError, match=r"Task not found"):
    #         todoList.tasks.remove(task1)
               
    # def test_list_task_already_exist(self):
    #     date_s = (datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
    #     task = Task("teste","testando a entidade", True, "uuid.uuid4().hex", date_s)
    #     task1 = Task("teste","testando a entidade", True, "uuid.uuid4().hex", date_s)
    #     todoList = TodoList("lista de compras","checkbox", "", [])
    #     todoList.tasks.append(task)
    #     todoList.tasks.append(task1)
    #     with pytest.raises(ValueError, match=r"Task already exists"):
    #         todoList.tasks.append(task1)
                     