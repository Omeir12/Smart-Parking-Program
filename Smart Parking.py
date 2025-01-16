import math

# Constants
MAX_CAPACITY = 50
FIRST_HOUR_FEE = 5.00
ADDITIONAL_HOUR_FEE = 1.00
MAX_DAILY_CHARGE = 16.00
MIN_HOURS = 1
MAX_HOURS = 24
PASSWORD = "cprg216"

# Lists to store vehicle information
plates = []
cc_numbers = []
parking_fees = []
parking_length = []

def print_menu():
    """Display the menu and validate input"""
    print("Smart Parking System")
    print("============================================================")
    print(" Parking fees")
    print(" First hour : $5.00")
    print(" Each additional hour: $1.00 / hour")
    print(" Maximum daily charge: $16.00")
    print("============================================================")
    print("1 - Register a Vehicle")
    print("2 - Display parking lot status")
    print("3 - Verify vehicle registration")
    print("4 - Display daily charges")
    print("5 - Save daily charges to a file")
    print("6 - Remove a vehicle")
    print("7 - Clear Vehicles")
    print("0 - Exit")
    
    while True:
        try:
            # Get the user's input
            option = int(input("Enter an option from the menu >>> "))
            
            # If the input is valid (0-7), return the option
            if 0 <= option <= 7:
                return option
            else:
                # If the option is outside the valid range, show an error message on the same line
                print("Invalid Input - Enter an option from the menu >>>", end=" ")
        except ValueError:
            # If the user doesn't enter a number, show an error message on the same line
            print("Invalid Input - Enter an option from the menu >>>", end=" ")

def calculate_parking_cost(hours):
    """Calculate the parking cost based on the parking hours"""
    hours = math.ceil(hours)  # Round up to the next whole hour
    if hours == 1:
        return FIRST_HOUR_FEE
    else:
        total_cost = FIRST_HOUR_FEE + (hours - 1) * ADDITIONAL_HOUR_FEE
        return min(total_cost, MAX_DAILY_CHARGE)

def register_vehicle():
    """Register a vehicle in the parking lot"""
    if len(plates) >= MAX_CAPACITY:
        print("The parking lot is full")
        return

    print("The parking lot has spaces for your vehicle")
    plate = input("Enter the plate number: ")
    cc_number = input("Enter your credit card number: ")

    while True:
        try:
            hours = int(input("Enter # of parking hours: "))
            if MIN_HOURS <= hours <= MAX_HOURS:
                break
            else:
                print(f"# of parking hours should be between {MIN_HOURS} and {MAX_HOURS}")
        except ValueError:
            print("Invalid input. Please enter a valid number of hours.")
    
    cost = calculate_parking_cost(hours)

    plates.append(plate)
    cc_numbers.append(cc_number)
    parking_length.append(hours)
    parking_fees.append(cost)

    print(f"Thank you, your plate {plate} has been added to the lot.")
    print(f"Total cost is ${cost:.2f}")
    input("Please press enter to continue....")

def display_parking_status():
    """Display the parking lot status"""
    print(f"Parking capacity is {MAX_CAPACITY}")
    
    if not plates:
        print("The parking lot is empty.")
    else:
        available_spaces = MAX_CAPACITY - len(plates)
        print(f"Occupied spaces: {len(plates)}")
        print(f"Available spaces: {available_spaces}")
    input("Please press enter to continue....")

def verify_vehicle():
    """Verify if a vehicle is registered"""
    plate = input("Enter license plate number to verify: ")
    if plate in plates:
        print(f"Vehicle with plate {plate} is registered.")
        return plate
    else:
        print("Vehicle is not registered.")
        return None

def display_charges():
    """Display all charges"""
    if not plates:
        print("The parking lot is empty.")
        return

    print(f"{'License Plate':<15}{'Credit Card':<15}{'Hours':<8}{'Charge':<8}")
    total = 0
    for i in range(len(plates)):
        print(f"{plates[i]:<15}{cc_numbers[i]:<15}{parking_length[i]:<8}{parking_fees[i]:<8.2f}")
        total += parking_fees[i]
    print(f"Total daily charges: ${total:.2f}")
    input("Please press enter to continue....")

    filename = input("Enter the filename to save charges (e.g., charges.txt): ")
    with open(filename, "w") as file:
        file.write(f"{'License Plate':<15}{'Credit Card':<15}{'Hours':<8}{'Charge':<8}\n")
        total = 0
        for i in range(len(plates)):
            file.write(f"{plates[i]:<15}{cc_numbers[i]:<15}{parking_length[i]:<8}{parking_fees[i]:<8.2f}\n")
            total += parking_fees[i]
        file.write(f"Total daily charges: ${total:.2f}\n")
    print(f"Charges saved to {filename}")
    input("Please press enter to continue....")

def remove_vehicle():
    """Remove a vehicle from the lot"""
    plate = verify_vehicle()
    if plate:
        index = plates.index(plate)
        plates.pop(index)
        cc_numbers.pop(index)
        parking_length.pop(index)
        parking_fees.pop(index)
        print(f"Vehicle {plate} has been removed.")
    else:
        print("Vehicle not found.")
    input("Please press enter to continue....")

def clear_vehicles():
    """Clear all vehicles from the parking lot"""
    plates.clear()
    cc_numbers.clear()
    parking_fees.clear()
    parking_length.clear()
    print("All vehicles have been cleared from the parking lot.")
    input("Please press enter to continue....")

def check_password():
    """Check the administrator password"""
    password = input("Enter the administrator password: ")
    if password == PASSWORD:
        return True
    else:
        print("Incorrect password.")
        return False

def main():
    """Main function to run the Smart Parking System"""
    while True:
        print("\nTest #2: Displaying an empty parking status")
        option = print_menu()
        
        if option == 0:
            print("Exiting the program.")
            break
        elif option == 1:
            register_vehicle()
        elif option == 2:
            display_parking_status()
        elif option == 3:
            if check_password():
                verify_vehicle()
        elif option == 4:
            display_charges()
        elif option == 5:
            save_charges()
        elif option == 6:
            if check_password():
                remove_vehicle()
        elif option == 7:
            if check_password():
                clear_vehicles()

if __name__ == "__main__":
    main()






