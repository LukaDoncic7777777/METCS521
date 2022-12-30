import random
import string
import csv


class Discover:
    _first_Name = None
    _last_Name = None

    def __init__(self, logo, credit_score, first_Name, last_Name):
        self.logo = logo
        self.credit_score = credit_score
        self._first_Name = first_Name
        self._last_Name = last_Name

    def serviceselector(self):
        service = input(
            "What service are you looking for today? Press (1) for opening a new credit card, press (2) for checking your credit: ")
        if service == '1':
            self.opencard()
        if service == '2':
            self.checkcredit()

    def randomNumbergenerator(self):
        firstdigit = "6"
        new_num = ''.join(random.choices(string.digits, k=3))
        othernum = ''.join(random.choices(string.digits, k=4))
        final = firstdigit + new_num + '-' + othernum + '-' + othernum + '-' + othernum
        return final

    def logochoice(self):
        logo = ""
        choice = input(
            "Please Enter your prefer logo on the card:(1)San Francisco Bridge (2)Dog (3)Rainbow (4)Dollar Cash: ")
        if choice == '1':
            logo = "San Francisco Bridge"
        if choice == '2':
            logo = "Dog"
        if choice == '3':
            logo = "Rainbow"
        if choice == '4':
            logo = 'Dollar Cash'
        return logo

    def opencard(self):
        self._first_Name = input("Please Enter your First Name: ")
        self._last_Name = input("Please Enter your Last Name: ")
        Address = input("Please Enter your address: ")
        State = input("Please Enter your state: ")
        Zip = input("Please Enter your zip code: ")
        Choice = self.logochoice()
        f = open('Discover.csv', 'a')
        f.write(
            self._first_Name + "," + self._last_Name + "," + Address + "," + State + "," + Zip + "," + Choice + "," + self.randomNumbergenerator())
        f.close()

    def checkcredit(self):
        f = open('Discover.csv', 'r')
        f = list(csv.reader(f, delimiter=","))
        card_num = input("What is your card number(Enter with dash): ")
        for row in f:
            if row[0] == "First Name":
                continue
            elif card_num == row[6]:
                self.credit_score = row[7]
                break
        if int(self.credit_score) > 600:
            print(f"your credit currently is {self.credit_score}, please keep it up!")
        else:
            print(f"your credit is {self.credit_score}, please try to pay off your credit card in time!!")
        userchoice = input("Do you still need other service? Press (Y/y) to continue, Press (N/n) to quit: ")
        if userchoice == 'Y' or userchoice == 'y':
            self.serviceselector()
        else:
            print(self.__repr__())

    def __repr__(self):
        if self.logo == "":
            return "Thank you for becoming a valuable member of Discover!"
        else:
            return f"Thank you for becoming a valuable member of Discover, the logo you choose is {self.logo}, we will " \
               f"deliver your card in 7 days."
