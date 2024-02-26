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
Market.append(LowRiskStock("PhillipsFischereiAG", 230))
Market.append(LowRiskStock("StableBankingAG", 230))
Market.append(LowRiskStock("ReliableUtilitiesAG", 230))
Market.append(MedRiskStock("MaximalGerüstbauAG", 500))
Market.append(MedRiskStock("DynamicTechAG", 500))
Market.append(MedRiskStock("ProgressiveAutoAG", 500))
Market.append(HighRiskStock("R&B RechtskanzleiAG", 727))
Market.append(HighRiskStock("VolatileCryptoAG", 727))
Market.append(HighRiskStock("RiskyStartUpAG", 727))


Market[0].desc = "This stock is low risk \n This is a fishery company. They are known for their high quality fish."
Market[1].desc = "This stock is low risk \n This is a bank. They are known for their stability."
Market[2].desc = "This stock is low risk \n This is a utility company. They are known for their reliability."
Market[3].desc = "This stock is medium risk \n This is a construction company. They are known for their maximalism."
Market[4].desc = "This stock is medium risk \n This is a tech company. They are known for their dynamism."
Market[5].desc = "This stock is medium risk \n This is a car company. They are known for their progressiveness."
Market[6].desc = "This stock is high risk \n This is a law firm. They are known for their long-standing law suits."
Market[7].desc = "This stock is high risk \n This is a crypto company. They are known for their volatility."
Market[8].desc = "This stock is high risk \n This is a start up. They are known for their riskiness."



##################################################
#                   Player                       #
##################################################
name = "Testosteronus Maximus"
Pl = Player(name,1000)



