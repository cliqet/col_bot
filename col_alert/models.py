"""
Enter details for User and Stock in col.db
Use DB Browser for SQLITE
You need to sign up for a Twilio account to get Twilio credentials
"""

class User:
    def __init__(self, username1, username2, password, twilio_sid, twilio_aid, phone, twilio_phone):
        self.username1 = username1
        self.username2 = username2
        self.password = password
        self.twilio_sid = twilio_sid
        self.twilio_aid = twilio_aid
        self.phone = phone
        self.twilio_phone = twilio_phone

"""
Direction should be "up" or "down" without the quotes
"up" means current price is below target price and you are waiting for the price to go up and hit the target price
"down" means current price is above target price and you are waiting for the price to go down and hit the target price
"""
class Stock:
    def __init__(self, code, target_price, direction):
        self.code = code
        self.target_price = target_price
        self.direction = direction