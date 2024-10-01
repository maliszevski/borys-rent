class Car:
    def __init__(self, brand, model, body, trunk_capacity):
        self.brand = brand
        self.model = model
        self.body = body
        self.trunk_capacity = trunk_capacity

    def __str__(self):
        return (f"Brand: {self.brand}\n"
                f"Model: {self.model}\n"
                f"Body: {self.body}\n"
                f"Trunk capacity: {self.trunk_capacity}")
class Fleet:
    def __init__(self):
        self.fleet = []
    @classmethod
    def add_cars_to_the_fleet(cls):
        fleet = [
            Car("Opel", "Astra", "Hatchback", "100l"),
            Car("Peugeot", "308", "Hatchback", "400l"),
            Car("Mercedes", "G Class", "SUV", "2000l"),
            Car("Nissan", "R35 GTR", "Coupe", "200l"),
            Car("Fiat", "500 Abarth", "Hatchback", "50l"),
            Car("Audi", "RS6 C8", "Combi", "600l")
        ]
        return fleet
    def add_fleet(self):
        self.fleet = Fleet.add_cars_to_the_fleet()
    def display_fleet(self):
        for car in self.fleet:
          print(f"{car}\n")






