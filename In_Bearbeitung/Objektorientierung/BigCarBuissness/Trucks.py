from BigCarBuisness import Vehicle


class Trucks(Vehicle):
    def __init__(self, brand, price):
        super().__init__(brand, price)

    def __str__(self):
        return super().__str__() + f" and is so strong, it can pull a house (neither tested nor recommended)"

    def pullTrailer(self):
        print("Pulling a trailer, wich is very cool, with the {}".format(self.brand))
