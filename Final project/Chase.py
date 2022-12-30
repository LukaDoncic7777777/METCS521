import csv
import random
import string
from Transfer import Transfer

transfer = Transfer(0)


class chase:
    def __init__(self, first_Name, last_Name, total_amount, service, currentnum, totalDeposit):
        self.first_Name = first_Name
        self.last_Name = last_Name
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
            "What type of service are you looking for today((1)Deposit Cash (2)Open Account (3)Transfer Money: ")
        if service == '1':
            self.Deposit()
        if service == '2':
            self.openaccount()
        if service == '3':
            self.transfer_money()

    def Deposit(self):
        current = input("Please Enter your current card number: ")
        pin = input("Please Enter your PIN number: ")
        amountDeposit = int(input("Please Enter the amount that you want to deposit: "))
        text = open("ChaseCustomer.csv", "r")
        text = ''.join([i for i in text])
        with open('ChaseCustomer.csv', 'r+', newline='') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                if row[5] == current and row[6] == pin:
                    totalAmount = int(row[7])
                    self.totalDeposit = totalAmount
                    self.totalDeposit += amountDeposit
                else:
                    continue
        text = text.replace(str(totalAmount), str(self.totalDeposit))
        x = open("ChaseCustomer.csv", "w")
        x.writelines(text)
        x.close()
        userchoice = input("Do you still need other service? Press (Y/y) to continue, Press (N/n) to quit: ")
        if userchoice == 'Y' or userchoice == 'y':
            self.serviceselector()
        else:
            print(self.__repr__())

    def openaccount(self):
        self.first_Name = input("Please Enter your First Name: ")
        self.last_Name = input("Please Enter your Last Name: ")
        address = input("Please Enter your address: ")
        State = input("Please Enter your state: ")
        Zip = input("Please Enter your zip code: ")
        PIN = input("Please Enter the PIN number you would like to use: ")
        f = open('ChaseCustomer.csv', 'a')
        f.write(
            self.first_Name + "," + self.last_Name + "," + address + "," + State + "," + Zip + "," + self.randomnumbergenerator() + "," + PIN)
        f.close()
        userchoice = input("Do you still need other service? Press (Y/y) to continue, Press (N/n) to quit: ")
        if userchoice == 'Y' or userchoice == 'y':
            self.serviceselector()
        else:
            print(self.__repr__())


    def transfer_money(self):
        current = input("Please Enter your current card number(Please Enter with -): ")
        pin = input("Please Enter your PIN number: ")
        amount = int(input("Please Enter the amount that you wish to transfer: "))
        text = open("ChaseCustomer.csv", "r")
        text = ''.join([i for i in text])
        with open('ChaseCustomer.csv', 'r+', newline='') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                if row[5] == current and row[6] == pin:
                    totalamount = int(row[7])
                    self.total_amount = totalamount
                    self.total_amount -= amount
                    #row[7] = str(self.total_amount)
                else:
                    continue
        text = text.replace(str(totalamount), str(self.total_amount))
        x = open("ChaseCustomer.csv", "w")
        x.writelines(text)
        x.close()
        choice = input(
            "Where do you want to transfer your money to(Press (1) for Bank Of America, Press (2) for Citi Bank): ")
        if choice == '1':
            transfer.transfer_to_BOA(amount)
        if choice == '2':
            transfer.transfer_to_Citi(amount)
        userchoice = input("Do you still need other service? Press (Y/y) to continue, Press (N/n) to quit: ")
        if userchoice == 'Y' or userchoice == 'y':
            self.serviceselector()
        else:
            print(self.__repr__())

    def __repr__(self):
        print("Thanks your visit to Chase Bank today, We appreciate your visit!")



