
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


import Trucks
import FamilyCars
import FourWheels
import CountryTrucks


if __name__ == "__main__":
    Garage = []
    car1 = Vehicle("Mercedes", 10000)
    car2 = FamilyCars.FamilyCar("Skoda", 12000, 5)
    car3 = FamilyCars.FamilyCar("Toyota", 10000, 5)
    car4 = FourWheels.FourWheelDrive("Jeep", 50000)
    car5 = FourWheels.FourWheelDrive("Ford", 40000)
    car6 = Trucks.Trucks("Tesla", 100000)
    car7 = Trucks.Trucks("MAN", 100000)
    car8 = CountryTrucks.CountryTruck("Mercedes", 100000)
    car9 = CountryTrucks.CountryTruck("Steyr", 100000)
    Garage.append(car1)
    Garage.append(car2)
    Garage.append(car3)
    Garage.append(car4)
    for c in Garage:
        c.drive()
        if isinstance(c, FourWheels.FourWheelDrive or CountryTrucks.CountryTruck):
            c.offRoad()
        if isinstance(c, Trucks.Trucks or CountryTrucks.CountryTruck):
            c.pullTrailer()
        print(c)
