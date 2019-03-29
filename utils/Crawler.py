from utils.rss.RssParser import RssParser

class Crawler():

    def __init__(self, urls=[]):
        self.urls = urls

    def run(self):
        for name,url in self.urls.items():
            rp = RssParser(url)
            for item in rp.items:
                print(item.find('./title').text)
                print(item.find('./link').text)
        return True