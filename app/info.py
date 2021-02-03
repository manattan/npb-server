import twitter
import os
# import config

ACCESSTOKEN=os.getenv('ACCESSTOKEN')
print(ACCESSTOKEN)
ACCESSTOKENSECRET=os.getenv('ACCESSTOKENSECRET')
print(ACCESSTOKENSECRET)
APIKEY=os.getenv('APIKEY')
print(APIKEY)
APIKEYSECRET=os.getenv('APIKEYSECRET')
print(APIKEYSECRET)

oauth = twitter.OAuth(ACCESSTOKEN, ACCESSTOKENSECRET,APIKEY,APIKEYSECRET)

twitter_api = twitter.Twitter(auth=oauth)
twitter_stream = twitter.TwitterStream(auth=oauth)