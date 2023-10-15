import configparser
import json
import requests
import asyncio
# from  aiogram import Bot, Dispatcher, executor,types
import time
import os

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

def send_msg(text):
    token = os.environ.get("TOKEN")
    chat_id = os.environ.get("CHAT_ID_1")
    chat_id2 = os.environ.get("CHAT_ID_2")
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    url_req2 = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id2 + "&text=" + text
    results = requests.get(url_req)
    # #print(results.json())
    results2 = requests.get(url_req2)
    # #print(results2.json())
# global data


def get_binance_price_ticker2():
    url = os.environ.get("URL")

    response = requests.get(url)
    data = response.json()
    #print(data)
    pair_id = 0
    pair = ''
    last_trade_binance = 0
    for sp_data in data:
        pair = sp_data['name'].replace("USDT", "")
        print(pair)
        for symbol, value in crypto_values.items():
            print(f"{symbol}: {value}")
            if symbol == pair.upper():
                # pair = symbol.replace("USDT", "")
                pair_id = value
                last_trade_binance = float(sp_data['value'])
                print(pair_id, last_trade_binance, pair)
                # #print(pair_id)
                # if pair.upper() in sp_data['name']:
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

                response = requests.post('https://yobit.net/ajax/system_status_data.php', cookies=cookies, headers=headers,
                                         data=datas)
                # print(response.json())
                for i in range(len(response.json()['buyord'])):
                    # #print(response.json()['buyord'][i]['p'], response.json()['buyord'][i]['a'])
                    # #print(response.json()['buyord'][i]['p'], response.json()['buyord'][i]['a'])
                    last_trade = float(response.json()['buyord'][i]['p'])
                    ltc_amount = float(response.json()['buyord'][i]['a'])
                    # calculate the difference
                    # send the message to telegram

                    # считаем разницу

                    percent = ((last_trade - last_trade_binance) / last_trade_binance) * int(100)
                    print(percent)
                    # percent = int(100) / (last_trade - last_trade_binance) / last_trade_binance * int(100000)
                    percent2 = round(percent, 4)
                    # #print('Difference between exchange rates in %', percent2)
                    # time.sleep(1)
                    binance_1000 = 1000 / last_trade_binance
                    yobit_1000 = binance_1000 * last_trade
                    # #print(yobit_1000)
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
                        print(percent_str)
                        # if percent2 < 7 or percent2 > 10:
                        send_msg(percent_str)


while True:
    get_binance_price_ticker2()
    time.sleep(30)
