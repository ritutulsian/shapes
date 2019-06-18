'''
This program displays the rental billing
'''

class BikeRental:
    """ This is to calculate the rental of bike"""

    STOCK = 10

    def display_details(self):
        """ This is to calculate the rental of bike"""
        print(f"Total stock available: {BikeRental.STOCK}\nFare Details: ")
        print("Per Hour:$5")
        print("Per Day:$20")
        print("Per Week:$60")

    def order_rental(self):
        """ This is to calculate the rental of bike"""

        initial = True
        while initial:
            self.qty = int(input("Enter the qty of bike to rent:"))
            if self.qty > BikeRental.STOCK:
                print("Enter qty lower than stock available: ")
            else:
                initial = False
        self.category = input("Enter the type of rental: Hourly/Daliy/weekly: ")
        self.duration = int(input("Enter the durantion of rental required: "))

    def billing_hourly(self):
        """ This is to calculate the rental of bike"""
        if self.category == "Hourly":
            print("Total Billing-Hourly:$", (self.qty*5)*self.duration)

    def billing_daily(self):
        """ This is to calculate the rental of bike"""
        if self.category == "Daily":
            print("Total Billing-Daily:$", (self.qty*20)*self.duration)

    def billing_weekly(self):
        """ This is to calculate the rental of bike"""
        if self.category == "Weekly":
            print("Total Billing-Weekly:$", (self.qty*60)*self.duration)


R = BikeRental()
R.display_details()
R.order_rental()
R.billing_hourly()
R.billing_daily()
R.billing_weekly()
