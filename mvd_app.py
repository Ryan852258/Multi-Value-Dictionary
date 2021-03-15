from multi_value_dict import MultiValueDictionary

# Dictionary holding amount of arguments for each command
COMMANDARGUMENTS = {"ADD": 2, "REMOVE": 2, "REMOVEALL": 1, "CLEAR": 0, "KEYEXISTS": 1, "VALUEEXISTS": 2, "KEYS": 0, "MEMBERS": 1, "ALLMEMBERS": 0, "ITEMS": 0, "QUIT": 0}
appDict = MultiValueDictionary()

def main():
    print("Welcome to my multivalue dictionary app!")
    while(True):
        try:
            # Get user input and extract the command and arguments 
            userInput = input("> ").split()

            # check  if userInput was empty
            if(len(userInput) <= 0):
                print(") Invalid command")
                continue

            command = userInput.pop(0).upper()

            # Check if user inputed a valid command
            if(command not in COMMANDARGUMENTS):
                print(") Invalid command")
                continue

            # Check if you have the corrent number of arguments for the command
            if(len(userInput) != COMMANDARGUMENTS[command]):
                print(") Invalid number of arguments")
                continue

            # Check command and exicute requested command
            if(command == "ADD"):
                appDict.add(userInput[0], userInput[1])
                print(") Added")

            elif(command == "REMOVE"):
                appDict.remove(userInput[0], userInput[1])
                print(") Removed")

            elif(command == "REMOVEALL"):
                appDict.removeall(userInput[0])
                print(") Removed")

            elif(command == "CLEAR"):
                appDict.clear()
                print(") Cleared")

            elif(command == "KEYEXISTS"):
                result = appDict.keyexists(userInput[0])
                print(") {}".format(str(result).lower()))

            elif(command == "VALUEEXISTS"):
                result = appDict.valueexists(userInput[0],userInput[1])
                print(") {0}".format(str(result).lower()))

            elif(command == "KEYS"):
                keys = appDict.keys()
                if(len(keys) == 0):
                    print("(empty set)")
                else:   
                    for i,keys in enumerate(keys):
                        print("{0}) {1}".format(i+1,keys))

            elif(command == "MEMBERS"):
                members = appDict.members(userInput[0])
                if(len(members) == 0):
                    print("(empty set)")
                else:   
                    for i,member in enumerate(members):
                        print("{0}) {1}".format(i+1,member))

            elif(command == "ALLMEMBERS"):
                members = appDict.allmembers()
                if(len(members) == 0):
                    print("(empty set)")
                else:   
                    for i,member in enumerate(members):
                        print("{0}) {1}".format(i+1,member))
    
            elif(command == "ITEMS"):
                items = appDict.allitems()
                if(len(items) == 0):
                    print("(empty set)")
                else:
                    for i,item in enumerate(items):
                        print("{0}) {1}".format(i+1,item))

            elif(command == "QUIT"):
                break

        except ValueError as e:
            print(") ERROR, {}".format(str(e)))
            
        except KeyError as e:
            print(") ERROR, {}".format(str(e).strip("'")))

        except Exception:
            print(") ERROR, an unexpected error has occured")

# load main when ran as a script
if __name__ == "__main__":
    main()