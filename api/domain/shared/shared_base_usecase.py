from abc import ABCMeta
from abc import abstractmethod


class SharedBaseUseCase(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, *args, **kwargs):
        ...