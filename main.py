import os
import praw
import time
import random

# Load Reddit credentials from environment variables
client_id = os.getenv("REDDIT_CLIENT_ID")
client_secret = os.getenv("REDDIT_CLIENT_SECRET")
username = os.getenv("REDDIT_USERNAME")
password = os.getenv("REDDIT_PASSWORD")
user_agent = os.getenv("USER_AGENT", "CamTeaserBot by u/Camille_Kosten")

# Reddit login
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    username=username,
    password=password,
    user_agent=user_agent
)

# Subreddits to post in
subreddits = ["CamGirlProblems", "CamWhores", "OnlyFansPromotions", "NSFWsnapchat", "Nudes"]

# Parts for title generation
intros = [
    "Live right now", "On cam now", "I'm streaming", "Come watch me live", "Streaming now"
]

actions = [
    "come see what I do when you watch", "let's get naughty together", "join me for a wild time", "watch me play", "let's have fun together"
]

emojis = [
    "💦", "💋", "🔥", "😍", "😈", "👀", "🍑"
]

tags = [
    "[F] 🔞", "[NSFW]", "[18+]", "[CamGirl]", "[Sexy]", "[Adult Content]"
]

# Cam link
cam_link = "https://camillekosten.cammodels.com"

def generate_title():
    intro = random.choice(intros)
    action = random.choice(actions)
    emoji_1 = random.choice(emojis)
    emoji_2 = random.choice(emojis)
    tag = random.choice(tags)
    # Build the title
    title = f"{intro} {emoji_1} {action} {emoji_2} {tag}"
    return title

# Post every 2 to 3 hours
while True:
    try:
        subreddit = random.choice(subreddits)
        title = generate_title()
        reddit.subreddit(subreddit).submit(title, url=cam_link)
        print(f"Posted to r/{subreddit}: {title}")
        time.sleep(random.randint(7200, 10800))  # wait 2–3 hours
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(600)  # wait 10 mins and try again
