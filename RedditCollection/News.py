#!/usr/bin/python3
import json
import praw




if __name__ == "__main__":

    reddit = praw.Reddit(client_id = '',
                         client_secret = '',
                         username = 'Miserable_Author',
                         password = '',
                         user_agent = 'RedditTest')

    subreddit = reddit.subreddit('news')

    for submission in subreddit.stream.submissions():
        try:
            JData = {}
            Title = submission.title
            Author = submission.author
            URL = submission.url
            JData['Title'] = Title
            #JData['Author'] = Author
            #JData['URL'] = URL
            json_data = json.dumps(JData)
            print(json_data)

        except Exception as e:
            print(str(e))
