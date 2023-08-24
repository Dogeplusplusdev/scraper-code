import tweepy

# Add your Twitter API credentials here
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""


# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

def findTweetId(url):
    tweet_id = url.split("/")[-1]
    return tweet_id
# Replace with the desired tweet ID
tweet_url = "https://twitter.com/PsycheWizard/status/1693982801371320701"
findTweetId(tweet_url)
def getRetweets(tweet_id):
    # Fetch the tweet
    tweet = api.get_status(tweet_id)

    # Get users who retweeted the tweet
    retweets = api.retweets(tweet_id)
    
    print(f"Tweet: {tweet.text}\n")
    print("Users who retweeted:")
    for retweet in retweets:
        print(f"- {retweet.user.screen_name}")
    return retweets
getRetweets(findTweetId(tweet_url))
