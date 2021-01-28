import twitter
import os
# import config

ACCESSTOKEN=os.environ['ACCESSTOKEN']
ACCESSTOKENSECRET=os.environ['ACCESSTOKENSECRET']
APIKEY=os.environ['APIKEY']
APIKEYSECRET=os.environ['APIKEYSECRET']

oauth = twitter.OAuth(ACCESSTOKEN, ACCESSTOKENSECRET,APIKEY,APIKEYSECRET)

twitter_api = twitter.Twitter(auth=oauth)
twitter_stream = twitter.TwitterStream(auth=oauth)