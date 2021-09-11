# source of this solution  https://github.com/pyxelr/simple-banking-system

import sqlite3

create_query = ('''CREATE TABLE IF NOT EXISTS card (id INTEGER PRIMARY KEY, number TEXT, 
                pin TEXT, balance INTEGER DEFAULT 0);''')


class BankDB:
    def __init__(self):
        self.conn = sqlite3.connect('card.s3db')
        self.cur = self.conn.cursor()
        self.cur.execute("DROP TABLE IF EXISTS card")
        self.cur.execute(create_query)
        self.conn.commit()

    def insertCard(self, card_number, pin):
        stmt = ("""INSERT INTO card (number, pin) VALUES (?,?)""")
        self.cur.execute(stmt, (card_number, pin))
        self.conn.commit()

    def check_card(self, card):
        check_query = "SELECT * FROM card WHERE number= (?)"
        self.cur.execute(check_query, (card,))
        rows = self.cur.fetchall()
        if len(rows) > 0:
            return rows[0][0]
        return -1

    def check_balance(self, card_number):
        balance_query = "SELECT balance FROM card WHERE number= (?)"
        self.cur.execute(balance_query, (card_number,))
        rows = self.cur.fetchall()
        if len(rows) > 0:
            return rows[0][0]
        return 0

    def add_income(self, card_number, income):
        current = int(self.check_balance(card_number))
        current += income
        income_query = "UPDATE card SET balance=(?) WHERE number= (?)"
        self.cur.execute(income_query, (current, card_number))
        self.conn.commit()

    def delete_acc(self, card_number):
        check_query = "DELETE FROM card WHERE number= (?)"
        try:
            self.cur.execute(check_query, (card_number,))
            self.conn.commit()
        except Exception as exp:
            print(exp)
