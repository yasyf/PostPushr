import os, pymongo, sendgrid, lob, stripe, bitly_api

bin_dir = os.environ['bin_dir']
lob.api_key = os.environ['lob_api_key']
s = sendgrid.Sendgrid(os.environ['s_user'], os.environ['s_pass'], secure=True)
stripe.api_key = os.environ['stripe_sk']
client = pymongo.MongoClient(os.environ['db'])
db = client.postpushr
users = db.users
letters = db.letters
postcards = db.postcards
gcode_cache = db.gcode_cache
bitly = bitly_api.Connection(access_token=os.environ['BITLY_ACCESS_TOKEN'])


def ucfirst(txt):
	return ' '.join([x[:1].upper()+x[1:].lower() for x in txt.split(' ')])