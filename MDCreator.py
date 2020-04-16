import os
import requests
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse


class MDCreator:
    def __init__(self, string):
        self.rawData = string

    def createFile(self, directory):
        try:
            os.makedirs(directory + "/" + self.rawData.title)
            print('Folder "' + self.rawData.title + '" Created ')
        except FileExistsError:
            print('Folder "' + self.rawData.title + '" already exists')
        self.directory = directory + "/" + self.rawData.title

        MDFile = open(self.directory + "/README.md", "w")
        MDFile.write(self.render())
        MDFile.close()

    def render(self):
        postTitle = "unknown"
        postTags = "unknown"
        postLink = "unknown"
        postID = "unknown"
        postAuthors = "unknown"
        postPublished = "unknown"

        try:
            postTitle = str(self.rawData.title)
        except AttributeError:
            print("Post Title does not exist")
        try:
            postTags = str(self.getValueListOfDictList(self.rawData.tags, "term"))
        except AttributeError:
            print("Post Tags does not exist")
        try:
            postLink = str(self.rawData.link)
        except AttributeError:
            print("Post Link does not exist")
        try:
            postID = str(self.rawData.id)
        except AttributeError:
            print("Post ID does not exist")
        try:
            postAuthors = str(self.rawData.authors)
        except AttributeError:
            print("Authors does not exist")
        try:
            postPublished = str(self.rawData.published)
        except AttributeError:
            print("Published Date does not exist")
        self.renderedData = (
            """---
layout: post
title: """
            + postTitle
            + """
tags: """
            + postTags
            + """
url: """
            + postLink
            + """
id: """
            + postID
            + """
authors: """
            + postAuthors
            + """
published: """
            + postPublished
            + """
---
"""
        )
        self.renderedData += "\n# " + self.rawData.title
        self.renderedData += "\n###### Summary\n" + self.rawData.summary
        for el in self.getValueListOfDictList(self.rawData.content, "value"):
            self.renderedData += "\n" + str(el)
        soup = bs(self.renderedData, features="html.parser")
        for img in soup.findAll("img"):
            remoteFile = img["src"]
            self.download(remoteFile, self.directory + "/images")
            img["src"] = "images/" + remoteFile.split("/")[-1]
            print(img["src"])
        self.renderedData = str(soup)
        return self.renderedData

    def getValueListOfDictList(self, dicList, targetkey):
        arr = []
        for dic in dicList:
            for key, value in dic.items():
                if key == targetkey:
                    arr.append(value)
        return arr

    def download(self, url, pathname):
        if not os.path.isdir(pathname):
            os.makedirs(pathname)
        response = requests.get(url, stream=True)
        file_size = int(response.headers.get("Content-Length", 0))
        filename = os.path.join(pathname, url.split("/")[-1])
        progress = tqdm(
            response.iter_content(256),
            f"Downloading {filename}",
            total=file_size,
            unit="B",
            unit_scale=True,
            unit_divisor=1024,
        )
        with open(filename, "wb") as f:
            for data in progress:
                f.write(data)
                progress.update(len(data))
