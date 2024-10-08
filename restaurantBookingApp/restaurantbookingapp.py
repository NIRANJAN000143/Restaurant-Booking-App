class RestaurantBookingApp:
    
    def __init__(self):

        self.tables = {1: None, 2:None, 3: None, 4: None, 5: None}

    def show_tables(self):

        print("\nTable stats:")

        for table, guest in self.tables.items():
            status = f"Reserved by {guest}" if guest else "Available"

            print(f"Table {table}: {status}")  

    def book_table(self):

        name = input("\nEnter your name:")

        self.show_tables()

        try:
            table_number = int(input("\nEnter table table number to reserve:"))

            if self.tables.get(table_number) is None:

                self.tables[table_number] = name

                print(f"Table {table_number} Successfully reserved by {name}. ")

            else:

                print(f"Table {table_number} is already reserved.")

        except ValueError:

            print("Please enter a valid table number.")

        except KeyError:

            print("Invalid table number. Please enter a table from the list. ")
    def cancel_reservation(self):

        name = input("\nEnter your name to canceled the  reservation:")

        for table, guest in self.tables.items():

            if guest == name:

                self.tables[table] = None

                print(f"Reservation for {name} at Table {table} has been canceled.")

                return
            
            print(f"No reservation found for {name}.")

    def run(self):

        while True:

            print("\nRestaurant Booking Menu: ")

            print("1. View available tables")

            print("2. Book a table")

            print("3. Cancel reservation ")

            print("4. Exit")

            choice = input("\nEnter your choice (1-4): ")

            if choice == "1":

                self.show_tables()

            elif choice == "2":

                self.book_table()

            elif choice == "3":

                self.cancel_reservation()

            elif choice == "4":

                print("thanks you for using the restaurant booking system!")

                break
            else:
                print("Invalid choice.Please enter a valid choice.")

if __name__=="__main__":
    app =RestaurantBookingApp()
    app.run()




                    






