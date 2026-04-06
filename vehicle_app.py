class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type


class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)

        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof


# ---------------- APP START ----------------

def main():
    print("Please enter vehicle information below:\n")

    vehicle_type = "car"  # fixed per assignment instructions

    year = input("Enter year: ")
    make = input("Enter make: ")
    model = input("Enter model: ")

    # Validate doors input (basic)
    doors = input("Enter number of doors (2 or 4): ")
    while doors not in ["2", "4"]:
        print("Invalid input. Please enter 2 or 4.")
        doors = input("Enter number of doors (2 or 4): ")

    # Validate roof input
    roof = input("Enter type of roof (solid or sun roof): ").lower()
    while roof not in ["solid", "sun roof"]:
        print("Invalid input. Please enter 'solid' or 'sun roof'.")
        roof = input("Enter type of roof (solid or sun roof): ").lower()

    # Create object
    car = Automobile(vehicle_type, year, make, model, doors, roof)

    # Output
    print("\n----- Vehicle Information -----")
    print(f"Vehicle type: {car.vehicle_type}")
    print(f"Year: {car.year}")
    print(f"Make: {car.make}")
    print(f"Model: {car.model}")
    print(f"Number of doors: {car.doors}")
    print(f"Type of roof: {car.roof}")


if __name__ == "__main__":
    main()