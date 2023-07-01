from abc import ABC, abstractmethod

from api.domain.list.dto.add_todo_list_dto import AddTodoListDto


class SharedRepositoryInterface(ABC):
    @abstractmethod
    def add(self, input):
        raise NotImplementedError
    def find(self, id):
        raise NotImplementedError
    def findAll(self):
        raise NotImplementedError
    def update(self, input):
        raise NotImplementedError
    def activate(self, id):
        raise NotImplementedError