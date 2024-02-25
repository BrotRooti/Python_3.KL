from Aktien_Classes import Player, LowRiskStock, MedRiskStock, HighRiskStock

##################################################
#                 Functions                      #
##################################################
def market_update():
    for stock in Market:
        stock.update_current_value()

##################################################
#                    Market                      #
##################################################

Market = []
Market.append(LowRiskStock("PhillipsFischereiAG", 230, 2))
Market.append(LowRiskStock("StableBankingAG", 230, 2))
Market.append(LowRiskStock("ReliableUtilitiesAG", 230, 2))
Market.append(MedRiskStock("MaximalGerüstbauAG", 500, 10))
Market.append(MedRiskStock("DynamicTechAG", 500, 10))
Market.append(MedRiskStock("ProgressiveAutoAG", 500, 10))
Market.append(HighRiskStock("R&B RechtskanzleiAG", 727, 50))
Market.append(HighRiskStock("VolatileCryptoAG", 727, 50))
Market.append(HighRiskStock("RiskyStartUpAG", 727, 50))


Market[0].desc = "Fischerei"
Market[1].desc = "Banking"
Market[2].desc = "Utilities"
Market[3].desc = "Gerüstbau"
Market[4].desc = "Tech"
Market[5].desc = "Auto"
Market[6].desc = "Rechtskanzlei"
Market[7].desc = "Crypto"
Market[8].desc = "StartUp"



##################################################
#                   Player                       #
##################################################
name = "Testosteronus Maximus"
Pl = Player(name,1000)



