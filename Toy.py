from ToyShop import ToyShop


class Toy:
    def __init__(self, id, name, quantity, weight):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.weight = weight

    def set_weight(self, weight):
        self.weight = weight

    def add_quantity(self, quantity):
        self.quantity += quantity

    def remove_quantity(self, quantity):
        if self.quantity >= quantity:
            self.quantity -= quantity
        else:
            print("Недостаточно игрушек на складе!")

    def __str__(self):
        return f"{self.id}. {self.name} - {self.quantity} шт., {self.weight}%"
