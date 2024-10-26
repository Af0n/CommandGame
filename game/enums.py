from enum import Enum

class KeywordTypes(Enum):
    NONE = 0
    ANY = 1
    COMMAND = 2
    IDENTIFIER = 3
    ARGUMENT = 4
    PARAMETER = 5

class ExecutionCodes(Enum):
    EXIT = 0
    CANCEL = 1
    SUCCESS = 2