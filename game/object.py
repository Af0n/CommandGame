from enums import *

class Object():
    def __init__(self, name, aliases, uid, desc):
        self.name = name
        self.aliases = aliases
        self.uid = uid
        self.desc = desc

        self.expects = KeywordTypes.COMMAND
        self.supports = ["info"]

    def __str__(self):
        return f"name: {self.name}"
    
    # tells if the given testID is equal to the item's unique identifier
    def identify(self, testID):
        return self.uid == testID

    # basic format for the command method
    def command(self, command):
        match command:
            case "info":
                print(f"=====\nobject : {self.name}\n{self.desc}\nidentifier: {self.uid}\naliases: {self.aliases}\n=====")