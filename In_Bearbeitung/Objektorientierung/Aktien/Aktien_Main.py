"""
A stock simulation with classes
Maximilian && Phillip
❤
29.01.2024
"""


##################################################
#                    Imports                     #
##################################################


import Aktien_GUI
from Aktien_Classes import Player, Stock, LowRiskStock, MedRiskStock, HighRiskStock


##################################################
#                   Functions                    #
##################################################

def buy_stock(Player, stock, amount):
    if stock.current_value * amount > Player.money:
        print("Hallo stop du hast nicht genug Geld!")
        return
    Player.stocks[stock] = amount + Player.stocks.get(stock, 0)
    Player.money -= stock.current_value * amount
    print(Player.stocks)
    print(Player.money)






##################################################
#                     Code                       #
##################################################

#name= input("What is your name? ")
name= "Testosteronus Maximus"
Pl = Player(name,10000)

Market = []
Market.append(LowRiskStock("PhillipsFischereiAG", 230, 2))
Market.append(MedRiskStock("MaximalGerüstbauAG", 500, 10))
Market.append(HighRiskStock("R&B RechtskanzleiAG", 727, 50))
print(Pl.money)


Aktien_GUI.app = Aktien_GUI.HomeScreen(name, 10000, {})
Aktien_GUI.app.mainloop()

buy_stock(Pl, Market[1], 4)
for st in Market:
    st.update_current_value()

for st in Market:
    print(st.name, end=": ")
    print(st.current_value)

