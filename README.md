# Purple Kiss Lyrics Twitter Bot
## Description
This project is a Twitter bot made with python, which tweets a random song lyric from a pre-defined set of lines from Purple Kiss songs.
It uses the Tweepy library to interact with Twitter's API.
## Features
- Ensures that the same lyric is not tweeted twice in a row.
- Tweets are sent every two hours (but can be customized by adjusting the `time.sleep()` duration).
- Sensitive API keys and tokens are securely loaded from a `.env` file.
## Prerequisites
- Python 3.7 or higher
- A Twitter Developer Account (for API keys)
- A set of song lyrics (provided in `albums.py`)
## Customization
- Can modify the `albums.py` file to add, remove, or change the lyrics being tweeted.
- Change the `time.sleep(7200)` to adjust how often the bot tweets (e.g., 3600 for every hour).
