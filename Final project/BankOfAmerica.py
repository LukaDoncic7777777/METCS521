import csv
import random
import string
from Transfer import Transfer
transfer = Transfer(0)

class BOA:
    def __init__(self, total_amount, service, currentnum, totalDeposit):
        self.total_amount = total_amount
        self.service = service
        self.currentnum = currentnum
        self.totalDeposit = totalDeposit

    def randomnumbergenerator(self):
        firstdigit = "4"
        new_num = ''.join(random.choices(string.digits, k=3))
        othernum = ''.join(random.choices(string.digits, k=4))
        final = firstdigit + new_num + '-' + othernum + '-' + othernum + '-' + othernum
        return final

    def serviceselector(self):
        service = input(
            "What type of service are you looking for today: (1)Request New Number, (2)Deposit, (3)Get Cash from account, (4)Delete Card, (5)Talk to Representative, (6)Transfer Money: ")
        if service == "1":
            self.service = "Request New Number"
            self.requestnewnumber()
        if service == "2":
            self.service = "Deposit"
            self.Deposit()
        if service == "3":
            self.service = "Get Money"
            self.getMoney()
        if service == "4":
            self.deletecard_num()
        if service == "5":
            self.talktorepresent()
        if service == '6':
            self.transfer_money()

    def requestnewnumber(self):
        current = input("Please Enter your current card number(please enter with -): ")
        text = open("BankOfAmerica.csv", "r")
        text = ''.join([i for i in text])
        if current in text:
            self.currentnum = self.randomnumbergenerator()
            text = text.replace(current, self.currentnum)
        x = open("BankOfAmerica.csv", "w")
        x.writelines(text)
        x.close()
        print("Your new number is " + self.currentnum)
        choice = input("Do you still need other service? Press (Y/y) to continue, Press (N/n) to quit: ")
        if choice == 'Y' or choice == 'y':
            self.serviceselector()
        else:
            print(self.__repr__())

    def transfer_money(self):
        current = input("Please Enter your current card number(Please Enter with -): ")
        pin = input("Please Enter your PIN number: ")
        amount = int(input("Please Enter the amount that you wish to transfer: "))
        text = open("BankOfAmerica.csv", "r")
        text = ''.join([i for i in text])
        with open('BankOfAmerica.csv', 'r+', newline='') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                if row[0] == current and row[1] == pin:
                    totalamount = int(row[2])
                    self.total_amount = totalamount
                    self.total_amount -= amount
                else:
                    continue
        text = text.replace(str(totalamount), str(self.total_amount))
        x = open("BankOfAmerica.csv", "w")
        x.writelines(text)
        x.close()
        choice = input(
            "Where do you want to transfer your money to(Press (1) for Chase, Press (2) for Citi Bank): ")
        if choice == '1':
            transfer.transfer_to_Chase(amount)
        if choice == '2':
            transfer.transfer_to_Citi(amount)
        userchoice = input("Do you still need other service? Press (Y/y) to continue, Press (N/n) to quit: ")
        if userchoice == 'Y' or userchoice == 'y':
            self.serviceselector()
        else:
            print(self.__repr__())

    def Deposit(self):
        current = input("Please Enter your current card number(Please enter with -): ")
        pin = input("Please Enter your PIN number: ")
        amountDeposit = int(input("Please Enter the amount that you want to deposit: "))
        text = open("BankOfAmerica.csv", "r")
        text = ''.join([i for i in text])
        with open('BankOfAmerica.csv', 'r+', newline='') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                if row[0] == current and row[1] == pin:
                    totalAmount = int(row[2])
                    self.totalDeposit = totalAmount
                    self.totalDeposit += amountDeposit
                else:
                    continue
        text = text.replace(str(totalAmount), str(self.totalDeposit))
        x = open("BankOfAmerica.csv", "w")
        x.writelines(text)
        x.close()
        print("Thanks! Your money has been deposited into your account.")
        choice = input("Do you still need other service? Press (Y/y) to continue, Press (N/n) to quit: ")
        if choice == 'Y' or choice == 'y':
            self.serviceselector()
        else:
            print(self.__repr__())

    def getMoney(self):
        current = input("Please Enter your current card number(Please enter with -): ")
        pin = input("Please Enter your PIN number: ")
        amount = int(input("Please Enter the amount that you wish to get: "))
        text = open("BankOfAmerica.csv", "r")
        text = ''.join([i for i in text])
        with open('BankOfAmerica.csv', 'r+', newline='') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                if row[0] == current and row[1] == pin:
                    totalAmount = int(row[2])
                    self.totalDeposit = totalAmount
                    self.totalDeposit -= amount
                else:
                    continue
        text = text.replace(str(totalAmount), str(self.totalDeposit))
        x = open("BankOfAmerica.csv", "w")
        x.writelines(text)
        x.close()
        choice = input("Do you still need other service? Press (Y/y) to continue, Press (N/n) to quit: ")
        if choice == 'Y' or choice == 'y':
            self.serviceselector()
        else:
            print(self.__repr__())

    def deletecard_num(self):
        current = input("Please Enter your current card number: ")
        pin = input("Please Enter your PIN number: ")
        lines = list()
        with open('BankOfAmerica.csv', 'r', newline='') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                lines.append(row)
                if row[0] == current and row[1] == pin:
                    self.total_amount = row[2]
                    lines.remove(row)
        userChoice = input("Where did you what to deposit your money to, Choose (1) to deposit to Chase, Choose (2) to deposit into CitiBank: ")
        if userChoice == '1':
            transfer.transfer_to_Chase(self.total_amount)
        if userChoice == '2':
            transfer.transfer_to_Citi(self.total_amount)
        with open('BankOfAmerica.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)

        choice = input("Do you still need other service? Press (Y/y) to continue, Press (N/n) to quit: ")
        if choice == 'Y' or choice == 'y':
            self.serviceselector()
        else:
            print(self.__repr__())

    def talktorepresent(self):
        reason = input("Please Enter why you are here today? ")
        text = open("BankOfAmericaAssociate.csv", "r")
        text = list(csv.reader(text, delimiter=","))
        for row in text:
            if row[0] == "ID":
                continue
            elif row[1] == "occupied":
                print(
                    "Our associates are busy with other customers. Please wait while we connect you with other "
                    "associates!")
                continue
            else:
                row[1] = "occupied"
                row[2] = reason
                print(f"Associate {row[0]} is ready to help you!")
                break

        x = open("BankOfAmericaAssociate.csv", "w")
        writer = csv.writer(x)
        writer.writerows(text)
        x.close()
        choice = input("Do you still need other service? Press (Y/y) to continue, Press (N/n) to quit: ")
        if choice == 'Y' or choice == 'y':
            self.serviceselector()
        else:
            print(self.__repr__())

    def __repr__(self):
        return 'Thanks for Visiting Bank Of America today, We appreciate your visit!'
