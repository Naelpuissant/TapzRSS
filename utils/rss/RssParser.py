import xml.etree.ElementTree as et
import requests


class RssParser():

    def __init__(self, url):
        response = requests.get(url)
        self.xml_object = et.fromstring(response.content)
        self.title          = self.xml_object.find('./channel/title').text
        self.link           = self.xml_object.find('./channel/link').text
        self.description    = self.xml_object.find('./channel/description').text
        self.pub_date       = self.xml_object.find('./channel/pubDate').text
        self.items          = self.xml_object.findall('./channel/item')

    def get_item(self, i):
        return self.items[i]
    
    def get_feed(self, name):
        feed = list()
        for item in self.items:
            article = dict()
            article['title'] = item.find('./title').text
            article['link'] = item.find('./link').text
            feed.append(article)
        return feed