# Shreyas Rajendra Shigwan , Roll no. 90, CSE(AIML)
#Exp 6.3: Vehicle rental System


class Vehicle:
    def __init__(self, reg_no, model, daily_rate):
        self.reg_no = reg_no
        self.model = model
        self.daily_rate = daily_rate
        self.is_rented = False

    def rent(self):
        if self.is_rented:
            print(f"{self.model} is already rented.")
            return False
        self.is_rented = True
        return True

    def return_vehicle(self):
        self.is_rented = False

class RentalAgency:
    def __init__(self, name):
        self.name = name
        self.fleet = []

    def add_vehicle(self, vehicle):
        self.fleet.append(vehicle)

    def show_available(self):
        print(f"Available Vehicles at {self.name}:")
        for v in self.fleet:
            if not v.is_rented:
                print(f"- {v.model} (${v.daily_rate}/day)")

    def rent_vehicle(self, reg_no, days):
        for v in self.fleet:
            if v.reg_no == reg_no:
                if v.rent():
                    cost = v.daily_rate * days
                    print(f"Rented {v.model} for {days} days. Total Cost: ${cost}")
                    return
        print("Vehicle not available or not found.")

def main():
    print("--- Vehicle Rental System ---")
    agency = RentalAgency("City Rentals")
    
    agency.add_vehicle(Vehicle("V001", "Mahindra Scorpio", 40))
    agency.add_vehicle(Vehicle("V002", "Ferarri 811", 45))
    agency.add_vehicle(Vehicle("V003", "Lamborgini Urus", 80))

    agency.show_available()
    
    print("\nRent Request:")
    agency.rent_vehicle("V002", 3)
    
    print("\nAvailable Vehicles after renting:")
    agency.show_available()

if __name__ == "__main__":
    main()
