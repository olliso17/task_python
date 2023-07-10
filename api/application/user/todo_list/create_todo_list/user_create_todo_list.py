
from api.application.user.todo_list.create_todo_list.user_create_todo_list_dto import InputCreateTodoListDto, OutputCreateTodoListDto
from api.domain.list.todo_list_repository_interface import TodoListRepositoryInterface


class CreateTodoListUsecase:
    def __init__(self):
        # self.user_repository =
        self.todo_list_repository = TodoListRepositoryInterface

    def execute(self, input: InputCreateTodoListDto):
        self.name = input.name
        self.typeTask = input.typeTask
        self.userId = input.userId
        # todo_list_repository = self.todo_list_repository.add(input)
        # output: OutputCreateTodoListDto = {
        #     id: todo_list_repository..id
        # }
