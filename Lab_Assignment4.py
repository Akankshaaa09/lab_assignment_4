class Flight:
    def __init__(self, f_id, source, destination, price):
        self.f_id = f_id
        self.source = source
        self.destination = destination
        self.price = price

class table:
    def __init__(self):
        self.flights = []

    def add(self, flight):
        self.flights.append(flight)

    def search_by_city(self, city):
        by_city_flights = [flight for flight in self.flights if flight.source == city or flight.destination == city]
        return by_city_flights

    def search_from_city(self, city):
        from_city_flights = [flight for flight in self.flights if flight.source == city]
        return from_city_flights

    def search_between_cities(self, city1, city2):
        between_cities_flights = [flight for flight in self.flights if (flight.source == city1 and flight.destination == city2) or (flight.source == city2 and flight.destination == city1)]
        return between_cities_flights

def display_flight_list(flights):
    if not flights:
        print("No flights found.")
        return

    print("{:<10} {:<6} {:<6} {:<10}".format("Flight ID", "From", "To", "Price"))
    for flight in flights:
        print("{:<10} {:<6} {:<6} {:<10}".format(flight.f_id, flight.source, flight.destination, flight.price))

# Creating flight objects
data = [
    ("AI161E90", "BLR", "BOM", 5600),
    ("BR161F91", "BOM", "BBI", 6750),
    ("AI161F99", "BBI", "BLR", 8210),
    ("VS171E20", "JLR", "BBI", 5500),
    ("AS171G30", "HYD", "JLR", 4400),
    ("AI131F49", "HYD", "BOM", 3499)
]

flights = [Flight(*data) for data in data]


flight_table = table()
for i in flights:
    flight_table.add(i)

ch="y"
while ch=="y" or ch=="Y":
    print("Select a search parameter:")
    print("1. Flights for a particular City")
    print("2. Flights From a city")
    print("3. Flights between two given cities")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        city = input("Enter City: ")
        city_flights = flight_table.search_by_city(city)
        display_flight_list(city_flights)
    elif choice == 2:
        city = input("Enter City: ")
        from_city_flights = flight_table.search_from_city(city)
        display_flight_list(from_city_flights)
    elif choice == 3:
        city1 = input("Enter First City: ")
        city2 = input("Enter Second City: ")
        between_cities_flights = flight_table.search_between_cities(city1, city2)
        display_flight_list(between_cities_flights)
    else:
        print("Invalid choice.")
    ch=input("Do you wish to continue?(Y/N): ")
    if ch=="N" or ch=="n":
        print("Thank you!")