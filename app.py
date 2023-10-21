import configparser
import json
import requests
import asyncio
# from  aiogram import Bot, Dispatcher, executor,types
import time
import os
import threading
import telebot
from telebot import types
# BUSD BNB ISSUES

crypto_values = {
        'LTC': 50004,
        'DOGE': 50007,
        'TRX': 6377,
        'USDT': 7223,
        'ETH': 50010,
        'BTC': 50001,
        'XRP': 8021,
        'MATIC': 8297,
        'LINK': 7835,
        'BUSD': 10355,
        'BNB': 40001
    }

def get_yobit_list(pair, pair_id):
    cookies = {
        '__ddg1_': 'p4pod51GNc8M8FBo8wiH',
        'locale': 'en',
        'c9839b948ceea6f557b8912b7229bec8': '1',
        'registertimer': '1',
        'LLXR': '1695900086',
        'LLXUR': 'ec99ee9e6bfb',
        '_ym_uid': '1695900088911625923',
        '_ym_d': '1695900088',
        '_ym_isad': '1',
        'marketbase': 'usd',
        'Rfr': 'https%3A%2F%2Fyobit.net%2Fen%2F',
        '__ddgid_': 'ae9EHVtYzWt9vWvD',
        '__ddgmark_': 'WCNb3BI9y8qb6YtV',
        '__ddg5_': 'a1KHVYth3P0yA19g',
        'PHPSESSID': 'bipggtgo5t7cqvnk89f3hgh0vc',
    }

    headers = {
        'authority': 'yobit.net',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '__ddg1_=p4pod51GNc8M8FBo8wiH; locale=en; c9839b948ceea6f557b8912b7229bec8=1; registertimer=1; LLXR=1695900086; LLXUR=ec99ee9e6bfb; _ym_uid=1695900088911625923; _ym_d=1695900088; _ym_isad=1; marketbase=usd; Rfr=https%3A%2F%2Fyobit.net%2Fen%2F; __ddgid_=ae9EHVtYzWt9vWvD; __ddgmark_=WCNb3BI9y8qb6YtV; __ddg5_=a1KHVYth3P0yA19g; PHPSESSID=bipggtgo5t7cqvnk89f3hgh0vc',
        'origin': 'https://yobit.net',
        'referer': 'https://yobit.net/en/trade/' + str(pair).upper() + '/USD',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    datas = {
        'pair_id': str(pair_id),
        'tz': 'Asia/Dhaka',
    }

    return requests.post('https://yobit.net/ajax/system_status_data.php', cookies=cookies,
                             headers=headers,
                             data=datas)

def send_msg(text):
    token = os.environ.get("TOKEN")
    chat_id = os.environ.get("CHAT_ID_1")
    chat_id2 = os.environ.get("CHAT_ID_2")
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    url_req2 = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id2 + "&text=" + text
    results = requests.get(url_req)
    # ##print((results.json())
    results2 = requests.get(url_req2)
    # ##print((results2.json())
# global data


def get_binance_price_ticker2():
    url = os.environ.get("URL")

    response = requests.get(url)
    data = response.json()
    ##print((data)
    pair_id = 7223
    pair = 'USDT'
    last_trade_binance = 1
    if pair == "USDT":
        print(pair)
        pair_id = 7223
        buy_ords = get_yobit_list(pair, pair_id).json()
        # #print((response.json())
        lx = 1
        for i in range(len(buy_ords['buyord'])):
            lx = lx + 1
            if lx > 2:
                continue
            print(pair)
            pair = 'USDT'
            # ##print((response.json()['buyord'][i]['p'], response.json()['buyord'][i]['a'])
            # ##print((response.json()['buyord'][i]['p'], response.json()['buyord'][i]['a'])
            last_trade = float(buy_ords['buyord'][i]['p'])
            ltc_amount = float(buy_ords['buyord'][i]['a'])
            # calculate the difference
            # send the message to telegram

            # считаем разницу

            percent = ((last_trade - last_trade_binance) / last_trade_binance) * int(100)
            #print((percent)
            # percent = int(100) / (last_trade - last_trade_binance) / last_trade_binance * int(100000)
            percent2 = round(percent, 4)
            # ##print(('Difference between exchange rates in %', percent2)
            # time.sleep(1)
            binance_1000 = 1000 / last_trade_binance
            yobit_1000 = binance_1000 * last_trade
            # ##print((yobit_1000)
            config = configparser.ConfigParser()
            config.read('config.ini')
            crypto_value = config.get('Section 1', str(pair))
            crypto_amount = config.get('Section 3', str(pair) + "_a")
            print(pair)

            if yobit_1000 > int(crypto_value) and float(ltc_amount) > float(crypto_amount):
                # percent_str = str(percent2) + ' The difference has reached the purchase level!!!! > 7%' + str()
                percent_str = str(pair).upper() + ' : The difference is now ' + str(
                    percent2) + '%' + '\nBinance rate: ' + str(last_trade_binance) + \
                              "\nYobit rate: " + str(last_trade) + "\n" + str(pair).upper() + " amount: " + str(
                    ltc_amount) + "\nYobit for 1000 , rate is " + str(yobit_1000)
                # #print((percent_str)
                # if percent2 < 7 or percent2 > 10:
                threading.Thread(target=send_msg, args=(percent_str,)).start()
                # send_msg(percent_str)
            # return percent_str
    # #print(("hello")
    for sp_data in data:
        pair = sp_data['name'].replace("USDT", "")
        #print((pair)
        for symbol, value in crypto_values.items():
            #print((f"{symbol}: {value}")
            if symbol in pair.upper():
                # pair = symbol.replace("USDT", "")
                pair_id = value
                last_trade_binance = float(sp_data['value'])
                #print((pair_id, last_trade_binance, pair)
                # ##print((pair_id)
                # if pair.upper() in sp_data['name']:
                buy_ords = get_yobit_list(pair, pair_id).json()
                lx = 1
                # #print((response.json())
                for i in range(len(buy_ords['buyord'])):
                    lx = lx + 1
                    if lx > 2:
                        continue
                    # ##print((response.json()['buyord'][i]['p'], response.json()['buyord'][i]['a'])
                    # ##print((response.json()['buyord'][i]['p'], response.json()['buyord'][i]['a'])
                    last_trade = float(buy_ords['buyord'][i]['p'])
                    ltc_amount = float(buy_ords['buyord'][i]['a'])
                    # calculate the difference
                    # send the message to telegram

                    # считаем разницу

                    percent = ((last_trade - last_trade_binance) / last_trade_binance) * int(100)
                    #print((percent)
                    # percent = int(100) / (last_trade - last_trade_binance) / last_trade_binance * int(100000)
                    percent2 = round(percent, 4)
                    # ##print(('Difference between exchange rates in %', percent2)
                    # time.sleep(1)
                    binance_1000 = 1000 / last_trade_binance
                    yobit_1000 = binance_1000 * last_trade
                    # ##print((yobit_1000)
                    config = configparser.ConfigParser()
                    config.read('config.ini')
                    crypto_value = config.get('Section 1', str(pair))
                    crypto_amount = config.get('Section 3', str(pair) + "_a")

                    if yobit_1000 > int(crypto_value) and float(ltc_amount) > float(crypto_amount):
                        # percent_str = str(percent2) + ' The difference has reached the purchase level!!!! > 7%' + str()
                        percent_str = str(pair).upper() + ' : The difference is now ' + str(
                            percent2) + '%' + '\nBinance rate: ' + str(last_trade_binance) + \
                                      "\nYobit rate: " + str(last_trade) + "\n" + str(pair).upper() + " amount: " + str(
                            ltc_amount) + "\nYobit for 1000 , rate is " + str(yobit_1000)
                        #print((percent_str)
                        # if percent2 < 7 or percent2 > 10:
                        send_msg(percent_str)


def get_specific_crypto_price_ticker(crypto_name):
    url = os.environ.get("URL")

    response = requests.get(url)
    data = response.json()
    # #print((data)
    pair_id = 0
    pair = ''
    last_trade_binance = 0
    pair = crypto_name.upper()
    #print((pair)
    if pair == "USDT":
        pair_id = 7223
        buy_ords = get_yobit_list(pair, pair_id).json()
        # #print((response.json())
        for i in range(len(buy_ords['buyord'])):
            # ##print((response.json()['buyord'][i]['p'], response.json()['buyord'][i]['a'])
            # ##print((response.json()['buyord'][i]['p'], response.json()['buyord'][i]['a'])
            last_trade = float(buy_ords['buyord'][i]['p'])
            ltc_amount = float(buy_ords['buyord'][i]['a'])
            # calculate the difference
            # send the message to telegram

            # считаем разницу
            last_trade_binance = 1

            percent = ((last_trade - last_trade_binance) / last_trade_binance) * int(100)
            #print((percent)
            # percent = int(100) / (last_trade - last_trade_binance) / last_trade_binance * int(100000)
            percent2 = round(percent, 4)
            # ##print(('Difference between exchange rates in %', percent2)
            # time.sleep(1)
            binance_1000 = 1000 / last_trade_binance
            yobit_1000 = binance_1000 * last_trade
            # ##print((yobit_1000)
            # config = configparser.ConfigParser()
            # config.read('config.ini')
            # crypto_value = config.get('Section 1', str(pair))
            # crypto_amount = config.get('Section 3', str(pair) + "_a")

            # if yobit_1000 > int(crypto_value) and float(ltc_amount) > float(crypto_amount):
                # percent_str = str(percent2) + ' The difference has reached the purchase level!!!! > 7%' + str()
            percent_str = str(pair).upper() + ' : The difference is now ' + str(
                percent2) + '%' + '\nBinance rate: ' + str(last_trade_binance) + \
                          "\nYobit rate: " + str(last_trade) + "\n" + str(pair).upper() + " amount: " + str(
                ltc_amount) + "\nYobit for 1000 , rate is " + str(yobit_1000)
            # #print((percent_str)
            # if percent2 < 7 or percent2 > 10:
            # send_msg(percent_str)
            return percent_str
    for sp_data in data:
        # pair = sp_data['name'].replace("USDT", "")


        for symbol, value in crypto_values.items():
            if symbol == pair.upper() and pair.upper() in sp_data['name'].replace("USD", ""):
                #print((sp_data['name'], sp_data['value'])
                #print((f"{symbol}: {value}")
                # pair = symbol.replace("USDT", "")
                pair_id = value
                last_trade_binance = float(sp_data['value'])
                #print((pair_id, last_trade_binance, pair)
                # ##print((pair_id)
                # if pair.upper() in sp_data['name']:
                buy_ords = get_yobit_list(pair, pair_id).json()
                # #print((response.json())
                for i in range(len(buy_ords['buyord'])):
                    # ##print((response.json()['buyord'][i]['p'], response.json()['buyord'][i]['a'])
                    # ##print((response.json()['buyord'][i]['p'], response.json()['buyord'][i]['a'])
                    last_trade = float(buy_ords['buyord'][i]['p'])
                    ltc_amount = float(buy_ords['buyord'][i]['a'])
                    # calculate the difference
                    # send the message to telegram

                    # считаем разницу

                    percent = ((last_trade - last_trade_binance) / last_trade_binance) * int(100)
                    #print((percent)
                    # percent = int(100) / (last_trade - last_trade_binance) / last_trade_binance * int(100000)
                    percent2 = round(percent, 4)
                    # ##print(('Difference between exchange rates in %', percent2)
                    # time.sleep(1)
                    binance_1000 = 1000 / last_trade_binance
                    yobit_1000 = binance_1000 * last_trade
                    # ##print((yobit_1000)
                    # config = configparser.ConfigParser()
                    # config.read('config.ini')
                    # crypto_value = config.get('Section 1', str(pair))
                    # crypto_amount = config.get('Section 3', str(pair) + "_a")

                    # if yobit_1000 > int(crypto_value) and float(ltc_amount) > float(crypto_amount):
                        # percent_str = str(percent2) + ' The difference has reached the purchase level!!!! > 7%' + str()
                    percent_str = str(pair).upper() + ' : The difference is now ' + str(
                        percent2) + '%' + '\nBinance rate: ' + str(last_trade_binance) + \
                                  "\nYobit rate: " + str(last_trade) + "\n" + str(pair).upper() + " amount: " + str(
                        ltc_amount) + "\nYobit for 1000 , rate is " + str(yobit_1000)
                    # #print((percent_str)
                    # if percent2 < 7 or percent2 > 10:
                    # send_msg(percent_str)
                    return percent_str


def all_time_running():
    while True:
        try:
            get_binance_price_ticker2()
        except Exception as e:
            #print(("maybe webserver is down")
            pass
        time.sleep(30)

threading.Thread(target=all_time_running).start()

TOKEN = os.environ.get("TOKEN")

bot = telebot.TeleBot(TOKEN)


LTC = 50004
DOGE = 50007
TRX = 6377
USDT = 7223
ETH = 50010
BTC = 50001
XRP = 8021
MATIC = 8297
LINK = 7835
# 1inch
BUSD = 10355
BNB = 40001

def default_config(defaul_value):
    config = configparser.ConfigParser()
    # config.read('config.ini')
    val = defaul_value
    config['Section 1'] = {
        'ltc': str(val),
        'doge': str(val),
        'trx': str(val),
        'usdt': str(val),
        'eth': str(val),
        'btc': str(val),
        'xrp': str(val),
        'matic': str(val),
        'link': str(val),
        'busd': str(val),
        'bnb': str(val),
        'all': str(val)
    }
    config['Section 2'] = {
        'value_to_change': 'new_value',
        'amount_to_change': 'new_value'
    }
    config['Section 3'] = {
        'ltc_a': '0',
        'doge_a': '0',
        'trx_a': '0',
        'usdt_a': '0',
        'eth_a': '0',
        'btc_a': '0',
        'xrp_a': '0',
        'matic_a': '0',
        'link_a': '0',
        'busd_a': '0',
        'bnb_a': '0',
        'all_a': '0'
    }

    # config.set('Section 2', 'value_to_change', "link")
    # config.set('Section 2', 'value_to_change', "link")
    # with open('config.ini', 'w') as configfile:
    #     config.write(configfile)
    with open("config.ini", 'w') as configfile:
        config.write(configfile)


# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup(row_width=2)
#     ltc = types.KeyboardButton('LTC')
#     doge = types.KeyboardButton('DOGE')
#     trx = types.KeyboardButton('TRX')
#     usdt = types.KeyboardButton('USDT')
#     eth = types.KeyboardButton('ETH')
#     btc = types.KeyboardButton('BTC')
#     xrp = types.KeyboardButton('XRP')
#     matic = types.KeyboardButton('MATIC')
#     link = types.KeyboardButton('LINK')
#     busd = types.KeyboardButton('BUSD')
#     bnb = types.KeyboardButton('BNB')
#     markup.add(ltc, doge, trx, usdt, eth, btc, xrp, matic, link, busd, bnb)
#     # item2 = types.KeyboardButton('Option 2')
#     # item3 = types.KeyboardButton('Option 3')
#     # markup.add(item1, item2, item3)
#     bot.send_message(message.chat.id, "Choose options:", reply_markup=markup)

# @bot.message_handler(func=lambda message: True)
# def handle_message(message):
#     if message.text == 'Option 1':
#         bot.send_message(message.chat.id, "You selected Option 1")
#     elif message.text == 'Option 2':
#         bot.send_message(message.chat.id, "You selected Option 2")
#     elif message.text == 'Option 3':
#         bot.send_message(message.chat.id, "You selected Option 3")
def is_float(string):
    try:
        # float() is a built-in function
        float(string)
        return True
    except ValueError:
        return False
def is_integer(string):
    return string.isdigit()
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    config = configparser.ConfigParser()
    config.read('config.ini')
    if message.text == "/start":
        markup = types.InlineKeyboardMarkup()
        calc = types.InlineKeyboardButton(text='Change calculation(1000)?', callback_data="calc")
        amount = types.InlineKeyboardButton(text='Change amount for crypto?', callback_data="amount")
        pair_price = types.InlineKeyboardButton(text='Check pair price', callback_data="pair_price")
        markup.add(calc)
        markup.add(amount)
        markup.add(pair_price)
        bot.send_message(message.chat.id, "Choose Options:", reply_markup=markup)
    if "/a" in message.text:
        amount_to_change = config.get('Section 2', 'amount_to_change')
        if amount_to_change == "":
            bot.send_message(message.chat.id, "Crypto not selected. Please click /start to select")
        else:
            amount_arr = message.text.split(" ")
            if len(amount_arr) > 1:
                if is_float(amount_arr[1]):
                    amount = amount_arr[1]
                    if amount_to_change == "all_a":
                        val = amount
                        config.set('Section 3', 'ltc_a', str(val))
                        config.set('Section 3', 'doge_a', str(val))
                        config.set('Section 3', 'trx_a', str(val))
                        config.set('Section 3', 'usdt_a', str(val))
                        config.set('Section 3', 'eth_a', str(val))
                        config.set('Section 3', 'btc_a', str(val))
                        config.set('Section 3', 'xrp_a', str(val))
                        config.set('Section 3', 'matic_a', str(val))
                        config.set('Section 3', 'link_a', str(val))
                        config.set('Section 3', 'busd_a', str(val))
                        config.set('Section 3', 'bnb_a', str(val))
                        config.set('Section 3', 'all_a', str(val))
                    else:
                        config.set('Section 3', amount_to_change, str(amount))
                    config.set('Section 2', 'value_to_change', '')
                    config.set('Section 2', 'amount_to_change', '')
                    with open('config.ini', 'w') as configfile:
                        config.write(configfile)
                    bot.send_message(message.chat.id, amount_to_change.replace("_a", "").upper() + " amount has been changed to " + str(amount))
    if is_integer(message.text):
        amount_to_change = config.get('Section 2', 'value_to_change')

        if amount_to_change == "":
            bot.send_message(message.chat.id, "Crypto not selected. Please click /start to select")
        else:
            if int(message.text) < 1000:
                bot.send_message(message.chat.id, "Enter value more than 1000")
            else:
                crypto_to_change_value = config.get('Section 2', 'value_to_change')
                if crypto_to_change_value == 'all':
                    val = message.text
                    config.set('Section 1', 'ltc', str(val))
                    config.set('Section 1', 'doge', str(val))
                    config.set('Section 1', 'trx', str(val))
                    config.set('Section 1', 'usdt', str(val))
                    config.set('Section 1', 'eth', str(val))
                    config.set('Section 1', 'btc', str(val))
                    config.set('Section 1', 'xrp', str(val))
                    config.set('Section 1', 'matic', str(val))
                    config.set('Section 1', 'link', str(val))
                    config.set('Section 1', 'busd', str(val))
                    config.set('Section 1', 'bnb', str(val))
                    config.set('Section 1', 'all', str(val))
                else:
                    config.set('Section 1', crypto_to_change_value, message.text)
                config.set('Section 2', 'value_to_change', '')
                config.set('Section 2', 'amount_to_change', '')
                with open('config.ini', 'w') as configfile:
                    config.write(configfile)
                bot.send_message(message.chat.id, crypto_to_change_value.upper() + " has been changed to " + str(message.text))
@bot.callback_query_handler(func=lambda call: True)
def beginning(call):
    config = configparser.ConfigParser()
    config.read('config.ini')
    if call.data == "calc":
        markup = types.InlineKeyboardMarkup()
        ltc = types.InlineKeyboardButton(text='LTC', callback_data="ltc")
        doge = types.InlineKeyboardButton(text='DOGE', callback_data="doge")
        trx = types.InlineKeyboardButton(text='TRX', callback_data="trx")
        usdt = types.InlineKeyboardButton(text='USDT', callback_data="usdt")
        eth = types.InlineKeyboardButton(text='ETH', callback_data="eth")
        btc = types.InlineKeyboardButton(text='BTC', callback_data="btc")
        xrp = types.InlineKeyboardButton(text='XRP', callback_data="xrp")
        matic = types.InlineKeyboardButton(text='MATIC', callback_data="matic")
        link = types.InlineKeyboardButton(text='LINK', callback_data="link")
        busd = types.InlineKeyboardButton(text='BUSD', callback_data="busd")
        bnb = types.InlineKeyboardButton(text='BNB', callback_data="bnb")
        all = types.InlineKeyboardButton(text='ALL', callback_data="all")
        check_all_values = types.InlineKeyboardButton(text='Check all values', callback_data="check_all_values")
        markup.add(check_all_values)
        markup.add(ltc)
        markup.add(doge)
        markup.add(trx)
        markup.add(usdt)
        markup.add(eth)
        markup.add(btc)
        markup.add(xrp)
        markup.add(matic)
        markup.add(link)
        markup.add(busd)
        markup.add(bnb)
        markup.add(all)
        # markup.add(ltc, doge, trx, usdt, eth, btc, xrp, matic, link, busd, bnb, all)
        bot.send_message(call.from_user.id, "Choose Crypto:", reply_markup=markup)
    if call.data == "amount":
        markup = types.InlineKeyboardMarkup()
        ltc = types.InlineKeyboardButton(text='LTC', callback_data="ltc_a")
        doge = types.InlineKeyboardButton(text='DOGE', callback_data="doge_a")
        trx = types.InlineKeyboardButton(text='TRX', callback_data="trx_a")
        usdt = types.InlineKeyboardButton(text='USDT', callback_data="usdt_a")
        eth = types.InlineKeyboardButton(text='ETH', callback_data="eth_a")
        btc = types.InlineKeyboardButton(text='BTC', callback_data="btc_a")
        xrp = types.InlineKeyboardButton(text='XRP', callback_data="xrp_a")
        matic = types.InlineKeyboardButton(text='MATIC', callback_data="matic_a")
        link = types.InlineKeyboardButton(text='LINK', callback_data="link_a")
        busd = types.InlineKeyboardButton(text='BUSD', callback_data="busd_a")
        bnb = types.InlineKeyboardButton(text='BNB', callback_data="bnb_a")
        all = types.InlineKeyboardButton(text='ALL', callback_data="all_a")
        check_all_values = types.InlineKeyboardButton(text='Check all values', callback_data="check_all_values_a")
        markup.add(check_all_values)
        markup.add(ltc)
        markup.add(doge)
        markup.add(trx)
        markup.add(usdt)
        markup.add(eth)
        markup.add(btc)
        markup.add(xrp)
        markup.add(matic)
        markup.add(link)
        markup.add(busd)
        markup.add(bnb)
        markup.add(all)
        # markup.add(ltc, doge, trx, usdt, eth, btc, xrp, matic, link, busd, bnb, all)
        bot.send_message(call.from_user.id, "Choose Crypto:", reply_markup=markup)

    if call.data == "pair_price":
        markup = types.InlineKeyboardMarkup()
        ltc = types.InlineKeyboardButton(text='LTC', callback_data="ltc_price")
        doge = types.InlineKeyboardButton(text='DOGE', callback_data="doge_price")
        trx = types.InlineKeyboardButton(text='TRX', callback_data="trx_price")
        usdt = types.InlineKeyboardButton(text='USDT', callback_data="usdt_price")
        eth = types.InlineKeyboardButton(text='ETH', callback_data="eth_price")
        btc = types.InlineKeyboardButton(text='BTC', callback_data="btc_price")
        xrp = types.InlineKeyboardButton(text='XRP', callback_data="xrp_price")
        matic = types.InlineKeyboardButton(text='MATIC', callback_data="matic_price")
        link = types.InlineKeyboardButton(text='LINK', callback_data="link_price")
        busd = types.InlineKeyboardButton(text='BUSD', callback_data="busd_price")
        bnb = types.InlineKeyboardButton(text='BNB', callback_data="bnb_price")
        # all = types.InlineKeyboardButton(text='ALL', callback_data="all")
        # check_all_values = types.InlineKeyboardButton(text='Check all values', callback_data="check_all_values")
        # markup.add(check_all_values)
        markup.add(ltc)
        markup.add(doge)
        markup.add(trx)
        markup.add(usdt)
        markup.add(eth)
        markup.add(btc)
        markup.add(xrp)
        markup.add(matic)
        markup.add(link)
        markup.add(busd)
        markup.add(bnb)
        # markup.add(all)
        # markup.add(ltc, doge, trx, usdt, eth, btc, xrp, matic, link, busd, bnb, all)
        bot.send_message(call.from_user.id, "Get price:", reply_markup=markup)

    if "_price" in call.data:
        pair_name = call.data.split("_")[0]
        #print((pair_name)
        # messs
        percent_str = get_specific_crypto_price_ticker(pair_name)
        bot.send_message(call.from_user.id, percent_str)


    if call.data == "check_all_values":
        for section in config.sections():
            # Loop through all options in each section
            if section == 'Section 1':
                for key, value in config.items(section):
                    # #print((f"{key} = {value}")
                    bot.send_message(call.from_user.id, str(key).upper() + " = " + str(value))
    if call.data == "check_all_values_a":
        for section in config.sections():
            # Loop through all options in each section
            if section == 'Section 3':
                for key, value in config.items(section):
                    # #print((f"{key} = {value}")
                    bot.send_message(call.from_user.id, str(key).replace("_a", "").upper() + " = " + str(value))
    if call.data == "no":
        config.set('Section 2', 'value_to_change', '')
        config.set('Section 2', 'amount_to_change', '')
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
        bot.send_message(call.from_user.id, "Aborted!")


    if call.data == "ALL":
        markup = types.InlineKeyboardMarkup()
        # ltc_change = types.KeyboardButton('Want to change default value?')
        ltc_change = types.InlineKeyboardButton(text='Yes', callback_data='Want to change all')
        no_button = types.InlineKeyboardButton(text='No', callback_data='no')
        markup.add(ltc_change)
        markup.add(no_button)
        # markup.add(ltc_change)
        value = config.get('Section 1', 'all')
        bot.send_message(call.from_user.id, "Default is set to: " + str(value) + '\nWant to change default value?', reply_markup=markup)



    # Loop through all sections
    for section in config.sections():
        # Loop through all options in each section
        for key, value in config.items(section):
            # #print((f"Key: {key}, Value: {value}")
            if call.data == key:
                # config = configparser.ConfigParser()
                # config.read('config.ini')
                # ltc_value = config.get('Section 1', 'LTC')
                markup = types.InlineKeyboardMarkup()
                ltc_change = types.InlineKeyboardButton(text='Yes', callback_data='Want to change ' + str(key))
                no_button = types.InlineKeyboardButton(text='No', callback_data='no')
                markup.add(ltc_change)
                markup.add(no_button)
                if "_a" in key:
                    bot.send_message(call.from_user.id, str(key).replace("_a", "").upper() +" is set to: " + str(value) + '\nWant to change ' + str(key).replace("_a", "").upper() + ' value?', reply_markup=markup)
                else:
                    bot.send_message(call.from_user.id, str(key).upper() +" is set to: " + str(value) + '\nWant to change ' + str(key).upper() + ' value?', reply_markup=markup)

    if "Want to change " in call.data:
        crypto_name = call.data.split(" ")[3]
        if "_a" in crypto_name:
            config.set('Section 2', 'amount_to_change', crypto_name)
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
            bot.send_message(call.from_user.id, "Enter new amount value for " + crypto_name.replace("_a", "").upper() + "(format: /a 40):")
        else:
            config.set('Section 2', 'value_to_change', crypto_name)
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
            bot.send_message(call.from_user.id, "Enter new value for " + crypto_name.upper() + " :")





bot.polling(none_stop=True, interval=0)
