from BigCarBuisness import Vehicle


class FamilyCar(Vehicle):
    def __init__(self, brand, price, doors):
        super().__init__(brand, price)
        self.doors = doors

    def __str__(self):
        return super().__str__() + f" and has {self.doors} doors"
