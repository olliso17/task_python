from abc import ABC, abstractmethod
from typing import List


class BaseRepositoryInterface(ABC):
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
