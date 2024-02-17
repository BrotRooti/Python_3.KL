##################################################
#                    Imports                     #
##################################################


import customtkinter as ctk
from Aktien_Config import Pl


##################################################
#                     Code                       #
##################################################


class HomeScreen(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Ballin' Aktien Sim!")
        self.geometry("800x600")
        self.name = Pl.name
        self.money = "Money: " + str(Pl.money) + "€"
        self.stocks = Pl.stocks

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
        self.destroy()
        TradeScreen().mainloop()

    def wait_week(self):
        self.WaitedLabel.grid(row=6, column=2, sticky="s")
        self.after(1000, self.WaitedLabel.grid_forget)

    def my_depot(self):
        pass

    def market(self):
        self.destroy()
        MarketScreen().mainloop()

    def log_out(self):
        self.destroy()
        quit()

class MarketScreen(HomeScreen):
    def __init__(self):
        super().__init__()
        self.title("Market")
        self.create_widgets()

    def create_widgets(self):
        Title = ctk.CTkLabel(self, text="Market", fg_color="transparent", bg_color="#EBEBEB",
                             font=("Futura", 70, "bold"))
        BackButton = ctk.CTkButton(self, text="Back", fg_color="#860808", bg_color="#EBEBEB", border_width=2,
                                     font=("Futura", 15, "bold"), command=self.back)
        Title.grid(row=2, column=2, sticky="n")
        BackButton.grid(row=7, column=0, sticky="sw")

    def conf(self):
        for i in range(5):
            self.columnconfigure(i, weight=1)
            if i == 2:
                self.rowconfigure(i, weight=1)
        for i in range(8):
            self.rowconfigure(i, weight=1)

    def back(self):
        self.destroy()
        Home = HomeScreen()
        Home.mainloop()

class TradeScreen(HomeScreen):
    def __init__(self):
        super().__init__()
        self.title("Trade")


        self.create_widgets()




    def create_widgets(self):
        self.frame1 = ctk.CTkScrollableFrame(self, bg_color="#EBEBEB")
        self.frame2 = ctk.CTkFrame(self, bg_color="#EBEBEB")


        Title = ctk.CTkLabel(self, text="Trade", fg_color="transparent", bg_color="#EBEBEB",
                             font=("Futura", 70, "bold"))
        BackButton = ctk.CTkButton(self, text="Back", fg_color="#860808", bg_color="#EBEBEB", border_width=2,
                                     font=("Futura", 15, "bold"), command=self.back)
        self.TestButton = ctk.CTkButton(self.frame1, text="Test", fg_color="#860808", bg_color="#EBEBEB", border_width=2,
                                     font=("Futura", 15, "bold"))

        self.frame1.grid(row=1, column=0, sticky="n")
        self.frame2.grid(row=1, column=1, sticky="n")
        Title.grid(row=0, column=2, sticky="n")
        BackButton.grid(row=7, column=0, sticky="sw")
        self.TestButton.pack()

    def conf(self):
        for i in range(5):
            self.columnconfigure(i, weight=1)
            if i == 2:
                self.rowconfigure(i, weight=1)
        for i in range(8):
            self.rowconfigure(i, weight=1)

    def back(self):
        self.destroy()
        Home = HomeScreen()
        Home.mainloop()


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
