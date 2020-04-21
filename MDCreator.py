# -*- coding: utf-8 -*-

import os
import codecs
import requests
import validators
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse


class MDCreator:
    def __init__(self, rawData, blogDomain):
        self.rawData = rawData
        self.blogDomain = blogDomain

    def createFile(self, directory):
        try:
            os.makedirs(directory + "/" + self.rawData.title)
            print('Folder "' + self.rawData.title + '" Created ')
        except FileExistsError:
            print(
                'Folder "' + self.rawData.title + '" already exists'
            )
        self.directory = directory + "/" + self.rawData.title

        MDFile = codecs.open(
            self.directory + "/README.md", "w", "utf-8"
        )
        MDFile.write(self.render())
        MDFile.close()

    def render(self):
        try:
            postTitle = str(self.rawData.title)
        except AttributeError:
            postTitle = "Post Title Unknown"
            print("Post Title does not exist")
        try:
            postTags = str(
                self.getValueListOfDictList(self.rawData.tags, "term")
            )
        except AttributeError:
            postTags = "Post Tags Unknown"
            print("Post Tags does not exist")
        try:
            postLink = "Post Link Unknown"
            postLink = str(self.rawData.link)
        except AttributeError:
            print("Post Link does not exist")
        try:
            postID = str(self.rawData.id)
        except AttributeError:
            postID = "Post ID unknown"
            print("Post ID does not exist")
        try:
            postAuthors = str(self.rawData.authors)
        except AttributeError:
            postAuthors = "Authors Unknown"
            print("Authors does not exist")
        try:
            postPublished = str(self.rawData.published)
        except AttributeError:
            postPublished = "Published Date unknown"
            print("Published Date does not exist")
        self.renderedData = (
            "---\nlayout: post\ntitle: "
            + postTitle
            + "\ntags: "
            + postTags
            + "\nurl: "
            + postLink
            + "\nauthors: "
            + postAuthors
            + "\npublished: "
            + postPublished
            + "\nid: "
            + postID
            + "\n---\n"
        )

        self.renderedData += (
            "\n\n# " + postTitle + "\n\n## Summary\n\n"
        )

        try:
            self.renderedData += self.rawData.summary
        except AttributeError:
            self.renderedData += "RSS summary does not exist."

        self.renderedData += "\n\n## Content\n\n"

        try:
            for el in self.getValueListOfDictList(
                self.rawData.content, "value"
            ):
                self.renderedData += "\n" + str(el)
        except AttributeError:
            self.renderedData += "RSS content does not exist."

        soup = bs(self.renderedData, features="html.parser")
        for img in soup.findAll("img"):

            for imgsrc in ["src", "data-src"]:
                try:
                    remoteFile = img[imgsrc]
                    break
                except KeyError:
                    continue

            if self.isDomain(remoteFile) != True:
                print("remoteFile", remoteFile, "is not a domain.")
                remoteFile = self.blogDomain + "/" + remoteFile
                print("Fixing it to", remoteFile)
            print(
                'Trying to download "'
                + remoteFile
                + '" and save it at "'
                + self.directory
                + '/images"'
            )
            self.download(remoteFile, self.directory + "/images")
            img["src"] = "images/" + remoteFile.split("/")[-1]
            img["srcset"] = ""
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
        if filename.find("?") > 0:
            filename = filename.split("?")[0]
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

    def isDomain(self, string):
        if string.startswith("https://") or string.startswith(
            "http://"
        ):
            return True
        elif string.startswith("/"):
            return False
        else:
            return validators.domain(string.split("/")[0])
