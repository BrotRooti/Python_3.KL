"""
Inheritance_Example.py
Phillip
15.01.2024
"""


class Animal:
    def __init__(self, name, rested):
        self.name = name
        self.rested = rested

    def __str__(self):
        return (f"This is an Animal Object with the name: {self.name}\n"
                f"And its rested status is: {self.rested}")

    def sleeping(self, duration):
        if duration >= 6:
            self.rested = True
        print(f"{self.name} is sleeping for {duration} hours")

    def running(self, running_time):
        if running_time >= 2:
            self.rested = False
        print(f"{self.name} is running for {running_time} hours")


class Mammal(Animal):
    def __init__(self, name, rested, hungry):
        super().__init__(name, rested)
        self.hungry = hungry

    def __str__(self):
        return super().__str__() + f"\nAnd its hungry status is: {self.hungry}"


if __name__ == "__main__":
    a1 = Animal("Garfield", True)
    a2 = Animal("Dorie", False)
    a3 = Mammal("Simba", True, True)
    a2.sleeping(6.5)
    a2.running(3)
    print(a1)
    print(a2)
    print(a3)
    a3.running(10)
    print(a3)
