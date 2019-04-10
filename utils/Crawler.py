import json
from utils.rss.RssManager import RssManager 
from utils.output.output import Output 


class Crawler():

    def __init__(self, urls=[]):
        self.urls     = urls
        self.listener = None
        self.verbose  = None
        self.output_file   = None
        self.output_type   = None


    def run(self):
        feeds = RssManager(self.urls).get_feeds()
        if self.verbose :
            print(json.dumps(feeds, sort_keys=True, indent=4, ensure_ascii=False))
        Output(self.output_type, feeds, output_file=self.output_file)
        
        return json.dumps(feeds, sort_keys=True, indent=4)