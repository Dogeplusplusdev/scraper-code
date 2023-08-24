import Scweet
from Scweet.scweet import scrape
from Scweet.user import get_user_information, get_users_following, get_users_followers

env_path = ".env"

following = get_users_following(users=["@agencydev68"], env=env_path, verbose=0, headless=True, wait=2, limit=50, file_path=None)

#code pulled from: https://github.com/Altimis/Scweet/tree/master#tweets-