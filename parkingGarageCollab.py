class parkingGarage:

    def __init__(self, tickets, parkingSpaces, currentTicket):
        self.tickets = tickets #list
        self.parkingSpaces = parkingSpaces #list
        self.currentTicket = currentTicket #dictionary {space# : paid/unpaid}

    # Method 1 
    def takeTicket(self):
        if len(self.tickets) == 0:
            print("We're full get lost!")
        else:
            open_stall = self.tickets.pop(0)
            

            print(f"Go to your spot now: Stall #{open_stall}. Lock your doors! We are not liable for losses/damages.")
            if self.currentTicket == {}:
                print("You've got the VIP spot.")
            else:
                print(self.currentTicket)
            

            self.parkingSpaces.append(open_stall)
            self.currentTicket[open_stall] = "unpaid"

    # Method 2 
    def payforParking(self):
        
        open_stall = int(input("What number space are you in? "))
        if len(self.parkingSpaces) == 0:
            print("Uhhh... try parking first.")
        
        if open_stall not in self.parkingSpaces:
            print("Gimme your space number foo.")
    
        if self.currentTicket[open_stall] == "paid":
            print('You paid already. What are you a wise guy?')
        else:
            print("You've got to pay to play.")
            pay = input("Please type 'Y' to pay ")
                
            if pay.lower() == "y":
                self.currentTicket[open_stall] = "paid"
                print(f'Guy, your ticket has been {self.currentTicket[parking_space]}. Leave in 15 minutes or that ride is OURS.')

    
    
    # Method 3
    def leaveGarage(self):
        
        paid_space = int(input("Enter the parking space number of your ticket: "))
        if len(self.parkingSpaces) == 0:
            print("You need to park first!!")
            return
                     
        if paid_space not in self.parkingSpaces:
                    print("What's your space number? We don't got all day...")
                   
        if self.currentTicket[paid_space] == 'paid':
            self.parkingSpaces.remove(paid_space)
            self.tickets.append(paid_space)
            self.tickets.sort()
            del self.currentTicket[paid_space]
            print("Thank you, safe travels :) Now GET OUTTA HERE.\n")
        else:
            command = input("I see you tryna dip out of here without paying. Pay up: yes/no ")
            if command.lower() == "no":
                print("You trying to live here?\n")
                    
            elif command.lower() == "yes":
                self.pay()

# ([tickets], [parking spaces], {current tickets: {parking ticket number : paid/unpaid}})
parking_stalls = [1,2,3,4,5,6,7,8,9,10]
kourteous = parkingGarage(parking_stalls,[],{})


def run():
    
    while True:
        do = input("Welcome to the one and only KOURTEOUS Parking Garage. What do you want?! Park/Pay/Leave/Quit ")
        if do.lower() == 'quit':
            print("DEUCES!")
            break
        elif do.lower() == 'park':
            kourteous.takeTicket()
        elif do.lower() == 'pay':
            kourteous.payforParking
        elif do.lower() == 'leave':
            kourteous.leaveGarage()
        else:
            print("???")        


run()


