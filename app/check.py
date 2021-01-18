from app.info import twitter_stream
from app.tweet import Tweet
from app.search import search

def start():
    tracking_text = '@manattan_me 背番号'
    print(tracking_text)
    for tweet in twitter_stream.statuses.filter(language='ja', track=tracking_text):
        tweet_obj = Tweet(tweet)

        text = tweet_obj.get_tweet_text().split()
        print(text)

        if len(text) < 2:
            tweet_obj.reply("'背番号 [数字] [teamのアルファベット]' と正しくリプライしてね.")
        else:
            res = search(text[2], text[3])
            if res == []:
                tweet_obj.reply('その背番号の選手がいないか, そもそもチームがないです')
            else:
                tweet_obj.reply(res)
