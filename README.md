# hotel_management_system_console_app

## Overview
The Hotel Management System is a simple console application developed in Python to manage room bookings, customer information, and checkouts for a hotel. This system is intended to provide basic functionalities for small-scale hotels or for learning purposes in Python programming. Users can view room availability, add new bookings, view specific booking details, and process checkouts—all from a command-line interface.

## Features
•	Display Room Availability: Shows a list of all rooms, indicating whether each is available or currently booked.

•	Add Booking: Allows the user to create a new booking by entering customer details, including name, contact information, and check-in/check-out dates.

•	View Booking: Retrieve and display booking details for a specific customer.

•	Checkout: Process a customer’s checkout, making the room available for new bookings.

•	Exit: Closes the application.

## Code Structure
•	Class HotelManagementSystem: This class contains all methods and logic for managing room bookings and customer information.

•	__init__: Initializes room and customer data structures.

•	display_rooms: Displays the current status of each room (available or booked).
•	add_booking: Adds a new booking by collecting customer details and assigning an available room.
•	view_booking: Retrieves and displays booking details for a specific customer by name.
•	checkout: Checks out a customer, freeing up their room.
•	main_menu: The main interface that displays options and handles user input.
## Requirements
•	Python 3.x: This application requires Python 3 to run. No additional libraries are needed.

## Usage
1. Run the Application: Save the code to a file named hotel_management_system.py. Open a terminal or command prompt, navigate to the file's directory, and run:
### python hotel_management_system_app.py ###

2. Menu Options:
•	Display Rooms: View all rooms and their availability.
•	Add Booking: Enter customer details and assign an available room.
•	View Booking: Search for a specific booking by customer name.
•	Checkout: Complete a customer's checkout, releasing their room.
•	Exit: Exit the application.
## Example ~(Output on the console)
Hotel Management System
1. Display Rooms
2. Add Booking
3. View Booking
4. Checkout
5. Exit
Choose an option (1-5): 

## Adding a Booking
When prompted to add a booking, you will enter details like the customer’s name, contact number, and check-in/check-out dates. If rooms are available, the customer will be assigned to an available room and the booking will be confirmed.

## Viewing and Checking Out
You can retrieve booking details by entering the customer’s name. For checkout, enter the customer’s name, and the system will free up the room for future bookings.

## Future Enhancements
This simple program can be extended by:

•	Adding a database to store room and customer data persistently.
•	Introducing room types and prices.
•	Enhancing error handling and input validation.
•	Adding an admin login system to secure access.

## License
This project is open-source and free to use and modify. No specific license is provided.

This application is a basic implementation of a hotel management system and is best suited for learning purposes in Python or as a foundational project for further development.
