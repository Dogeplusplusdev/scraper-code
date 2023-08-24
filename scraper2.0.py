import tweepy

# Replace with your API keys and access tokens
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

username = "mailamgc"
for follower in api.get_followers(screenname=username):
    print(follower.screen_name)