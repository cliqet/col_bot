import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
driver = webdriver.Chrome()

from send_sms import send

def col_login(username1, username2, password):
    print("Logging in ...")

    url = 'https://www.colfinancial.com/ape/Final2/home/HOME_NL_MAIN.asp?p=0'
    driver.get(url)

    user_id1 = driver.find_element_by_xpath('//*[@id="login"]/div/input[1]')
    user_id1.send_keys(username1)

    user_id2 = driver.find_element_by_xpath('//*[@id="login"]/div/input[2]')
    user_id2.send_keys(username2)

    password_field = driver.find_element_by_xpath('//*[@id="login"]/div/input[3]')
    password_field.send_keys(password)

    btn_login = driver.find_element_by_xpath('//*[@id="login"]/div/input[10]')
    btn_login.click()


def go_to_quotepage():
    print("Going to page with quotes ...")
    driver.switch_to.frame('main')
    driver.switch_to.frame('homequote')

def check_price(stocks, user):

    for stock in stocks:

        stock_code = driver.find_element_by_id('T1')
        stock_code.send_keys(stock.code)

        # check quote
        btn_quote = driver.find_element_by_xpath('//*[@id="B1"]')
        btn_quote.click()

        delay = 3  # seconds

        try:
            myElem = WebDriverWait(driver, delay).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="txtHint1"]/div/table[1]/tbody/tr[2]/td[1]/b/font')))
            print("Current price is ready")
        except TimeoutException:
            print("Loading took too much time in quote price!")

        price_element = driver.find_element_by_xpath('//*[@id="txtHint1"]/div/table[1]/tbody/tr[2]/td[1]/b/font')
        current_price = price_element.get_attribute('innerHTML')
        current_price = current_price.strip()
        print("Current price of {} is {}. Target price is {}".format(stock.code, current_price, stock.target_price))

        if stock.direction == 'up':
            # if current price is >= to target price
            if float(current_price) >= float(stock.target_price):
                message = "{} has reached upward price of {}".format(stock.code, stock.target_price)
                send(user.twilio_sid, user.twilio_aid, user.phone, user.twilio_phone, message)
                print("Sent: ", message)
        else:
            if float(current_price) <= float(stock.target_price):
                message = "{} has reached downward price of {}".format(stock.code, stock.target_price)
                send(user.twilio_sid, user.twilio_aid, user.phone, user.twilio_phone, message)
                print("Sent: ", message)

        print("======================================")

        time.sleep(3)


