from pymongo import MongoClient

def get_mongo_client():
	"""
		Get MongoClient client.
	"""
	client = MongoClient(port=27017)
	return client
	