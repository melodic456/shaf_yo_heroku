import configparser
import json
import requests
import asyncio
# from  aiogram import Bot, Dispatcher, executor,types
import time
# bot = Bot(token='5555491875:AAH-aKzegGa2ZGnKrnbvllac-tRueXQPzMI')
# dp = Dispatcher(bot)
from bs4 import BeautifulSoup
from random import randint, uniform, shuffle, choice
from fake_headers import Headers
import telebot
from telebot import types
from threading import Thread
# def pair_checks()
# import requests
# from telethon.sync import TelegramClient
from fake_useragent import UserAgent
# api_id = 'YOUR_API_ID'
# api_hash = 'YOUR_API_HASH'
# bot_token = 'YOUR_BOT_TOKEN'
API_ID = "22408723"
API_HASH = "9eef29e4b9d0d8cd9dd450812572cb8d"
BOT_TOKEN = "6615226579:AAGi0iUt-b2al7Gk-1kbQr9Mpd9Zvhun4dE"


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
def get_proxy_list():
    soup = BeautifulSoup(requests.get("https://proxylist.to/http/").text, features="lxml")
    # first we should find our table object:
    table = soup.find('table', class_="proxytable")
    # then we can iterate through each row and extract either header or row values:
    header = []
    rows = []
    for i, row in enumerate(table.find_all('tr')):
        if i == 0:
            header = [el.text.strip() for el in row.find_all('th')]
        else:
            rows.append([el.text.strip() for el in row.find_all('td')])

    proxies_list = list()
    for row in rows:
        # print(row[1], row[2])
        proxy = row[1] + ":" + row[2]
        proxies_list.append(proxy)
    shuffle(proxies_list)
    return proxies_list
    # print(proxies_list)


def Get_Valid_Proxy(proxies_list):
    header = Headers(
        headers=False
    ).generate()
    agent = header['User-Agent']

    headers = {
        'User-Agent': f'{agent}',
    }

    url = 'http://icanhazip.com'
    while (True):
        proxy = choice(proxies_list)
        proxies = {
            'http': f'http://{proxy}',
            'https': f'http://{proxy}',
        }
        try:
            response = requests.get(url, headers=headers, proxies=proxies, timeout=1)
            if (response.status_code == 200):
                return proxy
        except:
            continue


def Generate_Proxy():
    # proxies_list = []
    # with open("proxies.txt", "r") as f:
    #     for line in f:
    #         proxies_list.append(line.split("\n")[0])

    # proxies_list = Fetch_Proxies()
    proxies_list = get_proxy_list()

    proxy = Get_Valid_Proxy(proxies_list)
    print(proxy)
    return proxy

def send_msg(text):
    # token = "5555491875:AAH-aKzegGa2ZGnKrnbvllac-tRueXQPzMI"
    # token = "6100354506:AAESTtpgg1-OwF8VYNiMbUwcHXHCQEh-lOs"
    token = "6517055263:AAHojUJLP5O6oQ2lyz_IL9Vk1vKiR_rzcTc"
    chat_id = "5631242663"
    chat_id2 = "715039642"

    token = "7467031593:AAESLgzJCQb2HNetjRGFLz9yt7ZQlCETeUk"
    chat_id="7374728124"
    chat_id2="823974983794"

    print(text)
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    url_req2 = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id2 + "&text=" + text
    results = requests.get(url_req)
    # print(results.json())
    results2 = requests.get(url_req2)
    # print(results2.json())
# global data
# data = ''

def get_binance_price_ticker(pair):
    # try:
    #     proxy = Generate_Proxy()
    #     # proxy = "38.62.220.57:1337"
    #     PROXY_HOST = proxy.split(":")[0]
    #     PROXY_PORT = proxy.split(":")[1]
    #     proxy = {
    #         'http': 'http://' + proxy,
    #         'https': 'http://' + proxy,
    #     }
    #     key = "https://api.binance.com/api/v3/ticker/price?symbol=" + str(pair).upper() + "USDT"
    #     # global data
    #     data = requests.get(key, proxies=proxy, timeout=1)
    #     return data
    # except Exception as e:
    #     print(e)
    #     return ''
    proxy = "38.242.203.135:3128"
    proxy = {
        'http': 'http://' + proxy,
        'https': 'http://' + proxy,
    }
    key = "https://api.binance.com/api/v3/ticker/price?symbol=" + str(pair).upper() + "USDT"
    # global data
    # data = requests.get(key, proxies=proxy, headers={'User-Agent': UserAgent().random}, timeout=1)
    data = requests.get(key, headers={'User-Agent': UserAgent().random}, timeout=1)
    return data



def get_binance_price_ticker2(pair):
    url = "http://localhost:3000/api/data"

    response = requests.get(url)
    data = response.json()
    print(data)
    for sp_data in data:
        if pair.upper() in sp_data['name']:

            return sp_data['value']


