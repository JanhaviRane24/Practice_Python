# Write a Class 'Train' with methods to book a ticket,
# get status (number of seats), and get fare information.

class Train:
    def __init__(self, train_no, source, destination, seats, fare):
        self.train_no = train_no
        self.source = source
        self.destination = destination
        self.seats = seats
        self.fare = fare

    def book(self):
        if self.seats > 0:
            self.seats -= 1
            print("Ticket booked successfully!")
            print("Train No:", self.train_no)
            print("From:", self.source)
            print("To:", self.destination)
        else:
            print("Sorry! No seats available.")

    def get_status(self):
        print("Available Seats:", self.seats)

    def get_fare(self):
        print("Fare: Rs.", self.fare)


# Create object
t = Train(123463, "Delhi", "Pune", 5, 950)

# Call methods
t.book()
t.get_status()
t.get_fare()