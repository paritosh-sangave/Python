from Bank import *

account_holders = []

while True:
    print("Welcome to ABC Bank!!!")
    print("Please select an option")
    choice = int(input("1. open Account \
         \n2. deposit money \
         \n3. check balance \
         \n4. withdraw money \
         \n5. close the account \
         \n6. get the transactions report \
         \n7. exit \
         \n: "))

    if choice == 1:
        print("Welcome to account opening portal:")
        acc_no = int(input("Enter Custom Account number : "))
        name = input("Enter Name : ")
        age = int(input("Enter Age : "))
        balance = int(input("Enter Balance amount : "))
        acc_transaction = Transactions(acc_no, name, age, balance)
        account_holders.append(acc_transaction)
        print("Your account has been created..!!")
    
    elif choice == 2:
        print("Choice selected : Deposit Money")
        select_acc_no = int(input("Enter Account no. : "))
        acc_found = False
        for acc_holder in account_holders:
            if acc_holder.get_acc_no() == select_acc_no:
                acc_found = True
                print("Account Found..!!")
                deposit_amt = int(input("Enter deposit amount : "))
                acc_holder.deposit_money(deposit_amt)
                break
        if acc_found:
            print("Transaction Completed")
        else:
            print("Account Not Found")

    elif choice == 3:
        print('Choice selected : Check Balance')
        select_acc_no = int(input("Enter Account no. : "))
        acc_found = False
        for acc_holder in account_holders:
            if acc_holder.get_acc_no() == select_acc_no:
                acc_found = True
                print("Account Found..!!")
                acc_holder.check_balance()
                break
        if acc_found:
            print("Transaction Completed")
        else:
            print("Account Not Found")

    elif choice == 4:
        print("Choice selected : Withdraw Money")
        select_acc_no = int(input("Enter Account no. : "))
        acc_found = False
        for acc_holder in account_holders:
            if acc_holder.get_acc_no() == select_acc_no:
                acc_found = True
                print("Account Found..!!")
                withdraw_amt = int(input("Enter withdraw amount : "))
                acc_holder.withdraw_money(withdraw_amt)
                break
        if acc_found:
            print("Transaction Completed")
        else:
            print("Account Not Found")

    elif choice == 5:
        print("Choice Selected : Remove Account")
        select_acc_no = int(input("Enter Account no. : "))
        acc_found = False
        for acc_holder in account_holders:
            if acc_holder.get_acc_no() == select_acc_no:
                acc_found = True
                print("Account Found..!!")
                account_holders.remove(acc_holder)
                break
        if acc_found:
            print("Account Successfully Removed")
        else:
            print("Account Not Found")

    elif choice == 6:
        print("Choice Selected : Display Transactions Report")
        select_acc_no = int(input("Enter Account no. : "))
        acc_found = False
        for acc_holder in account_holders:
            if acc_holder.get_acc_no() == select_acc_no:
                acc_found = True
                print("Account Found")
                acc_holder.get_transactions_report()
                break
        if acc_found:
            print("Task Completed")
        else:
            print("Account Not Found")

    elif choice == 7:
        print("Exiting Banking Menu Program...Have a nice Day!!")
        break

    else:
        print("Invalid choice...exiting program")
        break
    print('\n\n')

