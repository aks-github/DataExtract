
import sys
import json
from tweepy import Cursor
from twitter_auth_client import get_twitter_client

if __name__ == '__main__':
	user = sys.argv[1]
	client = get_twitter_client()

	fname = "timeline_{}.json".format(user)

	with open(fname, 'w') as f:
		for page in Cursor(client.user_timeline, screen_name=user, count=2).pages(1):
			for status in page:
				f.write(json.dumps(status._json)+"\n")
