class Flight:
    def __init__(self, flight_id, source, destination, price):
        self.flight_id = flight_id
        self.source = source
        self.destination = destination
        self.price = price


class FlightTable:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def search_by_city(self, city):
        city_flights = [flight for flight in self.flights if flight.source == city or flight.destination == city]
        return city_flights

    def search_from_city(self, source_city):
        from_city_flights = [flight for flight in self.flights if flight.source == source_city]
        return from_city_flights

    def search_between_cities(self, source_city, destination_city):
        between_cities_flights = [flight for flight in self.flights if
                                  flight.source == source_city and flight.destination == destination_city]
        return between_cities_flights


# Creating flight objects
flights_data = [
    ("AI161E90", "BLR", "BOM", 5600),
    ("BR161F91", "BOM", "BBI", 6750),
    ("AI161F99", "BBI", "BLR", 8210),
    ("VS171E20", "JLR", "BBI", 5500),
    ("AS171G30", "HYD", "JLR", 4400),
    ("AI131F49", "HYD", "BOM", 3499)
]

flight_table = FlightTable()

for flight_data in flights_data:
    flight = Flight(*flight_data)
    flight_table.add_flight(flight)

# User interface
while True:
    print("Search Options:")
    print("1. Flights for a particular City")
    print("2. Flights From a city")
    print("3. Flights between two given cities")
    print("4. Quit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        city = input("Enter the city: ")
        city_flights = flight_table.search_by_city(city)
        for flight in city_flights:
            print(f"Flight {flight.flight_id} - From {flight.source} to {flight.destination}, Price: {flight.price}")
    elif choice == 2:
        source_city = input("Enter the source city: ")
        from_city_flights = flight_table.search_from_city(source_city)
        for flight in from_city_flights:
            print(f"Flight {flight.flight_id} - From {flight.source} to {flight.destination}, Price: {flight.price}")
    elif choice == 3:
        source_city = input("Enter the source city: ")
        destination_city = input("Enter the destination city: ")
        between_cities_flights = flight_table.search_between_cities(source_city, destination_city)
        for flight in between_cities_flights:
            print(f"Flight {flight.flight_id} - From {flight.source} to {flight.destination}, Price: {flight.price}")
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please select a valid option.")
