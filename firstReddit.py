import praw, requests, os

# If you don't want to have the variables stored in the 
reddit = praw.Reddit(
    client_id=os.environ['REDDIT_ID'],
    client_secret=os.environ['REDDIT_SECRET'],
    user_agent="<YOUR-USERNAME>",
    username="<YOUR-USERNAME>",
    password=os.environ['REDDIT_PWD']
)

accepted_contents = {'image/jpeg':'.jpg', 'image/png':'.png'}

# Change this to whatever folder you have for your lockscreen
FILEPATH = '../../../Pictures/LockScreen/'

# Use whatever reddit you want, I used r/Wallpaper
for submission in reddit.subreddit("Wallpaper").hot(limit=10):
	# Get the "picture"
	pic = requests.get(submission.url)
	# Check if the content type is a jpeg or png
	if pic.headers['Content-Type'] in accepted_contents.keys():
		# Save the image
		with open(FILEPATH + submission.title + accepted_contents[pic.headers['Content-Type']], 'wb') as f:
			f.write(pic.content)