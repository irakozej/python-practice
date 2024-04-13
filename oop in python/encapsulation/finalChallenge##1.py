class Vehicle:
    def __init__(self, company,fuel_amt, mileage_per_litre):
        self.company = company
        self.fuel_amt = fuel_amt
        self.mileage_per_litre = mileage_per_litre

class Car(Vehicle):
    def __init__(self, company, fuel_amt, mileage_per_litre):
        super().__init__(company, fuel_amt, mileage_per_litre)

    def run(self, distance_km):
        fuel_taken = distance_km / self.mileage_per_litre

        if self.fuel_amt >= fuel_taken:
            self.fuel_amt -= fuel_taken
            print("Ran Successfully")
        else:
            print("Not Enough Fuel")