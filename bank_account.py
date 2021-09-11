from random import randint
from random import seed


class BankAccount:
    seed(12)
    _active_numbers = []

    def __init__(self):
        self.INN = 400000
        self.pin = str(randint(1000, 9999))
        self.balance = 0
        self.not_valid_numbers = []

    def luhn_algo(self, credit_number):
        try:
            without_last_digit = credit_number[:-1]
            multiplied_numbers = [int(i) * 2 if int(j) % 2 == 0 else int(i) for j, i in enumerate(without_last_digit)]
            substract_9 = [i - 9 if i > 9 else i for i in multiplied_numbers]
            sum_numbers = sum(substract_9) + int(credit_number[-1])
            mod_10 = sum_numbers % 10
            luhn_check = True
            if mod_10 == 0:
                self.checksum = 0
                luhn_check = True
                return luhn_check
            else:
                self.not_valid_numbers.append(credit_number)
                self.checksum = 10 - mod_10
                luhn_check = False
                return luhn_check
        except Exception as exp:
            return False

    def generate_card_number(self, db):
        self.credit_number = str(self.INN) + str(randint(1000000000, 9999999999))
        if self.credit_number in self._active_numbers:
            new_seed = randint(0, 10)
            seed(new_seed)
            self.credit_number = str(self.INN) + str(randint(1000000000, 9999999999))  # '4000006904525580'
        if self.luhn_algo(self.credit_number) is True:
            cand_number = self.credit_number[:-1]
            last_digit = int(self.credit_number[-1]) + self.checksum
            new_number = str(cand_number) + str(abs(last_digit) % 10) if last_digit >= 10 else str(cand_number) + str(
                abs(last_digit))
            self.credit_number = new_number
            db.insertCard(self.credit_number, self.pin)
            self._active_numbers.append(self.credit_number)
        if self.luhn_algo(self.credit_number) is False:
            cand_number = self.credit_number[:-1]
            last_digit = int(self.credit_number[-1]) + self.checksum
            new_number = str(cand_number) + str(abs(last_digit) % 10) if last_digit >= 10 else str(cand_number) + str(
                abs(last_digit))
            self.credit_number = new_number
            db.insertCard(self.credit_number, self.pin)
            self._active_numbers.append(self.credit_number)
        else:
            print('Card is not valid')
