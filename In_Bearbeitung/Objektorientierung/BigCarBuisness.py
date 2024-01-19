class Vehicle:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def __str__(self):
        return f"This {self.brand} costs {self.price}"

    def drive(self):
        print("Driving the {}".format(self.brand))

    def getPrice(self):
        return self.price


class FamilyCar(Vehicle):
    def __init__(self, brand, price, doors):
        super().__init__(brand, price)
        self.doors = doors

    def __str__(self):
        return super().__str__() + f" and has {self.doors} doors"


class FourWheelDrive(Vehicle):
    def __init__(self, brand, price):
        super().__init__(brand, price)

    def __str__(self):
        return super().__str__() + f" and its really cool to drive a 4x4"

    def offRoad(self):
        print("Driving offroad, wich is very cool, with the {}".format(self.brand))


class Trucks(Vehicle):
    def __init__(self, brand, price):
        super().__init__(brand, price)

    def __str__(self):
        return super().__str__() + f" and is so strong, it can pull a house (neither tested nor recommended)"

    def pullTrailer(self):
        print("Pulling a trailer, wich is very cool, with the {}".format(self.brand))


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


if __name__ == "__main__":
    Garage = []
    car1 = Vehicle("Mercedes", 10000)
    car2 = FamilyCar("Skoda", 12000, 5)
    car3 = FamilyCar("Toyota", 10000, 5)
    car4 = FourWheelDrive("Jeep", 50000)
    car5 = FourWheelDrive("Ford", 40000)
    car6 = Trucks("Tesla", 100000)
    car7 = Trucks("MAN", 100000)
    car8 = CountryTruck("Mercedes", 100000)
    car9 = CountryTruck("Steyr", 100000)
    Garage.append(car1)
    Garage.append(car2)
    Garage.append(car3)
    Garage.append(car4)
    for c in Garage:
        c.drive()
        if isinstance(c, FourWheelDrive or CountryTruck):
            c.offRoad()
        if isinstance(c, Trucks or CountryTruck):
            c.pullTrailer()
        print(c)
