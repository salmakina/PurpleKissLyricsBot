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
## Installation
1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/purple-kiss-lyrics-bot.git
    cd purple-kiss-lyrics-bot
    ```

2. **Install the required packages**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up environment variables**: Create a file named `keys.env` in the root directory and add your Twitter API keys like so:

    ```plaintext
    ACCESS_TOKEN=your_access_token
    ACCESS_TOKEN_SECRET=your_access_token_secret
    API_KEY=your_api_key
    API_SECRET=your_api_secret
    BEARER_TOKEN=your_bearer_token
    ```

4. **Edit the script**: Update the following line in `main.py` to point to the location of your `.env` file:

    ```python
    load_dotenv(dotenv_path='C:/path/to/your/keys.env')
    ```

## Usage

Run the bot with:

```bash
python main.py
```

## Customization
- Can modify the `albums.py` file to add, remove, or change the lyrics being tweeted.
- Change the `time.sleep(7200)` to adjust how often the bot tweets (e.g., 3600 for every hour).
