from module import Pet

name = input("Enter a name for your pet: ")

pet = Pet(name)

while True:
    print("Commands: Feed | Play | Sleep | Check Health | Status| Rename | Quit ")
    command = input("What would you like to do next? ")

    if command == "Feed":
        amount = input ("How much to feed? ")
        print(pet.feed(amount))
    elif command == "Play":
        amount = input ("How much play? ")
        print(pet.play(amount))
    elif command == "Sleep":
        amount = input ("How long to sleep? ")
        print(pet.sleep(amount))
    elif command == "Check Health":
        print(pet.check_health())
    elif command == "Status":
        print(pet.status())
    elif command == "Rename":
        name = input("what name would you like to rename your pet to?")
        pet.name = name 
    elif command == "Quit":
        print("Quitting the simulator")
        break
    else:
        print("I don't recognize that command. Try again.")


