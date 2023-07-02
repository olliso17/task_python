import uuid
from datetime import datetime
from api.util.regex import regex


class BaseEntity():
    def __init__(self):
        self._id = uuid.uuid4().hex
        self._createdAt = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        self._updatedAt = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        self._isActive = True
        self._deletedAt = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        
    @property
    def id(self):
        return self._get_String(self._id, "Id")
    
    @property
    def createdAt(self):
        return self._get_String(self._createdAt, "Date created")
    @property
    def updatedAt(self):
        return self._get_String(self._updatedAt, "Date updated")
    
    @property
    def isActive(self):
        return self._isActive
    
    @property
    def deletedAt(self):
        return self._get_String(self._deletedAt, "Date deleted")
    
    def _get_String(self, value:str, name:str)->str:
      
        if regex.match(value) is None:
            raise ValueError(f'{name} is required')
        return value