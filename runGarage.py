def runGarage():
    while True:
        action = input("Welcome to the parking garage! What would you like to do today \n Park/Pay/Leave/Quit: ")
        if action.lower() == "quit":
            print("GoodBye")
            break
        elif action.lower() == "park":
            capitolParkingGarage.park()
        elif action.lower() == "pay":
            capitolParkingGarage.pay()
        elif action.lower() == "leave":
            capitolParkingGarage.leave()
        elif action.lower() == "show":
            capitolParkingGarage.show()
        else:
            print("Not a valid entry, please try again: ")