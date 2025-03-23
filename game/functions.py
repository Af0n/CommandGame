from references import *

from enums import *

# prompts the user to enter a command
def getCommand(message):
    command = input(message)
    command = command.casefold()
    return command

def verifyCommand(keyword):
    for key in commands:
        if(keyword in commands[key]["aliases"]):
            return key
        
    return errors["parseCommandErr"]["code"]

def verifyIdentifier(keyword, collection):
    for obj in collection:
        if(keyword in obj.aliases):
            return obj.uid
        
    return errors["findObjErr"]["code"]

def verifyArgument(keyword, command):
    # print(command)
    # print(keyword)
    if(command not in commands):
        return errors["parseCommandErr"]["code"]
    if(keyword not in arguments):
        return errors["parseArgumentErr"]["code"]
    if(KeywordTypes.ANY in commands[command]["supports"]):
        return keyword
    if(keyword not in commands[command]["supports"]):
        return errors["parseArgumentErr"]["code"]
    
    return keyword

def parseCommand(command, knownObjects):
    command = command.lower()
    keywordList = command.split()
    # print(keywordList)

    expect = KeywordTypes.ANY
    command = ""
    doEvalCommands = True
    
    for i in range(0, len(keywordList)):
        match expect:
            case KeywordTypes.ANY:
                # print("Any Case")
                test = verifyCommand(keywordList[i])
                # we have found a suitable command
                if(type(test) is not int):
                    command = test
                    keywordList[i] = commands[command]["code"]
                    if(doEvalCommands):
                        expect = commands[command]["expects"]
                    else:
                        command = ""
                    doEvalCommands = False
                    continue

                test = verifyIdentifier(keywordList[i], knownObjects)
                # we have found a suitable identifier
                if(type(test) is not int):
                    expect = KeywordTypes.COMMAND
                    keywordList[i] = test
                    continue

                test = verifyArgument(keywordList[i], command)
                # we have found a suitable argument
                if(type(test) is not int):
                    expect = arguments[test]["expects"]
                    continue
                elif(test == errors["parseArgumentCommandErr"]["code"]):
                    printErrorMessage("parseArgumentCommandErr", keywordList[i])
                    return test


                # if we get down here, we haven't found a suitable conversion for our keyword
                printErrorMessage("unknownKeywordErr", keywordList[i])
                return errors["unknownKeywordErr"]["code"]
            case KeywordTypes.PARAMETER:
                # print("Param Case")
                test = verifyIdentifier(keywordList[i], knownObjects)
                # we have found a suitable identifier
                if(type(test) is not int):
                    expect = KeywordTypes.COMMAND
                    keywordList[i] = test
                    continue

                test = verifyArgument(keywordList[i], command)
                # we have found a suitable argument
                if(type(test) is not int):
                    expect = arguments[test]["expects"]
                    continue
                elif(test == errors["parseArgumentCommandErr"]["code"]):
                    printErrorMessage("parseArgumentCommandErr", keywordList[i])
                    return test

                # if we get down here, we haven't found a suitable conversion for our keyword
                printErrorMessage("unknownKeywordErr", keywordList[i])
                return errors["unknownKeywordErr"]["code"]
            case KeywordTypes.IDENTIFIER:
                # print("ID Case")
                test = verifyIdentifier(keywordList[i], knownObjects)
                # we have found a suitable identifier
                if(type(test) is not int):
                    expect = KeywordTypes.COMMAND
                    keywordList[i] = test
                    continue

                printErrorMessage("findObjErr", keywordList[i])
                return test
            case KeywordTypes.ARGUMENT:
                # print("Argument Case")
                test = verifyArgument(keywordList[i], command)
                # we have found a suitable argument
                if(type(test) is not int):
                    expect = arguments[test]["expects"]
                    continue
                elif(test == errors["parseArgumentCommandErr"]["code"]):
                    printErrorMessage("parseArgumentCommandErr", keywordList[i])
                    return test
                printErrorMessage("parseArgumentErr", commands[command]["supports"])
                return test
            case KeywordTypes.COMMAND:
                # print("Command Case")
                test = verifyCommand(keywordList[i])
                # we have found a suitable command
                if(type(test) is not int):
                    command = test
                    keywordList[i] = commands[command]["code"]
                    if(doEvalCommands):
                        expect = commands[command]["expects"]
                        command = ""
                    else:
                        command = ""
                    doEvalCommands = False
                    continue
                printErrorMessage("parseCommandErr", keywordList[i])
                return test

    return keywordList
                
def executeCommand(keywordList, allObjects):
    toExecute = ""
    parameters = []
    args = []

    for keyword in keywordList:
        # if we don't have a command to execute, check for a command
        if(toExecute == ""):
            if(keyword in commands):
                toExecute = keyword
                continue

        if(keyword in arguments):
            args.append(keyword)
            continue

        parameters.append(keyword)

    # print(f"ToExecute {toExecute}")
    # print(f"Params {parameters}")
    # print(f"Args {args}")
    if(toExecute == ""):
        return
    
    match toExecute:
        case "exit":
            return close(args, allObjects)
        case "info":
            return info(parameters, args, allObjects)
        case "help":
            return help()
        
def close(args, allObjects):
    if("*y" in args):
        return ExecutionCodes.EXIT
    if("*n" in args):
        return ExecutionCodes.CANCEL
    
    while(True):
        user = getCommand("Exit game? [y/n]\n> ")

        keywordList = parseCommand(user, allObjects)

        if(keywordList[0] == commands["yes"]["code"]):
            return ExecutionCodes.EXIT
        elif(keywordList[0] == commands["no"]["code"]):
            return ExecutionCodes.CANCEL

def info(params, args, allObjects):
    if(len(params) == 0 ):
        if(len(args) == 0):
            print(commands["info"]["description"])
            return ExecutionCodes.SUCCESS
        params.append(args[0])
    
    testForObj = findObjectFromUID(params[0], allObjects)

    if(testForObj != None):
        testForObj.command("info")
        return ExecutionCodes.SUCCESS
    if(params[0] in commands):
        print(commands[params[0]]["description"])
        return ExecutionCodes.SUCCESS
    if(params[0] in arguments):
        print(arguments[params[0]]["description"])
        return ExecutionCodes.SUCCESS
    
    printErrorMessage("invalidInfoParameter", params[0])
    return ExecutionCodes.CANCEL
    
def help():
    print(commands["help"]["description"])
    return ExecutionCodes.SUCCESS

def findObjectFromUID(uid, allObjects):
    for obj in allObjects:
        if(uid == obj.uid):
            return obj
        
    return None

def printErrorMessage(key, add):
    print(f"{errors[key]["message"]}{add}")