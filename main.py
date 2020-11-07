from config import *
from utility import *
import os
import json
import pprint
import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
if(api.verify_credentials):
    print('Authentication completed succesfully!')



def getFollowers(account, path):
    followers_of_account = []

    for item in tweepy.Cursor(
            api.followers,
            screen_name=account,
            skip_status=True,
            include_user_entities=False
    ).items():

        json_data = item._json

        found_follower = {}
        found_follower["id"] = json_data["id"]
        found_follower["name"] = json_data["name"]
        found_follower["screen_name"] = json_data["screen_name"]
        found_follower["location"] = json_data["location"]
        if found_follower not in followers_of_account:
            followers_of_account.append(found_follower)
        print(f"Processing Follower {len(followers_of_account)} of account: {account}")

    serialize_json(data_folder, path, followers_of_account)

#getFollowers("mizzaro", "mizzaroFollowers.json")
#getFollowers("damiano10", "damiano10Followers.json")
#getFollowers("Miccighel_", "Miccighel_Followers.json")
#getFollowers("eglu81", "eglu81Followers.json")
getFollowers("KevinRoitero", "KevinRoiteroFollowers.json")
