#!/usr/bin/python3.6
import time
import tweepy
import datetime
from crypto import Crypto

poll = 1800 # 1/2 hour

#https://apps.twitter.com/app
consumerKey = ""
consumerSecret = ""
accessToken = ""
accessTokenSecret = ""


class Twitter:
	'''Twitter integration'''
	def __init__(self, apiKey, apiSecret, token, tokenSecret):
		self.apiKey = apiKey
		self.apiSecret = apiSecret
		self.token = token
		self.tokenSecret = tokenSecret

	def authenticate(self):
		global api
		auth = tweepy.auth.OAuthHandler(self.apiKey, self.apiSecret)
		auth.set_access_token(self.token, self.tokenSecret)
		api = tweepy.API(auth)

	def tweet(self, message):
		api.update_status(status=message)

if __name__ == '__main__':
	crypto_twitter = Twitter(consumerKey, consumerSecret, accessToken, accessTokenSecret) #twitter auth instance
	crypto_twitter.authenticate()
	crypto_fetch = Crypto()
	while 1:
		try:
			btc_eth_tuple = crypto_fetch.get_exchange()
			crypto_twitter.tweet(f'{datetime.datetime.now()}\nBTC: ${btc_eth_tuple[0]} USD\nETH: ${btc_eth_tuple[1]} USD')
			# Log tweet for my view
			print(f'{datetime.datetime.now()} :: BTC: {btc_eth_tuple[0]} && ETH: {btc_eth_tuple[1]}')
		except:
			continue

		# Sleep until time to tweet again
		time.sleep(poll)
