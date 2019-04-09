import xml.etree.ElementTree as et
from utils.rss.RssParser import RssParser

class RssManager():

    def __init__(self, urls=[]):
        self.urls = urls

    def get_feeds(self):
        feeds = dict()
        for name,url in self.urls.items():
            feeds = RssParser(url).get_feed(name)
        return feeds