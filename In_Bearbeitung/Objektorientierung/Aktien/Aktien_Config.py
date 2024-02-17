from Aktien_Classes import Player, Stock, LowRiskStock, MedRiskStock, HighRiskStock

### Market###

Market = []
Market.append(LowRiskStock("PhillipsFischereiAG", 230, 2))
Market.append(MedRiskStock("MaximalGerüstbauAG", 500, 10))
Market.append(HighRiskStock("R&B RechtskanzleiAG", 727, 50))

### Player##
name= "Testosteronus Maximus"
Pl = Player(name,690000)


#buy_stock(Pl, Market[1], 4)
for st in Market:
    st.update_current_value()

for st in Market:
    print(st.name, end=": ")
    print(st.current_value)