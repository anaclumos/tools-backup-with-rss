import os
from RSSReader import RSSReader as RR
from MDCreator import MDCreator as MC
import time

start = time.time()

# ------------
RSSURL = "https://yourblog.com/rss"
RSSDIR = "backups"
# ------------


def backup(rssURL, backupDirectory):
    feed = RR(rssURL)
    postlist = feed.parse()
    blogDomain = feed.getBlogDomain()
    for post in postlist:
        newMDFile = MC(post, blogDomain)
        newMDFile.createFile(backupDirectory)


backup(RSSURL, RSSDIR)

total = time.time() - start
print(
    "Total Runtime: " + str(int(total / 60)) + "m " + str(round(total % 60, 3)) + "s."
)
