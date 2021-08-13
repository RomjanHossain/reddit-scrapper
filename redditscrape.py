import praw
import re
import requests
import pandas as pd
from datetime import datetime

# reddit secret
reddit = praw.Reddit(
    client_id="Dyfbqy1qmnl9ftYQ1_2QXw",
    client_secret="K04SPTL992GM1oEGTZ2tk2fH8riR0Q",
    user_agent='my user agent',
)

# name of the subreddit
subreddit = reddit.subreddit('unixporn')

# save those info to a csv file
riceListo = {
    'id': [],  # id 
    'title': [],  # title 
    'rice': [],  # media link
    'post link': [],  # post link
    'created': [],  # time when created
    'upvote ratio': [],  # upvote ratio
    'upvote': [],  # upvote
    'downvote': [],  # downvote
}


# save file
def saveFile(loc: str, name: str, content: bytes) -> None:
    try:
        with open(f'{loc}/{name}', 'wb') as f:
            print('\t\twritting...............-> ', end='')
            f.write(response.content)
            print('Done')
    except:
        print('failed')


# let get 10 post from this subreddit
for i in subreddit.top(limit=None):
    response = requests.get(i.url)  # response
    name = i.id + '.' + i.url.split('.')[-1]  # file name
    time = datetime.fromtimestamp(i.created)
    # let's append all the info to the dictionary aka hashtable
    riceListo['id'].append(i.id)
    riceListo['title'].append(i.title)
    riceListo['rice'].append(i.url)
    riceListo['post link'].append('https://www.reddit.com/' + i.permalink)
    riceListo['created'].append(time)
    riceListo['upvote ratio'].append(i.upvote_ratio)
    riceListo['upvote'].append(i.score)
    riceListo['downvote'].append(i.downs)
    print(i.title)
    # let's match the distro name
    pattern = re.compile('\[(.*?)\]')
    match = pattern.search(i.title)
    if match:
        val = match.group(1).lower()
        if 'i3' in val:
            saveFile('i3', name, response.content)
        elif 'awesome' in val:
            saveFile('awesome', name, response.content)
        elif 'bspwm' in val:
            saveFile('bspwm', name, response.content)
        elif 'openbox' in val:
            saveFile('openbox', name, response.content)

    # print(i.id)
    # saveFile(name, response.content)

df = pd.DataFrame(riceListo)
df.to_csv('output.csv')
