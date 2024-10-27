from object import Object

from enums import KeywordTypes

commands = {
    "yes" : {
        "code" : "yes", 
        "aliases" : ["yes", "y", "confirm"],
        "expects" : KeywordTypes.NONE,
        "supports" : [],
        "description" : f"=====\ncommand : yes\nThis command is used to confirm within confirmation dialogs.\naliases: ['yes', 'y', 'confirm']\nparameters: none\n====="
        },
    "no" : {
        "code" : "no", 
        "aliases" : ["no", "n", "deny"],
        "expects" : KeywordTypes.NONE,
        "supports" : [],
        "description" : f"=====\ncommand : no\nThis command is used to deny within confirmation dialogs.\naliases: ['no', 'n', 'deny']\nparameters: none\n====="
        },
    "exit" : {
        "code" : "exit", 
        "aliases" : ["exit", "x", "quit"],
        "expects" : KeywordTypes.ARGUMENT,
        "supports" : ["*y"],
        "description" : f"=====\ncommand : exit\nThis command is used to exit the program at any point.\naliases: ['exit', 'x', 'quit']\nparameters: ['*y', '*n']\n====="
        },
    "info" : {
        "code": "info",
        "aliases" : ["check", "information", "info", "whatis", "describe", "description"],
        "expects" : KeywordTypes.ANY,
        "supports" : [KeywordTypes.ANY],
        "description" : f"=====\ncommand : info\nThis command can be used to provide information about most anything.\naliases: ['check', 'information', 'info', 'whatis', 'what', 'describe', 'description']\nparameters: any\n====="
    },
    "help" : {
        "code": "help",
        "aliases" : ["h", "commands", "help"],
        "expects" : KeywordTypes.NONE,
        "supports" : [],
        "description" : f"=====\nCommands:\n- yes\n- no\n- exit\n- info\n- help\n\nArguments:\n- *y\n- *n\n====="
    }
}

arguments = {
    "*y" : {
        "expects" : KeywordTypes.NONE,
        "description" : "=====\nargument : *y\nForces a command to skip confirmation dialogs by automatically confirming them\n====="
    },
    "*n" : {
        "expects" : KeywordTypes.NONE,
        "description" : "=====\nargument : *n\nForces a command to skip confirmation dialogs by automatically denying them\n====="
    }
}

errors = {
    "parseCommandErr" : {
        "code" : 1,
        "message" : "Unknown command entered: " # put unknown command here
    },
    "findObjErr" : {
        "code" : 2,
        "message" : "Object not found: " # put unfound obj here
    },
    "parseArgumentErr" : {
        "code" : 3,
        "message" : "Entered invalid argument for given command. Expected: " # put expected arguments here
    },
    "unknownKeywordErr" : {
        "code" : 4,
        "message" : "Entered unknown keyword: " # put unknown keyword here
    },
    "parseArgumentCommandErr" : {
        "code" : 5,
        "message" : "Trying to resolve argument for invalid command: " # put invalid command here
    },
    "invalidInfoParameter" : {
        "code" : 6,
        "message" : "Invalid parameter for info: " # put invalid command here
    }
}

messages = {
    "exit" : "Exit the game? [y/n]\n> "
}
