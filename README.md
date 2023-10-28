# mod-queue-to-discord-alerter
This bot will send a alert to your discord server when a post in your subreddit has been unmoderated for too long.

## Features
- You can adjust how old a post has to be before it sends an alert
- You can adjust what the alert says
- Easy and convenient 


## How do I set this up
Please make sure you setup a app at https://www.reddit.com/prefs/apps
Click "create app" and select "script"
Name it whatever
For redirect URL you can do "https://github.com/KvassBoy/mod-queue-to-discord-alerter" or choose a url of your choice. 

Once done, grab the client_id and client_secret and replace "CLIENT_ID HERE" with your client id and replace "CLIENT SECRET HERE' with your client_secret token

Put in the username and password of the reddit account you have made the client_id and client_secret on

Now go onto discord and create a webhook on your channel of your choosing. Grab the url link of the webhook and replace "ADD WEBHOOK HERE" on line 21 with your webhook

Now make or find a role you plan to have the bot ping to alert you of unmoderated posts
Grab the role ID and replace "ADD ROLE ID HERE" on line 22 with the role ID

Now for the final step, replace "ADD SUBREDDIT HERE' on line 20 with the subreddit of your choosing. Please make sure the bot does have proper permissions to view unmoderated queue.

Boom, run the script and enjoy


#How do i adjust how old a post can be before I get an alert
Go to line 42 and change 2 to another number
