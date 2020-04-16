import feedparser


class RSSReader:
    origin = ""
    feed = ""

    def __init__(self, URL):
        self.origin = URL
        self.feed = feedparser.parse(URL)

    def parse(self):
        return self.feed.entries
    
    def getBlogDomain(self):
        return self.origin[:self.origin.rfind("/")]