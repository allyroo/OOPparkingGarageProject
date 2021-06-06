class parkingGarage:

    def __init__(self, tickets, parkingSpaces, currentTicket):
        self.tickets = tickets #list
        self.parkingSpaces = parkingSpaces #list
        self.currentTicket = currentTicket #dictionary {space# : paid/unpaid}

    # Method 1 - take ticket
    def takeTicket(self):
        if len(self.tickets) == 0:
            print("Were full get lost!")
        else:
            open_stall = self.parkingSpace.pop(0)
            print(f"Go to your spot now {open_stall}. Don't forget to lock your doors! We are not liable for losses damages.")

            self.parkingSpaces.append(open_stall)
            self.currentTicket[open_stall] = "unpaid"

    def parkingSpaces(self):
        
        parking_space = int(input("What number space are you in? "))
        if len(self.parkingSpaces) == 0:
            print("Park Your ****ing Car man!")
            return
        
        if parking_space not in self.parkingSpaces:
            print("Gimme your space number foo")
            return
    
        if self.currentTicket[parking_space] == "paid":
            print('You paid. What are you a wise guy?')
        else:
            print('You got to pay to play.')
            pay = input("Please type 'Y' to pay ")
                
            if pay.lower() == "y":
                self.currentTicket[parking_space] = "paid"
                print(f'Guy your ticket has been {self.currentTicket[parking_space]} Leave in 15 minutes.')

    
    

    def leave(self):
        
        paid_space = int(input("Please enter the parking space number of your ticket? "))
        if len(self.parkingSpaces) == 0:
            print("Please go ahead and park first!")
            return
            
            
                 
        if paid_space not in self.parkingSpaces:
                    print("Please input a valid space number: ")
                
            
             
        if self.currentTicket[paid_space] == 'paid':
            self.parkingSpaces.remove(paid_space)
            self.tickets.append(paid_space)
            self.tickets.sort()
            del self.currentTicket[paid_space]
            print("Thank you safe travels :) \n")
        else:
            command = input("Your parking has not yet been paid for, would you like to pay y/ n?: ")
            if command.lower() == "n":
                print("Goodbye \n")
                    
            elif command.lower() == "y":
                self.pay()

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






    