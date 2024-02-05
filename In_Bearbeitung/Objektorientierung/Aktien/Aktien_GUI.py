##################################################
#                    Imports                     #
##################################################

import customtkinter
from customtkinter import CTkFrame, CTkLabel, CTkButton
#from tkinter import *

##################################################
#                     Code                       #
##################################################



class HomeScreen(customtkinter.CTk):
    def __init__(self, name="Testor", money=10000, stocks={}):
        super().__init__()
        self.title("Ballin' Aktien Sim!")
        self.geometry("800x600")
        self.name = name
        self.money = "Money: " + str(money) + "€"

        self.conf()
        self.create_widgets()

    def create_widgets(self):
        UserLabel = ctk.CTkLabel(self, text=self.name, fg_color="transparent", bg_color="#EBEBEB",
                                 font=("Futura", 20, "bold"))
        Title = ctk.CTkLabel(self, text="Ballin' Aktien Sim!", fg_color="transparent", bg_color="#EBEBEB",
                             font=("Futura", 70, "bold"))
        MoneyLabel = ctk.CTkLabel(self, text=self.money, fg_color="transparent", bg_color="#EBEBEB",
                                  font=("Futura", 20, "bold"))
        StartTradinButton = ctk.CTkButton(self, text="Start Tradin'!", fg_color="green", bg_color="#EBEBEB",
                                          border_width=2, font=("Futura", 40, "bold"))
        WaitWeekButton = ctk.CTkButton(self, text="Wait a Week", fg_color="#860808", bg_color="#EBEBEB", border_width=2,
                                       font=("Futura", 35, "bold"))
        MyDepotButton = ctk.CTkButton(self, text="My Depot", fg_color="#860808", bg_color="#EBEBEB", border_width=2,
                                      font=("Futura", 40, "bold"))
        MarketButton = ctk.CTkButton(self, text="Market", fg_color="#860808", bg_color="#EBEBEB", border_width=2,
                                     font=("Futura", 30, "bold"))
        LogOutButton = ctk.CTkButton(self, text="Log Out", fg_color="#860808", bg_color="#EBEBEB", border_width=2,
                                     font=("Futura", 15, "bold"))

        UserLabel.grid(row=0, column=4, sticky="ne")
        Title.grid(row=2, column=2, sticky="n")
        MoneyLabel.grid(row=0, column=0, sticky="nw")
        StartTradinButton.grid(row=4, column=2)
        WaitWeekButton.grid(row=5, column=2, sticky="s")
        MyDepotButton.grid(row=4, column=1, sticky="w")
        MarketButton.grid(row=4, column=3, sticky="e")
        LogOutButton.grid(row=7, column=0, sticky="sw")

    def conf(self):
        for i in range(5):
            self.columnconfigure(i, weight=1)
            if i == 2:
                self.rowconfigure(i, weight=1)
        for i in range(8):
            self.rowconfigure(i, weight=1)


    def start_trading(self):
        pass




ctk = customtkinter
app = HomeScreen()
