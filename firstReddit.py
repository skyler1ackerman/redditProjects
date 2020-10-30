import praw
import requests
import urllib
import os

reddit = praw.Reddit(
    client_id=os.environ['REDDIT_ID'],
    client_secret=os.environ['REDDIT_SECRET'],
    user_agent="aUCSDStud3nt",
    username="aUCSDStud3nt",
    password=os.environ['REDDIT_PWD']
)

FILEPATH = '../../../Pictures/LockScreen/'
for submission in reddit.subreddit("earthporn").hot(limit=20):
	if '.jpg' in submission.url:
		with open(FILEPATH + submission.title +'.jpg', 'wb') as f:
			pic = requests.get(submission.url)
			f.write(pic.content)