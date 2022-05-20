from secrets import choice


choice = 5

while choice != 0:
    choice = int(input("Insert a number from 1 to 4. Insert 0 for end the application\n"))
    if(choice == 1):
        name = input("Insert a name: ")
        adjective = input("Insert a adjective: ")
        noun = input("Insert a noun: ")
        print(f"Please excuse, {name} who is fat too {adjective} to attend {noun} class.")
    elif(choice == 2):
        name = input("Insert a name: ")
        body_part = input("Insert a body part: ")
        drink = input("Insert a drink: ")
        substance = input("Insert a substance: ")
        print(f"{name} is sick with the {body_part} flu. Drink more {drink} and take {substance} as needed.")
    elif(choice == 3):
        place = input("Insert a place: ")
        noun = input("Insert a noun: ")
        print(f" is authorized to be at {place} insted of {noun} class.")
    elif(choice == 4):
        name = input("Insert a name: ")
        noun = input("Insert a noun: ")
        event = input("Insert a event: ")
        print( f"{name} is too cool for {noun} class. Insted she/he will be attendind the {event}.")
    elif(choice == 0):
        print("Thanks for playing!")
    else:
        print("Invalid choice!")