from app.info import twitter_stream
from app.tweet import Tweet

def start():
    tracking_text = '@manattan_me 背番号'
    print(tracking_text)
    for tweet in twitter_stream.statuses.filter(language='ja', track=tracking_text):
        print(tweet)
        tweet_obj = Tweet(tweet)

        text = tweet_obj.get_tweet_text().split()
        print(text)

        tweet_obj.reply(str(text))
