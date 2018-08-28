import feedparser
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

RSS_FEEDS = {
	'crickinfo': 'http://www.espncricinfo.com/rss/content/story/feeds/0.xml',
	'cricbuzz': 'http://live-feeds.cricbuzz.com/CricbuzzFeed',
    'reddit' : 'https://www.reddit.com/r/Cricket/.rss'
}

@app.route("/", methods=['GET', 'POST'])
def default():
	query = request.form.get("publication")
	if not query or query.lower() not in RSS_FEEDS:
		publication = "cricbuzz"
	else:
		publication = query.lower()
	return get_news(publication)

@app.route("/info")
def wired():
	return get_news('crickinfo')

@app.route("/buzz")
def bbc():
	return get_news('cricbuzz')


def get_news(publication):
	feed = feedparser.parse(RSS_FEEDS[publication])
	return render_template("home.html", articles=feed['entries'], publication=publication)

if __name__ == "__main__":
	app.run(port=5000, debug=True)