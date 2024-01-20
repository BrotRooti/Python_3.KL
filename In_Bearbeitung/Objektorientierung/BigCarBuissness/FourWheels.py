from BigCarBuisness import Vehicle

class FourWheelDrive(Vehicle):
    def __init__(self, brand, price):
        super().__init__(brand, price)

    def __str__(self):
        return super().__str__() + f" and its really cool to drive a 4x4"

    def offRoad(self):
        print("Driving offroad, wich is very cool, with the {}".format(self.brand))