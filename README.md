# SimpleBankingSystem_pycharmacademy

Simple Banking System written in Python that uses sqlite3 to work with the SQL database.

This code was written for the [Simple Banking System assignment](https://hyperskill.org/projects/109) from the JetBrains Academy, as a part of Python Developer path.

## Table of Contents

* [Main assumptions](#main-assumptions)
* [Usage](#usage)
* [Workflow](#workflow)
  * [Main menu actions](#main-menu-actions)
  * [Account menu actions](#account-menu-actions)

## Main assumptions
The course provided:
* basic banking system building
* creating objects and deleting data in a SQLite database
* implementation and use of the Luhn algorithm 
* Python programming (classes, decorators, modular programming).


## Usage

Open your terminal and run:

```console
python banking.py
```
## Workflow
### Main menu actions

The main menu is as follows:

```console
1. Create an account
2. Log into account
0. Exit
```

**1. Create an account** – generate a new card number which meets all the conditions, such as Luhn's algorithm or a unique card number.

```console
> 1

Your card has been created
Your card number:
4000008334322372
Your card PIN:
5045
```

**2. Log into account** – when logging in the program checks the data stored in the database, if the card number or pin is wrong the user will not be able to log in:

```console
> 2

Enter your card number:
2300
Enter your PIN:
2300
Wrong card number or PIN!

1. Create an account
2. Log into account
3. Exit

> 2

Enter your card number:
4000008334322372
Enter your PIN:
5045
You have successfully logged in!
```

### Account menu actions

After a successful login, the user will see another menu with following options:

```console
1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
```

**1. Balance** – read the balance of the account from the database and output it into the console, balance is set to 0 by default:

```console
> 1

Balance: 0
```

**2. Add income** – item allows to add money to existing account:

```console
> 2

Enter income:
> 500
Income was added!
```

Balance should be now 0 + 500 = 500:

```console
> 1

Balance: 5000
```

**3. Do transfer** – item allows transferring money to another account. It handles the following errors:

* if the user tries to transfer more money than he/she has, output: "_Not enough money!_"
* if the user tries to transfer money to the same account, output the following message: "_You can't transfer money to the same account!_"
* if the receiver's card number doesn’t pass the Luhn algorithm, you should output: "_Probably you made a mistake in the card number. Please try again!_"
* if the receiver's card number doesn’t exist, you should output: "_Such a card does not exist._"
* if there is no error, ask the user how much money they want to transfer and make the transaction.

```console
> 3

Enter card number:
> 4000007916053702
Enter how much money you want to transfer:
> 5000
Success!
```

**4. Close account** – delete the logged in account from the database:

```console
> 4

The account has been closed!
```

**5. Log Out** – log out the user and come back to the main menu:

```console
> 5

You have successfully logged out!
```

**0. Exit** – terminate the scrip and say "Bye!" to the user:

```console
> 0

Bye!
```
