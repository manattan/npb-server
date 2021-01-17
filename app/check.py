from app.info import twitter_stream
from app.tweet import Tweet

def start():
    tracking_text = '@manattan_me 背番号'
    print(tracking_text)
    for tweet in twitter_stream.statuses.filter(language='ja', track=tracking_text):
        print(tweet)
        tweet_obj = Tweet(tweet)

        print(tweet_obj)

        tweet_obj.reply()