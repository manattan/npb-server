import twitter
import config

oauth = twitter.OAuth(config.APIKEY,config.APIKEYSECRET, config.ACCESSTOKEN, config.ACCESSTOKENSECRET)

twitter_api = twitter.Twitter(auth=oauth)
twitter_stream = twitter.TwitterStream(auth=oauth)