# menu driven application for
# 1. open bank account
# 2. deposit money
# 3. check balance
# 4. withdraw money
# 5. close the account
# 6. get the transactions report
# 7. exit

# classes: Bank, Account, AccountHolder, Transaction

class Bank:
    def __init__(self, bank_name, bank_address):
        self.bank_name = bank_name
        self.bank_address = bank_address

    def print_details(self):
        print(f"------Bank Details------ \
               \nBank: {self.bank_name}\nAddress: {self.bank_address}")


class Account(Bank):
    def __init__(self, acc_no, balance, bank_name, bank_address):
        Bank.__init__(self, bank_name, bank_address)
        self.acc_no = acc_no
        self.balance = balance

    def print_details(self):
        super().print_details()
        print(f"------Account Details------ \
               \nAccount No.: {self.acc_no} \
               \nAccount Balance : {self.balance}")


class AccountHolder(Account):
    def __init__(self, acc_no, balance, bank_name, bank_address, acc_holder_name, age):
        Account.__init__(self, acc_no, balance,  bank_name, bank_address)
        self.acc_holder_name = acc_holder_name
        self.age = age

    def print_details(self):
        super().print_details()
        print(f"------Account Holder Details------ \
              \nAccount Holder Name: {self.acc_holder_name} \
              \nAge : {self.age}")

class Transactions(AccountHolder):
    def __init__(self, acc_no, acc_holder_name, age, balance,  bank_name='ABC', bank_address='Goa'):
        AccountHolder.__init__(self, acc_no, balance, bank_name, bank_address, acc_holder_name, age)
        self.transactions = []

    def get_acc_no(self):
        return self.acc_no

    def print_details(self):
        super().print_details()

    def check_balance(self):
        str1 = f"Checking Balance.. \
              \nAccount No.: {self.acc_no} \
              \nCurrent Balance = {self.balance}"
        print(str1)
        self.transactions.append(str1)

    def withdraw_money(self, withdraw_amt):
        if withdraw_amt>0:
            balance_test = self.balance - withdraw_amt
            if balance_test<0:
                print("Withdraw amount exceeds balance amount.. \
                    \nTransaction Failed!!")
            else:
                self.balance = balance_test
                str1 = f"Withdrawing Money.. \
                    \nTransaction Complete \
                    \n{withdraw_amt} withdrawn from Account No. {self.acc_no} \
                    \nUpdated Balance = {self.balance}"
                print(str1)
                self.transactions.append(str1)
        else:
            print("Withdraw amount must be a positive number!!")

    def deposit_money(self, deposit_amt):
        if deposit_amt>0:
            self.balance = self.balance + deposit_amt
            str1 = f"Depositing Money.. \
                \nTransaction Complete \
                \n{deposit_amt} deposited to Account No. {self.acc_no} \
                \nUpdated Balance = {self.balance}"
            print(str1)
            self.transactions.append(str1)
        else:
            print("Deposit amount must be a positive number!!")
            
    def get_transactions_report(self):
        print(f"----Transaction Report for Acc No. {self.acc_no}")
        for i in range(0,len(self.transactions)):
            print("-----------------------")
            print(self.transactions[i])
            print("-----------------------")


    
