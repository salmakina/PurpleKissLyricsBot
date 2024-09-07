import os
import random
import time
from albums import all_lyrics
import tweepy
from dotenv import load_dotenv

#see where script is running from
print("Current Directory: ", os.getcwd())

#load .env file
load_dotenv(dotenv_path='path/to/your/keys.env')

#check if loaded
print(f"API_KEY: {os.getenv('API_KEY')}")

access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')
bearer_token = os.getenv('BEARER_TOKEN')

client = tweepy.Client(bearer_token, api_key, api_secret, access_token,
                       access_token_secret)

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token,
                                access_token_secret)
api = tweepy.API(auth)

used_choices = set()
tweets_count = 0
clear_interval = 10  #clear the set every 10 tweets

while True:
    chosen_song = random.choice(all_lyrics)
    tweet_choice = chosen_song

    #check if the lyric has been used before to avoid duplicates
    while tweet_choice in used_choices:
      tweet_choice = chosen_song

    #tweet the chosen lyric
    client.create_tweet(text=tweet_choice)

    #add the chosen lyric to the set of used choices
    used_choices.add(tweet_choice)

    tweets_count += 1

    if tweets_count >= clear_interval:
      #clear the set after a 10 tweets
      used_choices.clear()
      tweets_count = 0

    print("tweeted at: ", time.strftime("%Y-%m-%d %H:%M:%S"))
    print(tweet_choice)
    time.sleep(7200)  #sleep for 1 hour

