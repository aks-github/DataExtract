
import sys
import time
from tweepy import Stream
from tweepy.streaming import StreamListener
from twitter_auth_client import get_twitter_auth

class StreamLsitenerImp(StreamListener):
	""" Custom StreamListener from streaming Twitter data."""

	def __init__(self, filename):
		self.outfile = filename

	def on_data(self, data):
		try:
			with open(self.outfile, 'a') as f:
				f.write(data)
				return True
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
	filename = 'streaming_data.json'
	auth = get_twitter_auth()
	twitter_stream = Stream(auth, CustomLsitener(filename))
	twitter_stream.filter(track=hashtag, is_async=True)



