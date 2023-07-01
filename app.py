import uuid
from datetime import datetime

from api.domain.list.todo_list import TodoList
from api.domain.task.task_entity import Task

date_s = (datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
task = Task("teste","testando a entidade", True, uuid.uuid4().hex, date_s)
task1 = Task("teste3","testando a entidade", True, uuid.uuid4().hex, date_s)
todoList = TodoList("lista de compras","checkbox", "", [])
todoList.tasks.append(task)
# todoList.tasks.remove(task1)
# todoList.removeTasks(task)
listTask = set(todoList.tasks)
print(task.title)