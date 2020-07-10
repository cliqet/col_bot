import sqlite3

"""
Tables: User, Stock

User Table
===========
username1
username2
password
twilio_sid
twilio_aid
phone
twilio_phone

Stock Table
=============
code
target_price
direction

"""

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('col.db')
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.close()

    def get_user(self):
        self.cursor.execute("SELECT * FROM User")
        user = self.cursor.fetchone()
        self.conn.commit()

        return user

    def get_stocks(self):
        self.cursor.execute("SELECT * FROM Stock")
        stocks = self.cursor.fetchall()
        self.conn.commit()

        return stocks


