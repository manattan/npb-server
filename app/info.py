import twitter
import os
from config import insertConfig

insertConfig()
print(os.environ)
ACCESSTOKEN=os.getenv('ACCESSTOKEN')
ACCESSTOKENSECRET=os.getenv('ACCESSTOKENSECRET')
APIKEY=os.getenv('APIKEY')
APIKEYSECRET=os.getenv('APIKEYSECRET')

oauth = twitter.OAuth(ACCESSTOKEN, ACCESSTOKENSECRET,APIKEY,APIKEYSECRET)

twitter_api = twitter.Twitter(auth=oauth)
twitter_stream = twitter.TwitterStream(auth=oauth)