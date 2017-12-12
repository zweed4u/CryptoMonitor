#!/usr/bin/python3.6
import datetime
import requests


class Crypto:
	def __init__(self):
		self.session = requests.session()
		self.headers = {'CB-VERSION':datetime.datetime.now().strftime("%Y-%m-%d")}

	def get_exchange(self):
		if self.headers['CB-VERSION'] != datetime.datetime.now().strftime("%Y-%m-%d"):
			self.headers['CB-VERSION'] = datetime.datetime.now().strftime("%Y-%m-%d")
		btc_r = self.session.get('https://api.coinbase.com/v2/prices/BTC-USD/buy', headers=self.headers)
		eth_r = self.session.get('https://api.coinbase.com/v2/prices/ETH-USD/buy', headers=self.headers)
                ltc_r = self.session.get('https://api.coinbase.com/v2/prices/LTC-USD/buy', headers=self.headers)
		btc_price = btc_r.json()["data"]["amount"]
		eth_price = eth_r.json()["data"]["amount"]
		ltc_price = ltc_r.json()["data"]["amount"]
		return btc_price, eth_price, ltc_price

