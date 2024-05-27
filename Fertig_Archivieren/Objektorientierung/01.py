'''
first oop exmaple
simple car-class
Phillip
08.01.2024
'''


class Car:
    def __init__(self, manu, m, pri, y, c, p, d, t,mpg):
        self.year = y
        self.doors = d
        self.power = p
        self.color = c
        self.manufacturer = manu
        self.model = m
        self.price = pri
        self.tank = t
        self.tank_level = t
        self.miles_per_gallon = mpg

    def drive(self, range=100):
        if self.tank_level <= 0:
            print(f"Tank is empty, please refill")
            return
        used_fuel = range/self.miles_per_gallon
        if used_fuel > self.tank_level:
            print(f"Vroom, {self.manufacturer} {self.model} is driving. You ran out of fuel after {self.tank_level*self.miles_per_gallon:.1f} kilometers")
            return
        else:
            self.tank_level -= used_fuel
            print(f"Vroom Vroom, {self.manufacturer} {self.model} is driving. The tank is now at {self.tank_level:.1f} liters")



my_garage = []
car_1 = Car("Mercedes", "C63", 100000, 2022, "frog green", 350, 5, 50, 10)
car_2 = Car("BMW", "M3", 90000, 2021, "black", 350, 5, 50, 10)
car_3 = Car("Audi", "RS6", 120000, 2020, "white", 350, 5, 50, 10)
car_4 = Car("Skoda", "Octavia", 20000, 2019, "red", 50, 5, 50, 10)
car_5 = Car("Tesla", "Model 3", 53000, 2023, "blue", 350, 5, 40, 12)
my_garage.append(car_1)
my_garage.append(car_2)
my_garage.append(car_3)
my_garage.append(car_4)
my_garage.append(car_5)

whole_price = 0
for c in my_garage:
    whole_price += c.price
    print(f"{c.manufacturer}: {c.model} is",end=" ")
    c.drive()

print(f"The whole price of the cars in the garage is: {whole_price}€")

while True:
    print("Which car do you want to drive?")
    print("1: Mercedes C63")
    print("2: BMW M3")
    print("3: Audi RS6")
    print("4: Skoda Octavia")
    print("5: Tesla Model 3")
    print("6: Exit")
    choice = int(input("->"))
    match choice:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            break
        case _:
            print("Please choose a valid option")
            continue
    print(f"How many kilometers do you want to drive?")
    km = int(input("->"))
    match choice:
        case 1:
            car_1.drive(km)
        case 2:
            car_2.drive(km)
        case 3:
            car_3.drive(km)
        case 4:
            car_4.drive(km)
        case 5:
            car_5.drive(km)
        case 6:
            break
        case _:
            print("Please choose a valid option")
            continue

