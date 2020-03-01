
import sys
import time
from tweepy import Stream
from tweepy.streaming import StreamListener
from twitter_auth_client import get_twitter_auth
from mongodb_connection import get_mongo_client
import json

class StreamLsitenerImp(StreamListener):
	""" Custom StreamListener from streaming Twitter data."""

	def __init__(self):
		pass

	def on_data(self, data):
		try:
			mongo_client = get_mongo_client()
			db=mongo_client.twitter
			tweet = json.loads(data)
			result = db.tweet.insert_one(tweet)
			print("inserted successfully")
		except BaseException as e:
			sys.stderr.write("Error on_data : {}\n".format(e))
			time.sleep(5)
		return True

	def on_error(self, status):
		if status == 420:
			sys.stderr.write("Rate limit exceeded\n")
			return False
		else:
			sys.stderr.write("Error {}\n".format(status))
			return True


if __name__ == '__main__':
	hashtag = sys.argv[1:]
	auth = get_twitter_auth()
	twitter_stream = Stream(auth, StreamLsitenerImp())
	twitter_stream.filter(track=hashtag, is_async=True)



