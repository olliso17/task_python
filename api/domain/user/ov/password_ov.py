import re
from api.util.regex import regex
from api.util.regex import regexOneSpecialCaracter
from api.util.regex import regexOneNumber


class Password:
    def __init__(self, password: str):
        self._password = password

    @property
    def password(self):
        if regex.match(self._password) is None:
            raise ValueError('Password is required')
        if (len(self._password) < 8):
            raise ValueError('Password requires more than 8 characters')
        if not re.search(regexOneSpecialCaracter, self._password):
            raise ValueError('Password requires one special character')
        if not re.search(regexOneNumber, self._password):
            raise ValueError('Password requires one number')
        return self._password
