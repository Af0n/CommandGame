from object import *
from inventory import *
from functions import *

allObjects = []
objectsInScope = []
inv = Inventory("Inventory", ["inventory", "i", "inv", "bag"], "inv", "Where your items are held")
item = Object("Test Object", ["testobject", "testobj", "obj", "test"], "testobj", "The test object for testing")
afon = Object("Afon Cyffrous", ["afon", "corgi", "dog"], "corgi", "Hey look, it's me!")
allObjects.append(item)
allObjects.append(afon)
objectsInScope.append(afon)
objectsInScope.append(inv)

def mainLoop():
    while(True):
        command = getCommand("> ")

        keywordList = parseCommand(command, objectsInScope)

        if(type(keywordList) is int):
            continue
        
        execCode = executeCommand(keywordList, objectsInScope)

        match execCode:
            case ExecutionCodes.EXIT:
                break
            case ExecutionCodes.CANCEL:
                continue
            case ExecutionCodes.SUCCESS:
                continue

mainLoop()