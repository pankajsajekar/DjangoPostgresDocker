
from enum import Enum

class Gender(Enum):
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    OTHERS = 'OTHERS'

    @classmethod
    def choices(cls):
        return [(item.value, item.name.capitalize()) for item in cls]