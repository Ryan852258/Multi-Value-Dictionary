from multi_value_dict import MultiValueDictionary

# Dictionary holding amount of arguments for each command
COMMAND_ARGUMENTS = {"ADD": 2, "REMOVE": 2, "REMOVEALL": 1, "CLEAR": 0, "KEYEXISTS": 1, "VALUEEXISTS": 2, "KEYS": 0, "MEMBERS": 1, "ALLMEMBERS": 0, "ITEMS": 0, "QUIT": 0}
app_dict = MultiValueDictionary()

# Helper function to print lists
def print_list(input_list):
    if (len(input_list) == 0):
        print("(empty set)")
    else:   
        for i,item in enumerate(input_list):
            print("{0}) {1}".format(i+1,item))

# Main application loop
def main():
    print("Welcome to my multivalue dictionary app!")
    while (True):
        try:
            # Get user input and extract the command and arguments 
            user_input = input("> ").split()

            # Check if the user inputted anything 
            if (len(user_input) == 0):
                print(") Invalid command")
                continue

            command = user_input.pop(0).upper()

            # Check if user inputted a valid command
            if (command not in COMMAND_ARGUMENTS):
                print(") Invalid command")
                continue

            # Check if you have the corrent number of arguments for the command
            if (len(user_input) != COMMAND_ARGUMENTS[command]):
                print(") Invalid number of arguments")
                continue

            # Check command and execute requested command
            if (command == "ADD"):
                app_dict.add(user_input[0], user_input[1])
                print(") Added")

            elif (command == "REMOVE"):
                app_dict.remove(user_input[0], user_input[1])
                print(") Removed")

            elif (command == "REMOVEALL"):
                app_dict.remove_all(user_input[0])
                print(") Removed")

            elif (command == "CLEAR"):
                app_dict.clear()
                print(") Cleared")

            elif (command == "KEYEXISTS"):
                result = app_dict.key_exists(user_input[0])
                print(") {}".format(str(result).lower()))

            elif (command == "VALUEEXISTS"):
                result = app_dict.value_exists(user_input[0],user_input[1])
                print(") {0}".format(str(result).lower()))

            elif (command == "KEYS"):
                keys = app_dict.keys()
                print_list(keys)

            elif (command == "MEMBERS"):
                members = app_dict.members(user_input[0])
                print_list(members)

            elif (command == "ALLMEMBERS"):
                members = app_dict.all_members()
                print_list(members)
    
            elif (command == "ITEMS"):
                items = app_dict.all_items()
                print_list(items)

            elif (command == "QUIT"):
                break

        except ValueError as e:
            print(") ERROR, {}".format(str(e)))
            
        except KeyError as e:
            print(") ERROR, {}".format(str(e).strip("'")))

        except Exception:
            print(") ERROR, an unexpected error has occurred")

# load main when ran as a script
if __name__ == "__main__":
    main()