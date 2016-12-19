import feedparser
import util

url = 'http://feeds.nos.nl/nosnieuwseconomie'
feed = feedparser.parse(url)

for entry in feed["entries"]:
	filename = entry.title
	util.word_cloud(entry.summary, filename) 

