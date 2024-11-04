# hotel_management_system.py

class HotelManagementSystem:
    def __init__(self):
        self.rooms = {i: None for i in range(1, 11)}  # Assuming 10 rooms, numbered 1 to 10
        self.customers = {}

    def display_rooms(self):
        print("\nRoom Availability:")
        for room, customer in self.rooms.items():
            status = "Available" if customer is None else f"Booked by {customer['name']}"
            print(f"Room {room}: {status}")

    def add_booking(self):
        print("\nBooking a Room")
        name = input("Enter customer name: ")
        contact = input("Enter contact number: ")
        check_in = input("Enter check-in date (YYYY-MM-DD): ")
        check_out = input("Enter check-out date (YYYY-MM-DD): ")

        # Find an available room
        available_room = None
        for room, customer in self.rooms.items():
            if customer is None:
                available_room = room
                break

        if available_room:
            # Add booking
            self.rooms[available_room] = {
                "name": name,
                "contact": contact,
                "check_in": check_in,
                "check_out": check_out,
            }
            self.customers[name] = available_room
            print(f"\nRoom {available_room} booked successfully for {name}!")
        else:
            print("Sorry, no rooms are available.")

    def view_booking(self):
        name = input("\nEnter the customer name to view booking details: ")
        room = self.customers.get(name)
        if room:
            booking = self.rooms[room]
            print("\nBooking Details:")
            print(f"Customer Name: {booking['name']}")
            print(f"Contact: {booking['contact']}")
            print(f"Room Number: {room}")
            print(f"Check-in Date: {booking['check_in']}")
            print(f"Check-out Date: {booking['check_out']}")
        else:
            print("No booking found for this customer.")

    def checkout(self):
        name = input("\nEnter the customer name to check out: ")
        room = self.customers.get(name)
        if room:
            # Remove booking
            self.rooms[room] = None
            del self.customers[name]
            print(f"{name} has checked out from room {room}.")
        else:
            print("No booking found for this customer.")

    def main_menu(self):
        while True:
            print("\nHotel Management System")
            print("1. Display Rooms")
            print("2. Add Booking")
            print("3. View Booking")
            print("4. Checkout")
            print("5. Exit")
            choice = input("Choose an option (1-5): ")

            if choice == '1':
                self.display_rooms()
            elif choice == '2':
                self.add_booking()
            elif choice == '3':
                self.view_booking()
            elif choice == '4':
                self.checkout()
            elif choice == '5':
                print("Exiting the system.")
                break
            else:
                print("Invalid option, please choose again.")

if __name__ == "__main__":
    hms = HotelManagementSystem()
    hms.main_menu()
