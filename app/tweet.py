from app.info import twitter_api

class Tweet:
    def __init__(self, tweet):
        self.tweet = tweet
    
    def get_user_screenname(self):
        return self.tweet['user']['screen_name']
    
    def get_tweet_text(self):
        return self.tweet['text']
    
    def reply(self, text):
        status = '@' + self.get_user_screenname() + '\n'
        status += text
        return twitter_api.statuses.update(status=status, in_reply_to_status_id=self.tweet['id_str'])
    