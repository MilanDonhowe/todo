from ..crud import crud
from os import system

# Test
todoSystem = crud.System()

#todoSystem.create("watermelon")
#todoSystem.create("pineapple")
#todoSystem.create("pineapple")
#todoSystem.create("carrot")
#todoSystem.delete("watermelon")
#todoSystem.create("celery")
#todoSystem.update("celery", "KELTY")


# Write the current display
def display():
    schedule = todoSystem.read()
    system("cls")
    number = 1
    print("TODO Python Application v1.0 by Milan Donhowe\n\n")
    for index in schedule:
        print(f"{number}: {index}\n")
        number += 1
    print("type help for commands")



# DRAW GUI
while True:
    
    display()
    userInput = input(">> ")
    userCheckInput = userInput.upper()
    
    if userCheckInput == "HELP":
        print("\n help - lists help screen.\n\n add - USAGE: add [entry] - creates new entry to todo list.\n\n remove - USAGE: remove [entry] - deletes entry in todo list.\n\n update - USAGE: update [entry] [newData].\n\n")
        todoSystem.delay()
        
    elif userCheckInput == "QUIT":
        exit()

    elif userCheckInput.startswith("REMOVE"):
        
        todoSystem.delete(userInput[7:].strip()) 
    
    # example input: update "pineapple" pine
    elif userCheckInput.startswith("UPDATE"):
    
        arguments = userInput.split("\"")
        todoSystem.update(arguments[1], arguments[2])

    
    elif userCheckInput.startswith("ADD"):

        #sections = userInput.split(" ")
        todoSystem.create(userInput[4:])

    else:
        print('Command not recognized.')
        todoSystem.delay()



