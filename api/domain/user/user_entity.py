from api.domain.base.base import BaseEntity
from api.domain.user.ov.password_ov import Password


class User(BaseEntity):
    def __init__(self, name: str, email: str, password: Password):
        super().__init__(),
        self.__name = name
        self.__email = email
        self.__password = password

    @property
    def name(self):
        return self._get_String(self.__name, "Name")
