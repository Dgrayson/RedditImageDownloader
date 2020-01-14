import praw
import os
import urllib.request
import json
import wget
import re
from gfycat.client import GfycatClient



file_path = "c:/users/dgray/desktop/reddit image downloader/Images/"

_directory = ""

_currTitle = ""

_sortChoice = 0
_imageLimit = 10

def parseUrl(url):

    parsedUrl = ""

    parsedUrl = url.rsplit('/', 1)[-1]

    if "." in parsedUrl:
        temp = wget.download(url, out=_directory)
        renameFile(temp, ".jpg")
    else:
        if "gfycat" in url: 
            gfyJson = gfycatClient.query_gfy(parsedUrl)
            temp = wget.download(gfyJson['gfyItem']['mp4Url'], out=_directory)
            renameFile(temp, ".mp4")
        if "vid.me" in url: 
            temp = wget.download(url, out=_directory)
            renameFile(temp, ".mp4")
        else: 
            print("invalid url")      

def renameFile(fileLocation, fileExt):

    print("\n\n" + _directory)
    newTitle = re.sub(r'[\\/*?:"<>|.]', "_", _currTitle)
    os.rename(fileLocation, _directory + "/" + newTitle + fileExt)


def CheckDirectory(sub_name, name):

    if not os.path.exists(file_path + sub_name): 
        os.makedirs(file_path + sub_name)

    if not os.path.exists(file_path + sub_name + "/" + name):
        os.makedirs(file_path + sub_name + "/" + name)

    return file_path + sub_name + "/" + name

def GetSubreddits(sub_name):

    global _directory
    global _currTitle

    if _sortChoice == 1: 
        for sub in reddit.subreddit(sub_name).hot(limit=_imageLimit):
            GetContent(sub, sub_name)
    elif _sortChoice == 2:
        for sub in reddit.subreddit(sub_name).new(limit=_imageLimit):
            GetContent(sub, sub_name)
    elif _sortChoice == 3: 
        for sub in reddit.subreddit(sub_name).rising(limit=_imageLimit):
            GetContent(sub, sub_name)
    elif _sortChoice == 4: 
        for sub in reddit.subreddit(sub_name).top(limit=_imageLimit):
            GetContent(sub, sub_name)
    else:
        print("Invalid Choice")

def GetContent(sub, sub_name):
    print("\n\n\n" + sub.title + "  :  " + sub.url)
    _currTitle = sub.title

    if sub.author.name is not None:
        _directory = CheckDirectory(sub_name, sub.author.name)
    else:
        _directory = CheckDirectory(sub_name, 'deleted')

    parseUrl(sub.url)



def main():
    global _sortChoice
    global _imageLimit
    running = True
    
    while running: 
        sub_name = input("Enter subreddit name: ")
        _sortChoice = int(input("\nSelect subreddit type:\n\n1. Hot\n2. New\n3. Rising\n4. Top\n\n"))
        _imageLimit = int(input("\n\nEnter Image Limit (1 - 100): "))
        GetSubreddits(sub_name)
        choice = input("\n\nWould you like to enter another subreddit? Y/N")

        if choice.strip(',.').lower() == 'n':
            running = False


if __name__ == "__main__":
    main()
