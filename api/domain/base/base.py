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
        
    def _get_String(self, value:str, name:str)->str:
      
        if regex.match(value) is None:
            raise ValueError(f'{name} is required')
        return value