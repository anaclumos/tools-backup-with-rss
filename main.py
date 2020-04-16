import os
from RSSReader import RSSReader as RR
from MDCreator import MDCreator as MC

# ------------
DIRNAME = "backups"
RSSNAME = "https://openai.com/blog/rss/"
# ------------

obj = RR(RSSNAME)
postlist = obj.parse()

for post in postlist:
    newMDFile = MC(post)
    newMDFile.createFile(DIRNAME)
