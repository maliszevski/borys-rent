from Car import Car
class Fleet:
    def __init__(self):
        self.fleet = []

    def add_car_to_fleet(self, car):
        self.fleet.append(car)

    def build_initial_fleet(self):
        self.add_car_to_fleet(Car("Opel", "Astra", "Hatchback", "100l"))
        self.add_car_to_fleet(Car("Peugeot", "308", "Hatchback", "400l"))
        self.add_car_to_fleet(Car("Mercedes", "G Class", "SUV", "2000l"))
        self.add_car_to_fleet(Car("Nissan", "R35 GTR", "Coupe", "200l"))
        self.add_car_to_fleet(Car("Fiat", "500 Abarth", "Hatchback", "50l"))
        self.add_car_to_fleet(Car("Audi", "RS6 C8", "Combi", "600l"))

    def display_fleet(self):
        counter = 0
        for car in self.fleet:
            print(f"{counter + 1}. car in the fleet:")
            print(f"{car}\n")
            counter += 1