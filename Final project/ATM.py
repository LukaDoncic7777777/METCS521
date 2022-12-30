import string
from BankOfAmerica import BOA
from Chase import chase
from CitiBank import Citi
from Discover import Discover

chase_ = chase("", "", 0, "", "", 0)
citi = Citi("", "", 0, "", 0, "", 0)
boa = BOA(0, "", "", 0)
discover = Discover("", 0, "", "")

class ATM:
    def __init__(self, banksupplier):
        self.banksupplier = banksupplier

    def verfifycard(self, card_num):
        flag = True
        card_number = card_num.replace("-", "")
        card_number = card_number.replace(" ", "")
        card_number = "".join(char for char in card_number if char.isalnum())
        if any(c.isalpha() for c in card_number):
            flag = False
        if string.punctuation in card_number:
            flag = False
        if len(card_number) != 16:
            flag = False
        return flag

    def getcardinfo(self):
        attempt = 3
        card_number = ""
        while attempt != 0:
            try:
                card_number = input("Please enter the credit card information(Please enter with -): ")
                if self.verfifycard(card_number):
                    if card_number[0] == '4':
                        choice = input("Which bank provider do you have (1)Bank of America (2)Chase: ")
                        if choice == '1':
                            self.banksupplier = "Bank Of America"
                            boa.serviceselector()
                        else:
                            self.banksupplier = "Chase"
                            chase_.serviceselector()

                    if card_number[0] == '6':
                        self.banksupplier = "Discover"
                        discover.serviceselector()

                    if card_number[0] == '5':
                        self.banksupplier = "Citi Bank"
                        citi.serviceselector()
                    break
                else:
                    attempt -= 1

            except ValueError:
                print(f"{card_number} is not a valid card number! Try Again!")

atm = ATM("")
atm.getcardinfo()

