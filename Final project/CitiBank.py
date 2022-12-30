import csv
import random
import string
from Transfer import Transfer
transfer = Transfer(0)


class Citi:
    def __init__(self, first_Name, last_Name, total_amount, PIN, service, currentnum, totalDeposit):
        self.first_Name = first_Name
        self.last_Name = last_Name
        self.total_amount = total_amount
        self.service = service
        self.currentnum = currentnum
        self.totalDeposit = totalDeposit
        self.PIN = PIN

    def randomNumbergenerator(self):
        firstdigit = "5"
        new_num = ''.join(random.choices(string.digits, k=3))
        othernum = ''.join(random.choices(string.digits, k=4))
        final = firstdigit + new_num + '-' + othernum + '-' + othernum + '-' + othernum
        return final

    def serviceselector(self):
        service = input(
            "What type of service are you looking for today((1)Create an account, (2)Deposit, (3)Delete an Account, (4)Transfer Money: ")
        if service == '1':
            self.create_new_account()
        if service == '2':
            self.Deposit()
        if service == '3':
            self.remove_account()
        if service == '4':
            self.transfer_money()

    def Deposit(self):
        current = input("Please Enter your current card number: ")
        pin = input("Please Enter your PIN number: ")
        amountDeposit = int(input("Please Enter the amount that you want to deposit: "))
        text = open("CitiBank.csv", "r")
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
        x = open("CitiBank.csv", "w")
        x.writelines(text)
        x.close()
        userchoice = input("Do you still need other service? Press (Y/y) to continue, Press (N/n) to quit: ")
        if userchoice == 'Y' or userchoice == 'y':
            self.serviceselector()
        else:
            print(self.__repr__())

    def remove_account(self):
        current = input("Please Enter your current card number: ")
        pin = input("Please Enter your PIN number: ")
        lines = list()
        with open('CitiBank.csv', 'r', newline='') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                lines.append(row)
                if row[5] == current and row[6] == pin:
                    self.total_amount = row[7]
                    lines.remove(row)
        userChoice = input(
            "Where did you what to deposit your money to, Choose (1) to deposit to Chase, Choose (2) to deposit into Bank Of America: ")
        if userChoice == '1':
            transfer.transfer_to_Chase(self.total_amount)
        if userChoice == '2':
            transfer.transfer_to_BOA(self.total_amount)
        with open('CitiBank.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)
        userchoice = input("Do you still need other service? Press (Y/y) to continue, Press (N/n) to quit: ")
        if userchoice == 'Y' or userchoice == 'y':
            self.serviceselector()
        else:
            print(self.__repr__())

    def create_new_account(self):
        self.first_Name = input("Please Enter your First Name: ")
        self.last_Name = input("Please Enter your Last Name: ")
        Address = input("Please Enter your address: ")
        State = input("Please Enter your state: ")
        Zip = input("Please Enter your zip code: ")
        self.PIN = input("What would you like for your pin number: ")
        self.total_amount = input("How much do you want to deposit into the bank: ")
        f = open('CitiBank.csv', 'a')
        f.write(
            self.first_Name + "," + self.last_Name + "," + Address + "," + State + "," + Zip + "," + self.randomNumbergenerator() + "," + self.PIN + "," + self.total_amount)
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
        text = open("CitiBank.csv", "r")
        text = ''.join([i for i in text])
        with open('CitiBank.csv', 'r+', newline='') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                if row[5] == current and row[6] == pin:
                    totalamount = int(row[7])
                    self.total_amount = totalamount
                    self.total_amount -= amount
                else:
                    continue
        text = text.replace(str(totalamount), str(self.total_amount))
        x = open("CitiBank.csv", "w")
        x.writelines(text)
        x.close()
        choice = input(
            "Where do you want to transfer your money to(Press (1) for Bank Of America, Press (2) for Chase Bank): ")
        if choice == '1':
            transfer.transfer_to_BOA(amount)
        if choice == '2':
            transfer.transfer_to_Chase(amount)
        userchoice = input("Do you still need other service? Press (Y/y) to continue, Press (N/n) to quit: ")
        if userchoice == 'Y' or userchoice == 'y':
            self.serviceselector()
        else:
            print(self.__repr__())

    def __repr__(self):
        print("Thanks your visit to Citi Bank today, We appreciate your visit!")