from BikeRental import*
def main():
    shop=BikeRental(100)
    customer=Customer()
    while True:
        print(""" ====== Bike Rental Shop =======
        1. Display available bikes
        2. Request a bike on hourly basis $5
        3. Request a bike on daily basis $20
        4. Request a bike on weekly basis $60
        5. Return a bike
        6. Exit""")

        try:
            choice = int(input("Enter Choice :"))
        except ValueError:
            print("that's not an int!")
            continue
        if choice==1 :
            shop.displaystock()
        elif choice==2:
            customer.rentalTime=shop.rentbikeOnhour(customer.requestBike())
        elif choice==3:
            customer.rentalTime=shop.rentbikeOndaily(customer.requestBike())
        elif choice==4:
            customer.rentalTime=shop.rentbikeOnWeek(customer.requestBike())
        elif choice==5:
            customer.bill = shop.returnBike(customer.returnBike())
            customer.rentalBasis, customer.rentalTime, customer.bikes = 0, 0, 0
        elif choice == 6:
            break
        else:
            print("Invalid input. Please enter number between 1-6 ")

    print("Thank you for using the bike rental system.")



        # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
