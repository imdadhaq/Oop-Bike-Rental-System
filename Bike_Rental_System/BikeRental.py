import datetime


class BikeRental:
    # initialize stock
    def __init__(self, stock=0):
        self.stock = stock

    # Display the Bikes are currently available
    def displaystock(self):
        print("We have Currently {} bikes avaiable to rent ".format(self.stock))
        return self.stock

    # Rent bike on basis of hour
    def rentbikeOnhour(self, n):
        if n <= 0:
            print("Number of Bikes Should be positive ")
            return None
        elif n > self.stock:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock))
            return None

        else:
            now = datetime.datetime.now()
            print("you have ranted a {} Bikes(s) on a hourly basis today {} at hours ".format(n, now.hour))
            print("You will be charged $5 for each hour per bike ")
            print("We hope that you enjoy our service")
            self.stock -= n
            return now

    def rentbikeOndaily(self, n):
        if n <= 0:
            print("Number of Bikes Should be positive ")
            return None
        elif n > self.stock:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock))
            return None
        else:
            now = datetime.datetime.now()
            print("you have ranted a {} Bikes(s) on daily basis today {} at hours ".format(n, now.hour))
            print("You will be charged $5 for each hour per bike ")
            print("We hope that you enjoy our service")
            self.stock -= n
            return now

    def rentbikeOnWeek(self, n):
        if n <= 0:
            print("Number of Bikes Should be positive ")
            return None
        elif n > self.stock:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock))
            return None
        else:
            now = datetime.datetime.now()
            print("you have ranted a {} Bikes(s) on Weekly basis today {} at hours ".format(n, now.hour))
            print("You will be charged $5 for each hour per bike ")
            print("We hope that you enjoy our service")
            self.stock -= n
            return now

    def returnBike(self, request):
        """
               1. Accept a rented bike from a customer
               2. Replensihes the inventory
               3. Return a bill
        """
        rentalTime, rentalBasis, numOfBikes = request
        bill = 0
        if rentalTime and rentalBasis and numOfBikes:
            self.stock += numOfBikes
            now = datetime.datetime.now()
            rentalPeriod = now - rentalTime

            # hourly bill calculation
            if rentalBasis == 1:
                bill = round(rentalPeriod.seconds / 3600) * 5 * numOfBikes
            # daily bill calculation
            if rentalBasis == 2:
                bill = round(rentalPeriod.days) * 20 * numOfBikes
            # weekly bill calculation
            if rentalBasis == 3:
                bill = round(rentalPeriod.days / 7) * 60 * numOfBikes
            if (3 <= numOfBikes <= 5):
                print("YOu are eligible for family rental promotion of 30% discount")
                bill = bill * 0.7
            print("Thanks for returning your bike. Hope you enjoyed our service!")
            print("That would be ${}".format(bill))
        else:
            print("Are you sure you rented a bike with us?")
            return None


class Customer:
    def __init__(self):
        self.bike = 0
        self.rentalBasis = 0
        self.rentalTime = 0
        self.bill = 0

    def requestBike(self):

        try:
            bikes = int(input("how many bikes would you like to rent?"))
        except ValueError:
            print("That's not a postive integer ")
            return -1
        if bikes < 1:
            print("Invalid input .Number of Bikes should be greater than zero !")
            return -1
        else:
            self.bikes = bikes
        return self.bikes

    def returnBike(self):
        if self.rentalBasis and self.rentalTime and self.bikes:
            return self.rentalBasis and self.rentalTime and self.bikes
        else:
            return 0, 0, 0
