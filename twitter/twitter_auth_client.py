
from tweepy import API
from tweepy import OAuthHandler

ACCESS_TOKEN = "<Your ACCESS_TOKEN>"
ACCESS_TOKEN_SECRET = "<Your ACCESS_TOKEN_SECRET>"
CONSUMER_KEY = "<Your CONSUMER_KEY>"
CONSUMER_SECRET = "<Your CONSUMER_SECRET>"

def get_twitter_auth():
	"""
	Return: auth object
	"""
	auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
	return auth

def get_twitter_client():
	"""
	Return: tweepy.API object
	"""
	auth = get_twitter_auth
	client = API(auth)
	return client