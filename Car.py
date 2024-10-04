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