def get_prices_for_pair(pair, pair_id):
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



    #

    try:
        # proxy = Generate_Proxy()
        # # proxy = "38.62.220.57:1337"
        # PROXY_HOST = proxy.split(":")[0]
        # PROXY_PORT = proxy.split(":")[1]
        # proxy = {
        #     'http': 'http://' + proxy,
        #     'https': 'http://' + proxy,
        # }
        # # key = "https://api.binance.com/api/v3/ticker/price?symbol=" + str(pair).upper() + "USDT"
        # data = requests.get(key, proxies=proxy)
        # global data
        # data = get_binance_price_ticker(pair)
        # while data == '':
        #     # pass
        #     data = get_binance_price_ticker(pair)
        #     time.sleep(5)
        # data = data.json()
        # # last_trade_binance = float(0)
        # # with TelegramClient('session_name', API_ID, API_HASH) as client:
        # #     # Replace 'bot_username' with the actual username of the bot
        # #     entity = client.get_entity('@Cryptowhalebot')
        # z = data['price']
        # z = get_binance_price_ticker2(pair)
        z = get_binance_price_ticker2(pair)
        # # last_trade_binance = round(float(z))
        last_trade_binance = float(z)
        print(str(pair) + " " + str(last_trade_binance))
        # print(f"{data['symbol']} Binance цена: {data['price']}")

        # key2 = "https://yobit.net/api/3/ticker/ltc_usd"
        # data = requests.get(key2)
        # data = data.json()
        # b = data['ltc_usd']
        # # last_trade = int(round(b['last']))
        # last_trade = round(float(b['last']))
        # last_trade = float(b['last'])
        # print(f"LTCRUB Yobit цена: {last_trade}")
        # get the list of p and ac


        response = requests.post('https://yobit.net/ajax/system_status_data.php', cookies=cookies, headers=headers,
                                 data=datas)
        # print(response.json())
        for i in range(len(response.json()['buyord'])):
            # print(response.json()['buyord'][i]['p'], response.json()['buyord'][i]['a'])
            # print(response.json()['buyord'][i]['p'], response.json()['buyord'][i]['a'])
            last_trade = float(response.json()['buyord'][i]['p'])
            ltc_amount = float(response.json()['buyord'][i]['a'])
        # calculate the difference
        # send the message to telegram

        # считаем разницу

            percent = ((last_trade - last_trade_binance) / last_trade_binance ) * int(100)
            # percent = int(100) / (last_trade - last_trade_binance) / last_trade_binance * int(100000)
            percent2 = round(percent, 4)
            # print('Difference between exchange rates in %', percent2)
            time.sleep(1)
            binance_1000 = 1000 / last_trade_binance
            yobit_1000 = binance_1000 * last_trade
            # print(yobit_1000)
            config = configparser.ConfigParser()
            config.read('config.ini')
            crypto_value = config.get('Section 1', str(pair))
            crypto_amount = config.get('Section 3', str(pair) + "_a")

            if yobit_1000 > int(crypto_value) and float(ltc_amount) > float(crypto_amount):
            # percent_str = str(percent2) + ' The difference has reached the purchase level!!!! > 7%' + str()
                percent_str = str(pair).upper() + ' : The difference is now ' + str(percent2) + '%' + '\nBinance rate: ' + str(last_trade_binance) +\
                              "\nYobit rate: " + str(last_trade) + "\n" + str(pair).upper() + " amount: " + str(ltc_amount) + "\nYobit for 1000 , rate is " + str(yobit_1000)
            # if percent2 < 7 or percent2 > 10:
                send_msg(percent_str)

            # else:
            #     print('The difference in rates is less than 7 or more than 10')


        # теперь отправляем наш % разница в телегу если разница курсов дошла до требуемого значения



        # if percent2 < 7 or percent2 > 10:
        #     send_msg(percent_str)
        #
        # else:
        #     print('The difference in rates is less than 7 or more than 10')
        time.sleep(60)
    except Exception as e:
        print(e)
        time.sleep(30)


def start_main_thread_for_prices():
    while True:
        Thread(target=get_prices_for_pair, args=('ltc', LTC)).start()
        Thread(target=get_prices_for_pair, args=('doge', DOGE)).start()
        Thread(target=get_prices_for_pair, args=('trx', TRX)).start()
        Thread(target=get_prices_for_pair, args=('usdt', USDT)).start()
        Thread(target=get_prices_for_pair, args=('eth', ETH)).start()
        Thread(target=get_prices_for_pair, args=('btc', BTC)).start()
        Thread(target=get_prices_for_pair, args=('xrp', XRP)).start()
        Thread(target=get_prices_for_pair, args=('matic', MATIC)).start()
        Thread(target=get_prices_for_pair, args=('link', LINK)).start()
        Thread(target=get_prices_for_pair, args=('busd', BUSD)).start()
        Thread(target=get_prices_for_pair, args=('bnb', BNB)).start()
        time.sleep(30)


# Thread(target=start_main_thread_for_prices, args=()).start()
start_main_thread_for_prices()
