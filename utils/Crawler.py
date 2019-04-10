import json
from utils.rss.RssManager import RssManager 

class Crawler():

    def __init__(self, urls=[]):
        self.urls     = urls
        self.listener = False
        self.verbose  = False
        self.outputfile   = False


    def run(self):
        feeds = RssManager(self.urls).get_feeds()
        if self.verbose is True:
            print(json.dumps(feeds, sort_keys=True, indent=4, ensure_ascii=False))
        if self.outputfile:
            with open(self.outputfile, 'w', encoding='UTF8') as f:
                f.write(json.dumps(feeds, sort_keys=True, indent=4, ensure_ascii=False))
        return json.dumps(feeds, sort_keys=True, indent=4)