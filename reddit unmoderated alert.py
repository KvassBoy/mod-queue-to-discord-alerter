# Please use this script properly. This script is only intended to be used as a utility for moderation. Feel free to modifiy the script to better suit your needs. 
import praw
import requests
import time


# Initialize Reddit
 reddit = praw.Reddit(
    client_id='CLIENT_ID HERE',
    client_secret='CLIENT-SECRET HERE',
    username='USERNAME HERE',
    password='PASSWORD HERE',
    user_agent='Reddit Unmoderated Post Alert Bot (by /u/python_child)'
)

print("Successfully logged in to Reddit")

# Define your subreddits, Discord Webhook URLs and roles
subreddits_discord_data = {
    'minecraft_survival': {
        'webhook_url': 'ADD WEBOOK HERE',
        'role_id': 'ADD ROLE ID HERE'
    }
}

def send_discord_alert(post, webhook_url, role_id):
    data = {
        "content": f"<@&{role_id}> Post '{post.title}' has been unmoderated for 2 hours or more. Link: {post.url}"
    }
    result = requests.post(webhook_url, json=data)
    if result.status_code == 204:
        print(f"Alert sent to Discord for post: {post.title}")
    else:
        print(f"Failed to send alert to Discord for post: {post.title}")

while True:
    for subreddit_name, discord_data in subreddits_discord_data.items():
        subreddit = reddit.subreddit(subreddit_name)
        for post in subreddit.mod.unmoderated(limit=None):
            print(f"Found post: {post.title}")
            post_age_in_hours = (time.time() - post.created_utc) / 3600
            if post_age_in_hours >= 2: #YOU CAN ADJUST THE TIME HERE
                send_discord_alert(post, discord_data['webhook_url'], discord_data['role_id'])
    time.sleep(3600)  # Sleep for an hour before checking again