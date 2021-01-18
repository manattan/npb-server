import twitter
import config

oauth = twitter.OAuth(config.ACCESSTOKEN, config.ACCESSTOKENSECRET,config.APIKEY,config.APIKEYSECRET, )

twitter_api = twitter.Twitter(auth=oauth)
twitter_stream = twitter.TwitterStream(auth=oauth)