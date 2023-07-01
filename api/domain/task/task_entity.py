

from api.domain.base.base import BaseEntity


class Task(BaseEntity):

    def __init__(self, title:str, description:str, status:bool, listId:str, timeSelect:str):
        super().__init__()
        self.__title = title
        self.__description = description
        self.__status = status
        self.__listId = listId
        self.__timeSelect = timeSelect

    @property
    def title(self):
       
        return self._get_String(self.__title, "Title")

    @property
    def description(self):

        return self._get_String(self.__description, "Description")

    @property
    def status(self):
               
        return self.__status

    @property
    def listId(self):
        
        return self._get_String(self.__listId, "List id")

    @property
    def timeSelect(self):
        
        return self._get_String(self.__timeSelect, "Data")
   