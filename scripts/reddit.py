import praw

r = praw.Reddit(user_agent='my_cool_application')
submissions = list(r.get_subreddit('opensource').get_hot(limit=1))
for x in submissions: print x.title
