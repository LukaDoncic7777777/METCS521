import csv


class Transfer:
    def __init__(self, amount):
        self.amount = amount

    def transfer_to_Chase(self, amount):
        current = input("Please Enter your card number at Chase: ")
        pin = input("Please Enter your PIN number: ")
        lines = list()
        with open('ChaseCustomer.csv', 'r', newline='') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                lines.append(row)
                if row[0] == "First Name":
                    continue
                if row[5] == current and row[6] == pin:
                    self.amount = int(row[7])
                    self.amount += int(amount)
                    row[7] = str(self.amount)
        with open('ChaseCustomer.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)

    def transfer_to_BOA(self, amount):
        current = input("Please Enter your current card number at Bank Of America: ")
        pin = input("Please Enter your PIN number: ")
        lines = list()
        with open('BankOfAmerica.csv', 'r', newline='') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                lines.append(row)
                if row[0] == "First Name":
                    continue
                if row[0] == current and row[1] == pin:
                    self.amount = int(row[2])
                    self.amount += int(amount)
                    row[2] = str(self.amount)
        with open('BankOfAmerica.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)

    def transfer_to_Citi(self, amount):
        current = input("Please Enter your current card number in Citi Bank: ")
        pin = input("Please Enter your PIN number: ")
        lines = list()
        with open('CitiBank.csv', 'r', newline='') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                lines.append(row)
                if row[0] == "First Name":
                    continue
                if row[5] == current and row[6] == pin:
                    self.amount = int(row[7])
                    self.amount += int(amount)
                    row[7] = str(self.amount)
        with open('CitiBank.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)
