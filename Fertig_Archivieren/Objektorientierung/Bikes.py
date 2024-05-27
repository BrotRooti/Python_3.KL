

class Rad:
    def __init__(self, hersteller, preis, gaenge):
        self.hersteller = str(hersteller)
        self.preis = float(preis)
        self.gaenge = int(gaenge)

    def __str__(self):
        return f"Das Rad der Marke {self.hersteller} kostet {self.preis} und hat {self.gaenge} gänge"

    def fahren(self):
        return f"Ich fahre mit meinem {self.hersteller} Rad"


class MountainBike(Rad):
    def __int__(self, hersteller, preis, gaenge, federweg):
        super().__init__(hersteller, preis, gaenge)
        self.federweg = int(federweg)

    def __str__(self):
        return super().__str__() + f"und hat {self.federweg}mm Federweg"

    def schreddern(self):
        if self.federweg < 100:
            return f"Pass auf du hast nur {self.federweg} Federweg, fahr bitte langsam"
        else:
            return f"Du hat {self.federweg} Federweg. Für dich gibt es nur ein Gas: Vollgas"

Garage=[]
Garage.append(Rad("KTM", 100.50, 21))
Garage.append(Rad("Tesla", 420.69, 200))
Garage.append(MountainBike("MKB", 69.69, 10, 150))
Garage.append(MountainBike("MKB", 69.69, 10, 50))


for c in Garage:
    print(c)
    print(c.federweg)
    if isinstance(c, MountainBike):
        print(c.schreddern())
    print("______________________")
