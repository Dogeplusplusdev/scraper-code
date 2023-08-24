import tweepy
import requests

# Set up your API keys and tokens
API_KEY = ''
API_SECRET_KEY = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

# Replace with your Bearer Token
BEARER_TOKEN = ''

# Twitter API v1.1 endpoint URL
api_url = 'https://api.twitter.com/1.1/users/show.json?screen_name=@jaencarrodine'

# Set headers
headers = {
    'Authorization': f'Bearer {BEARER_TOKEN}'
}

# Make the API request
response = requests.get(api_url, headers=headers)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"API request failed with status code: {response.status_code}")

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

test_screen_name = '@agencydev68'
followers = []

#Getting a users description off of their screen name - should work
def getDesc(screen_name):
    user = api.get_user(screen_name=screen_name)
  
    # fetching the description
    description = user.description
  
    print("The description of the user is : " + description)

#getDesc(test_screen_name)
#followers doesnt work without paying elon your life savings
for follower in tweepy.Cursor(api.get_followers, screen_name=test_screen_name).items():
    followers.append(follower.screen_name)

# Print the list of followers
print("Followers of", test_screen_name, ":", followers)
