import requests
from requests_oauthlib import OAuth1Session

url = "https://api.twitter.com/1.1/statuses/retweets/:id.json"

# Replace with your actual keys and tokens
oauth = OAuth1Session("api-key", "api-token", "access-token", "access-secret")

#Works - really simple
def findTweetId(url):
    tweet_id = url.split("/")[-1]
    return tweet_id

tweet_id = findTweetId("https://twitter.com/PsycheWizard/status/1693982801371320701")

response = oauth.get(url.replace(":id", tweet_id))
retweets = response.json()
print(retweets)