class parkingGarage:

    def __init__(self, tickets, parkingSpaces, currentTicket):
        self.tickets = tickets #list
        self.parkingSpaces = parkingSpaces #list
        self.currentTicket = currentTicket #dictionary {space# : paid/unpaid}

    # Method 1 - take ticket
    def takeTicket(self):
        if len(self.tickets) == 0:
            print("Sorry, the parking garage is at full capacity!")
        else:
            open_stall = self.parkingSpace.pop(0)
            print(f"Please proceed to park in stall {open_stall}. Don't forget to lock your doors!")

            self.parkingSpaces.append(open_stall)
            self.currentTicket[open_stall] = "unpaid"

    def payForParking(self):

    
    def leaveGarage(self):

# ([tickets], [parking spaces], {current tickets: {parking ticket number : paid/unpaid}})
frustration_temple = parkingGarage([1,2,3,4,5,6,7,8,9,10],[],{})


run()
    while True:
        do = input("Welcome to the Frustration Temple Parking Garage! What do you want?! Park/Pay/Leave/Quit ")
        if do.lower() == 'quit':
            print("DEUCES")
            break
        elif do.lower() == 'park':
            frustration_temple.takeTicket()
        elif do.lower() == 'pay':
            frustration_temple.payForParking()
        elif do.lower() == 'leave':
            frustration_temple.leaveGarage()
        else:
            print("Not an option, champ. Try again.")        





    