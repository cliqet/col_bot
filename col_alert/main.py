from col import col_login, check_price, go_to_quotepage
from models import User, Stock

from db import Database

db = Database()
db_user = db.get_user()
db_stocks = db.get_stocks()
db.close()


user = User(db_user[0], db_user[1], db_user[2], db_user[3], db_user[4], db_user[5], db_user[6])

stock_list = []
for db_stock in db_stocks:
    stock = Stock(db_stock[0], db_stock[1], db_stock[2])
    stock_list.append(stock)

col_login(user.username1, user.username2, user.password)
go_to_quotepage()

while True:
    check_price(stock_list, user)

