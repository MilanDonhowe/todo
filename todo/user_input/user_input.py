from ..crud import crud
from os import system

# Test
todoSystem = crud.System()
todoSystem.create("watermelon")
todoSystem.create("pineapple")
todoSystem.create("pineapple")
todoSystem.create("carrot")
todoSystem.delete("watermelon")
todoSystem.create("celery")
todoSystem.update("celery", "CELLLLLLLLRYYYY")


# Write the current display
def display():
    schedule = todoSystem.read()
    system("cls")
    number = 1
    print("TODO Python Application v1.0 by Milan Donhowe")
    for index in schedule:
        print(f"{number}: {index}")
        number += 1
    print("type help for commands")

def delay():
    print("Press enter to continue.")
    input()


# DRAW GUI
while True:
    
    display()
    userInput = input(">> ")
    userCheckInput = userInput.upper()

    if userCheckInput == "HELP":
        print(" help - lists help screen.\n add - USAGE: add [entry] - creates new entry to todo list.\n remove - USAGE: remove [entry] - deletes entry in todo list.\n update - USAGE: update [entry] [newData].")
        delay()
        
    elif userCheckInput == "QUIT":
        exit()

    elif userCheckInput.startswith("REMOVE"):

        todoSystem.delete(userInput[6:])
        delay()
    
    elif userCheckInput.startswith("ADD"):

        #sections = userInput.split(" ")
        todoSystem.create(userInput[3:] + "\n")
        delay()

    else:
        print('Command not recognized.')



