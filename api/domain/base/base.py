import uuid
from datetime import datetime
from api.util.regex import regex
from Cryptodome.Cipher import AES
from Cryptodome.Util import Padding

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
    
    def encrypt(self, value:str):
        key =b"H" * 32
        IV = b"H" * 16
        encryptor = AES.new(key, AES.MODE_CBC, IV)
        padded_value = Padding.pad(value, 16)
        encrypted_value = encryptor.encrypt(padded_value)
        return encrypted_value
    
    def decrypt(self, value:str):
        key =b"H" * 32
        IV = b"H" * 16
        decryptor = AES.new(key, AES.MODE_CBC, IV)
        decrypted_padded_value = decryptor.decrypt(value)
        decrypted_value = Padding.unpad(decrypted_padded_value, 16)
        return decrypted_value