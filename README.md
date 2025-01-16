#Smart Parking Program
Smart Parking System
Welcome to the Smart Parking System! This project is designed to help manage parking lots by allowing users to register vehicles, calculate parking fees, and view parking lot 
statuses—all through a user-friendly command-line interface. The system includes an admin mode for managing vehicles and daily charges.

Key Features
Vehicle Registration: Easily register a vehicle by entering its plate number, credit card information, and parking duration.
Parking Lot Status: View real-time status of available and occupied spaces in the parking lot.
Charge Calculation: Automatically calculate parking fees based on parking duration with transparent pricing:
First hour: $5.00
Additional hours: $1.00 per hour
Maximum daily charge: $16.00
Admin Access: Admin functions allow you to remove vehicles or clear all vehicles from the system (password protected).
Daily Charge Reports: View and save a detailed report of daily parking charges for all vehicles in the system.
How It Works
The system is implemented entirely in Python and offers the following options in the main menu:

Register a Vehicle: Add a vehicle by entering its plate number, credit card details, and number of hours parked.
View Parking Lot Status: Check how many spaces are occupied or available.
Verify Vehicle Registration: Confirm if a vehicle is already registered in the system.
View Charges: View all the parking charges for registered vehicles.
Save Charges to a File: Export parking charges and vehicle data to a file for record-keeping.
Remove a Vehicle: Admin users can remove a specific vehicle from the system (admin access required).
Clear All Vehicles: Admin users can clear all vehicles from the parking lot (admin access required).
Exit: Exit the system.
Administrator Mode
Certain functions, such as removing a vehicle or clearing all vehicles, are restricted to admins. To gain access to these features, admins must input the correct password (cprg216).

Example Workflow
Register a Vehicle:

When registering a vehicle, you’ll provide the plate number, credit card info, and number of parking hours. The system will calculate and display the total parking charge.
View Parking Charges:

You can view a breakdown of all parking charges for the day. This includes vehicle plate numbers, parking hours, and total fees.
Save Charges to a File:

At any point, you can save the charge details to a file for record-keeping or reporting purposes.
Admin Functions:

Admins can remove specific vehicles or clear all vehicles from the system using the password-protected admin mode.
Why This Project?
This system was designed to offer a practical solution for parking management. By automating vehicle registration and parking charge calculations, it reduces human error and streamlines the parking process.
With the built-in admin features, this system is perfect for parking lot operators or businesses managing small to medium-sized lots.

Future Improvements
Real-time Updates: Integrating real-time parking space updates (e.g., tracking spaces in use).
Web Interface: A web-based front end for a more user-friendly experience.
Payment Integration: Allow users to pay parking fees directly through the system.
How to Contribute
I welcome contributions to make this project even better! If you’d like to contribute:

Fork the repository.
Create a new branch (git checkout -b feature-name).
Commit your changes (git commit -m 'Add feature').
Push to your fork (git push origin feature-name).
Submit a pull request!
