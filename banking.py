import bank_account
import banking_database

db = banking_database.BankDB()
database = {}
choice = ' '
while choice != 0:
    print("""
    1. Create an account
    2. Log into account
    0. Exit""")
    choice = int(input())
    if choice == 1:
        print('Your card has been created')
        c1 = bank_account.BankAccount()
        c1.generate_card_number(db)
        database[c1.credit_number] = c1
        print(f'Your card number:')
        print(c1.credit_number)
        print('Your card PIN:')
        print(c1.pin)

    if choice == 2:
        print(bank_account.BankAccount._active_numbers)
        print('Enter your card number:')
        card_nr = input()
        log_status = False
        try:
            card_nr_check = database[card_nr]
            print('Enter your PIN:')
            pin_input = input()
            pin_nr_check = True if card_nr_check.pin == pin_input else False

            if card_nr_check.pin == pin_input:
                print('You have successfully logged in!')
                log_status = True
                print("""
                    1. Balance
                    2. Add income
                    3. Do transfer 
                    4. Close account
                    5. Log out
                    0. Exit
                    """)
                while pin_nr_check is True:
                    option_logged = int(input())
                    if option_logged == 1:
                        result = db.check_balance(card_nr)
                        print('Balance: ', result)
                    # Add income
                    if option_logged == 2:
                        print('Enter income: ')
                        income = int(input())
                        db.add_income(card_nr, income)
                        print('Income was added!')
                    # Do transfer
                    if option_logged == 3:
                        print("Transfer")
                        print('Enter card number:')
                        money = 0
                        is_error = 0
                        card_number_receiver = input()
                        try:
                            result_luhn = c1.luhn_algo('4000003972196502')
                            print(result_luhn)
                        except Exception as exp:
                            print(exp)
                        if c1.luhn_algo(card_number_receiver) == 0:  # 4000003972196502
                            print("Probably you made a mistake in the card number. Please try again!")
                            is_error = 1
                        if card_nr == (card_number_receiver):
                            print("You can't transfer money to the same account!")
                            is_error = 1
                        if is_error == 0:
                            receiver_id = db.check_card(card_number_receiver)
                            if receiver_id == -1:
                                print("Such a card does not exist.")
                                is_error = 1
                        if is_error == 0:
                            money = int(input("Enter how much money you want to transfer:"))
                            balance = db.check_balance(card_nr)
                            if money > int(balance):
                                print("Not enough money!")
                                is_error = 1
                        if is_error == 0:
                            db.add_income(card_nr, -money)
                            db.add_income(card_number_receiver, money)
                            print("Success!")
                    # Close account
                    if option_logged == 4:
                        db.delete_acc(card_nr)
                        print('The account has been closed!')
                    # Log out
                    if option_logged == 5:
                        print('You have successfully logged out!')
                        break
                    # Close program
                    if option_logged == 0:
                        exit()
            else:
                raise Exception
        except Exception as exp:
            print(exp)
            print('Wrong card number or PIN!')
print('Bye')
