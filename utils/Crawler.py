import json
from utils.rss.RssParser import RssParser

class Crawler():

    def __init__(self, urls=[]):
        self.urls     = urls
        self.listener = False
        self.output   = False

    def run(self):
        feeds = dict()
        for name,url in self.urls.items():
            feed = list()
            rp = RssParser(url)
            for item in rp.items:
                article = dict()
                article['title'] = item.find('./title').text
                article['link'] = item.find('./link').text
                feed.append(article)
            feeds[name] = feed
        json.dumps(feeds, sort_keys=True, indent=4)
        return True