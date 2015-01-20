import praw

def run_bot(r):
	subreddit = r.get_subreddit("Turkey")
	comments = subreddit.get_comments(limit=25)
	for comment in comments:
		comment_body = comment.body.lower()
		print comment_body.encode('ascii', 'ignore')


if __name__ == "__main__":
	r = praw.Reddit(user_agent = "/u/Salyangoz's tutorial comment reader bot")
	with open("password.txt") as f:
		password = f.readline().strip('\n')
	r.login('herkes_bot', password)

	search_word = []
	run_bot(r)