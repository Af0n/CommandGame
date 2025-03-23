from object import *

class Inventory(Object):
    def __init__(self, name, aliases, uid, desc):
        super().__init__(name, aliases, uid, desc)
        self.items = []

    def command(self, command):
        match command:
            case "info":
                self.info()

    def info(self):
        print(f"=====\nobject : {self.name}\n{self.desc}\nidentifier: {self.uid}\naliases: {self.aliases}\n")
        print("~ items ~\n")
        for item in self.items:
            print(f"[ {item.name} ]\n")
        print("=====")