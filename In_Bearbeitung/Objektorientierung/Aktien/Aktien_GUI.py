##################################################
#                    Imports                     #
##################################################


import customtkinter as ctk
import time


##################################################
#                     Code                       #
##################################################


class HomeScreen(ctk.CTk):
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
                                          border_width=2, font=("Futura", 40, "bold"), command=self.start_trading)
        WaitWeekButton = ctk.CTkButton(self, text="Wait a Week", fg_color="#860808", bg_color="#EBEBEB", border_width=2,
                                       font=("Futura", 35, "bold"), command=self.wait_week)
        MyDepotButton = ctk.CTkButton(self, text="My Depot", fg_color="#860808", bg_color="#EBEBEB", border_width=2,
                                      font=("Futura", 40, "bold"), command=self.my_depot)
        MarketButton = ctk.CTkButton(self, text="Market", fg_color="#860808", bg_color="#EBEBEB", border_width=2,
                                     font=("Futura", 40, "bold"), command=self.market)
        LogOutButton = ctk.CTkButton(self, text="Log Out", fg_color="#860808", bg_color="#EBEBEB", border_width=2,
                                     font=("Futura", 15, "bold"), command=self.log_out)
        self.WaitedLabel = ctk.CTkLabel(self, text="You waited a week!", fg_color="transparent", bg_color="#EBEBEB",
                                      font=("Futura", 20, "bold"))

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

    def wait_week(self):
        self.WaitedLabel.grid(row=6, column=2, sticky="s")
        self.after(1000, self.WaitedLabel.grid_forget)

    def my_depot(self):
        pass

    def market(self):
        pass

    def log_out(self):
        self.destroy()
        quit()

class Loginwindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.creds = ""
        self.UsernameVar = ctk.StringVar()
        self.title("Login made easy by M&P!")
        self.geometry("500x250")
        self.create_widgets()

    def create_widgets(self):
        self.label = ctk.CTkLabel(master = self,
                                  text = "Login mit einem Username!",
                                  font = ("Roboto", 20, "bold"))
        self.label.pack(pady = 12, padx = 10)

        self.username_entry = ctk.CTkEntry(master = self,
                                           width = 200,
                                           textvariable = self.UsernameVar)
        self.username_entry.pack(pady = 12, padx = 18)

        self.logbutton = ctk.CTkButton(master = self,
                                       text = "Login", fg_color = "green",
                                       hover_color = "dark green",
                                       command = self.login)
        self.logbutton.pack(pady = 12, padx = 18)

    def login(self):
        self.creds = self.username_entry.get()
        self.destroy()
        self.quit()


app = HomeScreen()