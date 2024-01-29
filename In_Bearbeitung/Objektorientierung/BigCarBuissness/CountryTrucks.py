from FourWheels import FourWheelDrive


class CountryTruck(FourWheelDrive):
    def __init__(self, brand, price):
        super().__init__(brand, price)

    def __str__(self):
        return super().__str__() + (f" and is really cool to drive, because its a 4x4, but it is so "
                                    f"strong, it can pull a house (neither tested nor recommended)")

    def offRoad(self):
        super().offRoad()

    def pullTrailer(self):
        print("Pulling a trailer, wich is very cool, with the {}".format(self.brand))
