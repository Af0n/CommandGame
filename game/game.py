from object import *
from functions import *

allObjects = []
item = Object("Test Object", ["testobject", "testobj", "obj", "test"], "testobj", "The test object for testing")
afon = Object("Afon Cyffrous", ["afon", "corgi", "dog"], "corgi", "Hey look, it's me!")
allObjects.append(item)
allObjects.append(afon)

def mainLoop():
    while(True):
        command = getCommand("> ")

        keywordList = parseCommand(command, allObjects)

        if(type(keywordList) is int):
            continue
        
        execCode = executeCommand(keywordList, allObjects)

        match execCode:
            case ExecutionCodes.EXIT:
                break
            case ExecutionCodes.CANCEL:
                continue
            case ExecutionCodes.SUCCESS:
                continue

mainLoop()