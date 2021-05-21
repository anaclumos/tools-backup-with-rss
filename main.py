# -*- coding: utf-8 -*-

import os
from RSSReader import RSSReader as RR
from MDCreator import MDCreator as MC
import time
import pprint

start = time.time()

# ------------
RSSURL = "https://yourblog.com/rss"
RSSHome = "https://yourblog.com/"
RSSDIR = "backups"
# ------------


def backup(rssURL, backupDirectory):
    feed = RR(rssURL)
    postlist = feed.parse()
    for post in postlist:
        newMDFile = MC(post, RSSHome)
        newMDFile.createFile(backupDirectory)


backup(RSSURL, RSSDIR)

total = time.time() - start
print(
    "Total Runtime: "
    + str(int(total / 60))
    + "m "
    + str(round(total % 60, 3))
    + "s."
)
