from api.domain.base.base_repository_interface import BaseRepositoryInterface


class TodoListRepositoryInterface(BaseRepositoryInterface):
    def __init__(self) -> None:
        super().__init__()
