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
from Aktien_Config import Pl


##################################################
#                     Code                       #
##################################################


Login = Aktien_GUI.Loginwindow()
Login.mainloop()
Pl.name = Login.creds

Aktien_GUI.app = Aktien_GUI.HomeScreen()
Aktien_GUI.app.mainloop()
